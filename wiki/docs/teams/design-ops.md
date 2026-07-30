# 🎨 Hướng Dẫn Vận Hành Đội Ngũ Design Ops

Tài liệu này giải thích cách thức hoạt động của **Design Ops**, chuyên gia quản trị và duy trì (Maintain) Design System của dự án.

---

## 1. 👥 Các Thành Viên Khung (AI Agents)

Đội ngũ Design Ops hiện tại do một Agent duy nhất đảm nhiệm vị trí Tổng Tư Lệnh:

**🛡️ Design Ops (`roles/Design Ops/design_ops.md`):**
- **Vai trò:** Chuyên gia quản trị hệ thống thiết kế.
- **Nhiệm vụ:** Giám sát, đồng bộ, và hệ thống hóa các thành phần thiết kế (Components, Tokens, Guidelines) từ Figma. Chịu trách nhiệm xây dựng và cập nhật trang tài liệu nội bộ (Design System Docs Site) để đảm bảo mọi thành viên (Dev, QA, Designer) đều có chung một nguồn chân lý (Single Source of Truth).
- **Đầu ra:** Các bài viết Document cho Component, Changelog/Release Notes mỗi khi thay đổi Design System, và báo cáo kiểm tra tính đồng bộ (Consistency Report).

---

## 2. 🚀 Các Quy Trình Vận Hành (Workflows)

Design Ops hoạt động dựa trên bộ kỹ năng MCP kết nối trực tiếp với thiết kế để tự động hóa:

### ⚙️ Quy trình Quản lý Tokens & Components
- **Cách làm:** Sử dụng kỹ năng `/manage-tokens` để theo dõi thay đổi trên Figma MCP. Rút trích thông số kỹ thuật (Properties) và ánh xạ sang Code Variables.
- **Tự động viết Docs:** Kỹ năng `/build-docs` sẽ lấy dữ liệu từ Figma để sinh ra các bài viết Markdown/HTML chi tiết về trạng thái (States) và quy tắc (Guidelines: Do & Don't) của từng Component.

### 🛡️ Quy trình Rà soát & Đóng gói (Audit & Release)
- **Cách làm:** Kỹ năng `/audit-components` soi chiếu các luồng thiết kế để bắt lỗi các thành phần bị "detach" hoặc làm sai chuẩn Design System.
- **Phát hành (Version Control):** Khi đội Design chốt thay đổi, Design Ops sẽ sinh ra Release Notes theo chuẩn Semantic Versioning, ghi rõ thay đổi tác động đến tầng Code (Breaking Changes) để báo cho team Dev.
