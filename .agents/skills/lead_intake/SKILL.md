---
name: lead-intake-and-task-synthesizer
description: Kỹ năng xử lý tin nhắn tiếp nhận brief, thu thập ngữ cảnh chat, trích xuất yêu cầu và tạo SOW / Timeline.
---

# Lead Intake & Task Synthesizer Skill

Kỹ năng chuyên biệt để phân tích hội thoại văn bản tự nhiên từ các ứng dụng chat (Telegram, Zalo, WhatsApp) và chuyển hóa thành thông tin công việc có cấu trúc.

---

## 1. Quy trình Xử lý Hội thoại Telegram (Internal VNPT)

```
[Tin nhắn Tag @username]
         │
         ▼
[Gom 10-15 tin nhắn trước] ──► [Lọc thông tin cốt lõi] ──► [Tóm tắt 3 ý chính] ──► [Gửi Alert]
                                                                                        │
                                                                   (Nếu có yêu cầu /sow)▼
                                                                           [Tạo file SOW & Timeline]
```

### Tiêu chí Trích xuất Ngữ cảnh:
1. **Người yêu cầu (Requester):** Tên, phòng ban/vai trò, cách xưng hô.
2. **Dự án liên quan:** Thuộc phân hệ nào (vd: My VNPT, SmartCA, Grab Voucher, Payment, CMS, Portal...).
3. **Mục tiêu công việc:**
   * Cần làm mới (New feature) hay sửa đổi (Change request / Bug fix)?
   * Đang ở bước nào (URD review, Wireframe, UI Figma, hay Handoff Dev)?
4. **Mức độ khẩn cấp (Urgency):**
   * 🔴 **Khẩn cấp:** Chứa các từ "gấp", "ngay hôm nay", "hotfix", "release tuần này", "block dev".
   * 🟡 **Tiêu chuẩn:** Các yêu cầu theo sprint thông thường.
   * 🟢 **Thảo luận sơ bộ:** Các câu hỏi thăm dò ý kiến, brainstorming.

---

## 2. Quy tắc Quản lý Checklist & Timeline (`/todo`, `/add`)

Khi người dùng kích hoạt lệnh `/todo` hoặc `/add`:
1. Phân tích nội dung công việc và hạn chót `DD/MM`.
2. Khởi tạo Checklist với mã số ID tương ứng trong `tasks_db.json`.
3. Sinh giao diện thẻ công việc kèm nút bấm tương tác `[ 1. ⬜ ]` để tick hoàn thành và thanh tiến độ trực quan.
4. Tự động đưa vào tiến trình nhắc việc 08:00 AM mỗi sáng.
