#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Task Monitor & Synthesizer for VNPT Internal Tasks
-----------------------------------------------------------
Tự động lắng nghe các tin nhắn tag/mention trong các nhóm Telegram nội bộ VNPT,
thu thập 10-15 tin nhắn xung quanh để gom ngữ cảnh, tóm tắt nội dung và gửi cảnh báo
vào Telegram cá nhân của bạn kèm tùy chọn tạo SOW & Timeline theo yêu cầu.
"""

import os
import sys
import json
import time
import asyncio
import re
import urllib.request
import urllib.parse
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# Cấu hình đường dẫn
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent
CONFIG_PATH = SCRIPT_DIR / "config.json"
SAMPLE_CONFIG_PATH = SCRIPT_DIR / "config.sample.json"
CACHE_DIR = SCRIPT_DIR / ".task_cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def load_config() -> Dict[str, Any]:
    """Đọc file cấu hình hoặc tạo từ file mẫu"""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    elif SAMPLE_CONFIG_PATH.exists():
        print(f"[!] config.json chưa tồn tại. Đang sử dụng cấu hình mẫu từ {SAMPLE_CONFIG_PATH.name}")
        with open(SAMPLE_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "telegram_notifier_bot": {"bot_token": "", "my_chat_id": ""},
            "settings": {
                "my_usernames": ["@tuanvq", "tuanvq"],
                "keywords": ["Tuấn", "Anh Tuấn", "TuanVQ", "Mew", "URD", "Design", "Figma", "Gấp", "Review"],
                "context_history_limit": 15
            }
        }

def sanitize_filename(name: str) -> str:
    """Loại bỏ ký tự đặc biệt khỏi tên file"""
    return re.sub(r'[\/*?:"<>|]', "", name).strip().replace(" ", "_")

def build_message_link_and_cmd(chat, msg_id: int, fallback_chat_id: Optional[int] = None) -> Tuple[Optional[str], str, str]:
    """Tạo link mở tin nhắn trực tiếp (nếu có), clean_id và link button Xem chi tiết"""
    cid = getattr(chat, "id", fallback_chat_id)
    if not cid:
        return (None, "0", f"https://t.me/mew629_bot?start=view_0_{msg_id}")

    cid_str = str(cid)
    clean_id = cid_str.replace("-", "")
    view_link = f"https://t.me/mew629_bot?start=view_{clean_id}_{msg_id}"

    # 1. Nhóm công khai có username
    if getattr(chat, "username", None):
        return (f"https://t.me/{chat.username}/{msg_id}", clean_id, view_link)

    # 2. Supergroup / Channel (-100...)
    if cid_str.startswith("-100"):
        supergroup_id = cid_str[4:]
        return (f"https://t.me/c/{supergroup_id}/{msg_id}", clean_id, view_link)

    # 3. Basic Group (Nhóm thường) -> Không có link Telegram hợp lệ
    return (None, clean_id, view_link)

async def get_message_context_thread(client, chat_id_raw: str, target_msg_id: int) -> str:
    """Bốc tách đoạn hội thoại xung quanh tin nhắn trực tiếp từ nhóm bằng tài khoản Userbot cá nhân"""
    clean_id = chat_id_raw.replace("-", "").replace("100", "").strip()
    target_entity = None

    # Tìm entity nhóm tương ứng
    id_variants = []
    try:
        id_variants.append(int(chat_id_raw))
    except Exception:
        pass
    try:
        id_variants.append(int(f"-{clean_id}"))
        id_variants.append(int(f"-100{clean_id}"))
        id_variants.append(int(clean_id))
    except Exception:
        pass

    for cid in id_variants:
        try:
            target_entity = await client.get_entity(cid)
            if target_entity:
                break
        except Exception:
            continue

    if not target_entity:
        try:
            dialogs = await client.get_dialogs(limit=60)
            for d in dialogs:
                d_id_clean = str(d.id).replace("-", "").replace("100", "")
                if d_id_clean == clean_id or str(d.id) == chat_id_raw:
                    target_entity = d.entity
                    break
        except Exception:
            pass

    if not target_entity:
        return f"⚠️ Không tìm thấy nhóm chat có ID: <code>{chat_id_raw}</code>"

    group_title = getattr(target_entity, "title", "Nhóm Telegram")
    messages = []

    # 1. Thử kéo trực tiếp dải message id xung quanh
    try:
        start_id = max(1, target_msg_id - 3)
        end_id = target_msg_id + 4
        id_list = list(range(start_id, end_id + 1))
        fetched = await client.get_messages(target_entity, ids=id_list)
        for m in fetched:
            if m and m.raw_text:
                messages.append(m)
    except Exception:
        pass

    # 2. Fallback: Kéo qua iter_messages nếu danh sách rỗng
    if not messages:
        try:
            async for m in client.iter_messages(target_entity, offset_id=target_msg_id + 4, limit=8):
                if m and m.raw_text:
                    messages.append(m)
            messages.reverse()
        except Exception as e:
            return f"⚠️ Lỗi khi trích xuất tin nhắn: {e}"

    if not messages:
        return f"⚠️ Không tìm thấy đoạn hội thoại quanh tin nhắn #{target_msg_id} trong nhóm <b>{group_title}</b>"

    thread_lines = []
    for m in sorted(messages, key=lambda x: x.id):
        sender = await m.get_sender()
        sname = getattr(sender, "first_name", "Thành viên") if sender else "Thành viên"
        if getattr(sender, "last_name", None):
            sname += f" {sender.last_name}"
        time_str = m.date.strftime("%H:%M") if m.date else ""
        text_clean = m.raw_text.strip()

        if m.id == target_msg_id:
            thread_lines.append(
                f"🎯 <b>[{time_str}] {sname}:</b>\n"
                f"🔥 <b><i>\"{text_clean}\"</i></b>"
            )
        else:
            thread_lines.append(
                f"💬 <b>[{time_str}] {sname}:</b> {text_clean}"
            )

    return (
        f"📖 <b>CHI TIẾT TIN NHẮN</b>\n"
        f"📍 <b>Nhóm:</b> <code>{group_title}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n" +
        "\n\n".join(thread_lines) +
        "\n\n━━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 <i>(Được trích xuất trực tiếp bằng tài khoản cá nhân của bạn)</i>"
    )

def score_importance(trigger_msg: Dict[str, Any], context_messages: List[Dict[str, Any]], group_name: str, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Chấm điểm mức độ ưu tiên có trọng số theo phong cách WorkSync Engine"""
    text = (trigger_msg.get("text") or "").lower()
    raw_text = trigger_msg.get("text") or ""
    sender_name = trigger_msg.get("sender_name") or ""
    
    settings = (config or {}).get("settings", {})
    vip_senders = [v.lower() for v in settings.get("vip_senders", ["hà po", "po", "lead", "sếp", "pm", "quynhmaihavi", "lê", "giám đốc"])]
    my_usernames = [u.lower().lstrip("@") for u in settings.get("my_usernames", ["tuanvq", "quctuan"])]

    score = 0
    reasons = []

    # 1. VIP Sender (+15 điểm)
    if any(vip in sender_name.lower() for vip in vip_senders):
        score += 15
        reasons.append("👑 VIP / Sếp / PO")

    # 2. Mention trực tiếp @tuanvq (+12 điểm)
    if any(f"@{u}" in text for u in my_usernames) or trigger_msg.get("is_mentioned"):
        score += 12
        reasons.append("🎯 Tag trực tiếp bạn")

    # 3. Trả lời (Reply) tin nhắn của bạn (+12 điểm - mức ưu tiên ngang với Tag/Mention)
    if trigger_msg.get("is_reply_to_me"):
        score += 12
        reasons.append("🎯 Reply tin nhắn bạn")

    # 4. Có câu hỏi '?' (+8 điểm) - Cần bạn phản hồi
    if "?" in raw_text or any(w in text for w in ["chưa", "không ạ", "sao anh", "sao em", "thế nào", "được ko"]):
        score += 8
        reasons.append("❓ Có câu hỏi / Cần phản hồi")

    # 5. Từ khóa Khẩn cấp / Deadline (+7 điểm)
    urgent_keywords = ["gấp", "khẩn", "asap", "blocker", "cháy", "hotfix", "hôm nay", "trước 12h", "trước 17h", "deadline"]
    for kw in urgent_keywords:
        if kw in text:
            score += 7
            reasons.append(f"⚡ Khẩn: \"{kw}\"")
            break

    # 6. Có link Figma / Google Docs đính kèm (+6 điểm)
    if re.search(r'https?://(?:www\.)?figma\.com/[^\s]+', raw_text) or re.search(r'https?://docs\.google\.com/[^\s]+', raw_text):
        score += 6
        reasons.append("🎨 Kèm link Figma / Doc")

    # 7. Từ khóa Review / Thiết kế (+4 điểm)
    design_keywords = ["review", "duyệt", "chốt", "góp ý", "sửa", "feedback", "luồng", "urd", "motion", "prototype", "animation"]
    for kw in design_keywords:
        if kw in text:
            score += 4
            reasons.append(f"🎨 Thiết kế: \"{kw}\"")
            break

    # Phân cấp mức độ ưu tiên
    if score >= 15:
        level = "CRITICAL"
        badge = "🚨 CRITICAL (CỰC KỲ KHẨN CẤP)"
        emoji_dot = "🔴"
    elif score >= 8:
        level = "HIGH"
        badge = "🔥 HIGH (ƯU TIÊN CAO)"
        emoji_dot = "🟠"
    elif score >= 4:
        level = "NORMAL"
        badge = "🟡 NORMAL (TIÊU CHUẨN)"
        emoji_dot = "🟡"
    else:
        level = "LOW"
        badge = "⚪ LOW (THÔNG TIN)"
        emoji_dot = "⚪"

    return {
        "score": score,
        "level": level,
        "badge": badge,
        "emoji_dot": emoji_dot,
        "reasons": reasons
    }

def extract_smart_action_and_context(trigger_msg: Dict[str, Any], context_messages: List[Dict[str, Any]], scoring: Dict[str, Any]) -> Tuple[str, List[str]]:
    """Trích xuất Ngữ cảnh cô đọng và Hành động cụ thể cần làm (Smart Action Extraction)"""
    text = (trigger_msg.get("text") or "").strip()
    sender = trigger_msg.get("sender_name") or "Đồng nghiệp"
    clean_snippet = text.replace("\n", " ")
    if len(clean_snippet) > 130:
        clean_snippet = clean_snippet[:130] + "..."

    # Xác định ngữ cảnh cốt lõi
    context_sentence = f"<i>\"{clean_snippet}\"</i>"

    # Suy luận hành động cụ thể (Action Needed)
    actions = []
    text_lower = text.lower()

    if trigger_msg.get("is_reply_to_me"):
        actions.append(f"Đọc nội dung phản hồi và tiếp tục trao đổi với <b>{sender}</b>")

    if "?" in text or any(w in text_lower for w in ["chưa", "không", "sao", "được ko", "được không", "thế nào"]):
        if not trigger_msg.get("is_reply_to_me"):
            actions.append(f"Phản hồi câu hỏi / giải đáp thắc mắc cho <b>{sender}</b>")

    if re.search(r'https?://(?:www\.)?figma\.com/[^\s]+', text):
        actions.append("Mở link Figma đính kèm để kiểm tra layout & chỉnh sửa token")
    elif any(w in text_lower for w in ["figma", "layout", "màn hình", "giao diện", "ui", "ux", "motion", "prototype"]):
        actions.append("Cập nhật / chỉnh sửa file thiết kế Figma theo yêu cầu")

    if re.search(r'https?://docs\.google\.com/[^\s]+', text):
        actions.append("Mở tài liệu Google Docs/Sheet đính kèm để đối soát kịch bản & URD")

    if any(w in text_lower for w in ["review", "duyệt", "feedback", "góp ý", "chốt"]):
        actions.append(f"Review giao diện và phản hồi ý kiến chuyên môn với <b>{sender}</b>")

    if any(w in text_lower for w in ["deadline", "gấp", "asap", "hôm nay", "trước 12h", "trước 17h"]):
        actions.append("Ưu tiên xử lý ngay trong ngày để kịp tiến độ bàn giao")

    if not actions:
        actions.append(f"Rà soát nội dung trao đổi và phản hồi lại <b>{sender}</b> nếu cần")

    return (context_sentence, actions)

