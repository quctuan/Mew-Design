---
hide:
  - toc
---
# 🛠️ Bộ Công Cụ (Tool Stack)

Danh sách các công cụ nền tảng trong AI Workspace. Mỗi công cụ được phân định vai trò cụ thể nhằm tối ưu hóa quy trình làm việc và chất lượng thông tin.

---

## 1. 🤖 Antigravity (Agentic AI Workspace)
- **Vai trò:** Product Owner (PO), UI/UX Designer, Project Manager.
- **Mục đích:**
  Trung tâm quản lý phân bổ công việc cho hệ thống AI Agents.
  - **Dành cho PO:** Giao việc cho AI Teams (Research, Jira Tracking,...) qua Chat. Kiểm duyệt kết quả (HITL - Human in The Loop) và triển khai wiki qua lệnh `/deploy-website`.
  - **Dành cho UI/UX Designer:** Phối hợp cùng `ux-design-team` và `uiux-audit-team` để phân tích hành vi và kiểm định lỗi Edge Cases trải nghiệm.

---

## 2. 🎨 Figma
- **Vai trò:** UI/UX Designer, PO.
- **Mục đích:**
  Thiết kế giao diện và nguyên mẫu trực quan (Prototype).
  - **Thiết kế & Prototype:** Phác thảo Wireframes và thiết kế UI High-fidelity dựa trên luồng thao tác.
  - **Input cho AI Audit:** Cấp URL thiết kế cho `uiux-audit-team` thẩm định mức độ đảm bảo trải nghiệm người dùng theo đúng mục tiêu cấu trúc (JTBD).

---

## 3. 🎫 Jira (Task Tracking)
- **Vai trò:** Product Owner (PO), Techlead, Scrum Master.
- **Mục đích:**
  Theo dõi tiến trình Backlog, phân bổ công việc và quản lý rủi ro Sprint.
  - **Project Management:** Tạo, sắp xếp ưu tiên và theo dõi trạng thái các Tickets.
  - **Automated Tracking:** Hoạt động cùng nhánh `jira-tracking-team` tự động dò quét Tickets trễ hạn hoặc rủi ro vướng mắc (Blocked) để báo cáo.

---

## 4. ✈️ Telegram
- **Vai trò:** Bộ phận nhân sự và AI Bot.
- **Mục đích:**
  Hệ thống tiếp nhận thông báo nhanh (Alerts & Notifications).
  - **Reporting:** Cập nhật bản tin trạng thái dự án tự động hàng ngày từ quá trình report sinh bởi AI.
  - **Handoff (Chuyển giao):** Kênh thông báo phối hợp xét duyệt tài liệu hoặc nghiệm thu sản phẩm giữa các khối. Không sử dụng mục đích chuyển phát file.
