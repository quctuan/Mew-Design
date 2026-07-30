---
description: Lệnh chóp bu điều hướng 3 Use-cases (Report, Warning, Auto-Reply) của Jira Tracking Team.
---

# Jira Tracking Master Workflow

**Mục tiêu:** Workflow tổng rẽ nhánh thông minh dựa trên mong đợi của User, vận hành trơn tru giữa **Jira Operations Bot** và **Jira Logic Analyst**.

1. **Khởi Trình:** User gõ lệnh `/jira_tracking_master` kèm theo Use-case mong muốn (Report / Warning / Phản hồi tự động).
// turbo-all
2. **Định Tuyến Yêu Cầu:**
   - Nếu User cần **Tổng hợp Báo cáo Recap (Phân loại Task, Lọc thời hạn hạn chót/mới nhận)**: Gọi `/Jira/workflow_jira_weekly_recap`.
   - Nếu User chỉ cần **Xem số liệu rỗng/đang mở nhanh**: Gọi `/Jira/workflow_jira_daily_report`.
   - Nếu User cần **Phân tích độ gấp, soi rủi ro (Risk)**: Gọi `/Jira/workflow_jira_risk_warning`.
   - Nếu User cần **AI phân tích và tự động viết Comment lên thẻ Jira của nhân viên**: Gọi `/Jira/workflow_jira_auto_reply`.

3. **Luật Bất Di Bất Dịch:**
    - Bot Operations tuyệt đối không được tự Push dữ liệu (Write action) lên web Jira nếu chưa bắn bản nháp Draft lên Telegram cho nội bộ sếp đọc.
    - Bot Operations tuyệt đối không Push dữ liệu nếu hệ thống chưa nhận được lệnh `Approved` cuối cùng từ rào chắn HITL.
