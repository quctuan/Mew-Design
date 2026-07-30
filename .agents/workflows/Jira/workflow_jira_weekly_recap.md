---
description: Pipeline tổng hợp và tạo báo cáo Recap các Task Jira (Tự động kéo, phân loại và tóm tắt).
---

# Thực thi Tổng hợp Báo cáo (Weekly/Daily Recap) cho Jira

**Mục tiêu:** Workflow này kết hợp hai AI Agents để tự động hóa hoàn toàn quy trình truy xuất và phân loại tiến độ công việc trên hệ thống Jira.

1. **Khởi Trình:** User gọi lệnh phân tích tiến độ, gọi `/Jira/workflow_jira_weekly_recap.md`.

// turbo-all
2. **Kéo Dữ Liệu - Bộ Đọc:** (Do **Jira Operations Bot** đảm nhiệm)
    - Truy cập API Jira.
    - Đọc Cấu hình (Config) từ `.agents/roles/Jira/jira_report_config.md` để lấy danh sách Assignee hợp lệ, và các Trạng thái cần loại trừ.
    - Gọi API theo định dạng JQL (Thêm điều kiện ORDER BY duedate DESC) để load toàn bộ list Task thô.
    - (Nâng cao): Đối với mỗi Task, gọi API lấy nội dung của trường `Description`. Nếu có file đính kèm (Attachment) dạng Text (Word, Log, v.v.), xin quyền Session API để tải về và gộp vào Description (Nếu hệ thống vnpt không chặn).

3. **Phân Tích Dữ Liệu & Phân loại:** (Do **Jira Logic Analyst** đảm nhiệm)
    - Đọc Data JSON/Array thô vừa lấy về.
    - So sánh trường Issue Type với bộ quy tắc từ `.agents/skills/Jira/jira_classification_rules.md`.
    - Tách toàn bộ task thành 2 nhánh dữ liệu độc lập: **Nhánh PYC** và **Nhánh Support**.

4. **Khai thác Báo cáo (Recap Builder):** (Do **Jira Logic Analyst** đảm nhiệm)
    - Logic Analyst sử dụng kỹ năng `/professional_communication` đọc bộ khung mẫu `.agents/skills/Jira/telegram_report_template.md`.
    - Điền dữ liệu từ 2 Nhánh (PYC, Support) vào Template.
    - Tạo thành file báo cáo `jira_recap_report.md` chứa **2 bản báo cáo (Report) riêng biệt**.

5. **Cập nhật nội dung vào Google Sheet:** (Do **Jira Operations Bot** đảm nhiệm)
    - Cập nhật nội dung vào ggsheet này, ở tab `PhatSinh`.
    - Dữ liệu sẽ được fill vào theo rule như sau (dựa trên `.agents/skills/Jira/jira_classification_rules.md`):
        - **Cột Category**: fill theo output của bước 1 (gồm PYC và Support)
        - **Cột Phan loai**: fill theo output của bước 2 (các nhóm nghiệp vụ vd: Di động, Băng rộng cố định,....)
        - **Cột Ten dau viec**: fill tên task trên jira vào
        - **Cột Jira**: fill link jira của task đấy
        - **Cột Ngay tiep nhan**: lấy dữ liệu ngày tạo task
        - **Cột Ngay hoan thanh**: lấy dữ liệu due date

6. **Gửi Thông điệp / Auto-Split:** (Do **Jira Operations Bot** đảm nhiệm)
    - Bot Operations đọc Output từ báo cáo `jira_recap_report.md`.
    - **Thực thi 2 lệnh Push API Telegram độc lập:** Lệnh 1 gửi Báo cáo Tệp PYC. Lệnh 2 gửi Báo cáo Tệp Support.
    - (Hệ thống tự động cắt đôi (Split message) ở những ngắt dòng hợp lý nếu một trong 2 report vượt quá giới hạn API 4096 ký tự).
    
    *(Hoặc thay thế chạy toàn bộ quy trình trên bằng Script Python tự động: `python3 .agents/scripts/jira/jira_reporter.py`)*
