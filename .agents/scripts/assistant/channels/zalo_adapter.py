# -*- coding: utf-8 -*-
"""
Zalo Channel Adapter - Mew Assistant
Lắng nghe tin nhắn từ đối tác / khách hàng Việt Nam trên Zalo và chuyển tiếp về Telegram.
Tự động chấm điểm ưu tiên & bóc tách hành động cần làm.
"""

import asyncio
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# Nạp module Core
SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

from core.scoring import score_importance
from core.action_extractor import extract_smart_action_and_context
from core.formatter import format_omnichannel_alert

class ZaloChannelAdapter:
    def __init__(self, config: Dict[str, Any], telegram_bot_sender=None):
        self.config = config
        self.telegram_bot_sender = telegram_bot_sender
        self.enabled = config.get("active_channels", {}).get("zalo", False)
        self.session_dir = SCRIPT_DIR / ".zalo_session"
        self.session_dir.mkdir(parents=True, exist_ok=True)

    async def process_incoming_message(self, raw_msg: Dict[str, Any]):
        """
        Xử lý khi có tin nhắn mới từ Zalo:
        raw_msg: {
            "sender_name": "Anh Nam Tech",
            "chat_name": "Nhóm Dự án App FinTech",
            "text": "Tuấn ơi check giúp anh file Google Sheet kịch bản này nhé https://docs.google.com/spreadsheets/d/xyz",
            "is_group": True,
            "timestamp": "14:35 09/08/2026"
        }
        """
        if not self.enabled:
            return

        text = raw_msg.get("text", "")
        sender_name = raw_msg.get("sender_name", "Khách Zalo")
        chat_name = raw_msg.get("chat_name", sender_name)
        is_group = raw_msg.get("is_group", False)

        trigger_msg = {
            "channel_type": "zalo",
            "sender_name": sender_name,
            "text": text,
            "is_direct": not is_group,
            "is_mentioned": True if not is_group else ("Tuấn" in text or "tuan" in text.lower()),
            "is_reply_to_me": False,
            "link": None
        }

        # 1. Chấm điểm ưu tiên theo Core Engine
        scoring = score_importance(trigger_msg, None, chat_name, self.config)

        # 2. Bóc tách ngữ cảnh & hành động cần làm
        context_sentence, action_items = extract_smart_action_and_context(trigger_msg, None, scoring)

        task_data = {
            "channel_type": "zalo",
            "task_id": f"ZL_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "group_name": f"Zalo: {chat_name}",
            "sender_name": sender_name,
            "timestamp": raw_msg.get("timestamp", datetime.now().strftime("%H:%M %d/%m/%Y")),
            "context_sentence": context_sentence,
            "action_items": action_items,
            "scoring": scoring,
            "message_link": None,
            "view_link": None
        }

        alert_text = format_omnichannel_alert(task_data)

        # Gửi thông báo về Telegram của bạn
        if self.telegram_bot_sender:
            await self.telegram_bot_sender(alert_text)
        else:
            print(f"\n[🔵 ZALO ALERT]:\n{alert_text}\n")

    async def start_listening(self):
        """Khởi động tiến trình lắng nghe Zalo Session Bridge"""
        if not self.enabled:
            print("[-] Kênh Zalo đang TẮT trong config.json. Bỏ qua.")
            return

        print("[+] Đang khởi động Zalo Adapter Bridge...")
        print("[i] Trạng thái: Sẵn sàng kết nối Zalo Session.")
        while True:
            await asyncio.sleep(60)