def format_telegram_alert(task_info: Dict[str, Any]) -> str:
    """Tạo format tin nhắn cảnh báo gửi về Telegram cá nhân chuẩn WorkSync Pro"""
    group_name = task_info.get("group_name", "Nhóm VNPT")
    sender_name = task_info.get("sender_name", "Đồng nghiệp")
    timestamp = task_info.get("timestamp", datetime.now().strftime("%H:%M %d/%m/%Y"))
    context_sentence = task_info.get("context_sentence", "")
    action_items = task_info.get("action_items", ["Rà soát thông tin"])
    msg_link = task_info.get("message_link")
    view_link = task_info.get("view_link", "")
    task_id = task_info.get("task_id", f"TASK_{int(time.time())}")

    scoring = task_info.get("scoring", {})
    badge = scoring.get("badge", "🟡 TIÊU CHUẨN")
    score = scoring.get("score", 5)
    reasons = scoring.get("reasons", [])
    reasons_str = " · ".join(reasons) if reasons else "Từ khóa nội bộ"

    actions_text = "\n".join([f"  👉 {a}" for a in action_items])

    link_lines = []
    if view_link:
        link_lines.append(f"👉 <a href='{view_link}'><b>Xem chi tiết</b></a>")
    if msg_link:
        link_lines.append(f"🔗 <a href='{msg_link}'>Mở tin nhắn</a>")

    links_display = " | ".join(link_lines) if link_lines else ""

    alert_msg = (
        f"{badge} (⭐ <b>{score} điểm</b>)\n"
        f"<i>({reasons_str})</i>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"📍 <b>Nhóm:</b> <code>{group_name}</code>\n"
        f"👤 <b>Người gọi:</b> <b>{sender_name}</b> (⏰ {timestamp})\n\n"
        f"📝 <b>Ngữ cảnh:</b> {context_sentence}\n\n"
        f"🎯 <b>Hành động Cần làm:</b>\n"
        f"{actions_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"{links_display}\n"
        f"<i>(ID: {task_id})</i>"
    )
    return alert_msg

