// -*- coding: utf-8 -*-
/**
 * Zalo WebSocket Bridge Daemon - Mew Assistant
 * Sử dụng zca-js để kết nối trực tiếp với Zalo Web.
 * Tự động đồng bộ tin nhắn, chấm điểm ưu tiên & đẩy thông báo về Telegram.
 */

const { Zalo, LoginQRCallbackEventType } = require('zca-js');
const qrcodeTerminal = require('qrcode-terminal');
const fs = require('fs');
const path = require('path');
const https = require('https');

const CONFIG_PATH = path.resolve(__dirname, '../../config.json');
let config = {};
try {
  config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
} catch (e) {
  console.error('Không thể đọc config.json:', e.message);
}

const BOT_TOKEN = config?.telegram_notifier_bot?.bot_token || "8820364042:AAG5XOtQmRls7Tvfjakv3ajUzbAa6CLe8hc";
const CHAT_ID = config?.telegram_notifier_bot?.my_chat_id || 1083272610;
const ZL_HISTORY_FILE = path.resolve(__dirname, 'zalo_messages.json');
const CREDENTIALS_FILE = path.resolve(__dirname, 'zalo_credentials.json');

const CONTACTS_CACHE = {};
const GROUPS_CACHE = {};

// Hàm gửi tin nhắn về Telegram
function sendTelegramMessage(text, photoPath = null) {
  if (!BOT_TOKEN || !CHAT_ID) return;

  if (photoPath && fs.existsSync(photoPath)) {
    const boundary = '----WebKitFormBoundary' + Math.random().toString(36).substring(2);
    const fileData = fs.readFileSync(photoPath);
    const fileName = path.basename(photoPath);

    let postData = Buffer.concat([
      Buffer.from(`--${boundary}\r\nContent-Disposition: form-data; name="chat_id"\r\n\r\n${CHAT_ID}\r\n`),
      Buffer.from(`--${boundary}\r\nContent-Disposition: form-data; name="caption"\r\n\r\n${text}\r\n`),
      Buffer.from(`--${boundary}\r\nContent-Disposition: form-data; name="parse_mode"\r\n\r\nHTML\r\n`),
      Buffer.from(`--${boundary}\r\nContent-Disposition: form-data; name="photo"; filename="${fileName}"\r\nContent-Type: image/png\r\n\r\n`),
      fileData,
      Buffer.from(`\r\n--${boundary}--\r\n`)
    ]);

    const req = https.request({
      hostname: 'api.telegram.org',
      path: `/bot${BOT_TOKEN}/sendPhoto`,
      method: 'POST',
      headers: {
        'Content-Type': `multipart/form-data; boundary=${boundary}`,
        'Content-Length': postData.length
      }
    }, (res) => {
      res.on('data', () => {});
    });
    req.on('error', (err) => console.error('Lỗi gửi ảnh Telegram:', err.message));
    req.write(postData);
    req.end();
    return;
  }

  const payload = JSON.stringify({
    chat_id: CHAT_ID,
    text: text,
    parse_mode: 'HTML',
    disable_web_page_preview: true
  });

  const req = https.request({
    hostname: 'api.telegram.org',
    path: `/bot${BOT_TOKEN}/sendMessage`,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload)
    }
  }, (res) => {
    res.on('data', () => {});
  });
  req.on('error', (err) => console.error('Lỗi gửi tin nhắn Telegram:', err.message));
  req.write(payload);
  req.end();
}

function extractZaloMessageText(msgData) {
  if (!msgData) return '';
  if (typeof msgData.content === 'string') return msgData.content;
  if (msgData.content && typeof msgData.content === 'object') {
    if (msgData.content.title || msgData.content.description || msgData.content.href) {
      return `${msgData.content.title || ''} ${msgData.content.description || ''} ${msgData.content.href || ''}`.trim();
    }
    return JSON.stringify(msgData.content);
  }
  return '';
}

