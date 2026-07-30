---
name: Build Design System Docs Site
description: Quy trình tự động hóa cho role Design Ops để xây dựng tài liệu chi tiết cho các Component và cập nhật vào Design System Docs Site hiện có.
---

# Pipeline: Build Design System Docs Site

**Vai trò thực thi:** Cấp quyền điều khiển cho Agent **@Design Ops** (@[/Users/tuanvq/Documents/gds-myvnpt-wiki/.agents/roles/Design Ops/design_ops.md]). Toàn bộ quy trình phải tuân thủ nghiêm ngặt các quy tắc Pixel-Perfect, Data-Perfect và Zero Hallucination quy định trong Role này.
**Đầu vào (Input):** Link Figma chứa UI Components & Design Tokens.
**Môi trường đích:** Trang web tài liệu hiện có (https://gds-myvnpt-wiki.vercel.app/design-system/#/) và mã nguồn tương ứng trong dự án.

---

## Bước 1: Quét & Đọc hiểu Figma (Figma Extraction)
- **Hành động:** AI tiếp nhận Link Figma từ người dùng cho một Component cụ thể (VD: Button, Input, Card).
- **Phân tích:** Kích hoạt giao thức MCP để bóc tách toàn bộ thông số thiết kế, cấu trúc Auto-layout, Variants (trạng thái) và Design Tokens từ bản vẽ. 
- **Quy tắc:** Bắt buộc áp dụng Strict Token Mapping (chỉ ánh xạ vào `var(--token-name)`), tuyệt đối không tự "sáng tác" thông số rác.

## Bước 2: Tạo trang Component chi tiết (Documenting)
- **Hành động:** Kích hoạt kỹ năng `2_build_component_doc` để sinh ra file tài liệu chi tiết (Docs Page) cho Component vừa quét.
- **Tiêu chuẩn đầu ra:** Phải áp dụng đúng 7 phần cấu trúc bắt buộc (Header, Hero Preview, Examples/Variants, Usage Guidelines, Accessibility, Design Specifications, API Reference).
- **Đặc thù Code:** Code mô phỏng Component bắt buộc phải sinh ra cho các nền tảng được quy định (iOS dùng Swift, Android dùng Kotlin hoặc React/Tailwind tùy dự án).
- **Tích hợp:** Đưa nội dung tài liệu vừa tạo vào cấu trúc thư mục của dự án (map với Docs Site hiện hữu).

## Bước 3: Kiểm định chéo & Vòng lặp (Interactive Checkpoint & Loop)
- **Hành động:** 🛑 **BẮT BUỘC DỪNG LẠI** sau khi hoàn thành tài liệu của một Component.
- **Trình bày:** Hiển thị kết quả công việc và hỏi người dùng: *"Tôi đã hoàn tất tài liệu chi tiết cho [Tên Component] và cập nhật vào thư mục Docs Site. Bạn có muốn bổ sung thêm Variant nào không? Nếu ổn, hãy cung cấp link Figma của Component tiếp theo để tôi xây dựng, hoặc gõ 'Hoàn tất' để kết thúc."*
- **Vòng lặp:** Cứ lặp lại quy trình từ **Bước 1** đến **Bước 3** cho đến khi người dùng báo đã hoàn thành toàn bộ công việc.
