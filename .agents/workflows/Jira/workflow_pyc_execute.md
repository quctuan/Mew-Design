---
description: Pipeline xử lý và thực thi một Phiếu Yêu Cầu (PYC) cụ thể từ Jira hoặc Link.
---

# Quy trình Thực thi PYC (PYC Execute)

**Mục tiêu:** Workflow dành cho việc bóc tách chi tiết yêu cầu từ một thẻ Jira PYC để đưa ra phương án triển khai, thiết kế hoặc báo cáo.

1. **Khởi Trình:** User gọi lệnh `/pyc_execute` kèm theo Link Jira hoặc mã Task (ví dụ: `IT360-1585614`).

// turbo-all
2. **Tiếp nhận & Bóc tách (Giai đoạn 1):** (Do **Jira Operations Bot** đảm nhiệm)
    - Truy cập Link Jira được cung cấp.
    - **Rào chắn SSO:** Nếu gặp màn hình Login, Bot yêu cầu BOSS cung cấp nội dung Description hoặc chụp ảnh màn hình thẻ Jira.
    - Trích xuất các thông tin:
        - Tiêu đề (Summary)
        - Nội dung chi tiết (Description)
        - Tài liệu đính kèm (Specs/Attachments)
        - Người yêu cầu & Deadline.

3. **Phân tích Nghiệp vụ (Giai đoạn 2):** (Do **Jira Logic Analyst** đảm nhiệm)
    - Đối chiếu nội dung PYC với bộ kiến thức hiện tại (Wiki/Existing Docs).
    - Phân tích luồng nghiệp vụ (Flow), các quy tắc (Rules) cần lấy.
    - Đánh giá mức độ ảnh hưởng đến hệ thống hiện tại.

4. **Đề xuất Giải pháp (Giai đoạn 3):**
    - Soạn thảo bản Draft phương án thực hiện (Implementation Plan).
    - Phác thảo cấu trúc dữ liệu hoặc giao diện (nếu cần).
    - Gửi bản nháp cho BOSS duyệt.

5. **Cập nhật Hệ thống (Giai đoạn 4):**
    - Sau khi BOSS `Approved`, tự động cập nhật vào Wiki dự án (`/wiki/docs`).
    - Gửi thông báo xác nhận thực thi lên Telegram nhóm.