// Phân tích và chuyển tiếp tin nhắn Zalo về Telegram
function processAndForwardZaloMessage(msgObj) {
  const { senderName, chatName, text, isGroup } = msgObj;
  const rawText = text.trim();
  const lowerText = rawText.toLowerCase();

  let score = 0;
  const reasons = [];

  const vipKeywords = (config?.settings?.vip_senders || []).map(v => v.toLowerCase());
  if (vipKeywords.some(v => senderName.toLowerCase().includes(v))) {
    score += 15;
    reasons.push("👑 VIP / Khách hàng VIP");
  }

  if (!isGroup) {
    score += 12;
    reasons.push("💬 Nhắn riêng 1-1");
  } else if (msgObj.isReplyToMe) {
    score += 12;
    reasons.push("🎯 Reply tin nhắn bạn");
  } else if (lowerText.includes("tuấn") || lowerText.includes("tuan")) {
    score += 12;
    reasons.push("🎯 Nhắc tên bạn");
  }

  if (rawText.includes("?") || lowerText.includes("khi nào") || lowerText.includes("bao nhiêu") || lowerText.includes("giá") || lowerText.includes("được không")) {
    score += 8;
    reasons.push("❓ Có câu hỏi / Cần phản hồi");
  }

  const urgentKws = ["gấp", "khẩn", "asap", "urgent", "deadline", "hôm nay", "chậm", "blocker"];
  for (const kw of urgentKws) {
    if (lowerText.includes(kw)) {
      score += 7;
      reasons.push(`⚡ Khẩn: "${kw}"`);
      break;
    }
  }

  if (rawText.includes("figma.com") || rawText.includes("docs.google.com") || rawText.includes("drive.google.com")) {
    score += 6;
    reasons.push("🎨 Kèm link Figma / Doc");
  }

  const designKws = ["thiết kế", "design", "ui", "ux", "figma", "báo giá", "hợp đồng", "nghiệm thu", "chỉnh sửa", "layout"];
  for (const kw of designKws) {
    if (lowerText.includes(kw)) {
      score += 4;
      reasons.push(`🎨 Thiết kế/Dự án: "${kw}"`);
      break;
    }
  }

  let badge = "🟡 NORMAL (TIÊU CHUẨN)";
  if (score >= 15) badge = "🚨 CRITICAL (CỰC KỲ KHẨN CẤP)";
  else if (score >= 8) badge = "🔥 HIGH (ƯU TIÊN CAO)";
  else if (score < 4) badge = "⚪ LOW (THÔNG TIN)";

  const actions = [];
  if (msgObj.isReplyToMe) {
    actions.push(`Đọc nội dung phản hồi và tiếp tục trao đổi với <b>${senderName}</b>`);
  }
  if ((rawText.includes("?") || lowerText.includes("được không") || lowerText.includes("thế nào")) && !msgObj.isReplyToMe) {
    actions.push(`Phản hồi câu hỏi / giải đáp thắc mắc cho <b>${senderName}</b>`);
  }
  if (rawText.includes("figma.com")) {
    actions.push("Mở link Figma đính kèm để xem phản hồi và chỉnh sửa UI");
  } else if (lowerText.includes("figma") || lowerText.includes("ui") || lowerText.includes("ux") || lowerText.includes("thiết kế")) {
    actions.push("Kiểm tra / rà soát file thiết kế theo yêu cầu của đối tác");
  }
  if (lowerText.includes("báo giá") || lowerText.includes("chi phí") || lowerText.includes("hợp đồng") || lowerText.includes("giá")) {
    actions.push(`Lập phương án báo giá & gửi thông tin dịch vụ cho <b>${senderName}</b>`);
  }
  if (lowerText.includes("gấp") || lowerText.includes("deadline") || lowerText.includes("hôm nay") || lowerText.includes("khẩn")) {
    actions.push("Ưu tiên xử lý sớm để kịp tiến độ cho khách hàng");
  }
  if (actions.length === 0) {
    actions.push(`Xem tin nhắn và trao đổi lại với <b>${senderName}</b>`);
  }

  const actionsText = actions.map(a => `  👉 ${a}`).join('\n');
  const reasonsStr = reasons.length > 0 ? reasons.join(' · ') : 'Tin nhắn khách hàng';
  const timeStr = new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit' });
  const snippet = rawText.length > 130 ? rawText.substring(0, 130) + '...' : rawText;

  const alertMsg = (
    `<b>🔵 [ZALO CLIENT]</b>\n` +
    `${badge} (⭐ <b>${score} điểm</b>)\n` +
    `<i>(${reasonsStr})</i>\n` +
    `━━━━━━━━━━━━━━━━━━━━━\n` +
    `📍 <b>Nguồn:</b> <code>Zalo: ${chatName}</code>\n` +
    `👤 <b>Người gửi:</b> <b>${senderName}</b> (⏰ ${timeStr})\n\n` +
    `📝 <b>Ngữ cảnh:</b> <i>"${snippet}"</i>\n\n` +
    `🎯 <b>Hành động Cần làm:</b>\n` +
    `${actionsText}\n\n` +
    `━━━━━━━━━━━━━━━━━━━━━\n` +
    `💡 <i>(Mở app Zalo trên điện thoại hoặc máy tính để phản hồi khách)</i>`
  );

  sendTelegramMessage(alertMsg);
  console.log(`\n[✓ ĐÃ BẮN CẢNH BÁO ZALO VỀ TELEGRAM] Từ: ${senderName} | Nhóm: ${chatName}`);
}

