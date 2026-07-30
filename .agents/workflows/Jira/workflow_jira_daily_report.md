---
description: Pipeline Report: Kéo danh sách task rỗng/đang mở, báo cáo Telegram cơ bản.
---

# Workflow Jira Daily Report

**Mục tiêu:** Quy trình kéo report hàng ngày. (Quy trình 1 Sub-agent).

1. **Nhận lệnh:** Mở đầu ngày, Boss gõ `/workflow_jira_daily_report`.
2. **Kích hoạt System (Operations Bot):** 
   - Operations Bot dùng kỹ năng `jira_fetch` chạy script `/.agents/scripts/jira/jira_reporter.py`.
   - Script này sẽ gọi thẳng vào JQL của Hệ thống Jira nội bộ, trích xuất 50 Task mới nhất.
3. **Bắn Telegram:**
   - Bot dùng phương thức `telegram_notify` đẩy cục Data HTML/Plaintext đó lên Channel Telegram cho Sếp.
   - Báo cáo hoàn tất chu trình.
