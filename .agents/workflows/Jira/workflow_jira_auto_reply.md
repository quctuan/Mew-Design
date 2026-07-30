---
description: Tính năng Tự động phản hồi (Auto-reply): Thay mặt Boss comment thẳng vào Jira kèm duyệt Telegram.
---

# Workflow Jira Auto Reply

**Mục tiêu:** Viết Comment thay thế con người trên Jira để giục task. (Yêu cầu HITL tối cao).

1. **Nhận lệnh:** Boss gõ `/workflow_jira_auto_reply`.
2. **Kích hoạt System (Operations Bot):** Kéo Data thô về.
3. **Kích hoạt Brain (Logic Analyst):** 
   - Soi Rủi ro (Risk).
   - Suy nghĩ cách nhắn tin nhờ `professional_communication` để ra các Comments chuyên nghiệp.
   - Lưu trữ tạm vào file `jira_draft_comments.md`.
4. **Bắn Nháp Telegram:** 
   - Yêu cầu Operations Bot đẩy cục Draft đỏ chót rủi ro và các Comment định bắn vào Jira lên Telegram trước để nội bộ Boss nắm thông tin (Đáp ứng đúng Use-case).
5. **🛑 CHỜ PHÊ DUYỆT (HITL):** 
   - Dừng toàn bộ hệ thống API. 
   - Chờ Boss gõ `Approved` qua môi trường chat. Nếu Boss sửa chữ, lưu lại phiên bản sửa.
6. **Thực thi Ghi Đè (Operations Bot):**
   - Boss duyệt. Bot dùng API đẩy Action `Auto-Comment` thẳng vào Server Jira. Nhiệm vụ hoàn thành.
