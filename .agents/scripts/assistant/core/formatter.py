# -*- coding: utf-8 -*-
"""
Core Alert Formatter - Mew Omnichannel Assistant
Định dạng tin nhắn cảnh báo gửi về Telegram Controller với nhãn kênh nhận diện trực quan.
"""

from datetime import datetime
from typing import Dict, Any, List, Optional
import time

CHANNEL_BADGES = {
    "telegram": "🔷 [VNPT TELEGRAM]",
    "whatsapp": "🟢 [WHATSAPP CLIENT]",
    "zalo": "🔵 [ZALO CLIENT]"
}

def format_omnichannel_alert(task_info: Dict[str, Any]) -> str:
    """
    Tạo format tin nhắn cảnh báo chuẩn WorkSync Pro cho mọi nền tảng:
    - Hiển thị Badge Kênh: 🔷 [VNPT TELEGRAM], 🟢 [WHATSAPP CLIENT], 🔵 [ZALO CLIENT]
    - Hiển thị Điểm ưu tiên (Score) & Lý do
    - Hiển thị Ngữ cảnh & Hành động cụ thể cần làm
    """
    channel_type = task_info.get("channel_type", "telegram").lower()
    channel_badge = CHANNEL_BADGES.get(channel_type, "💬 [MESSAGE]")

    group_name = task_info.get("group_name", "Tin nhắn trực tiếp")
    sender_name = task_info.get("sender_name", "Đồng nghiệp / Khách hàng")
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
    reasons_str = " · ".join(reasons) if reasons else "Từ khóa nhận diện"

    actions_text = "\n".join([f"  👉 {a}" for a in action_items])

    link_lines = []
    if view_link:
        link_lines.append(f"👉 <a href='{view_link}'><b>Xem chi tiết</b></a>")
    if msg_link:
        link_lines.append(f"🔗 <a href='{msg_link}'>Mở tin nhắn</a>")

    links_display = " | ".join(link_lines) if link_lines else ""

    alert_msg = (
        f"<b>{channel_badge}</b>\n"
        f"{badge} (⭐ <b>{score} điểm</b>)\n"
        f"<i>({reasons_str})</i>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"📍 <b>Nguồn:</b> <code>{group_name}</code>\n"
        f"👤 <b>Người gửi:</b> <b>{sender_name}</b> (⏰ {timestamp})\n\n"
        f"📝 <b>Ngữ cảnh:</b> {context_sentence}\n\n"
        f"🎯 <b>Hành động Cần làm:</b>\n"
        f"{actions_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"{links_display}\n"
        f"<i>(ID: {task_id})</i>"
    )
    return alert_msg
