# Figma-to-Code Hybrid Rules

Đây là bộ quy tắc lai (Hybrid Rules) kết hợp sức mạnh từ **Figma MCP chính thức** (khả năng can thiệp sâu, tạo/sửa file) và triết lý tối ưu của **Figma-Context-MCP (GLips)** (lọc dữ liệu rác, hướng dẫn AI viết code chuẩn 1:1).

Khi thực thi bất kỳ nhiệm vụ Design-to-Code nào, Agent BẮT BUỘC phải tuân thủ 3 nguyên tắc cốt lõi sau:

## 1. Nguyên tắc Lọc Dữ liệu (Pruning Strategy)
Tuyệt đối không nhồi nhét toàn bộ file JSON từ Figma vào prompt để tránh "ảo giác". Áp dụng phễu lọc 3 bước:
- **Layout Extractor:** Chỉ lấy thông số về Auto Layout (Flexbox), Width, Height, Constraints. Bỏ qua các toạ độ X, Y tuyệt đối nếu đang dùng Flexbox.
- **Visuals Extractor:** Chỉ lấy thông số Fills, Strokes, Effects (Shadow, Blur), và Corner Radius. Bỏ qua các blend mode không cần thiết hoặc các layer bị ẩn (visible: false).
- **Text Extractor:** Chỉ lấy content text, Font family, Font weight, Font size, Line height, và Letter spacing.
- **Component Extractor:** Luôn ưu tiên trích xuất **Tên Variable/Token** thay vì giá trị cứng (Ví dụ: Lấy `color-brand-primary` thay vì `#0055FF`).

## 2. Tiêu chuẩn 1:1 Visual Parity (Bảo chứng Giao diện)
Code được sinh ra phải khớp 100% với bản vẽ. Agent cần thực hiện checklist sau trước khi hoàn thành:
- [ ] Mọi khoảng cách (Spacing, Padding) đã được ánh xạ chính xác sang Tailwind/CSS classes dựa trên Design System Tokens chưa?
- [ ] Cấu trúc DOM có đang tuân thủ đúng trật tự xếp chồng (Z-index) và định dạng khung (Frame/Group) trên Figma không?
- [ ] Đã loại bỏ các "Magic Numbers" (các con số px tự chế không nằm trong quy chuẩn) chưa?
- [ ] Các Component có hỗ trợ đủ các Variants (Hover, Active, Disabled) như khai báo trong Figma Component Set không?

## 3. Triết lý Unix (Do One Thing Well)
- **Đơn nhiệm (Focused Scope):** Một lệnh chỉ làm một việc. Đừng cố gắng vừa lấy thông số, vừa tải ảnh, vừa tự ý viết text. Lấy thông số trước, xác nhận, sau đó mới implement code.
- **Không tự sáng tác (Zero Hallucination):** Nếu Figma không quy định Auto Layout mà sử dụng toạ độ tuyệt đối, hãy cảnh báo ngay cho người dùng để họ sửa thiết kế, KHÔNG tự ý dùng `position: absolute` một cách bừa bãi trong code (trừ khi đó là chủ ý thiết kế).

## 4. Quản trị Asset & Hình ảnh (Asset Management)
- **Tính tạm thời của Dev Mode:** Các URL hình ảnh dạng `http://localhost:3845` được sinh ra bởi Figma MCP là TẠM THỜI (chỉ hoạt động khi ứng dụng Figma Desktop đang mở và Focus vào file).
- **Quy tắc xuất File:** Để đảm bảo Code chạy độc lập trên môi trường Production, BẮT BUỘC phải hướng dẫn User Export chính xác các Icon, Illustration (định dạng SVG, PNG) trực tiếp từ Figma và lưu vào thư mục `public/assets` của dự án. Không sử dụng ký tự text tĩnh thay thế cho Icon phức tạp.

## 5. Ánh xạ Cấu trúc Layout (Structural Parity)
- **Tôn trọng cấu trúc gốc:** Tuyệt đối không tự ý "chế" lại cấu trúc HTML/DOM (ví dụ: chia giao diện theo từng dòng (Row-by-Row) và dùng Padding ảo để canh lề) nếu Figma không làm vậy.
- **Tuân thủ Auto Layout:** Nếu Figma sử dụng cấu trúc 2 cột (Two-Column Flex Layout: Cột trái chứa toàn bộ Icon & Line, Cột phải chứa Text) để đảm bảo đồng bộ Spacing, Agent BẮT BUỘC phải dịch chính xác cấu trúc 2 cột đó vào Code (`flex flex-row > flex-col`). Đây là bí quyết duy nhất để đạt được Pixel-Perfect 100%.

---
**Agent Directive:** Khi kích hoạt các công cụ như `get_design_context` hoặc khi chuyển đổi Figma sang React/Tailwind/Swift, hãy tải bộ quy tắc này vào Context để duy trì mã nguồn sạch, chính xác và không bị đứt gãy hình ảnh (Broken Assets).
