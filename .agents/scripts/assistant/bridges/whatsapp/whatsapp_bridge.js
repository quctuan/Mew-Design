// -*- coding: utf-8 -*-
const { default: makeWASocket, useMultiFileAuthState, DisconnectReason, fetchLatestBaileysVersion } = require('@whiskeysockets/baileys');
const qrcodeTerminal = require('qrcode-terminal');
const QRCode = require('qrcode');
const pino = require('pino');
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
const WA_HISTORY_FILE = path.resolve(__dirname, 'whatsapp_messages.json');

const CONTACTS_CACHE = {};
const CHATS_CACHE = {};

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

function extractMsgText(msg) {
  const c = msg.message;
  if (!c) return '';
  if (c.conversation) return c.conversation;
  if (c.extendedTextMessage?.text) return c.extendedTextMessage.text;
  if (c.imageMessage?.caption) return `[Ảnh] ${c.imageMessage.caption}`;
  if (c.documentMessage?.caption || c.documentMessage?.fileName) return `[File] ${c.documentMessage?.caption || c.documentMessage?.fileName}`;
  if (c.templateButtonReplyMessage?.selectedId) return c.templateButtonReplyMessage.selectedId;
  if (c.buttonsResponseMessage?.selectedButtonId) return c.buttonsResponseMessage.selectedButtonId;
  return '';
}