function isWhitelisted(senderName, chatName) {
  let currentConfig = config;
  try {
    currentConfig = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  } catch {}

  const whitelist = currentConfig?.zalo_settings?.whitelist || [
    "Anh Tín",
    "[VFS] Design outsource",
    "Huu Nghi - Opla CRM",
    "Trình Khánh",
    "Vũ Thị Thuỷ Tiên",
    "Group của tôi, Thuỳ Trang, Vũ Thị Thuỷ Tiên"
  ];

  const sLower = (senderName || '').toLowerCase().trim();
  const cLower = (chatName || '').toLowerCase().trim();

  for (const item of whitelist) {
    const itemLower = item.toLowerCase().trim();
    if (!itemLower) continue;

    // Khớp tên người gửi
    if (sLower.includes(itemLower) || (itemLower.includes(sLower) && sLower.length >= 3)) {
      return { matched: true, reason: item };
    }
    // Khớp tên nhóm chat
    if (cLower.includes(itemLower) || (itemLower.includes(cLower) && cLower.length >= 3)) {
      return { matched: true, reason: item };
    }
  }
  return { matched: false, reason: null };
}

function saveZaloMessageToCache(item, shouldNotify = false) {
  let zlHistory = [];
  try {
    if (fs.existsSync(ZL_HISTORY_FILE)) {
      zlHistory = JSON.parse(fs.readFileSync(ZL_HISTORY_FILE, 'utf8'));
    }
  } catch {}

  const seenIds = new Set(zlHistory.map(m => m.id));
  if (seenIds.has(item.id)) return;

  zlHistory.unshift(item);
  if (zlHistory.length > 3000) zlHistory = zlHistory.slice(0, 3000);

  try {
    fs.writeFileSync(ZL_HISTORY_FILE, JSON.stringify(zlHistory, null, 2), 'utf8');
  } catch (e) {
    console.error('Lỗi lưu cache tin nhắn Zalo:', e.message);
  }

  if (shouldNotify && !item.fromMe) {
    const check = isWhitelisted(item.senderName, item.chatName);
    const isDirect = !item.isGroup;
    const lowerText = (item.text || '').toLowerCase();
    const hasMention = lowerText.includes('tuấn') || lowerText.includes('tuan');
    const hasUrgentOrLink = lowerText.includes('figma.com') || lowerText.includes('docs.google.com') || lowerText.includes('drive.google.com') || lowerText.includes('gấp') || lowerText.includes('báo giá') || lowerText.includes('deadline');

    if (check.matched || isDirect || hasMention || hasUrgentOrLink || item.isReplyToMe) {
      processAndForwardZaloMessage({
        senderName: item.senderName,
        chatName: item.chatName,
        text: item.text,
        isGroup: item.isGroup,
        isReplyToMe: item.isReplyToMe || false
      });
    } else {
      console.log(`[i Bỏ qua cảnh báo Zalo] Từ: "${item.senderName}" | Nhóm: "${item.chatName}" (Tin nhắn nhóm thông thường)`);
    }
  }
}

let isFirstTimeZaloQRScan = false;

