# -*- coding: utf-8 -*-
"""
Core Action Extractor - Mew Omnichannel Assistant
Trích xuất Ngữ cảnh cô đọng và Hành động Cụ thể cần làm (Action Needed)
Chuẩn hóa đồng nhất cho cả 3 kênh Telegram, WhatsApp và Zalo.
"""

import re
from typing import Dict, Any, List, Tuple, Optional

def extract_smart_action_and_context(trigger_msg: Dict[str, Any], context_messages: Optional[List[Dict[str, Any]]] = None, scoring: Optional[Dict[str, Any]] = None) -> Tuple[str, List[str]]:
    """
    Trích xuất:
    1. Ngữ cảnh tóm tắt cô đọng (Context snippet)
    2. Danh sách hành động cụ thể cần làm (Action Needed)
    """
    text = (trigger_msg.get("text") or "").strip()
    sender = trigger_msg.get("sender_name") or "Khách hàng / Đồng nghiệp"
    clean_snippet = text.replace("\n", " ")
    if len(clean_snippet) > 130:
        clean_snippet = clean_snippet[:130] + "..."

    # Xác định ngữ cảnh cốt lõi
    context_sentence = f"<i>\"{clean_snippet}\"</i>"

    # Suy luận hành động cụ thể (Action Needed)
    actions = []
    text_lower = text.lower()

    # 1. Hành động khi có người Reply tin nhắn của bạn
    if trigger_msg.get("is_reply_to_me"):
        actions.append(f"Đọc nội dung phản hồi và tiếp tục trao đổi với <b>{sender}</b>")

    # 2. Hành động phản hồi câu hỏi
    if "?" in text or any(w in text_lower for w in ["chưa", "không", "sao", "được ko", "được không", "thế nào", "how much", "when", "can you"]):
        if not trigger_msg.get("is_reply_to_me"):
            actions.append(f"Phản hồi câu hỏi / giải đáp thắc mắc cho <b>{sender}</b>")

    # 3. Hành động mở link Figma / sửa thiết kế
    if re.search(r'https?://(?:www\.)?figma\.com/[^\s]+', text):
        actions.append("Mở link Figma đính kèm để kiểm tra layout & chỉnh sửa token")
    elif any(w in text_lower for w in ["figma", "layout", "màn hình", "giao diện", "ui", "ux", "motion", "prototype"]):
        actions.append("Cập nhật / chỉnh sửa file thiết kế Figma theo yêu cầu")

    # 3. Hành động đối soát tài liệu / URD / Google Docs
    if re.search(r'https?://docs\.google\.com/[^\s]+', text):
        actions.append("Mở tài liệu Google Docs/Sheet đính kèm để đối soát kịch bản & URD")

    # 4. Hành động review / duyệt
    if any(w in text_lower for w in ["review", "duyệt", "feedback", "góp ý", "chốt"]):
        actions.append(f"Review giao diện và phản hồi ý kiến chuyên môn với <b>{sender}</b>")

    # 5. Hành động báo giá / scope (nếu khách ngoài hỏi giá / hợp đồng)
    if any(w in text_lower for w in ["báo giá", "chi phí", "budget", "pricing", "hợp đồng", "cost", "proposal"]):
        actions.append(f"Gửi Portfolio & Lập phương án báo giá dự toán cho <b>{sender}</b>")

    # 6. Hành động ưu tiên thời gian khẩn cấp
    if any(w in text_lower for w in ["deadline", "gấp", "asap", "hôm nay", "trước 12h", "trước 17h", "urgent"]):
        actions.append("Ưu tiên xử lý ngay trong ngày để kịp tiến độ bàn giao")

    if not actions:
        actions.append(f"Rà soát nội dung trao đổi và phản hồi lại <b>{sender}</b> nếu cần")

    return (context_sentence, actions)