// Hàm phân tích và định dạng tin nhắn cảnh báo
function processAndForwardMessage(msgObj) {
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

  if (rawText.includes("?") || lowerText.includes("how much") || lowerText.includes("when") || lowerText.includes("can you")) {
    score += 8;
    reasons.push("❓ Có câu hỏi / Cần phản hồi");
  }

  const urgentKws = ["urgent", "asap", "gấp", "khẩn", "deadline", "today", "hôm nay", "blocker"];
  for (const kw of urgentKws) {
    if (lowerText.includes(kw)) {
      score += 7;
      reasons.push(`⚡ Khẩn: "${kw}"`);
      break;
    }
  }

  if (rawText.includes("figma.com") || rawText.includes("docs.google.com")) {
    score += 6;
    reasons.push("🎨 Kèm link Figma / Doc");
  }

  const designKws = ["design", "ui", "ux", "figma", "quote", "price", "báo giá", "review", "proposal", "contract"];
  for (const kw of designKws) {
    if (lowerText.includes(kw)) {
      score += 4;
      reasons.push(`🎨 Thiết kế/Báo giá: "${kw}"`);
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
  if ((rawText.includes("?") || lowerText.includes("can you") || lowerText.includes("how")) && !msgObj.isReplyToMe) {
    actions.push(`Phản hồi câu hỏi / giải đáp thắc mắc cho <b>${senderName}</b>`);
  }
  if (rawText.includes("figma.com")) {
    actions.push("Mở link Figma đính kèm để kiểm tra layout & chỉnh sửa token");
  } else if (lowerText.includes("figma") || lowerText.includes("ui") || lowerText.includes("ux") || lowerText.includes("design")) {
    actions.push("Kiểm tra / cập nhật file thiết kế theo yêu cầu của khách");
  }
  if (lowerText.includes("quote") || lowerText.includes("price") || lowerText.includes("báo giá") || lowerText.includes("budget") || lowerText.includes("cost")) {
    actions.push(`Gửi Portfolio & Lập phương án báo giá dự toán cho <b>${senderName}</b>`);
  }
  if (lowerText.includes("deadline") || lowerText.includes("urgent") || lowerText.includes("asap") || lowerText.includes("today") || lowerText.includes("gấp")) {
    actions.push("Ưu tiên xử lý sớm để kịp tiến độ bàn giao cho khách");
  }
  if (actions.length === 0) {
    actions.push(`Rà soát nội dung trao đổi và phản hồi lại <b>${senderName}</b>`);
  }

  const actionsText = actions.map(a => `  👉 ${a}`).join('\n');
  const reasonsStr = reasons.length > 0 ? reasons.join(' · ') : 'Tin nhắn khách hàng';
  const timeStr = new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit' });
  const snippet = rawText.length > 130 ? rawText.substring(0, 130) + '...' : rawText;

  const alertMsg = (
    `<b>🟢 [WHATSAPP CLIENT]</b>\n` +
    `${badge} (⭐ <b>${score} điểm</b>)\n` +
    `<i>(${reasonsStr})</i>\n` +
    `━━━━━━━━━━━━━━━━━━━━━\n` +
    `📍 <b>Nguồn:</b> <code>WhatsApp: ${chatName}</code>\n` +
    `👤 <b>Người gửi:</b> <b>${senderName}</b> (⏰ ${timeStr})\n\n` +
    `📝 <b>Ngữ cảnh:</b> <i>"${snippet}"</i>\n\n` +
    `🎯 <b>Hành động Cần làm:</b>\n` +
    `${actionsText}\n\n` +
    `━━━━━━━━━━━━━━━━━━━━━\n` +
    `💡 <i>(Mở app WhatsApp trên điện thoại hoặc máy tính để trả lời khách)</i>`
  );

  sendTelegramMessage(alertMsg);
  console.log(`\n[✓ ĐÃ BẮN CẢNH BÁO WHATSAPP VỀ TELEGRAM] Từ: ${senderName} | Nhóm: ${chatName}`);
}

function saveBatchMessagesToCache(msgs, shouldNotify = false) {
  let waHistory = [];
  try {
    if (fs.existsSync(WA_HISTORY_FILE)) {
      waHistory = JSON.parse(fs.readFileSync(WA_HISTORY_FILE, 'utf8'));
    }
  } catch {}

  const seenIds = new Set(waHistory.map(m => m.id));
  let addedCount = 0;

  for (const msg of msgs) {
    if (!msg || !msg.key) continue;
    const msgId = msg.key.id;
    if (seenIds.has(msgId)) continue;

    const jid = msg.key.remoteJid || '';
    if (jid.includes('status@broadcast')) continue;

    const text = extractMsgText(msg);
    if (!text || !text.trim()) continue;

    const isGroup = jid.endsWith('@g.us');
    let senderName = msg.pushName || CONTACTS_CACHE[msg.key.participant || jid] || jid.split('@')[0];
    let chatName = CHATS_CACHE[jid] || senderName;

    const timestampSec = msg.messageTimestamp ? (typeof msg.messageTimestamp === 'number' ? msg.messageTimestamp : Number(msg.messageTimestamp)) : (Date.now() / 1000);
    const dateObj = new Date(timestampSec * 1000);
    const timeStr = dateObj.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit' });

    waHistory.push({
      id: msgId,
      senderName,
      chatName,
      text,
      isGroup,
      timestamp: timeStr,
      date: dateObj.toISOString(),
      fromMe: msg.key.fromMe || false
    });
    seenIds.add(msgId);
    addedCount++;

    const nowSec = Date.now() / 1000;
    const isRecent = (nowSec - timestampSec) < 300; // Trong vòng 5 phút gần nhất

    if ((shouldNotify || isRecent) && !msg.key.fromMe) {
      processAndForwardMessage({
        senderName,
        chatName,
        text,
        isGroup,
        isReplyToMe: msg.isReplyToMe || false
      });
    }
  }

  // Sắp xếp theo ngày mới nhất lên đầu
  waHistory.sort((a, b) => new Date(b.date) - new Date(a.date));
  if (waHistory.length > 3000) waHistory = waHistory.slice(0, 3000);

  try {
    fs.writeFileSync(WA_HISTORY_FILE, JSON.stringify(waHistory, null, 2), 'utf8');
    if (addedCount > 0) {
      console.log(`[✓] Đã đồng bộ & lập chỉ mục ${addedCount} tin nhắn WhatsApp vào kho tìm kiếm (Tổng: ${waHistory.length})`);
    }
  } catch (e) {
    console.error('Lỗi lưu cache tin nhắn WhatsApp:', e.message);
  }
}

let isFirstTimeQRScan = false;

async function startWhatsAppBridge() {
  const authPath = path.resolve(__dirname, 'auth_info_baileys');
  const { state, saveCreds } = await useMultiFileAuthState(authPath);
  const { version } = await fetchLatestBaileysVersion();

  console.log(`[+] Đang khởi động WhatsApp Socket (Baileys v${version.join('.')})...`);

  const sock = makeWASocket({
    version,
    auth: state,
    logger: pino({ level: 'silent' }),
    printQRInTerminal: false,
    syncFullHistory: true,
    browser: ['Mew Design Ops', 'Chrome', '120.0.0']
  });

  sock.ev.on('creds.update', saveCreds);

  sock.ev.on('contacts.upsert', (contacts) => {
    for (const c of contacts) {
      if (c.id && (c.name || c.notify)) {
        CONTACTS_CACHE[c.id] = c.name || c.notify;
      }
    }
  });

  sock.ev.on('chats.upsert', (chats) => {
    for (const c of chats) {
      if (c.id && (c.name || c.subject)) {
        CHATS_CACHE[c.id] = c.name || c.subject;
      }
    }
  });

  sock.ev.on('messaging-history.set', async ({ chats, contacts, messages, isLatest }) => {
    console.log(`[+] Nhận gói đồng bộ lịch sử toàn diện từ WhatsApp: ${chats?.length || 0} chats, ${messages?.length || 0} tin nhắn.`);
    if (contacts) {
      for (const c of contacts) {
        if (c.id && (c.name || c.notify)) CONTACTS_CACHE[c.id] = c.name || c.notify;
      }
    }
    if (chats) {
      for (const c of chats) {
        if (c.id && (c.name || c.subject)) CHATS_CACHE[c.id] = c.name || c.subject;
      }
    }
    if (messages && messages.length > 0) {
      saveBatchMessagesToCache(messages, false);
    }
  });

  sock.ev.on('connection.update', async (update) => {
    const { connection, lastDisconnect, qr } = update;

    if (qr) {
      isFirstTimeQRScan = true;
      console.log('\n======================================================');
      console.log('📱 MÃ QR KẾT NỐI WHATSAPP:');
      console.log('1. Mở WhatsApp trên điện thoại');
      console.log('2. Vào Cài đặt (Settings) > Thiết bị liên kết (Linked Devices) > Liên kết thiết bị');
      console.log('3. Quét mã QR dưới đây hoặc trên Telegram:');
      console.log('======================================================\n');
      qrcodeTerminal.generate(qr, { small: true });

      const qrImagePath = path.resolve(__dirname, 'whatsapp_qr.png');
      try {
        await QRCode.toFile(qrImagePath, qr, { width: 350, margin: 2 });
        sendTelegramMessage(
          `📱 <b>MÃ QR KẾT NỐI WHATSAPP</b>\n\n` +
          `1. Mở WhatsApp trên điện thoại của bạn.\n` +
          `2. Vào <b>Cài đặt (Settings) > Thiết bị liên kết (Linked Devices) > Liên kết thiết bị</b>.\n` +
          `3. Quét mã QR này để đồng bộ tin nhắn khách hàng!`,
          qrImagePath
        );
      } catch (err) {
        console.error('Lỗi tạo ảnh QR:', err.message);
      }
    }

    if (connection === 'close') {
      const shouldReconnect = (lastDisconnect?.error)?.output?.statusCode !== DisconnectReason.loggedOut;
      console.log(`[!] Kết nối WhatsApp bị ngắt (${lastDisconnect?.error?.message || 'Unknown'}). Tự động kết nối lại: ${shouldReconnect}`);
      if (shouldReconnect) {
        setTimeout(startWhatsAppBridge, 3000);
      }
    } else if (connection === 'open') {
      console.log('\n======================================================');
      console.log('✅ KẾT NỐI WHATSAPP THÀNH CÔNG VÀ ĐANG CHẠY!');
      console.log('Đang đồng bộ toàn bộ lịch sử trò chuyện để lập chỉ mục...');
      console.log('======================================================\n');

      try {
        const groups = await sock.groupFetchAllParticipating();
        for (const [id, g] of Object.entries(groups)) {
          CHATS_CACHE[id] = g.subject;
        }
        console.log(`[+] Đã nạp ${Object.keys(groups).length} nhóm WhatsApp: ${Object.values(groups).map(g => g.subject).join(', ')}`);
      } catch (e) {
        console.error('Lỗi nạp nhóm:', e.message);
      }

      // Chỉ gửi tin nhắn thông báo về Telegram 1 lần duy nhất khi vừa quét mã thành công
      if (!global.hasNotifiedWhatsAppConnected && isFirstTimeQRScan) {
        global.hasNotifiedWhatsAppConnected = true;
        sendTelegramMessage(
          `✅ <b>KẾT NỐI WHATSAPP THÀNH CÔNG!</b>\n` +
          `━━━━━━━━━━━━━━━━━━━━━\n` +
          `Trợ lý <b>Mew Assistant</b> đã kết nối và đang đồng bộ toàn bộ lịch sử trò chuyện WhatsApp để phục vụ tra cứu (/find, /link)!`
        );
      }
    }
  });

  sock.ev.on('messages.upsert', async (m) => {
    try {
      if (m.messages && m.messages.length > 0) {
        saveBatchMessagesToCache(m.messages, m.type === 'notify');
      }
    } catch (err) {
      console.error('[!] Lỗi xử lý tin nhắn WhatsApp:', err.message);
    }
  });
}

startWhatsAppBridge();
