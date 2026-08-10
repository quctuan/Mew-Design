#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mew Omnichannel Assistant Supervisor Daemon
-------------------------------------------
Quản lý, giám sát và tự động duy trì 24/7 toàn bộ 3 kênh:
1. 🔷 Telegram VNPT Monitor (Userbot + Notifier Bot)
2. 🟢 WhatsApp Client Socket Bridge
3. 🔵 Zalo Client Socket Bridge

Tự động hồi sinh (Auto-Respawn) ngay lập tức nếu bất kỳ tiến trình nào bị ngắt hoặc crash.
"""

import os
import sys
import time
import json
import signal
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path
from typing import Dict, Any

SCRIPT_DIR = Path(__file__).parent
WORKSPACE_ROOT = SCRIPT_DIR.parent.parent.parent
CONFIG_PATH = SCRIPT_DIR / "config.json"

SERVICES = {
    "telegram": {
        "name": "🔷 Telegram VNPT Monitor",
        "cmd": [sys.executable, str(SCRIPT_DIR / "telegram_vnpt_monitor.py"), "--listen"],
        "cwd": str(SCRIPT_DIR),
        "proc": None
    },
    "whatsapp": {
        "name": "🟢 WhatsApp Bridge",
        "cmd": ["node", str(SCRIPT_DIR / "bridges" / "whatsapp" / "whatsapp_bridge.js")],
        "cwd": str(SCRIPT_DIR / "bridges" / "whatsapp"),
        "proc": None
    },
    "zalo": {
        "name": "🔵 Zalo Bridge",
        "cmd": ["node", str(SCRIPT_DIR / "bridges" / "zalo" / "zalo_bridge.js")],
        "cwd": str(SCRIPT_DIR / "bridges" / "zalo"),
        "proc": None
    }
}

RUNNING = True

def load_config() -> Dict[str, Any]:
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def send_telegram_notify(html_text: str):
    cfg = load_config()
    bot_token = cfg.get("telegram_notifier_bot", {}).get("bot_token")
    my_chat_id = cfg.get("telegram_notifier_bot", {}).get("my_chat_id")
    if not bot_token or not my_chat_id:
        return

    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": str(my_chat_id),
        "text": html_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(api_url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as response:
            pass
    except Exception as e:
        print(f"[!] Lỗi gửi Telegram notify từ supervisor: {e}")

def signal_handler(signum, frame):
    global RUNNING
    print("\n[!] Đang dừng toàn bộ các tiến trình nền của Mew Assistant...")
    RUNNING = False
    for s_key, s_data in SERVICES.items():
        proc = s_data["proc"]
        if proc and proc.poll() is None:
            try:
                proc.terminate()
                proc.wait(timeout=2)
            except Exception:
                proc.kill()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def cleanup_stale_locks():
    """Xóa các file lock session-journal còn sót lại nếu tiến trình trước đó bị tắt đột ngột"""
    for j_file in SCRIPT_DIR.glob("*.session-journal"):
        try:
            j_file.unlink()
            print(f"[✓] Đã dọn dẹp file lock cũ: {j_file.name}")
        except Exception:
            pass

def start_service(service_key: str):
    s_data = SERVICES[service_key]
    print(f"[+] Khởi động: {s_data['name']}...")
    try:
        proc = subprocess.Popen(
            s_data["cmd"],
            cwd=s_data["cwd"],
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        s_data["proc"] = proc
        print(f"[✓] {s_data['name']} đã chạy (PID: {proc.pid})")
    except Exception as e:
        print(f"[!] Lỗi khởi động {s_data['name']}: {e}")

def main():
    print("="*65)
    print("🚀 MEW OMNICHANNEL ASSISTANT SUPERVISOR WATCHDOG")
    print("• Tự động duy trì và giám sát 3 kênh: Telegram, WhatsApp, Zalo")
    print("• Tự động hồi sinh (Auto-respawn) khi có sự cố mạng hoặc crash")
    print("="*65)

    # 1. Kill các tiến trình cũ nếu còn sót lại & xóa lock
    os.system("pkill -f 'telegram_vnpt_monitor.py'")
    os.system("pkill -f 'whatsapp_bridge.js'")
    os.system("pkill -f 'zalo_bridge.js'")
    cleanup_stale_locks()
    time.sleep(1)

    # 2. Khởi chạy 3 services
    for s_key in SERVICES:
        start_service(s_key)

    # 3. Gửi thông báo khởi động toàn diện
    time.sleep(3)
    startup_msg = (
        "🚀 <b>MEW OMNICHANNEL ASSISTANT ĐÃ KÍCH HOẠT 24/7</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "Tất cả các kênh đã sẵn sàng nhận diện và cảnh báo tự động:\n"
        "• 🔷 <b>Telegram VNPT:</b> Lắng nghe mention (@tuanvq, @quctuan), reply và từ khóa trong mọi nhóm.\n"
        "• 🟢 <b>WhatsApp Client:</b> Tự động cảnh báo tin nhắn khách hàng 1-1, hỏi giá, link Figma/Docs.\n"
        "• 🔵 <b>Zalo Client:</b> Cảnh báo tin nhắn 1-1, nhóm đối tác, nhắc tên và link thiết kế.\n\n"
        "🛡️ <i>Tiến trình giám sát Supervisor Watchdog đang chạy ngầm để đảm bảo hệ thống luôn online!</i>"
    )
    send_telegram_notify(startup_msg)

    # 4. Vòng lặp Watchdog kiểm tra định kỳ
    while RUNNING:
        time.sleep(5)
        for s_key, s_data in SERVICES.items():
            proc = s_data["proc"]
            if proc is None or proc.poll() is not None:
                exit_code = proc.poll() if proc else "None"
                print(f"\n[⚠️ CẢNH BÁO] {s_data['name']} bị dừng (Mã thoát: {exit_code}). Đang tự động hồi sinh lại...")
                start_service(s_key)

if __name__ == "__main__":
    main()