def synthesize_context(messages: List[Dict[str, Any]], trigger_msg: Dict[str, Any], group_name: str, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Phân tích và tóm tắt ngữ cảnh từ danh sách tin nhắn trước đó"""
    sender = trigger_msg.get("sender_name", "Unknown")
    text = trigger_msg.get("text", "")
    task_id = f"VNPT_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Trích xuất link Figma hoặc Doc nếu có trong lịch sử chat
    figma_links = []
    doc_links = []
    all_texts = []

    for m in messages:
        m_text = m.get("text", "")
        all_texts.append(f"{m.get('sender_name', 'User')}: {m_text}")
        found_figma = re.findall(r'https?://(?:www\.)?figma\.com/[^\s]+', m_text)
        found_docs = re.findall(r'https?://docs\.google\.com/[^\s]+', m_text)
        figma_links.extend(found_figma)
        doc_links.extend(found_docs)

    # Chấm điểm ưu tiên thông minh theo WorkSync Engine
    scoring = score_importance(trigger_msg, messages, group_name, config)

    # Trích xuất Ngữ cảnh & Hành động cốt lõi (Action Extraction)
    context_sentence, action_items = extract_smart_action_and_context(trigger_msg, messages, scoring)

    task_data = {
        "task_id": task_id,
        "group_name": group_name,
        "sender_name": sender,
        "timestamp": datetime.now().strftime("%H:%M %d/%m/%Y"),
        "trigger_message": text,
        "context_history": messages,
        "context_sentence": context_sentence,
        "action_items": action_items,
        "scoring": scoring,
        "urgency": scoring.get("badge", "Tiêu chuẩn"),
        "message_link": trigger_msg.get("link", "https://t.me/"),
        "figma_links": list(set(figma_links)),
        "doc_links": list(set(doc_links))
    }

    # Lưu cache để dùng khi cần
    task_cache_file = CACHE_DIR / f"{task_id}.json"
    with open(task_cache_file, "w", encoding="utf-8") as f:
        json.dump(task_data, f, ensure_ascii=False, indent=2)

    return task_data

# -------------------------------------------------------------
# TASK & CHECKLIST MANAGEMENT MODULE (Quản lý Đầu việc & Timeline)
# -------------------------------------------------------------
TASKS_DB_PATH = SCRIPT_DIR / "tasks_db.json"

def load_tasks_db() -> Dict[str, Any]:
    """Đọc dữ liệu checklist từ tasks_db.json"""
    if TASKS_DB_PATH.exists():
        try:
            with open(TASKS_DB_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"checklists": {}, "last_id": 0}
    return {"checklists": {}, "last_id": 0}

def save_tasks_db(data: Dict[str, Any]):
    """Ghi dữ liệu checklist vào tasks_db.json"""
    with open(TASKS_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def calculate_deadline_badge(deadline_str: Optional[str]) -> Tuple[str, str]:
    """Tính toán trạng thái deadline (chỉ định dạng Ngày/Tháng DD/MM hoặc DD/MM/YYYY)"""
    if not deadline_str or deadline_str.strip() == "":
        return ("Không thời hạn", "⚪ Không thời hạn")
    
    clean_d = deadline_str.strip()
    now = datetime.now()
    target_date = None
    
    # Parse DD/MM hoặc DD/MM/YYYY
    parts = clean_d.split("/")
    if len(parts) == 2:
        try:
            d = int(parts[0])
            m = int(parts[1])
            target_date = datetime(now.year, m, d, 23, 59, 59)
        except Exception:
            pass
    elif len(parts) == 3:
        try:
            d = int(parts[0])
            m = int(parts[1])
            y = int(parts[2])
            target_date = datetime(y, m, d, 23, 59, 59)
        except Exception:
            pass
            
    if not target_date:
        return (clean_d, f"📅 {clean_d}")

    today_start = datetime(now.year, now.month, now.day, 0, 0, 0)
    target_day_start = datetime(target_date.year, target_date.month, target_date.day, 0, 0, 0)
    diff_days = (target_day_start - today_start).days
    
    formatted_date = target_date.strftime("%d/%m")
    if diff_days < 0:
        overdue_days = abs(diff_days)
        return (formatted_date, f"🔴 ĐÃ QUÁ HẠN {overdue_days} NGÀY")
    elif diff_days == 0:
        return (formatted_date, "🟡 HÔM NAY HẾT HẠN")
    elif diff_days == 1:
        return (formatted_date, "⏳ Ngày mai hết hạn")
    else:
        return (formatted_date, f"🟢 Còn {diff_days} ngày")

def render_progress_bar(done_count: int, total_count: int, length: int = 10) -> str:
    """Tạo thanh tiến độ trực quan dạng ký tự"""
    if total_count <= 0:
        return "░░░░░░░░░░ 0% (0/0)"
    percent = int((done_count / total_count) * 100)
    filled = int(round((percent / 100) * length))
    filled = min(length, max(0, filled))
    bar = "█" * filled + "░" * (length - filled)
    return f"{bar} {percent}% ({done_count}/{total_count})"

def format_checklist_card(cid: str, data: Dict[str, Any]) -> Tuple[str, dict]:
    """Tạo nội dung tin nhắn và inline buttons cho 1 Checklist chuẩn Telegram Bot API"""
    title = data.get("title", "Checklist Công việc")
    deadline_input = data.get("deadline", "")
    date_display, status_badge = calculate_deadline_badge(deadline_input)
    items = data.get("items", [])

    total_items = len(items)
    done_items = sum(1 for it in items if it.get("done", False))
    progress_str = render_progress_bar(done_items, total_items)

    item_lines = []
    for idx, it in enumerate(items, start=1):
        icon = "✅" if it.get("done", False) else "⬜"
        item_text = it.get("text", "")
        if it.get("done", False):
            item_lines.append(f"  {icon} <s>{idx}. {item_text}</s>")
        else:
            item_lines.append(f"  {icon} <b>{idx}. {item_text}</b>")

    items_display = "\n".join(item_lines) if item_lines else "  <i>(Chưa có đầu việc nào)</i>"

    all_done = (total_items > 0 and done_items == total_items)
    congrats_line = "\n🎉 <b>TẤT CẢ ĐẦU VIỆC ĐÃ HOÀN THÀNH XUẤT SẮC!</b>\n" if all_done else ""

    text_msg = (
        f"📋 <b>[CHECKLIST DỰ ÁN: {title.upper()}]</b> (Mã: <code>#{cid}</code>)\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 <b>Tiến độ:</b> <code>{progress_str}</code>\n"
        f"⏰ <b>Hạn chót:</b> <b>{date_display}</b> ({status_badge})\n"
        f"{congrats_line}\n"
        f"<b>Danh sách công việc:</b>\n"
        f"{items_display}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 <i>Bấm các nút số bên dưới để Tick Hoàn Thành:</i>"
    )

    # Sinh các nút bấm Toggle cho từng item
    inline_keyboard = []
    current_row = []
    for idx, it in enumerate(items, start=1):
        btn_icon = "✅" if it.get("done", False) else "⬜"
        btn_text = f"{idx}. {btn_icon}"
        cb_data = f"chk_{cid}_{idx}"
        current_row.append({"text": btn_text, "callback_data": cb_data})
        if len(current_row) == 4:
            inline_keyboard.append(current_row)
            current_row = []
    if current_row:
        inline_keyboard.append(current_row)

    # Thêm hàng nút quản trị (Xóa / Làm mới)
    admin_row = [
        {"text": "🔄 Làm mới", "callback_data": f"ref_{cid}"},
        {"text": "🗑 Xóa Checklist", "callback_data": f"del_{cid}"}
    ]
    inline_keyboard.append(admin_row)

    return (text_msg, {"inline_keyboard": inline_keyboard})

def parse_new_checklist_input(raw_text: str) -> Tuple[str, str, List[str]]:
    """Phân tích nội dung người dùng nhập để tạo Checklist"""
    lines = [line.strip() for line in raw_text.strip().split("\n") if line.strip()]
    if not lines:
        return ("", "", [])

    # Kiểu 1: Phân cách bằng dấu gạch đứng | trên 1 dòng
    first_line = lines[0]
    if "|" in first_line:
        parts = [p.strip() for p in first_line.split("|")]
        title = parts[0]
        deadline = parts[1] if len(parts) > 1 else ""
        items = []
        if len(parts) > 2:
            raw_subitems = ",".join(parts[2:])
            items = [s.strip() for s in raw_subitems.split(",") if s.strip()]
        return (title, deadline, items)

    # Kiểu 2: Nhập nhiều dòng tự nhiên
    title = lines[0]
    deadline = ""
    items = []

    start_idx = 1
    if len(lines) > 1:
        second_line = lines[1].lower()
        if any(second_line.startswith(k) for k in ["deadline:", "hạn:", "due:", "dl:"]):
            deadline = lines[1].split(":", 1)[1].strip()
            start_idx = 2

    for line in lines[start_idx:]:
        clean_item = re.sub(r'^[-*•\d.]+\s*', '', line).strip()
        if clean_item:
            items.append(clean_item)

    return (title, deadline, items)

def generate_daily_morning_report(checklists: Dict[str, Any]) -> str:
    """Tạo báo cáo nhắc việc tổng quan buổi sáng lúc 08:00 AM"""
    now = datetime.now()
    today_display = now.strftime("%d/%m/%Y")
    
    overdue_tasks = []
    today_tasks = []
    active_summary = []

    for cid, data in checklists.items():
        title = data.get("title", "Dự án")
        deadline = data.get("deadline", "")
        date_display, status_badge = calculate_deadline_badge(deadline)
        items = data.get("items", [])
        total = len(items)
        done = sum(1 for it in items if it.get("done", False))
        
        if total > 0 and done == total:
            continue  # Đã xong 100%, bỏ qua
            
        progress = render_progress_bar(done, total, length=8)
        
        if "QUÁ HẠN" in status_badge:
            overdue_tasks.append(f"  🔴 <b>{title}</b> (Hạn: {date_display} - {status_badge})\n     └ Tiến độ: {progress}")
        elif "HÔM NAY" in status_badge:
            today_tasks.append(f"  🟡 <b>{title}</b> (Hạn: Hôm nay)\n     └ Tiến độ: {progress}")
        else:
            active_summary.append(f"  🔹 <b>{title}</b> (Hạn: {date_display} - {status_badge})\n     └ Tiến độ: {progress}")

    sections = [
        f"🌅 <b>BÁO CÁO CÔNG VIỆC ĐẦU NGÀY ({today_display} - 08:00 AM)</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━"
    ]

    if overdue_tasks:
        sections.append("🚨 <b>CÔNG VIỆC ĐANG QUÁ HẠN:</b>\n" + "\n".join(overdue_tasks))
    
    if today_tasks:
        sections.append("🎯 <b>CÔNG VIỆC CẦN HOÀN THÀNH HÔM NAY:</b>\n" + "\n".join(today_tasks))

    if active_summary:
        sections.append("📋 <b>CÁC DỰ ÁN ĐANG THỰC HIỆN:</b>\n" + "\n".join(active_summary))

    if not overdue_tasks and not today_tasks and not active_summary:
        sections.append("🎉 <i>Tuyệt vời! Bạn không còn đầu việc nào tồn đọng.</i>")

    sections.append("\n💡 <i>Gõ <code>/todo</code> để mở bảng điều khiển checklist và tick hoàn thành.</i>")
    return "\n\n".join(sections)

def bot_api_call(bot_token: str, method: str, payload: dict = None, timeout: int = 30) -> dict:
    """Gọi trực tiếp Telegram Bot API qua HTTP REST chuẩn"""
    url = f"https://api.telegram.org/bot{bot_token}/{method}"
    headers = {"Content-Type": "application/json"}
    data = json.dumps(payload).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"ok": False, "error": str(e)}

async def bot_api_call_async(bot_token: str, method: str, payload: dict = None, timeout: int = 30) -> dict:
    """Bọc gọi Bot API không đồng bộ (non-blocking thread)"""
    return await asyncio.to_thread(bot_api_call, bot_token, method, payload, timeout)

async def send_bot_message(bot_token: str, chat_id: int, text: str, reply_markup: dict = None, link_preview: bool = False) -> dict:
    """Gửi tin nhắn Telegram qua Bot API"""
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": not link_preview
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return await bot_api_call_async(bot_token, "sendMessage", payload)

async def edit_bot_message(bot_token: str, chat_id: int, message_id: int, text: str, reply_markup: dict = None, link_preview: bool = False) -> dict:
    """Chỉnh sửa tin nhắn kèm Inline Buttons tức thì"""
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": not link_preview
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return await bot_api_call_async(bot_token, "editMessageText", payload)

async def answer_callback(bot_token: str, callback_query_id: str, text: str = None) -> dict:
    """Phản hồi thông báo Toast popup khi người dùng bấm Inline Button"""
    payload = {"callback_query_id": callback_query_id}
    if text:
        payload["text"] = text
    return await bot_api_call_async(bot_token, "answerCallbackQuery", payload)

async def daily_morning_reminder_loop(bot_token: str, target_chat_id: int):
    """Tiến trình ngầm gửi Báo cáo công việc tự động vào buổi sáng (từ 08:00 AM trở đi hoặc khi máy thức dậy)"""
    while True:
        try:
            now = datetime.now()
            today_str = now.strftime("%Y-%m-%d")
            db = load_tasks_db()
            last_sent_date = db.get("last_morning_report_date", "")

            # Gửi lúc 08:00 sáng hoặc gửi bù ngay khi bật máy/thức dậy trong buổi sáng (từ 08:00 đến 18:00) nếu hôm nay chưa gửi
            if now.hour >= 8 and last_sent_date != today_str:
                db["last_morning_report_date"] = today_str
                save_tasks_db(db)
                
                checklists = db.get("checklists", {})
                if checklists:
                    report_text = generate_daily_morning_report(checklists)
                    if bot_token and target_chat_id:
                        await send_bot_message(bot_token, target_chat_id, report_text)
                        print(f"[✓] Đã tự động gửi Báo cáo nhắc việc sáng ({today_str} lúc {now.strftime('%H:%M')})")
            await asyncio.sleep(30)
        except Exception as e:
            print(f"[!] Lỗi trong daily_morning_reminder_loop: {e}")
            await asyncio.sleep(30)

def run_mock_simulation():
    """Chạy thử nghiệm giả lập một tình huống tin nhắn tag tên tại VNPT"""
    print("\n--- 🧪 BẮT ĐẦU MÔ PHỎNG SỰ KIỆN MENTION TẠI NHÓM VNPT ---")
    
    mock_group = "Dự án My VNPT - Phân hệ C06 & SmartCA"
    mock_history = [
        {"sender_name": "Trưởng nhóm PM", "text": "Hôm nay bên kỹ thuật đã hoàn thành luồng xác thực C06."},
        {"sender_name": "Dev Lead", "text": "Còn vướng chỗ popup xác thực vân tay và camera nhận diện khuôn mặt."},
        {"sender_name": "Tester QA", "text": "Màn hình chưa có xử lý trường hợp người dùng từ chối cấp quyền camera."},
        {"sender_name": "BA My VNPT", "text": "Cần thêm case fallback sang mã PIN OTP khi nhận diện thất bại quá 3 lần."},
        {"sender_name": "Trưởng nhóm PM", "text": "Tài liệu URD đã cập nhật tại https://docs.google.com/document/d/mock-c06-spec"},
        {"sender_name": "Trưởng nhóm PM", "text": "@tuanvq Anh Tuấn xem lại giúp em luồng UX này trên Figma https://figma.com/file/mock-myvnpt và bổ sung case lỗi nhé, cần gấp mai demo với Lãnh đạo."}
    ]
    
    trigger_msg = mock_history[-1]
    trigger_msg["link"] = "https://t.me/c/123456789/999"

    print(f"[1] Phát hiện tin nhắn tag tên: '{trigger_msg['text']}' trong nhóm '{mock_group}'")
    print(f"[2] Kéo {len(mock_history)} tin nhắn liền trước để trích xuất ngữ cảnh...")
    
    task_data = synthesize_context(mock_history, trigger_msg, mock_group)
    alert_text = format_telegram_alert(task_data)

    print("\n[3] 📨 NỘI DUNG THÔNG BÁO GỬI VỀ TELEGRAM CÁ NHÂN:")
    print("--------------------------------------------------")
    print(alert_text.replace("<b>", "").replace("</b>", "").replace("<code>", "`").replace("</code>", "`").replace("<a href='", "[").replace("'>", "](").replace("</a>", ")").replace("<i>", "").replace("</i>", ""))
    print("--------------------------------------------------")

    # Thử nghiệm sinh SOW khi có yêu cầu
    print("\n[4] ⚡ Giả lập người dùng bấm yêu cầu tạo SOW (/sow)...")
    sow_path = generate_sow_document(task_data["task_id"])
    if sow_path and sow_path.exists():
        print(f"[✓] File SOW đã được lưu tại: {sow_path}")
        print("--- 🎉 HOÀN THÀNH MÔ PHỎNG THÀNH CÔNG ---")

# Bộ nhớ tạm lưu truy vấn tìm kiếm phục vụ lọc kênh qua Inline Buttons
SEARCH_QUERY_CACHE: Dict[str, Dict[str, Any]] = {}

def get_active_channels(config: Dict[str, Any]) -> List[str]:
    """Lấy danh sách các channel đang ở trạng thái true"""
    active = config.get("active_channels", {"telegram": True, "whatsapp": False, "zalo": False})
    return [k for k, v in active.items() if v]

def parse_channel_prefix_from_query(query: str) -> Tuple[Optional[str], str]:
    """Bóc tách channel prefix nếu user nhập: /find tele figma, /find wa deadline, /find all c06"""
    clean = query.strip()
    parts = clean.split(maxsplit=1)
    if not parts:
        return None, ""
    
    first = parts[0].lower()
    remainder = parts[1].strip() if len(parts) > 1 else ""

    if first in ["tele", "tg", "telegram"]:
        return "telegram", remainder
    elif first in ["wa", "whatsapp"]:
        return "whatsapp", remainder
    elif first in ["zl", "zalo"]:
        return "zalo", remainder
    elif first in ["all", "tatca", "toanbo"]:
        return "all", remainder
    
    return None, clean

async def search_messages_across_groups(client, query: str, limit: int = 8, channel_filter: str = "all") -> str:
    """Tìm kiếm tin nhắn chứa từ khóa với bộ lọc kênh độc lập (telegram, whatsapp, zalo, all)"""
    results = []
    seen_msg_ids = set()
    clean_query = query.strip()
    query_lower = clean_query.lower()

    try:
        # Nhánh 1: Quét trên Telegram VNPT (nếu channel_filter là all hoặc telegram)
        if channel_filter in ["all", "telegram"]:
            # 1. Telegram Global Search API
            try:
                async for msg in client.iter_messages(None, search=clean_query, limit=30):
                    if not (msg.is_group or msg.is_channel):
                        continue
                    if msg.id in seen_msg_ids:
                        continue
                    seen_msg_ids.add(msg.id)

                    chat = await msg.get_chat()
                    title = getattr(chat, "title", "Nhóm Telegram")
                    sender = await msg.get_sender()
                    sender_name = getattr(sender, "first_name", "Đồng nghiệp") if sender else "Đồng nghiệp"
                    time_str = msg.date.strftime("%d/%m %H:%M") if msg.date else ""

                    direct_link, clean_id, view_link = build_message_link_and_cmd(chat, msg.id, fallback_chat_id=getattr(msg, "chat_id", None))

                    snippet = (msg.raw_text or "").replace("\n", " ")
                    if len(snippet) > 130:
                        snippet = snippet[:130] + "..."

                    action_lines = [f"👉 <a href='{view_link}'><b>Xem chi tiết</b></a>"]
                    if direct_link:
                        action_lines.append(f"🔗 <a href='{direct_link}'>Mở tin nhắn</a>")

                    link_line = " | ".join(action_lines)

                    results.append(
                        f"🔷 <b>Nhóm VNPT:</b> <code>{title}</code>\n"
                        f"👤 <b>Từ:</b> {sender_name} (⏰ {time_str})\n"
                        f"💬 <i>\"{snippet}\"</i>\n"
                        f"{link_line}"
                    )
                    if len(results) >= limit:
                        break
            except Exception as e:
                print(f"[!] Global search notice: {e}")

            # 2. Quét trực tiếp tin nhắn gần đây trong các nhóm Telegram
            if len(results) < limit:
                dialogs = await client.get_dialogs(limit=30)
                group_dialogs = [d for d in dialogs if d.is_group or d.is_channel]
                for d in group_dialogs:
                    if len(results) >= limit:
                        break
                    try:
                        async for msg in client.iter_messages(d.entity, limit=25):
                            if not msg.raw_text:
                                continue
                            if msg.id in seen_msg_ids:
                                continue
                            if query_lower in msg.raw_text.lower():
                                seen_msg_ids.add(msg.id)
                                sender = await msg.get_sender()
                                sender_name = getattr(sender, "first_name", "Đồng nghiệp") if sender else "Đồng nghiệp"
                                time_str = msg.date.strftime("%d/%m %H:%M") if msg.date else ""

                                direct_link, clean_id, view_link = build_message_link_and_cmd(d.entity, msg.id, fallback_chat_id=d.id)

                                snippet = msg.raw_text.replace("\n", " ")
                                if len(snippet) > 130:
                                    snippet = snippet[:130] + "..."

                                action_lines = [f"👉 <a href='{view_link}'><b>Xem chi tiết</b></a>"]
                                if direct_link:
                                    action_lines.append(f"🔗 <a href='{direct_link}'>Mở tin nhắn</a>")

                                link_line = " | ".join(action_lines)

                                results.append(
                                    f"🔷 <b>Nhóm VNPT:</b> <code>{d.title}</code>\n"
                                    f"👤 <b>Từ:</b> {sender_name} (⏰ {time_str})\n"
                                    f"💬 <i>\"{snippet}\"</i>\n"
                                    f"{link_line}"
                                )
                                if len(results) >= limit:
                                    break
                    except Exception:
                        continue

        # Nhánh 2: Quét tin nhắn WhatsApp (nếu channel_filter là all hoặc whatsapp)
        if channel_filter in ["all", "whatsapp"]:
            WA_MSG_FILE = SCRIPT_DIR / "bridges" / "whatsapp" / "whatsapp_messages.json"
            if WA_MSG_FILE.exists() and len(results) < limit:
                try:
                    with open(WA_MSG_FILE, "r", encoding="utf-8") as f:
                        wa_msgs = json.load(f)
                    for w in wa_msgs:
                        if len(results) >= limit:
                            break
                        w_text = w.get("text", "")
                        w_chat = w.get("chatName", "WhatsApp")
                        w_sender = w.get("senderName", "Khách hàng")
                        w_time = w.get("timestamp", "")

                        if query_lower in w_text.lower() or query_lower in w_chat.lower() or query_lower in w_sender.lower():
                            snippet = w_text.replace("\n", " ")
                            if len(snippet) > 130:
                                snippet = snippet[:130] + "..."

                            results.append(
                                f"🟢 <b>Nguồn:</b> <code>WhatsApp: {w_chat}</code>\n"
                                f"👤 <b>Từ:</b> {w_sender} (⏰ {w_time})\n"
                                f"💬 <i>\"{snippet}\"</i>\n"
                                f"💡 <i>(Mở app WhatsApp để phản hồi)</i>"
                            )
                except Exception as e:
                    print(f"[!] WA search notice: {e}")

        # Nhánh 3: Quét tin nhắn Zalo (nếu channel_filter là all hoặc zalo)
        if channel_filter in ["all", "zalo"]:
            ZL_MSG_FILE = SCRIPT_DIR / "bridges" / "zalo" / "zalo_messages.json"
            if ZL_MSG_FILE.exists() and len(results) < limit:
                try:
                    with open(ZL_MSG_FILE, "r", encoding="utf-8") as f:
                        zl_msgs = json.load(f)
                    for z in zl_msgs:
                        if len(results) >= limit:
                            break
                        z_text = z.get("text", "")
                        z_chat = z.get("chatName", "Zalo")
                        z_sender = z.get("senderName", "Khách hàng")
                        z_time = z.get("timestamp", "")

                        if query_lower in z_text.lower() or query_lower in z_chat.lower() or query_lower in z_sender.lower():
                            snippet = z_text.replace("\n", " ")
                            if len(snippet) > 130:
                                snippet = snippet[:130] + "..."

                            results.append(
                                f"🔵 <b>Nguồn:</b> <code>Zalo: {z_chat}</code>\n"
                                f"👤 <b>Từ:</b> {z_sender} (⏰ {z_time})\n"
                                f"💬 <i>\"{snippet}\"</i>\n"
                                f"💡 <i>(Mở app Zalo để phản hồi)</i>"
                            )
                except Exception as e:
                    print(f"[!] ZL search notice: {e}")

        channel_titles = {
            "telegram": "🔷 [TELEGRAM VNPT]",
            "whatsapp": "🟢 [WHATSAPP CLIENT]",
            "zalo": "🔵 [ZALO CLIENT]",
            "all": "🌐 TOÀN BỘ KÊNH"
        }
        filter_header = channel_titles.get(channel_filter, "🌐 TOÀN BỘ KÊNH")

        if not results:
            return f"🔍 <b>Không tìm thấy tin nhắn nào trên {filter_header} chứa:</b> <code>{query}</code>\n💡 <i>Mẹo: Hãy thử tìm các từ khóa như: <code>figma</code>, <code>myvnpt</code>, <code>sim</code>, <code>font</code>...</i>"

        return (
            f"🔎 <b>KẾT QUẢ TÌM KIẾM TRÊN {filter_header} CHO:</b> <code>{query}</code> ({len(results)} kết quả)\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n\n" +
            "\n\n━━━━━━━━━━━━━━━━━━━━━\n\n".join(results)
        )
    except Exception as e:
        return f"⚠️ <b>Lỗi khi tìm kiếm:</b> {e}"

async def extract_recent_links_across_groups(client, query: Optional[str] = None, limit: int = 8, channel_filter: str = "all") -> str:
    """Tìm và lọc tất cả các link Figma, Google Docs, Sheet theo bộ lọc kênh (telegram, whatsapp, zalo, all)"""
    results = []
    seen_urls = set()
    clean_query = query.strip().lower() if query else None

    # Danh sách các domain tài liệu cần bắt
    doc_patterns = [
        ("🎨 Figma", r'https?://(?:www\.)?figma\.com/[^\s<>"\']+'),
        ("📊 Google Sheet", r'https?://docs\.google\.com/spreadsheets/[^\s<>"\']+'),
        ("📄 Google Doc", r'https?://docs\.google\.com/document/[^\s<>"\']+'),
        ("📑 Google Slide", r'https?://docs\.google\.com/presentation/[^\s<>"\']+'),
        ("📁 Google Drive", r'https?://drive\.google\.com/[^\s<>"\']+'),
        ("📓 Notion", r'https?://(?:www\.)?notion\.(?:so|site)/[^\s<>"\']+'),
        ("📋 Miro", r'https?://(?:www\.)?miro\.com/[^\s<>"\']+')
    ]

    try:
        # Nhánh 1: Quét link Telegram VNPT (nếu channel_filter là all hoặc telegram)
        if channel_filter in ["all", "telegram"]:
            if clean_query:
                try:
                    async for msg in client.iter_messages(None, search=clean_query, limit=35):
                        if not (msg.is_group or msg.is_channel) or not msg.raw_text:
                            continue
                        
                        found_links = []
                        for label, pattern in doc_patterns:
                            matches = re.findall(pattern, msg.raw_text)
                            for m in matches:
                                if m not in seen_urls:
                                    seen_urls.add(m)
                                    found_links.append((label, m))

                        if found_links:
                            chat = await msg.get_chat()
                            title = getattr(chat, "title", "Nhóm Telegram")
                            sender = await msg.get_sender()
                            sender_name = getattr(sender, "first_name", "Đồng nghiệp") if sender else "Đồng nghiệp"
                            time_str = msg.date.strftime("%d/%m %H:%M") if msg.date else ""
                            direct_link, clean_id, view_link = build_message_link_and_cmd(chat, msg.id, fallback_chat_id=getattr(msg, "chat_id", None))

                            snippet = msg.raw_text.replace("\n", " ")
                            if len(snippet) > 110:
                                snippet = snippet[:110] + "..."

                            links_formatted = []
                            for label, url in found_links:
                                short_url = url.split("?")[0]
                                if len(short_url) > 42:
                                    short_url = short_url[:42] + "..."
                                links_formatted.append(f"{label}: <a href='{url}'>{short_url}</a>")

                            links_str = "\n".join(links_formatted)
                            action_lines = [f"👉 <a href='{view_link}'><b>Xem chi tiết</b></a>"]
                            if direct_link:
                                action_lines.append(f"🔗 <a href='{direct_link}'>Mở tin nhắn</a>")

                            results.append(
                                f"🔷 <b>Nhóm VNPT:</b> <code>{title}</code>\n"
                                f"👤 <b>Từ:</b> {sender_name} (⏰ {time_str})\n"
                                f"💬 <i>\"{snippet}\"</i>\n"
                                f"{links_str}\n"
                                f"{' | '.join(action_lines)}"
                            )
                            if len(results) >= limit:
                                break
                except Exception as e:
                    print(f"[!] Links global search notice: {e}")

            if len(results) < limit:
                dialogs = await client.get_dialogs(limit=35)
                group_dialogs = [d for d in dialogs if d.is_group or d.is_channel]

                for d in group_dialogs:
                    if len(results) >= limit:
                        break
                    try:
                        async for msg in client.iter_messages(d.entity, limit=25):
                            if not msg.raw_text:
                                continue

                            if clean_query:
                                match_text = clean_query in msg.raw_text.lower() or clean_query in d.title.lower()
                                if not match_text:
                                    continue

                            found_links = []
                            for label, pattern in doc_patterns:
                                matches = re.findall(pattern, msg.raw_text)
                                for m in matches:
                                    if m not in seen_urls:
                                        seen_urls.add(m)
                                        found_links.append((label, m))

                            if found_links:
                                sender = await msg.get_sender()
                                sender_name = getattr(sender, "first_name", "Đồng nghiệp") if sender else "Đồng nghiệp"
                                time_str = msg.date.strftime("%d/%m %H:%M") if msg.date else ""
                                direct_link, clean_id, view_link = build_message_link_and_cmd(d.entity, msg.id, fallback_chat_id=d.id)

                                snippet = msg.raw_text.replace("\n", " ")
                                if len(snippet) > 110:
                                    snippet = snippet[:110] + "..."

                                links_formatted = []
                                for label, url in found_links:
                                    short_url = url.split("?")[0]
                                    if len(short_url) > 42:
                                        short_url = short_url[:42] + "..."
                                    links_formatted.append(f"{label}: <a href='{url}'>{short_url}</a>")

                                links_str = "\n".join(links_formatted)
                                action_lines = [f"👉 <a href='{view_link}'><b>Xem chi tiết</b></a>"]
                                if direct_link:
                                    action_lines.append(f"🔗 <a href='{direct_link}'>Mở tin nhắn</a>")

                                results.append(
                                    f"🔷 <b>Nhóm VNPT:</b> <code>{d.title}</code>\n"
                                    f"👤 <b>Từ:</b> {sender_name} (⏰ {time_str})\n"
                                    f"💬 <i>\"{snippet}\"</i>\n"
                                    f"{links_str}\n"
                                    f"{' | '.join(action_lines)}"
                                )
                                if len(results) >= limit:
                                    break
                    except Exception:
                        continue

        # Nhánh 2: Lọc link từ tin nhắn WhatsApp (nếu channel_filter là all hoặc whatsapp)
        if channel_filter in ["all", "whatsapp"]:
            WA_MSG_FILE = SCRIPT_DIR / "bridges" / "whatsapp" / "whatsapp_messages.json"
            if WA_MSG_FILE.exists() and len(results) < limit:
                try:
                    with open(WA_MSG_FILE, "r", encoding="utf-8") as f:
                        wa_msgs = json.load(f)
                    for w in wa_msgs:
                        if len(results) >= limit:
                            break
                        w_text = w.get("text", "")
                        w_chat = w.get("chatName", "WhatsApp")
                        w_sender = w.get("senderName", "Khách hàng")
                        w_time = w.get("timestamp", "")

                        if clean_query:
                            match_text = clean_query in w_text.lower() or clean_query in w_chat.lower()
                            if not match_text:
                                continue

                        found_links = []
                        for label, pattern in doc_patterns:
                            matches = re.findall(pattern, w_text)
                            for m in matches:
                                if m not in seen_urls:
                                    seen_urls.add(m)
                                    found_links.append((label, m))

                        if found_links:
                            snippet = w_text.replace("\n", " ")
                            if len(snippet) > 110:
                                snippet = snippet[:110] + "..."

                            links_formatted = []
                            for label, url in found_links:
                                short_url = url.split("?")[0]
                                if len(short_url) > 42:
                                    short_url = short_url[:42] + "..."
                                links_formatted.append(f"{label}: <a href='{url}'>{short_url}</a>")

                            links_str = "\n".join(links_formatted)
                            results.append(
                                f"🟢 <b>Nguồn:</b> <code>WhatsApp: {w_chat}</code>\n"
                                f"👤 <b>Từ:</b> {w_sender} (⏰ {w_time})\n"
                                f"💬 <i>\"{snippet}\"</i>\n"
                                f"{links_str}\n"
                                f"💡 <i>(Mở app WhatsApp để xem file)</i>"
                            )
                except Exception as e:
                    print(f"[!] WA links notice: {e}")

        # Nhánh 3: Lọc link từ tin nhắn Zalo (nếu channel_filter là all hoặc zalo)
        if channel_filter in ["all", "zalo"]:
            ZL_MSG_FILE = SCRIPT_DIR / "bridges" / "zalo" / "zalo_messages.json"
            if ZL_MSG_FILE.exists() and len(results) < limit:
                try:
                    with open(ZL_MSG_FILE, "r", encoding="utf-8") as f:
                        zl_msgs = json.load(f)
                    for z in zl_msgs:
                        if len(results) >= limit:
                            break
                        z_text = z.get("text", "")
                        z_chat = z.get("chatName", "Zalo")
                        z_sender = z.get("senderName", "Khách hàng")
                        z_time = z.get("timestamp", "")

                        if clean_query:
                            match_text = clean_query in z_text.lower() or clean_query in z_chat.lower()
                            if not match_text:
                                continue

                        found_links = []
                        for label, pattern in doc_patterns:
                            matches = re.findall(pattern, z_text)
                            for m in matches:
                                if m not in seen_urls:
                                    seen_urls.add(m)
                                    found_links.append((label, m))

                        if found_links:
                            snippet = z_text.replace("\n", " ")
                            if len(snippet) > 110:
                                snippet = snippet[:110] + "..."

                            links_formatted = []
                            for label, url in found_links:
                                short_url = url.split("?")[0]
                                if len(short_url) > 42:
                                    short_url = short_url[:42] + "..."
                                links_formatted.append(f"{label}: <a href='{url}'>{short_url}</a>")

                            links_str = "\n".join(links_formatted)
                            results.append(
                                f"🔵 <b>Nguồn:</b> <code>Zalo: {z_chat}</code>\n"
                                f"👤 <b>Từ:</b> {z_sender} (⏰ {z_time})\n"
                                f"💬 <i>\"{snippet}\"</i>\n"
                                f"{links_str}\n"
                                f"💡 <i>(Mở app Zalo để xem file)</i>"
                            )
                except Exception as e:
                    print(f"[!] ZL links notice: {e}")

        channel_titles = {
            "telegram": "🔷 [TELEGRAM VNPT]",
            "whatsapp": "🟢 [WHATSAPP CLIENT]",
            "zalo": "🔵 [ZALO CLIENT]",
            "all": "🌐 TOÀN BỘ KÊNH"
        }
        filter_header = channel_titles.get(channel_filter, "🌐 TOÀN BỘ KÊNH")

        if not results:
            if clean_query:
                return f"🔍 <b>Không tìm thấy tài liệu/link nào trên {filter_header} liên quan đến:</b> <code>{query}</code>\n💡 <i>Mẹo: Thử gõ <code>/links figma</code> hoặc <code>/links docs</code></i>"
            else:
                return f"🔗 <b>Chưa tìm thấy link Figma hoặc Google Docs nào gần đây trên {filter_header}.</b>"

        header_title = f"🔗 <b>TÀI LIỆU & LINK THIẾT KẾ TRÊN {filter_header} CHO:</b> <code>{query}</code>" if clean_query else f"🔗 <b>DANH SÁCH LINK FIGMA & DOCS GẦN ĐÂY ({filter_header})</b>"

        return (
            f"{header_title} ({len(results)} kết quả)\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n\n" +
            "\n\n━━━━━━━━━━━━━━━━━━━━━\n\n".join(results)
        )
    except Exception as e:
        return f"⚠️ <b>Lỗi khi lọc link:</b> {e}"

def get_help_menu() -> str:
    """Menu hướng dẫn các lệnh điều khiển bot"""
    return (
        "🤖 <b>BẢNG ĐIỀU KHIỂN TRỢ LÝ MEW DESIGN OPS</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📋 <b>QUẢN LÝ CHECKLIST & TIMELINE:</b>\n"
        "• <code>/todo</code> hoặc <code>/tasks</code> - Xem danh sách checklist công việc & tiến độ\n"
        "• <code>/add &lt;nội_dung&gt;</code> - Tạo checklist mới kèm deadline (DD/MM)\n"
        "  <i>Ví dụ 1 dòng: <code>/add C06 | 15/08 | Khảo sát, Wireframe, UI Figma</code></i>\n"
        "  <i>Ví dụ nhiều dòng:</i>\n"
        "  <code>/add Dự án SIM C06\n"
        "Deadline: 15/08\n"
        "- Khảo sát luồng cũ\n"
        "- Thiết kế UI Figma\n"
        "- Review với PO</code>\n\n"
        "🔍 <b>TÌM KIẾM & LỌC TIN NHẮN:</b>\n"
        "• <code>/find &lt;từ_khóa&gt;</code> - Tìm tin nhắn chứa từ khóa xuyên suốt mọi nhóm\n"
        "  <i>Ví dụ: <code>/find Figma C06</code> hoặc <code>/find deadline</code></i>\n\n"
        "📖 <b>CHI TIẾT TIN NHẮN:</b>\n"
        "• Nhấp vào link hoặc nút <b>Xem chi tiết</b> dưới mỗi tin nhắn để đọc toàn bộ ngữ cảnh hội thoại\n\n"
        "🔗 <b>LỌC TÀI LIỆU & LINK THIẾT KẾ:</b>\n"
        "• <code>/links [từ_khóa]</code> - Gom và tìm nhanh các link Figma, Google Docs/Sheets theo dự án\n"
        "  <i>Ví dụ: <code>/links C06</code> hoặc <code>/links figma</code> hoặc <code>/links</code></i>\n\n"
        "👑 <b>QUẢN LÝ VIP SENDERS (ƯU TIÊN):</b>\n"
        "• <code>/vip</code> - Xem danh sách người gửi ưu tiên (Sếp/PO/Lead)\n"
        "• <code>/vip add &lt;tên&gt;</code> - Thêm người vào danh sách VIP\n"
        "• <code>/vip del &lt;tên&gt;</code> - Xóa người khỏi danh sách VIP\n\n"
        "🌅 <b>NHẮC VIỆC TỰ ĐỘNG:</b>\n"
        "• Đúng <b>08:00 Sáng mỗi ngày</b>, Bot tự động gửi Báo cáo việc cần làm trong ngày và cảnh báo các việc sắp/quá hạn! (Gõ <code>/report</code> để xem ngay)"
    )

async def scan_recent_missed_mentions(client, bot_token: str, config: Dict[str, Any], processed_ids: set):
    """Quét bù các tin nhắn tag tên hoặc reply bị lỡ trong thời gian bot khởi động lại hoặc máy sleep"""
    try:
        await asyncio.sleep(3)
        my_id = (await client.get_me()).id
        settings = config.get("settings", {})
        my_usernames = [u.lower().lstrip("@") for u in settings.get("my_usernames", ["tuanvq", "quctuan"])]
        keywords = [k.lower() for k in settings.get("keywords", ["Tuấn", "URD", "Design", "Figma", "Gấp"])]
        history_limit = settings.get("context_history_limit", 15)
        target_chat_id = config.get("telegram_notifier_bot", {}).get("my_chat_id", 1083272610)

        print("[+] Đang kiểm tra quét bù các tin nhắn nhắc tên gần nhất...")
        async for dialog in client.iter_dialogs(limit=30):
            if not (dialog.is_group or dialog.is_channel):
                continue
            async for msg in client.iter_messages(dialog.id, limit=5):
                if msg.id in processed_ids or msg.sender_id == my_id:
                    continue
                sender = await msg.get_sender()
                if not sender or getattr(sender, "bot", False):
                    continue

                text = msg.raw_text or ""
                text_lower = text.lower()
                is_mentioned = msg.mentioned or any(f"@{u}" in text_lower for u in my_usernames)
                is_reply_to_me = False
                if msg.is_reply:
                    reply_msg = await msg.get_reply_message()
                    if reply_msg and reply_msg.sender_id == my_id:
                        is_reply_to_me = True

                matched_keywords = [k for k in keywords if k in text_lower]

                if is_mentioned or is_reply_to_me:
                    now_utc = datetime.now(timezone.utc)
                    msg_date = msg.date
                    if msg_date and (now_utc - msg_date).total_seconds() > 7200:
                        continue

                    processed_ids.add(msg.id)
                    sender_name = getattr(sender, "first_name", "Đồng nghiệp")
                    if getattr(sender, "last_name", None):
                        sender_name += f" {sender.last_name}"

                    direct_link, clean_id, view_link = build_message_link_and_cmd(dialog.entity, msg.id, fallback_chat_id=dialog.id)

                    trigger_msg = {
                        "sender_name": sender_name,
                        "text": text,
                        "link": direct_link,
                        "view_link": view_link,
                        "is_mentioned": is_mentioned,
                        "is_reply_to_me": is_reply_to_me
                    }

                    history_messages = []
                    async for m in client.iter_messages(dialog.id, limit=history_limit, max_id=msg.id):
                        m_sender = await m.get_sender()
                        m_name = getattr(m_sender, "first_name", "User") if m_sender else "User"
                        if m.raw_text:
                            history_messages.append({"sender_name": m_name, "text": m.raw_text})

                    history_messages.reverse()
                    history_messages.append(trigger_msg)

                    task_data = synthesize_context(history_messages, trigger_msg, dialog.name, config=config)
                    task_data["view_link"] = view_link
                    task_data["message_link"] = direct_link
                    alert_text = format_telegram_alert(task_data)

                    if bot_token and target_chat_id:
                        btn_row = [{"text": "📖 Xem chi tiết", "url": view_link}]
                        if direct_link:
                            btn_row.append({"text": "🔗 Mở tin nhắn", "url": direct_link})
                        reply_markup = {"inline_keyboard": [btn_row]}
                        await send_bot_message(bot_token, int(target_chat_id), alert_text, reply_markup=reply_markup)
                        print(f"[✓ Quét bù] Đã gửi cảnh báo bị lỡ từ nhóm '{dialog.name}'!")
    except Exception as e:
        print(f"[!] Lưu ý scan_recent_missed_mentions: {e}")

async def bot_api_polling_loop(client, bot_token: str, config: Dict[str, Any]):
    """Vòng lặp Long Polling Bot API chuẩn Telegram - Nhận và xử lý lệnh tức thì 100% không bao giờ trễ"""
    last_offset = None
    my_chat_id = config.get("telegram_notifier_bot", {}).get("my_chat_id")

    print("[+] Bot API Poller đã kích hoạt và đang lắng nghe lệnh người dùng...")

    while True:
        try:
            params = {"timeout": 15}
            if last_offset is not None:
                params["offset"] = last_offset

            res = await bot_api_call_async(bot_token, "getUpdates", params, timeout=25)
            if not res.get("ok"):
                await asyncio.sleep(2)
                continue

            updates = res.get("result", [])
            for update in updates:
                last_offset = update["update_id"] + 1

                # 1. Xử lý Callback Query (Bấm Inline Button)
                if "callback_query" in update:
                    cb = update["callback_query"]
                    cb_id = cb["id"]
                    from_user = cb.get("from", {})
                    chat_id = cb.get("message", {}).get("chat", {}).get("id")
                    msg_id = cb.get("message", {}).get("message_id")
                    data_str = cb.get("data", "")

                    if not data_str:
                        await answer_callback(bot_token, cb_id)
                        continue

                    # Toggle Item: chk_{cid}_{idx}
                    if data_str.startswith("chk_"):
                        parts = data_str.split("_")
                        if len(parts) >= 3:
                            cid = parts[1]
                            try:
                                idx = int(parts[2])
                                db = load_tasks_db()
                                chk = db.get("checklists", {}).get(cid)
                                if chk and 1 <= idx <= len(chk.get("items", [])):
                                    current_val = chk["items"][idx - 1].get("done", False)
                                    chk["items"][idx - 1]["done"] = not current_val
                                    save_tasks_db(db)

                                    new_text, new_buttons = format_checklist_card(cid, chk)
                                    await edit_bot_message(bot_token, chat_id, msg_id, new_text, reply_markup=new_buttons)
                                    action_status = "Hoàn thành" if not current_val else "Chưa xong"
                                    await answer_callback(bot_token, cb_id, f"Đã cập nhật mục #{idx}: {action_status}!")
                                    continue
                            except Exception as e:
                                print(f"[!] Lỗi callback toggle: {e}")
                        await answer_callback(bot_token, cb_id, "⚠️ Không thể cập nhật mục này.")
                        continue

                    # Xóa Checklist: del_{cid}
                    if data_str.startswith("del_"):
                        cid = data_str[4:]
                        db = load_tasks_db()
                        if cid in db.get("checklists", {}):
                            title = db["checklists"][cid].get("title", "Checklist")
                            del db["checklists"][cid]
                            save_tasks_db(db)
                            await edit_bot_message(bot_token, chat_id, msg_id, f"🗑 <b>Đã xóa thành công Checklist:</b> <i>{title}</i> (#{cid})", reply_markup={"inline_keyboard": []})
                            await answer_callback(bot_token, cb_id, "Đã xóa checklist!")
                        else:
                            await answer_callback(bot_token, cb_id, "Checklist không tồn tại hoặc đã bị xóa.")
                        continue

                    # Làm mới thẻ: ref_{cid}
                    if data_str.startswith("ref_"):
                        cid = data_str[4:]
                        db = load_tasks_db()
                        chk = db.get("checklists", {}).get(cid)
                        if chk:
                            new_text, new_buttons = format_checklist_card(cid, chk)
                            await edit_bot_message(bot_token, chat_id, msg_id, new_text, reply_markup=new_buttons)
                            await answer_callback(bot_token, cb_id, "Đã làm mới thông tin!")
                        else:
                            await answer_callback(bot_token, cb_id, "Không tìm thấy dữ liệu.")
                        continue

                    # Lọc Tìm kiếm Tin nhắn theo Kênh: fnd_{ch}_{qid}
                    if data_str.startswith("fnd_"):
                        parts = data_str.split("_")
                        if len(parts) >= 3:
                            target_ch_code = parts[1]
                            qid = parts[2]
                            query_info = SEARCH_QUERY_CACHE.get(qid, {})
                            query = query_info.get("query", "")
                            ch_map = {"tg": "telegram", "wa": "whatsapp", "zl": "zalo", "all": "all"}
                            channel_filter = ch_map.get(target_ch_code, "all")

                            if query:
                                await answer_callback(bot_token, cb_id, "Đang quét dữ liệu...")
                                search_res = await search_messages_across_groups(client, query, channel_filter=channel_filter)
                                await edit_bot_message(bot_token, chat_id, msg_id, search_res, reply_markup={"inline_keyboard": []})
                            else:
                                await answer_callback(bot_token, cb_id, "Yêu cầu đã hết hạn. Hãy gõ lại lệnh tìm kiếm.")
                        continue

                    # Lọc Link Tài liệu theo Kênh: lnk_{ch}_{qid}
                    if data_str.startswith("lnk_"):
                        parts = data_str.split("_")
                        if len(parts) >= 3:
                            target_ch_code = parts[1]
                            qid = parts[2]
                            query_info = SEARCH_QUERY_CACHE.get(qid, {})
                            query = query_info.get("query", "")
                            ch_map = {"tg": "telegram", "wa": "whatsapp", "zl": "zalo", "all": "all"}
                            channel_filter = ch_map.get(target_ch_code, "all")

                            await answer_callback(bot_token, cb_id, "Đang lọc tài liệu & link...")
                            links_res = await extract_recent_links_across_groups(client, query=query if query else None, channel_filter=channel_filter)
                            await edit_bot_message(bot_token, chat_id, msg_id, links_res, reply_markup={"inline_keyboard": []})
                        continue

                    await answer_callback(bot_token, cb_id)
                    continue

                # 2. Xử lý Tin nhắn / Lệnh gửi tới Bot
                if "message" in update:
                    msg = update["message"]
                    sender_id = msg.get("from", {}).get("id")
                    chat_id = msg.get("chat", {}).get("id")
                    text = (msg.get("text") or "").strip()

                    if not text:
                        continue

                    print(f"[🤖 Telegram Bot Command] Từ {sender_id} (@{msg.get('from', {}).get('username', 'user')}): '{text}'")

                    # Chuẩn hóa lệnh
                    first_word = text.split()[0].lower()
                    cmd = first_word.split("@")[0]
                    text_lower = text.lower()

                    # Cập nhật chat id nếu chưa có
                    if not my_chat_id or my_chat_id != sender_id:
                        config["telegram_notifier_bot"]["my_chat_id"] = sender_id
                        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                            json.dump(config, f, ensure_ascii=False, indent=2)

                    # Lệnh kiểm tra trạng thái hoạt động: /status, /ping, /check
                    if cmd in ["/status", "/ping", "/check"]:
                        db = load_tasks_db()
                        checklists = db.get("checklists", {})
                        active_channels = get_active_channels(config)
                        ch_status = []
                        for ch in ["telegram", "whatsapp", "zalo"]:
                            icon = "🟢" if ch in active_channels else "⚪"
                            ch_status.append(f"{icon} {ch.upper()}")
                        
                        status_msg = (
                            "🟢 <b>MEW ASSISTANT ĐANG HOẠT ĐỘNG ONLINE 24/7</b>\n"
                            "━━━━━━━━━━━━━━━━━━━━━\n"
                            f"• <b>Các kênh kết nối:</b> {' | '.join(ch_status)}\n"
                            f"• <b>Checklist đang theo dõi:</b> {len(checklists)} dự án\n"
                            f"• <b>VIP Senders:</b> {len(config.get('settings', {}).get('vip_senders', []))} người\n"
                            f"• <b>Keywords giám sát:</b> {len(config.get('settings', {}).get('keywords', []))} từ khóa\n\n"
                            "💡 <i>Gõ <code>/help</code> hoặc <code>/todo</code> để bắt đầu quản lý công việc!</i>"
                        )
                        await send_bot_message(bot_token, chat_id, status_msg)
                        continue

                    if cmd in ["/start", "/help", "/menu", "/huongdan"]:
                        parts = text.split()
                        if len(parts) > 1 and parts[1].startswith("view_"):
                            view_args = parts[1][5:].split("_")
                            if len(view_args) >= 2:
                                chat_id_arg = view_args[0]
                                try:
                                    msg_id_arg = int(view_args[1])
                                    await send_bot_message(bot_token, chat_id, f"📖 <i>Đang trích xuất toàn bộ ngữ cảnh hội thoại quanh tin nhắn #{msg_id_arg}...</i>")
                                    context_result = await get_message_context_thread(client, chat_id_arg, msg_id_arg)
                                    await send_bot_message(bot_token, chat_id, context_result)
                                    continue
                                except Exception:
                                    pass

                        await send_bot_message(bot_token, chat_id, get_help_menu())
                        continue

                    # Lệnh xem danh sách Checklist: /todo, /todos, /task, /tasks, /checklist, /ds
                    if cmd in ["/todo", "/todos", "/task", "/tasks", "/checklist", "/ds"] or text_lower.startswith(("/todo list", "/task list", "/tasks list")):
                        db = load_tasks_db()
                        checklists = db.get("checklists", {})
                        if not checklists:
                            help_create = (
                                "📋 <b>BẠN CHƯA CÓ CHECKLIST CÔNG VIỆC NÀO</b>\n"
                                "━━━━━━━━━━━━━━━━━━━━━\n\n"
                                "💡 <b>Cách tạo checklist mới cực nhanh:</b>\n\n"
                                "<b>Cách 1 (1 dòng):</b>\n"
                                "<code>/add Dự án SIM C06 | 15/08 | Khảo sát luồng, Vẽ Wireframe, Thiết kế UI</code>\n\n"
                                "<b>Cách 2 (Nhiều dòng):</b>\n"
                                "<code>/add Thiết kế Luồng C06\n"
                                "Deadline: 15/08\n"
                                "- Khảo sát luồng cũ\n"
                                "- Thiết kế UI Figma\n"
                                "- Review với PO</code>"
                            )
                            await send_bot_message(bot_token, chat_id, help_create)
                            continue

                        await send_bot_message(bot_token, chat_id, f"📋 <b>DANH SÁCH {len(checklists)} CHECKLIST ĐANG THEO DÕI:</b>")
                        for cid, chk in checklists.items():
                            card_text, card_buttons = format_checklist_card(cid, chk)
                            await send_bot_message(bot_token, chat_id, card_text, reply_markup=card_buttons)
                        continue

                    # Lệnh xem Báo cáo công việc tổng quan: /report, /baocao, /today, /morning
                    if cmd in ["/report", "/baocao", "/today", "/morning"]:
                        db = load_tasks_db()
                        checklists = db.get("checklists", {})
                        report_text = generate_daily_morning_report(checklists)
                        await send_bot_message(bot_token, chat_id, report_text)
                        continue

                    # Lệnh tạo Checklist mới: /add, /new hoặc /todo add, /task add
                    if cmd in ["/add", "/new"] or text_lower.startswith(("/todo add", "/task add", "/tasks add", "/add")):
                        clean_content = text
                        for prefix in ["/todo add", "/task add", "/tasks add", "/add", "/new"]:
                            if clean_content.lower().startswith(prefix):
                                clean_content = clean_content[len(prefix):].strip()
                                break

                        if not clean_content:
                            await send_bot_message(
                                bot_token, chat_id,
                                "⚠️ <b>Vui lòng nhập nội dung checklist:</b>\n\n"
                                "<i>Cú pháp 1 dòng:</i>\n<code>/add Tên Dự án | Hạn DD/MM | Việc 1, Việc 2, Việc 3</code>\n\n"
                                "<i>Cú pháp nhiều dòng:</i>\n<code>/add Tên Dự án\nDeadline: 15/08\n- Việc 1\n- Việc 2</code>"
                            )
                            continue

                        title, deadline, items = parse_new_checklist_input(clean_content)
                        if not title:
                            await send_bot_message(bot_token, chat_id, "⚠️ Không tìm thấy tên dự án. Vui lòng thử lại.")
                            continue

                        db = load_tasks_db()
                        last_id = db.get("last_id", 0) + 1
                        db["last_id"] = last_id
                        cid = str(last_id)

                        items_struct = [{"id": i, "text": item_text, "done": False} for i, item_text in enumerate(items, start=1)]

                        new_checklist = {
                            "id": cid,
                            "title": title,
                            "created_at": datetime.now().strftime("%d/%m/%Y"),
                            "deadline": deadline,
                            "items": items_struct
                        }

                        if "checklists" not in db:
                            db["checklists"] = {}
                        db["checklists"][cid] = new_checklist
                        save_tasks_db(db)

                        card_text, card_buttons = format_checklist_card(cid, new_checklist)
                        await send_bot_message(bot_token, chat_id, "✅ <b>ĐÃ TẠO CHECKLIST THÀNH CÔNG:</b>")
                        await send_bot_message(bot_token, chat_id, card_text, reply_markup=card_buttons)
                        continue

                    # Lệnh xóa checklist: /del, /delete, /rm hoặc /todo del, /task del
                    if cmd in ["/del", "/delete", "/rm"] or text_lower.startswith(("/del", "/todo del", "/task del", "/tasks del")):
                        parts = text.split()
                        if len(parts) > 1:
                            cid = parts[-1].lstrip("#")
                            db = load_tasks_db()
                            if cid in db.get("checklists", {}):
                                title = db["checklists"][cid].get("title", "Checklist")
                                del db["checklists"][cid]
                                save_tasks_db(db)
                                await send_bot_message(bot_token, chat_id, f"🗑 <b>Đã xóa thành công Checklist:</b> <i>{title}</i> (#{cid})")
                            else:
                                await send_bot_message(bot_token, chat_id, f"⚠️ Không tìm thấy Checklist có mã <code>#{cid}</code>")
                        else:
                            await send_bot_message(bot_token, chat_id, "⚠️ Vui lòng nhập mã checklist: <code>/del &lt;MÃ_ID&gt;</code>")
                        continue

                    # Quản lý danh sách VIP Senders: /vip, /vip add, /vip del
                    if text_lower.startswith("/vip"):
                        current_vips = config.get("settings", {}).get("vip_senders", [])
                        parts = text.split(maxsplit=2)
                        
                        if len(parts) == 1 or parts[1].lower() == "list":
                            vip_items = "\n".join([f"  👑 {i}. <code>{v}</code>" for i, v in enumerate(current_vips, start=1)]) if current_vips else "  <i>(Chưa có thành viên nào)</i>"
                            msg_content = (
                                f"👑 <b>DANH SÁCH VIP SENDERS ({len(current_vips)} người)</b>\n"
                                f"━━━━━━━━━━━━━━━━━━━━━\n\n"
                                f"{vip_items}\n\n"
                                f"━━━━━━━━━━━━━━━━━━━━━\n"
                                f"💡 <b>Cách quản lý:</b>\n"
                                f"• Thêm: <code>/vip add &lt;tên_hoặc_username&gt;</code>\n"
                                f"• Xóa: <code>/vip del &lt;tên_hoặc_số_thứ_tự&gt;</code>"
                            )
                            await send_bot_message(bot_token, chat_id, msg_content)
                            continue

                        sub_cmd = parts[1].lower()
                        if sub_cmd == "add":
                            raw_content = text[text.lower().find("add") + 3:].strip()
                            if not raw_content:
                                await send_bot_message(
                                    bot_token, chat_id,
                                    "⚠️ <b>Vui lòng nhập danh sách cần thêm:</b>\n\n"
                                    "<i>Cú pháp 1 dòng (dấu phẩy):</i>\n<code>/vip add Hoàng PO, Minh Lead, @boss, Linh PM</code>\n\n"
                                    "<i>Cú pháp nhiều dòng:</i>\n<code>/vip add\n- Hoàng PO\n- Minh Lead\n- @boss</code>"
                                )
                                continue

                            candidates = []
                            for line in raw_content.split("\n"):
                                clean_line = re.sub(r'^[-*•\d.]+\s*', '', line.strip()).strip()
                                if "," in clean_line:
                                    candidates.extend([p.strip() for p in clean_line.split(",") if p.strip()])
                                elif clean_line:
                                    candidates.append(clean_line)

                            added_list = []
                            existed_list = []
                            for member in candidates:
                                if member not in current_vips:
                                    current_vips.append(member)
                                    added_list.append(member)
                                else:
                                    existed_list.append(member)

                            if added_list:
                                config["settings"]["vip_senders"] = current_vips
                                with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                                    json.dump(config, f, ensure_ascii=False, indent=2)

                            msg_res = []
                            if added_list:
                                added_str = ", ".join([f"<b>{m}</b>" for m in added_list])
                                msg_res.append(f"✅ Đã thêm <b>{len(added_list)}</b> thành viên vào VIP Senders:\n👉 {added_str}")
                            if existed_list:
                                existed_str = ", ".join([f"<i>{m}</i>" for m in existed_list])
                                msg_res.append(f"ℹ️ Đã có sẵn: {existed_str}")

                            await send_bot_message(bot_token, chat_id, "\n\n".join(msg_res) if msg_res else "⚠️ Không có thành viên hợp lệ để thêm.")
                            continue

                        if sub_cmd in ["del", "remove", "delete"]:
                            raw_content = text[text.lower().find(sub_cmd) + len(sub_cmd):].strip()
                            if not raw_content:
                                await send_bot_message(bot_token, chat_id, "⚠️ Vui lòng nhập tên/số thứ tự cần xóa: <code>/vip del Hoàng PO, Minh Lead</code> hoặc <code>/vip del 1, 2</code>")
                                continue

                            candidates = []
                            for line in raw_content.split("\n"):
                                clean_line = re.sub(r'^[-*•\d.]+\s*', '', line.strip()).strip()
                                if "," in clean_line:
                                    candidates.extend([p.strip() for p in clean_line.split(",") if p.strip()])
                                elif clean_line:
                                    candidates.append(clean_line)

                            deleted_list = []
                            not_found = []

                            for target_member in candidates:
                                matched = None
                                if target_member.isdigit():
                                    idx = int(target_member)
                                    if 1 <= idx <= len(current_vips):
                                        matched = current_vips[idx - 1]
                                else:
                                    for v in current_vips:
                                        if v.lower() == target_member.lower():
                                            matched = v
                                            break
                                if matched and matched in current_vips:
                                    current_vips.remove(matched)
                                    deleted_list.append(matched)
                                else:
                                    not_found.append(target_member)

                            if deleted_list:
                                config["settings"]["vip_senders"] = current_vips
                                with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                                    json.dump(config, f, ensure_ascii=False, indent=2)

                            msg_res = []
                            if deleted_list:
                                del_str = ", ".join([f"<b>{m}</b>" for m in deleted_list])
                                msg_res.append(f"🗑 Đã xóa <b>{len(deleted_list)}</b> thành viên khỏi VIP Senders:\n👉 {del_str}")
                            if not_found:
                                not_found_str = ", ".join([f"<i>{m}</i>" for m in not_found])
                                msg_res.append(f"⚠️ Không tìm thấy: {not_found_str}")

                            await send_bot_message(bot_token, chat_id, "\n\n".join(msg_res))
                            continue

                    # Lệnh tìm kiếm tin nhắn: /find, /tim, /search
                    if cmd in ["/find", "/tim", "/search"]:
                        parts = text.split(maxsplit=1)
                        if len(parts) > 1:
                            raw_query = parts[1].strip()
                            active_channels = get_active_channels(config)

                            # Trường hợp 1: Chỉ có 1 channel duy nhất đang bật -> Tự động tìm luôn
                            if len(active_channels) <= 1:
                                single_ch = active_channels[0] if active_channels else "telegram"
                                await send_bot_message(bot_token, chat_id, f"🔍 <i>Đang tìm kiếm:</i> <code>{raw_query}</code>...")
                                search_result = await search_messages_across_groups(client, raw_query, channel_filter=single_ch)
                                await send_bot_message(bot_token, chat_id, search_result)
                                continue

                            # Trường hợp 2: Có prefix trực tiếp (VD: /find tele figma, /find wa deadline)
                            explicit_ch, clean_query = parse_channel_prefix_from_query(raw_query)
                            if explicit_ch:
                                ch_name = "TELEGRAM VNPT" if explicit_ch == "telegram" else ("WHATSAPP" if explicit_ch == "whatsapp" else "ZALO")
                                await send_bot_message(bot_token, chat_id, f"🔍 <i>Đang tìm kiếm trên [{ch_name}]:</i> <code>{clean_query}</code>...")
                                search_result = await search_messages_across_groups(client, clean_query, channel_filter=explicit_ch)
                                await send_bot_message(bot_token, chat_id, search_result)
                                continue

                            # Hiện bảng chọn kênh qua Inline Buttons
                            qid = str(int(time.time() * 1000))[-8:]
                            SEARCH_QUERY_CACHE[qid] = {"query": raw_query, "type": "find"}

                            btn_row_1 = []
                            if "telegram" in active_channels:
                                btn_row_1.append({"text": "🔷 Telegram VNPT", "callback_data": f"fnd_tg_{qid}"})
                            if "whatsapp" in active_channels:
                                btn_row_1.append({"text": "🟢 WhatsApp", "callback_data": f"fnd_wa_{qid}"})
                            if "zalo" in active_channels:
                                btn_row_1.append({"text": "🔵 Zalo", "callback_data": f"fnd_zl_{qid}"})

                            btn_row_2 = [{"text": "🌐 Tìm trên Tất cả Kênh", "callback_data": f"fnd_all_{qid}"}]
                            filter_buttons = [btn_row_1, btn_row_2] if btn_row_1 else [btn_row_2]

                            prompt_msg = (
                                f"🔍 <b>CHỌN KÊNH TRA CỨU CHO:</b> <code>{raw_query}</code>\n"
                                f"━━━━━━━━━━━━━━━━━━━━━\n"
                                f"<i>Vui lòng chọn kênh để kết quả không bị lẫn lộn giữa các nền tảng:</i>"
                            )
                            await send_bot_message(bot_token, chat_id, prompt_msg, reply_markup={"inline_keyboard": filter_buttons})
                        else:
                            await send_bot_message(bot_token, chat_id, "⚠️ Vui lòng nhập từ khóa cần tìm: <code>/find &lt;từ_khóa&gt;</code>")
                        continue

                    # Lệnh xem chi tiết tin nhắn: /view
                    if text_lower.startswith("/view"):
                        chat_id_arg = None
                        msg_id_arg = None

                        if text_lower.startswith("/view_"):
                            raw_args = text[6:].split("_")
                            if len(raw_args) >= 2:
                                chat_id_arg = raw_args[0]
                                try:
                                    msg_id_arg = int(raw_args[1].split()[0])
                                except Exception:
                                    pass
                        else:
                            parts = text.split()
                            if len(parts) >= 3:
                                chat_id_arg = parts[1]
                                try:
                                    msg_id_arg = int(parts[2])
                                except Exception:
                                    pass

                        if chat_id_arg and msg_id_arg:
                            await send_bot_message(bot_token, chat_id, f"📖 <i>Đang trích xuất toàn bộ ngữ cảnh hội thoại quanh tin nhắn #{msg_id_arg}...</i>")
                            context_result = await get_message_context_thread(client, chat_id_arg, msg_id_arg)
                            await send_bot_message(bot_token, chat_id, context_result)
                        else:
                            await send_bot_message(bot_token, chat_id, "⚠️ Cú pháp không hợp lệ. Hãy bấm trực tiếp vào mã lệnh dạng: <code>/view_&lt;chat_id&gt;_&lt;msg_id&gt;</code>")
                        continue

                    # Lệnh gom link tài liệu: /link, /links, /figma, /docs, /doc, /tailieu
                    if any(text_lower.startswith(prefix) for prefix in ["/link", "/links", "/figma", "/docs", "/doc", "/tailieu"]):
                        parts = text.split(maxsplit=1)
                        raw_query = parts[1].strip() if len(parts) > 1 else ""
                        if text_lower.startswith("/figma") and not raw_query:
                            raw_query = "figma"
                        elif (text_lower.startswith("/docs") or text_lower.startswith("/doc")) and not raw_query:
                            raw_query = "docs"

                        active_channels = get_active_channels(config)

                        # TH 1: Chỉ có 1 channel đang bật -> Tự động gom luôn
                        if len(active_channels) <= 1:
                            single_ch = active_channels[0] if active_channels else "telegram"
                            if raw_query:
                                await send_bot_message(bot_token, chat_id, f"🔗 <i>Đang lọc link liên quan đến:</i> <code>{raw_query}</code>...")
                            else:
                                await send_bot_message(bot_token, chat_id, "🔗 <i>Đang lọc các link Figma và tài liệu mới nhất...</i>")
                            links_result = await extract_recent_links_across_groups(client, query=raw_query if raw_query else None, channel_filter=single_ch)
                            await send_bot_message(bot_token, chat_id, links_result)
                            continue

                        # TH 2: Có prefix trực tiếp
                        explicit_ch, clean_query = parse_channel_prefix_from_query(raw_query) if raw_query else (None, "")
                        if explicit_ch:
                            ch_name = "TELEGRAM VNPT" if explicit_ch == "telegram" else ("WHATSAPP" if explicit_ch == "whatsapp" else "ZALO")
                            await send_bot_message(bot_token, chat_id, f"🔗 <i>Đang lọc link trên [{ch_name}]:</i> <code>{clean_query}</code>...")
                            links_result = await extract_recent_links_across_groups(client, query=clean_query if clean_query else None, channel_filter=explicit_ch)
                            await send_bot_message(bot_token, chat_id, links_result)
                            continue

                        # Hiện bảng chọn kênh
                        qid = str(int(time.time() * 1000))[-8:]
                        SEARCH_QUERY_CACHE[qid] = {"query": raw_query, "type": "links"}

                        btn_row_1 = []
                        if "telegram" in active_channels:
                            btn_row_1.append({"text": "🔷 Telegram VNPT", "callback_data": f"lnk_tg_{qid}"})
                        if "whatsapp" in active_channels:
                            btn_row_1.append({"text": "🟢 WhatsApp", "callback_data": f"lnk_wa_{qid}"})
                        if "zalo" in active_channels:
                            btn_row_1.append({"text": "🔵 Zalo", "callback_data": f"lnk_zl_{qid}"})

                        btn_row_2 = [{"text": "🌐 Lọc trên Tất cả Kênh", "callback_data": f"lnk_all_{qid}"}]
                        filter_buttons = [btn_row_1, btn_row_2] if btn_row_1 else [btn_row_2]

                        q_display = f" <code>{raw_query}</code>" if raw_query else ""
                        prompt_msg = (
                            f"🔗 <b>CHỌN KÊNH LỌC TÀI LIỆU & LINK{q_display}:</b>\n"
                            f"━━━━━━━━━━━━━━━━━━━━━\n"
                            f"<i>Vui lòng chọn kênh để danh sách link Figma/Docs không bị lẫn lộn:</i>"
                        )
                        await send_bot_message(bot_token, chat_id, prompt_msg, reply_markup={"inline_keyboard": filter_buttons})
                        continue

        except asyncio.CancelledError:
            break
        except Exception as e:
            print(f"[!] Lỗi trong bot_api_polling_loop: {e}")
            await asyncio.sleep(3)

async def start_telethon_listener(config: Dict[str, Any]):
    """Chạy Userbot Telethon quét nhóm kết hợp tương tác Bot API hai chiều tức thì"""
    try:
        from telethon import TelegramClient, events
        from telethon.tl.types import PeerUser
    except ImportError:
        print("[!] Chưa cài đặt thư viện telethon. Vui lòng chạy: pip3 install telethon")
        return

    userbot_cfg = config.get("telegram_userbot", {})
    api_id = userbot_cfg.get("api_id")
    api_hash = userbot_cfg.get("api_hash")
    session_name = userbot_cfg.get("session_name", "vnpt_tuanvq_session")
    session_file = SCRIPT_DIR / session_name

    notifier_bot_cfg = config.get("telegram_notifier_bot", {})
    bot_token = notifier_bot_cfg.get("bot_token")
    my_chat_id = notifier_bot_cfg.get("my_chat_id")

    settings = config.get("settings", {})
    my_usernames = [u.lower().lstrip("@") for u in settings.get("my_usernames", ["tuanvq", "quctuan"])]
    keywords = [k.lower() for k in settings.get("keywords", ["Tuấn", "URD", "Design", "Figma", "Gấp"])]
    history_limit = settings.get("context_history_limit", 15)

    client = TelegramClient(str(session_file), int(api_id), api_hash, connection_retries=None, auto_reconnect=True, retry_delay=5)
    processed_message_ids = set()

    # 1. Lắng nghe tin nhắn trên tài khoản Userbot cá nhân (các nhóm VNPT)
    @client.on(events.NewMessage(incoming=True))
    async def group_message_handler(event):
        try:
            # Bỏ qua tin nhắn riêng tư hoặc từ Bot
            if isinstance(event.peer_id, PeerUser) or event.is_private or not (event.is_group or event.is_channel):
                return

            my_id = (await client.get_me()).id
            if event.sender_id == my_id or event.chat_id == my_id:
                return

            sender = await event.get_sender()
            if not sender or getattr(sender, "bot", False):
                return

            if event.id in processed_message_ids:
                return
            processed_message_ids.add(event.id)
            if len(processed_message_ids) > 1000:
                processed_message_ids.clear()

            text = event.raw_text or ""
            text_lower = text.lower()

            chat = await event.get_chat()
            group_name = getattr(chat, "title", "Nhóm Telegram")

            is_mentioned = event.mentioned or any(f"@{u}" in text_lower for u in my_usernames)
            is_reply_to_me = False
            if event.is_reply:
                reply_msg = await event.get_reply_message()
                if reply_msg and reply_msg.sender_id == my_id:
                    is_reply_to_me = True

            matched_keywords = [k for k in keywords if k in text_lower]

            if not (is_mentioned or is_reply_to_me or matched_keywords):
                return

            print(f"\n[🔔 PHÁT HIỆN SỰ KIỆN] Nhóm: '{group_name}' | Từ: {event.sender_id}")
            
            sender_name = getattr(sender, "first_name", "Đồng nghiệp")
            if getattr(sender, "last_name", None):
                sender_name += f" {sender.last_name}"

            direct_link, clean_id, view_link = build_message_link_and_cmd(chat, event.id, fallback_chat_id=event.chat_id)

            trigger_msg = {
                "sender_name": sender_name,
                "text": text,
                "link": direct_link,
                "view_link": view_link,
                "is_mentioned": is_mentioned,
                "is_reply_to_me": is_reply_to_me
            }

            history_messages = []
            async for m in client.iter_messages(event.chat_id, limit=history_limit, max_id=event.id):
                m_sender = await m.get_sender()
                m_name = getattr(m_sender, "first_name", "User") if m_sender else "User"
                if m.raw_text:
                    history_messages.append({"sender_name": m_name, "text": m.raw_text})
            
            history_messages.reverse()
            history_messages.append(trigger_msg)

            task_data = synthesize_context(history_messages, trigger_msg, group_name, config=config)
            task_data["view_link"] = view_link
            task_data["message_link"] = direct_link
            alert_text = format_telegram_alert(task_data)

            target_chat_id = config.get("telegram_notifier_bot", {}).get("my_chat_id", 1083272610)
            if bot_token and target_chat_id:
                btn_row = [{"text": "📖 Xem chi tiết", "url": view_link}]
                if direct_link:
                    btn_row.append({"text": "🔗 Mở tin nhắn", "url": direct_link})
                reply_markup = {"inline_keyboard": [btn_row]}
                await send_bot_message(bot_token, int(target_chat_id), alert_text, reply_markup=reply_markup)
                print(f"[✓] Đã gửi thông báo cảnh báo về Telegram của bạn!")

        except Exception as e:
            print(f"[!] Lỗi khi xử lý tin nhắn: {e}")

    # Khởi chạy Userbot client
    await client.connect()
    if not await client.is_user_authorized():
        print("[!] Userbot Telethon chưa xác thực session.")
    else:
        me = await client.get_me()
        print(f"[+] Userbot Telethon đã kết nối tài khoản: {me.first_name} (@{me.username})")

    print("\n" + "="*65)
    print("🚀 MEW TELEGRAM ASSISTANT BOT ĐANG CHẠY TOÀN DIỆN")
    print("• Quét và lắng nghe tự động tất cả các nhóm bạn tham gia")
    print("• Gửi cảnh báo nhắc việc trực tiếp từ Bot riêng của bạn")
    print("• Quản lý Checklist công việc & Tiến độ: /todo, /task, /add")
    print("• Tự động gửi Báo cáo nhắc việc 08:00 Sáng mỗi ngày")
    print("• Hỗ trợ tìm kiếm xuyên nhóm: /find <từ_khóa>")
    print("• Hỗ trợ gom link tài liệu:   /links [từ_khóa]")
    print("="*65 + "\n")

    # Các tác vụ ngầm chạy song song: Polling Bot API + Morning Reminder + Missed Mentions Scan
    tasks = [client.run_until_disconnected()]
    if bot_token and bot_token != "YOUR_TELEGRAM_BOT_TOKEN_FROM_BOTFATHER":
        tasks.append(bot_api_polling_loop(client, bot_token, config))
        target_id_for_reminder = int(my_chat_id) if my_chat_id else 0
        if target_id_for_reminder:
            tasks.append(daily_morning_reminder_loop(bot_token, target_id_for_reminder))
            tasks.append(scan_recent_missed_mentions(client, bot_token, config, processed_message_ids))

    await asyncio.gather(*tasks)

def main():
    parser = argparse.ArgumentParser(description="Telegram VNPT Task Monitor & Synthesizer")
    parser.add_argument("--test", action="store_true", help="Chạy chế độ mô phỏng kiểm tra (Mock test)")
    parser.add_argument("--listen", action="store_true", help="Kích hoạt Userbot quét tất cả các nhóm chat")
    args = parser.parse_args()

    config = load_config()

    if args.test:
        run_mock_simulation()
        return

    if args.listen:
        while True:
            try:
                asyncio.run(start_telethon_listener(config))
            except (KeyboardInterrupt, SystemExit):
                print("\n[!] Đã dừng tiến trình theo yêu cầu của bạn.")
                break
            except Exception as e:
                print(f"[!] Kết nối mạng bị gián đoạn ({e}). Đang tự động kết nối lại sau 10 giây...")
                time.sleep(10)
        return

    print("🤖 TELEGRAM VNPT TASK MONITOR")
    print("  1. Chạy thử nghiệm mô phỏng: python3 telegram_vnpt_monitor.py --test")
    print("  2. Kích hoạt quét tất cả nhóm: python3 telegram_vnpt_monitor.py --listen")

if __name__ == "__main__":
    main()