async function startZaloBridge() {
  const zalo = new Zalo({
    logging: false,
    selfListen: true
  });

  let api = null;

  // 1. Thử đăng nhập bằng Session/Credentials đã lưu nếu có
  if (fs.existsSync(CREDENTIALS_FILE)) {
    try {
      console.log('[+] Tìm thấy phiên đăng nhập Zalo trước đó. Đang kết nối lại...');
      const savedCreds = JSON.parse(fs.readFileSync(CREDENTIALS_FILE, 'utf8'));
      api = await zalo.login(savedCreds);
    } catch (err) {
      console.log('[!] Phiên Zalo cũ đã hết hạn hoặc không hợp lệ. Tạo mã QR mới...');
      api = null;
    }
  }

  // 2. Nếu chưa có session -> Đăng nhập bằng QR Code
  if (!api) {
    console.log('[+] Đang khởi tạo mã QR đăng nhập Zalo...');
    try {
      api = await zalo.loginQR({}, (event) => {
        if (event.type === LoginQRCallbackEventType.QRCodeGenerated) {
          isFirstTimeZaloQRScan = true;
          const qrPath = path.resolve(__dirname, 'zalo_qr.png');
          const base64Data = event.data.image.replace(/^data:image\/png;base64,/, "");
          fs.writeFileSync(qrPath, base64Data, 'base64');

          console.log('\n======================================================');
          console.log('📱 MÃ QR KẾT NỐI ZALO:');
          console.log('1. Mở Zalo trên điện thoại');
          console.log('2. Bấm vào biểu tượng Quét mã QR ở góc trên bên phải');
          console.log('3. Quét mã QR để liên kết tài khoản');
          console.log('======================================================\n');

          sendTelegramMessage(
            `📱 <b>MÃ QR KẾT NỐI ZALO</b>\n\n` +
            `1. Mở app <b>Zalo</b> trên điện thoại của bạn.\n` +
            `2. Bấm vào biểu tượng <b>Quét mã QR</b> (ở thanh tìm kiếm trên cùng).\n` +
            `3. Quét mã QR này để đồng bộ tin nhắn khách hàng Zalo!`,
            qrPath
          );
        } else if (event.type === LoginQRCallbackEventType.QRCodeScanned) {
          console.log('[+] Đã quét mã QR Zalo trên điện thoại! Đang xác thực...');
        } else if (event.type === LoginQRCallbackEventType.GotLoginInfo) {
          console.log('[✓] Đã lấy thông tin phiên đăng nhập Zalo thành công!');
          fs.writeFileSync(CREDENTIALS_FILE, JSON.stringify(event.data, null, 2), 'utf8');
        }
      });
    } catch (err) {
      console.error('[!] Lỗi đăng nhập Zalo:', err.message);
      setTimeout(startZaloBridge, 5000);
      return;
    }
  }

  if (!api) {
    console.error('[!] Không thể khởi tạo API Zalo.');
    return;
  }

  console.log('\n======================================================');
  console.log('✅ KẾT NỐI ZALO THÀNH CÔNG VÀ ĐANG CHẠY!');
  console.log('Đang nạp danh bạ và nhóm chat để phục vụ tra cứu...');
  console.log('======================================================\n');

  // Kích hoạt channel Zalo trong config.json nếu chưa bật
  try {
    const liveConfig = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
    if (!liveConfig.active_channels) liveConfig.active_channels = {};
    liveConfig.active_channels.zalo = true;
    fs.writeFileSync(CONFIG_PATH, JSON.stringify(liveConfig, null, 2), 'utf8');
  } catch {}

  // Chỉ gửi thông báo kết nối thành công 1 lần duy nhất khi vừa quét mã QR mới
  if (!global.hasNotifiedZaloConnected && isFirstTimeZaloQRScan) {
    global.hasNotifiedZaloConnected = true;
    sendTelegramMessage(
      `✅ <b>KẾT NỐI ZALO THÀNH CÔNG!</b>\n` +
      `━━━━━━━━━━━━━━━━━━━━━\n` +
      `Trợ lý <b>Mew Assistant</b> đã kết nối và đang lắng nghe toàn bộ tin nhắn, nhóm chat từ khách hàng Zalo!`
    );
  }

  // Nạp danh bạ bạn bè và danh sách nhóm
  try {
    const groupsRes = await api.getAllGroups();
    if (groupsRes && groupsRes.data) {
      for (const [gid, ginfo] of Object.entries(groupsRes.data)) {
        GROUPS_CACHE[gid] = ginfo.name || ginfo.grid || 'Nhóm Zalo';
      }
      console.log(`[+] Đã nạp ${Object.keys(GROUPS_CACHE).length} nhóm Zalo vào bộ nhớ cache.`);
    }
  } catch (e) {
    console.log('[!] Lưu ý nạp nhóm Zalo:', e.message);
  }

  try {
    const friendsRes = await api.getAllFriends();
    if (friendsRes && friendsRes.data) {
      for (const f of friendsRes.data) {
        if (f.userId && (f.displayName || f.zaloName)) {
          CONTACTS_CACHE[f.userId] = f.displayName || f.zaloName;
        }
      }
      console.log(`[+] Đã nạp ${Object.keys(CONTACTS_CACHE).length} bạn bè Zalo vào bộ nhớ cache.`);
    }
  } catch (e) {
    console.log('[!] Lưu ý nạp bạn bè Zalo:', e.message);
  }

  // Khởi động WebSocket Listener nhận tin nhắn theo thời gian thực
  try {
    api.listener.start({ retryOnClose: true });

    api.listener.on('connected', () => {
      console.log('[+] Zalo WebSocket Listener đã kết nối.');
    });

    api.listener.on('old_messages', (messages, threadType) => {
      try {
        if (!Array.isArray(messages)) return;
        console.log(`[+] Nhận ${messages.length} tin nhắn lịch sử Zalo từ đồng bộ WebSocket`);
        for (const m of messages) {
          const msgData = m.data;
          if (!msgData) continue;
          const text = extractZaloMessageText(msgData);
          if (!text || !text.trim()) continue;

          const isGroup = threadType === 1 || m.isGroup;
          const senderName = msgData.dName || CONTACTS_CACHE[msgData.uidFrom] || 'Khách Zalo';
          const chatName = isGroup ? (GROUPS_CACHE[msgData.idTo] || 'Nhóm Zalo') : senderName;
          const msgId = msgData.msgId || msgData.cliMsgId || `${Date.now()}`;
          const ts = msgData.ts ? Number(msgData.ts) : Date.now();
          const dateObj = new Date(ts);
          const timeStr = dateObj.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit' });

          saveZaloMessageToCache({
            id: String(msgId),
            senderName,
            chatName,
            text,
            isGroup,
            timestamp: timeStr,
            date: dateObj.toISOString(),
            fromMe: false
          }, false);
        }
      } catch (err) {
        console.error('[!] Lỗi xử lý old_messages Zalo:', err.message);
      }
    });

    api.listener.on('message', async (messageEvent) => {
      try {
        const msgData = messageEvent.data;
        if (!msgData) return;

        const text = extractZaloMessageText(msgData);
        if (!text || !text.trim()) return;

        const isGroup = messageEvent.type === 1; // 1: Group, 0: User
        const senderName = msgData.dName || CONTACTS_CACHE[msgData.uidFrom] || 'Khách Zalo';
        
        let chatName = senderName;
        if (isGroup) {
          if (!GROUPS_CACHE[msgData.idTo] || GROUPS_CACHE[msgData.idTo] === 'Nhóm Zalo') {
            try {
              const gInfo = await api.getGroupInfo(msgData.idTo);
              if (gInfo && gInfo.data && gInfo.data.groupMap && gInfo.data.groupMap[msgData.idTo]) {
                GROUPS_CACHE[msgData.idTo] = gInfo.data.groupMap[msgData.idTo].name || gInfo.data.groupMap[msgData.idTo].gname || 'Nhóm Zalo';
              }
            } catch {}
          }
          chatName = GROUPS_CACHE[msgData.idTo] || 'Nhóm Zalo';
        }

        const msgId = msgData.msgId || msgData.cliMsgId || `${Date.now()}`;
        const ts = msgData.ts ? Number(msgData.ts) : Date.now();
        const dateObj = new Date(ts);
        const timeStr = dateObj.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit' });

        saveZaloMessageToCache({
          id: String(msgId),
          senderName,
          chatName,
          text,
          isGroup,
          timestamp: timeStr,
          date: dateObj.toISOString(),
          fromMe: false
        }, true);
      } catch (err) {
        console.error('[!] Lỗi xử lý tin nhắn Zalo:', err.message);
      }
    });

    api.listener.on('error', (err) => {
      console.error('[!] Zalo Listener Error:', err);
    });

    api.listener.on('closed', (code, reason) => {
      console.log(`[!] Zalo connection closed (${code}: ${reason}). Đang tự động kết nối lại...`);
    });
  } catch (err) {
    console.error('[!] Lỗi khởi động Zalo Listener:', err.message);
  }
}

startZaloBridge();
