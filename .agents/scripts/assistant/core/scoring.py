# -*- coding: utf-8 -*-
"""
Core Importance Scoring Engine - Mew Omnichannel Assistant
Chấm điểm mức độ ưu tiên có trọng số theo chuẩn WorkSync Engine.
Dùng chung cho tất cả các kênh (Telegram, WhatsApp, Zalo).
"""

import re
from typing import Dict, Any, List, Optional

def score_importance(trigger_msg: Dict[str, Any], context_messages: Optional[List[Dict[str, Any]]] = None, group_name: str = "", config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Chấm điểm mức độ ưu tiên có trọng số cho tin nhắn:
    - VIP Sender: +15 điểm
    - Direct Mention (@tuanvq): +12 điểm
    - Direct Message (1-1): +12 điểm
    - Reply tin nhắn của bạn: +10 điểm
    - Có câu hỏi '?' / Cần phản hồi: +8 điểm
    - Từ khóa Khẩn cấp / Deadline: +7 điểm
    - Có link Figma / Google Docs: +6 điểm
    - Từ khóa Thiết kế / Review: +4 điểm
    """
    text = (trigger_msg.get("text") or "").lower()
    raw_text = trigger_msg.get("text") or ""
    sender_name = trigger_msg.get("sender_name") or ""
    is_direct = trigger_msg.get("is_direct", False)
    
    settings = (config or {}).get("settings", {})
    vip_senders = [v.lower() for v in settings.get("vip_senders", ["hà po", "po", "lead", "sếp", "pm", "quynhmaihavi", "lê", "giám đốc"])]
    my_usernames = [u.lower().lstrip("@") for u in settings.get("my_usernames", ["tuanvq", "quctuan"])]

    score = 0
    reasons = []

    # 1. VIP Sender (+15 điểm)
    if any(vip in sender_name.lower() for vip in vip_senders):
        score += 15
        reasons.append("👑 VIP / Sếp / PO")

    # 2. Mention trực tiếp @tuanvq (+12 điểm) hoặc Tin nhắn riêng 1-1 (+12 điểm)
    if any(f"@{u}" in text for u in my_usernames) or trigger_msg.get("is_mentioned"):
        score += 12
        reasons.append("🎯 Tag trực tiếp bạn")
    elif is_direct:
        score += 12
        reasons.append("💬 Nhắn riêng 1-1")

    # 3. Trả lời (Reply) tin nhắn của bạn (+12 điểm - mức ưu tiên ngang với Tag/Mention)
    if trigger_msg.get("is_reply_to_me"):
        score += 12
        reasons.append("🎯 Reply tin nhắn bạn")

    # 4. Có câu hỏi '?' (+8 điểm) - Cần bạn phản hồi
    if "?" in raw_text or any(w in text for w in ["chưa", "không ạ", "sao anh", "sao em", "thế nào", "được ko"]):
        score += 8
        reasons.append("❓ Có câu hỏi / Cần phản hồi")

    # 5. Từ khóa Khẩn cấp / Deadline (+7 điểm)
    urgent_keywords = ["gấp", "khẩn", "asap", "blocker", "cháy", "hotfix", "hôm nay", "trước 12h", "trước 17h", "deadline", "urgent"]
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
    design_keywords = ["review", "duyệt", "chốt", "góp ý", "sửa", "feedback", "luồng", "urd", "motion", "prototype", "animation", "layout"]
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
