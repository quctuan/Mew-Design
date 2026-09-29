# Lệnh Thực Thi: XÂY DỰNG KHUNG DESIGN SYSTEM DOCS SITE

## MỤC TIÊU
Thiết lập bộ khung (Base Layout), hệ thống định hướng (Routing) và nền tảng Design Tokens cho toàn bộ trang web tài liệu.

## QUY TRÌNH THỰC THI (Tuân thủ nghiêm ngặt)

1. **Khởi tạo Nền tảng & Design Tokens:**
   - Sử dụng MCP để quét file Figma Foundation (Colors, Typography, Spacing).
   - Khởi tạo file `styles/globals.css` chứa các biến đã quét.
   - Định nghĩa các biến gốc (ví dụ: `--color-primary`, `--spacing-md`, `--font-size-body`). Tuyệt đối không hardcode mã màu hex hay giá trị px thủ công vào component.

2. **Xây dựng Cấu trúc Giao diện (Layout):**
   - Tạo Layout chính cho trang web. Trang web BẮT BUỘC phải có thanh bên (sidebar) điều hướng cố định nằm bên trái.
   - Nội dung thanh bên phải được chia theo nhóm (Foundation, Components, Patterns) và các hạng mục bên trong mỗi nhóm PHẢI được sắp xếp theo bảng chữ cái (A-Z).
   - Xác định danh sách các Route cần thiết cho trang tài liệu.

3. **Thiết lập Cấu trúc Thư mục:**
   - Đề xuất cấu trúc Folder dựa trên bản blueprint. 
   - Xây dựng các nguyên tử (atoms) trong thư mục UI và tái sử dụng chúng.

4. **INTERACTIVE CHECKPOINT (BẮT BUỘC DỪNG LẠI):**
   - 🛑 KHÔNG tự ý viết code tiếp.
   - Hãy dừng lại và hỏi người dùng: *"Tôi đã trích xuất xong bảng màu, thông số spacing và dựng xong bộ khung Layout với Sidebar điều hướng. Đây là danh sách các trang và cấu trúc thư mục của Docs Site, bạn có muốn điều chỉnh gì không?"*