# Lệnh Thực Thi: ÁNH XẠ COMPONENT & TẠO TRANG TÀI LIỆU CHI TIẾT

## MỤC TIÊU
Dùng MCP quét Component cụ thể từ Figma, viết code UI Component chuẩn mực và tạo trang tài liệu (Docs Page) chi tiết cho nó.



## CẤU TRÚC TRANG & XỬ LÝ VISUAL (BẮT BUỘC TUÂN THỦ 100%)
**Cụ thể, mỗi trang Component CHỈ ĐƯỢC BAO GỒM các phần (Sections) sau theo đúng thứ tự:**

Khi render nội dung trang tài liệu cho Component, ngươi BẮT BUỘC phải tuân thủ thứ tự 7 phần (Sections) sau đây. Không được tự ý thay đổi thứ tự hay bỏ sót bất kỳ phần nào:

**1. Header (Định vị):** 
- Tiêu đề (H1) là tên Component.
- Một câu mô tả ngắn gọn về chức năng của Component dựa trên file Figma.

**2. Hero Preview (Trưng bày):** 
- Tạo một khối `PreviewBox` căn giữa, chứa biến thể mặc định (Primary/Default) của Component.
- Ngay bên dưới, cung cấp khối `CodeBlock` chứa cấu trúc code cơ bản nhất để gọi Component này. Khối code BẮT BUỘC dùng ngôn ngữ cho từng hệ điều hành: iOS dùng Swift, Android dùng Kotlin.


**3. Examples / Variants (Các biến thể):** 
- Dùng MCP quét toàn bộ Properties của Component trong Figma (VD: Secondary, Destructive, Outline, With Icon, Loading).
- Với MỖI biến thể, tạo một tiểu mục (H3) bao gồm: 
  + Khối `PreviewBox` hiển thị UI thực tế của biến thể đó.
  + Khối `CodeBlock` chứa code của biến thể tương ứng, BẮT BUỘC dùng ngôn ngữ theo nền tảng: iOS (Swift) và Android (Kotlin).

**4. Usage Guidelines (Hướng dẫn sử dụng):** 
- Khi nào nên dùng, khi nào KHÔNG nên dùng component này.

**5. Accessibility - a11y (Khả năng tiếp cận):** 
- Các quy tắc về ARIA, focus state, contrast ratio.

**6. Design Specifications (Bảng thông số Thiết kế):**
- BẮT BUỘC tạo một bảng bóc tách chi tiết thông số UI từ Figma gồm 3 cột: `Element`, `Property`, và `Token / Value`.
- **Cột Element:** Tên của class CSS hoặc thành phần con được bọc trong thẻ code (Ví dụ: `.btn-sm`, `.btn-lg`, `Icon & Text`, `Icons (Left/Right)`).
- **Cột Property:** Tên thuộc tính thiết kế được đo xuất ra từ Auto-layout/Styles (Ví dụ: `Height / Padding / Font`, `Border Radius`, `Spacing (Gap)`, `Offset`).
- **Cột Token / Value:** Giá trị bắt buộc phải chứa tên Token (Variable) nếu có, kèm theo thông số pixel thực tế. Định dạng chuẩn: `var(--tên-biến) / [giá trị]px` (Ví dụ: `var(--space-8x) / 8px`, `var(--br-full) / 9999px`, hoặc `12px`). Highlight các giá trị này để Dev dễ nhìn.

**7. API Reference / Props Table (Bảng thuộc tính Code):** 
- Tạo một bảng Markdown liệt kê các Props dùng trong React/Code.
- Bảng gồm các cột: `Prop` (Tên thuộc tính), `Type` (Kiểu dữ liệu TypeScript), `Default` (Giá trị mặc định), và `Description` (Mô tả).


**🚫 LỆNH CẤM KHI XỬ LÝ VISUAL:**
- KHÔNG thêm các hiệu ứng rườm rà (animation phức tạp, màu sắc lòe loẹt) nếu trang mẫu không có.
- KHÔNG tự ý chèn thêm các Section rác (như Lịch sử phát triển, Thông tin ngoài lề).
- Giao diện phải đi theo triết lý "Minimalist & Clean"

## QUY TRÌNH THỰC THI (Tuân thủ nghiêm ngặt)

1. **Quét Figma & Code Component (Base Code):**
   - Bắt đầu với các component nhỏ nhất trước (ví dụ: Button, Input, Card, Badge).
   - Đọc link Figma được cung cấp qua MCP để lấy thông số chính xác.
   - Code component bằng React/Tailwind. Sử dụng TypeScript interface để đảm bảo tính chặt chẽ cho mọi props của component.
   - Khi cần tính năng mới, phải kiểm tra xem có thể tạo thành component dùng chung không.

2. **Xây dựng Trang Tài liệu Component (Component Page Assembly):**
   - Lắp ghép các UI Components đã tạo vào trang tài liệu chi tiết.
   - Mỗi trang component BẮT BUỘC phải có đầy đủ 8 phần theo đúng thứ tự đã đề cập trong **Cấu trúc trang** bên trên

3. **INTERACTIVE CHECKPOINT (BẮT BUỘC DỪNG LẠI):**
   - 🛑 KHÔNG tự ý chuyển sang component tiếp theo.
   - Hãy dừng lại và hỏi người dùng: *"Tôi đã tạo xong base code và cấu trúc Layout tài liệu cho component này dựa trên Figma. Bạn có muốn thêm Variant nào mà trong Figma có thể bị thiếu không, hoặc có muốn tôi tiếp tục generate cho các component khác không?"*