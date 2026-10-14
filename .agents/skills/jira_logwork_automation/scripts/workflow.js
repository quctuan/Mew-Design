/**
 * Automated Jira Sub-Task & Google Sheet Worklog Flow
 * Usage: ego-browser nodejs < scripts/workflow.js
 */
import fs from "node:fs/promises";

const CONFIG = {
  sheetUrl: process.env.SHEET_URL || "https://docs.google.com/spreadsheets/d/1E-6bkX8QzpIVsDOf7OXS6vQAXLUVTr8GgfEoU3PHIgk/edit?pli=1&gid=1374299408#gid=1374299408",
  targetPic: process.env.TARGET_PIC || "Tuấn",
  jiraBase: process.env.JIRA_BASE || "https://dvs.vnptmedia.vn",
  projectKey: process.env.PROJECT_KEY || "GMYVNPT1", // Sub-tasks belong to [GDS]-MyVNPT-Line1
  issueTypeId: "10003", // Sub-Task
  workStageId: "12332", // customfield_12809 = UI/UX
  assignee: process.env.ASSIGNEE || "vqtuan",
  year: parseInt(process.env.YEAR || "2026", 10),
  month: parseInt(process.env.MONTH || "9", 10),
};

function getSheetExportUrl(sheetUrl) {
  const matchId = sheetUrl.match(/\/d\/([a-zA-Z0-9-_]+)/);
  const matchGid = sheetUrl.match(/[#&?]gid=([0-9]+)/);
  if (!matchId) throw new Error("Invalid Google Sheet URL: missing Spreadsheet ID");
  const id = matchId[1];
  const gid = matchGid ? matchGid[1] : "0";
  return `https://docs.google.com/spreadsheets/d/${id}/export?format=csv&gid=${gid}`;
}

function parseCSV(text) {
  const lines = [];
  let row = [];
  let inQuotes = false;
  let cur = "";

  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    const next = text[i + 1];
    if (c === '"') {
      if (inQuotes && next === '"') {
        cur += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (c === ',' && !inQuotes) {
      row.push(cur);
      cur = "";
    } else if ((c === '\r' || c === '\n') && !inQuotes) {
      if (c === '\r' && next === '\n') i++;
      row.push(cur);
      lines.push(row);
      row = [];
      cur = "";
    } else {
      cur += c;
    }
  }
  if (cur || row.length > 0) {
    row.push(cur);
    lines.push(row);
  }
  return lines;
}

function getWorkdays(year, month) {
  const workdays = [];
  const daysInMonth = new Date(year, month, 0).getDate();
  for (let day = 1; day <= daysInMonth; day++) {
    const d = new Date(year, month - 1, day);
    const dayOfWeek = d.getDay(); // 0: Sun, 6: Sat
    if (dayOfWeek !== 0 && dayOfWeek !== 6) {
      const yyyy = year;
      const mm = String(month).padStart(2, "0");
      const dd = String(day).padStart(2, "0");
      workdays.push(`${yyyy}-${mm}-${dd}`);
    }
  }
  return workdays;
}

async function run() {
  console.log("=== BẮT ĐẦU QUY TRÌNH TỰ ĐỘNG TẠO SUB-TASK JIRA & LOG WORK ===");
  console.log(`- Sheet URL: ${CONFIG.sheetUrl}`);
  console.log(`- Target PIC: ${CONFIG.targetPic}`);
  console.log(`- Jira: ${CONFIG.jiraBase} (Project: ${CONFIG.projectKey}, Type: Sub-Task, Assignee: ${CONFIG.assignee})`);
  console.log(`- Tháng/Năm log work: ${CONFIG.month}/${CONFIG.year}`);

  const task = await taskSpace("jira subtask automation");
  const page = task.page("p1");

  // BƯỚC 1: ĐỌC DỮ LIỆU TỪ GOOGLE SHEET
  console.log("\n[Bước 1/4] Đang mở Google Sheet và trích xuất danh sách task...");
  await page.goto(CONFIG.sheetUrl);
  await page.waitForTimeout(4000);

  const exportUrl = getSheetExportUrl(CONFIG.sheetUrl);
  const csvRaw = await page.evaluate(async (url) => {
    const res = await fetch(url);
    if (!res.ok) throw new Error("HTTP " + res.status);
    return await res.text();
  }, exportUrl);

  const rows = parseCSV(csvRaw);
  console.log(`Đã đọc ${rows.length} dòng từ Google Sheet.`);

  // Parse tasks
  const tasks = [];
  let currentGroup = "";
  let lastParentKey = "";

  for (let idx = 1; idx < rows.length; idx++) {
    const r = rows[idx];
    if (!r || r.length < 5) continue;
    if (r[0] && r[0].trim()) currentGroup = r[0].trim();

    const picUiux = (r[4] || "").trim();
    if (!picUiux.toLowerCase().includes(CONFIG.targetPic.toLowerCase())) continue;

    const rowNum = idx + 1; // 1-indexed Excel row
    const rawTask = (r[2] || "").trim();
    let parentTicket = (r[1] || "").trim();
    const figmaLink = (r[6] || "").trim();
    const status = (r[10] || "").trim();
    const existingCreated = (r[23] || "").trim();

    // Bỏ qua task NA hoặc bị hủy
    if (status.toUpperCase() === "NA" || rawTask.includes("(Bỏ")) {
      console.log(`  -> Bỏ qua task tại hàng ${rowNum}: ${rawTask} (Status: ${status})`);
      continue;
    }

    // Chuẩn hóa parent ticket key
    if (parentTicket) {
      if (parentTicket === "GMYVNPT-539") parentTicket = "GMYVNPT1-539";
      lastParentKey = parentTicket;
    } else {
      // Kế thừa task mẹ gần nhất nếu dòng con bị khuyết cột B
      parentTicket = lastParentKey;
    }

    tasks.push({
      rowNum,
      group: currentGroup,
      rawTask,
      parentTicket,
      figmaLink,
      status,
      existingCreated
    });
  }

  console.log(`\nTìm thấy ${tasks.length} task hợp lệ cần tạo Sub-Task:`);
  tasks.forEach((t, i) => console.log(`  ${i + 1}. [Hàng ${t.rowNum}] ${t.rawTask} -> Task mẹ: ${t.parentTicket}`));

  // BƯỚC 2: TẠO SUB-TASK TRONG JIRA
  console.log("\n[Bước 2/4] Đang tạo Sub-Task trong từng Story mẹ trên Jira...");
  await page.goto(`${CONFIG.jiraBase}/secure/Dashboard.jspa`);
  await page.waitForTimeout(2000);

  const createdSubtasks = [];
  for (const t of tasks) {
    const summary = `[UI/UX] ${t.rawTask.replace(/^[-\s]+/, "")}`;
    const desc = `h3. 1. Mục tiêu\r\nThiết kế UI/UX cho tính năng ${t.rawTask} trên MyVNPT.\r\n\r\nh3. 2. Link đầu ra\r\n* Figma: [Thiết kế|${t.figmaLink || ""}]\r\n* Task mẹ: [${t.parentTicket}|${CONFIG.jiraBase}/browse/${t.parentTicket}]\r\n\r\nh3. 3. Phạm vi công việc\r\n* Nghiên cứu yêu cầu nghiệp vụ và phối hợp PO/BA làm rõ luồng trải nghiệm (UX flow).\r\n* Thiết kế giao diện chi tiết (UI mockup), component và các trạng thái hiển thị trên Figma.\r\n* Phối hợp UX Writing chuẩn hóa nội dung hiển thị; bàn giao specs thiết kế cho Dev.\r\n\r\nh3. 4. Tiêu chí hoàn thành\r\n* Đầy đủ các màn hình, trạng thái tương tác và component specs được bàn giao, làm rõ với đội ngũ BA và Dev.`;

    const createRes = await page.evaluate(async (data) => {
      const body = {
        fields: {
          project: { key: data.projectKey },
          parent: { key: data.parentKey },
          summary: data.summary,
          description: data.description,
          issuetype: { id: data.issueTypeId },
          customfield_12809: { id: data.workStageId },
          assignee: { name: data.assignee }
        }
      };
      try {
        const response = await fetch("/rest/api/2/issue", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body)
        });
        if (!response.ok) return { error: `HTTP ${response.status}: ${await response.text()}` };
        const d = await response.json();
        return { success: true, key: d.key, id: d.id };
      } catch (e) {
        return { error: e.message };
      }
    }, {
      projectKey: CONFIG.projectKey,
      parentKey: t.parentTicket,
      summary,
      description: desc,
      issueTypeId: CONFIG.issueTypeId,
      workStageId: CONFIG.workStageId,
      assignee: CONFIG.assignee
    });

    if (createRes.success && createRes.key) {
      const url = `${CONFIG.jiraBase}/browse/${createRes.key}`;
      console.log(`  -> Đã tạo Sub-Task: ${createRes.key} (thuộc ${t.parentTicket})`);
      t.newKey = createRes.key;
      t.newUrl = url;
      createdSubtasks.push(t);
    } else {
      console.error(`  -> Lỗi tạo subtask hàng ${t.rowNum}:`, createRes.error);
    }
  }

  // BƯỚC 3: CẬP NHẬT ĐƯỜNG LINK VÀO CỘT X TRÊN GOOGLE SHEET
  console.log("\n[Bước 3/4] Cập nhật đường link Sub-Task vào cột X trên Google Sheet...");
  await page.goto(CONFIG.sheetUrl);
  await page.waitForTimeout(4000);

  for (const item of createdSubtasks) {
    const cell = `X${item.rowNum}`;
    let val = item.newUrl;
    // Nếu ô đã có ticket của PO, giữ lại và thêm link subtask
    if (item.existingCreated && !item.existingCreated.includes(item.newKey)) {
      val = `${item.existingCreated}, ${item.newUrl}`;
    }
    console.log(`  -> Ghi ô ${cell} = ${val}`);

    await page.click("#t-name-box");
    await page.keyboard.press("Meta+a");
    await page.keyboard.type(cell);
    await page.keyboard.press("Enter");
    await page.waitForTimeout(300);

    await page.click("#t-formula-bar-input");
    await page.waitForTimeout(200);
    await page.keyboard.press("Meta+a");
    await page.keyboard.press("Backspace");
    await page.keyboard.type(val);
    await page.keyboard.press("Enter");
    await page.waitForTimeout(400);
  }

  // BƯỚC 4: PHÂN BỔ VÀ LOG WORK 3 ĐỢT (8H/NGÀY)
  console.log("\n[Bước 4/4] Phân bổ và log work cả tháng vào các Sub-Task...");
  await page.goto(`${CONFIG.jiraBase}/secure/Dashboard.jspa`);
  await page.waitForTimeout(2000);

  const workdays = getWorkdays(CONFIG.year, CONFIG.month);
  console.log(`Tháng ${CONFIG.month}/${CONFIG.year} có ${workdays.length} ngày làm việc (không tính T7/CN).`);

  const batch1Days = workdays.slice(0, Math.floor(workdays.length / 3));
  const batch2Days = workdays.slice(Math.floor(workdays.length / 3), Math.floor((workdays.length * 2) / 3));
  const batch3Days = workdays.slice(Math.floor((workdays.length * 2) / 3));

  const totalTasks = createdSubtasks.length;
  const tPerBatch = Math.ceil(totalTasks / 3);
  const tasksBatch1 = createdSubtasks.slice(0, tPerBatch);
  const tasksBatch2 = createdSubtasks.slice(tPerBatch, tPerBatch * 2);
  const tasksBatch3 = createdSubtasks.slice(tPerBatch * 2);

  function buildDailyLogs(days, batchTasks) {
    const logs = [];
    if (batchTasks.length === 0) return logs;
    const hoursPerTask = 8 / batchTasks.length;
    const timeSpentStr = hoursPerTask >= 2 ? `${Math.floor(hoursPerTask)}h` : `${Math.floor(hoursPerTask)}h 30m`;

    for (const d of days) {
      let currentHour = 8;
      let currentMin = 30;
      for (const t of batchTasks) {
        const hh = String(currentHour).padStart(2, "0");
        const mm = String(currentMin).padStart(2, "0");
        logs.push({
          key: t.newKey,
          comment: `Thiết kế UI/UX ${t.rawTask}`,
          timeSpent: timeSpentStr,
          started: `${d}T${hh}:${mm}:00.000+0700`,
          date: d
        });
        currentMin += Math.round(hoursPerTask * 60);
        while (currentMin >= 60) {
          currentHour++;
          currentMin -= 60;
        }
      }
    }
    return logs;
  }

  const allLogs = [
    ...buildDailyLogs(batch1Days, tasksBatch1),
    ...buildDailyLogs(batch2Days, tasksBatch2),
    ...buildDailyLogs(batch3Days, tasksBatch3)
  ];

  console.log(`Tổng cộng cần log ${allLogs.length} bản ghi...`);

  const chunkSize = 15;
  for (let i = 0; i < allLogs.length; i += chunkSize) {
    const chunk = allLogs.slice(i, i + chunkSize);
    await page.evaluate(async (items) => {
      return await Promise.all(items.map(async (item) => {
        return await fetch(`/rest/api/2/issue/${item.key}/worklog`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            timeSpent: item.timeSpent,
            started: item.started,
            comment: item.comment
          })
        });
      }));
    }, chunk);
    console.log(`  -> Đã log ${Math.min(i + chunkSize, allLogs.length)}/${allLogs.length} bản ghi.`);
  }

  await task.finish({ keep: [] });
  console.log("\n=== HOÀN TẤT TOÀN BỘ QUY TRÌNH TỰ ĐỘNG SUB-TASK & LOG WORK! ===");
}

run().catch(err => {
  console.error("Lỗi quy trình:", err);
  process.exit(1);
});
