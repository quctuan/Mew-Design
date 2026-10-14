---
name: jira-logwork-automation
description: "Quy trình tự động hóa end-to-end từ Google Sheet: Nhận link Google Sheet các đầu việc (giống bảng Excel Logwork), tự động trích xuất các task theo PIC (UI/UX Tuấn), tạo Jira Sub-Tasks trực tiếp bên trong Story mẹ (Cột B), gán Work Stage = UI/UX, cập nhật ngược link Jira vào cột X ('Issue đã tạo') trên Google Sheet, và phân bổ Log Work tự động cả tháng (đủ 8h/ngày, 3 đợt, loại trừ Thứ 7 và CN) thông qua ego-browser."
compatibility: Antigravity IDE với ego-browser CLI
---

# SKILL: TỰ ĐỘNG HÓA JIRA SUB-TASKS & LOG WORK TỪ GOOGLE SHEET

## 📌 1. Mục tiêu & Tổng quan

Kỹ năng này tự động hóa toàn bộ quy trình ghi nhận công việc của nhân sự UI/UX trên hệ thống Jira VNPT-Media từ Google Sheet (Master plan):
1. **Trích xuất công việc:** Đọc Google Sheet qua `ego-browser`, lọc đúng các đầu việc của nhân sự (mặc định: `Tuấn`, Role: `UIUX`), bỏ qua các task bị hủy/NA.
2. **Khởi tạo Jira Sub-Tasks trong Task mẹ:** Tự động tạo **Sub-Task** trực thuộc Story mẹ tương ứng ở Cột B (dự án: `[GDS]-MyVNPT-Line1` - `GMYVNPT1`, Issue Type ID: `10003`), tự động gán `customfield_12809` (Work Stage) = `UI/UX` (ID: `12332`), gán Assignee: `vqtuan`.
3. **Cập nhật ngược Sheet:** Dùng `ego-browser` ghi nhận đường link Sub-Task vừa tạo vào cột X (*"Issue đã tạo"*) của Google Sheet (bảo tồn ticket của PO nếu có sẵn).
4. **Log Work Cả Tháng:** Tự động tính toán các ngày làm việc trong tháng (từ Thứ 2 đến Thứ 6, loại trừ Thứ 7 & CN), chia các task làm 3 đợt xuyên suốt tháng, phân bổ thời gian sao cho **mỗi ngày làm việc đạt đúng 8.0 tiếng**, và gửi worklog tự động lên các Sub-Task.

---

## ⚙️ 2. Cấu hình Chuẩn Hệ thống VNPT Jira

- **Jira Server:** `https://dvs.vnptmedia.vn`
- **Project Task mẹ / Sub-Task:** `[GDS]-MyVNPT-Line1` (Key: `GMYVNPT1`, ID: `15191`)
- **Issue Type:** `Sub-Task` (ID: `10003`)
- **Work Stage Field:** `customfield_12809` = `12332` (`UI/UX`)
- **Mặc định Nhân sự:** `Tuấn` (Username: `vqtuan`, Email: `vqtuan@vnpt.vn`)
- **Quy chuẩn giờ làm việc:** 8.0 giờ/ngày (chia đều các task trong ngày), khung giờ hành chính `08:30` – `17:30`, không log Thứ 7 và Chủ nhật.

---

## 🚀 3. Cách Sử dụng Nhanh

Khi người dùng gửi link Google Sheet (ví dụ: `https://docs.google.com/spreadsheets/d/...`), Agent chỉ cần chạy lệnh sau:

```bash
export PATH="$HOME/.local/bin:$PATH"
SHEET_URL="<LINK_GOOGLE_SHEET>" \
TARGET_PIC="Tuấn" \
MONTH="<THANG_CAN_LOG>" \
YEAR="<NAM_CAN_LOG>" \
ego-browser nodejs < .agents/skills/jira_logwork_automation/scripts/workflow.js
```

---

## 🛠️ 4. Quy trình Chi tiết Từng Bước (SOP)

### Bước 1: Trích xuất Dữ liệu Sheet qua `ego-browser`
- Lấy `Spreadsheet ID` và `gid` từ URL.
- Xuất dữ liệu qua URL CSV export: `https://docs.google.com/spreadsheets/d/{id}/export?format=csv&gid={gid}`.
- Duyệt qua từng dòng:
  - Cột E (`PIC UIUX`): Chứa từ khóa `Tuấn`.
  - Cột C (`TASK`): Tên đầu việc.
  - Cột B (`Jira Ticket`): Mã Story mẹ (ví dụ `GMYVNPT1-8`, `GMYVNPT1-72`...).
  - Cột G (`Link figma`): Đường link canvas/frame Figma.
  - Cột K (`Status`): Bỏ qua nếu là `NA` hoặc task có ghi chú `(Bỏ)`.

### Bước 2: Tạo Sub-Tasks trong Story mẹ
- Gọi Jira REST API trong phiên trình duyệt đã xác thực của `ego-browser`:
  - `POST /rest/api/2/issue`
- Payload:
  ```json
  {
    "fields": {
      "project": { "key": "GMYVNPT1" },
      "parent": { "key": "{PARENT_KEY}" },
      "summary": "[UI/UX] {TASK_NAME}",
      "description": "...",
      "issuetype": { "id": "10003" },
      "customfield_12809": { "id": "12332" },
      "assignee": { "name": "vqtuan" }
    }
  }
  ```

### Bước 3: Cập nhật Google Sheet Cột X
- Điều hướng tới URL Google Sheet.
- Nhập nhanh qua Name Box:
  - Click `#t-name-box`, gõ `X{ROW_NUMBER}`, nhấn `Enter`.
  - Click `#t-formula-bar-input`, nhập link Sub-Task mới (nối thêm nếu đã có link PO cũ), nhấn `Enter`.

### Bước 4: Phân bổ Chiến lược Log Work 3 Đợt Cả Tháng
1. **Lọc ngày làm việc:**
   - Quét toàn bộ các ngày trong tháng chỉ định, loại trừ Thứ 7 và Chủ nhật.
2. **Chia 3 đợt:**
   - **Đợt 1:** 1/3 số ngày đầu tháng $\rightarrow$ Nhóm 1 các sub-task.
   - **Đợt 2:** 1/3 số ngày giữa tháng $\rightarrow$ Nhóm 2 các sub-task.
   - **Đợt 3:** 1/3 số ngày cuối tháng $\rightarrow$ Nhóm 3 các sub-task.
3. **Phân bổ 8.0h/ngày:**
   - Tổng số giờ log mỗi ngày của tất cả các task **luôn bằng chính xác 8.0 giờ**.
4. **Gửi Worklog:**
   - Gọi `POST /rest/api/2/issue/{SUBTASK_KEY}/worklog` theo batch nhỏ để đảm bảo tốc độ và không timeout.

---

## 🛡️ 5. Quy tắc Bất biến (Guardrails)
1. **Bắt buộc tạo dạng Sub-Task:** Toàn bộ công việc con của UI/UX phải nằm trong Story mẹ (Cột B), không tạo thành issue độc lập cấp cao nhất.
2. **Không log ngày cuối tuần:** Tuyệt đối không log vào Thứ 7 hoặc Chủ nhật.
3. **Kiểm soát trần 8h:** Tổng số giờ log của tất cả các công việc trong cùng 1 ngày không được vượt quá 8 giờ.
4. **Bảo tồn dữ liệu cũ:** Nếu ô ở Cột X của Sheet đã có link PO tạo trước đó (ví dụ `GMYVNPT-1160`), phải giữ lại và thêm link UI/UX mới dạng cách nhau bằng dấu phẩy.
