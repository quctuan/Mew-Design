---
description: Quy trình tự động hoá hand-off design figma to code
---

# 🚀 Workflow: Design to Code (Auto-Extraction & Preview)

**Mô tả:** Workflow tự động hóa toàn trình việc lấy giao diện từ Figma, bóc tách Component dùng chung vào Thư viện (Library) và sinh ra Code UI, đồng thời khởi chạy môi trường Preview trên IDE.
**Kích hoạt:** Khi User cung cấp một Link Figma và yêu cầu chạy workflow `/design-to-code`.

---

## Bước 1: Tiếp nhận và Phân tích Nguồn (Foundation Scan)
1. **Đọc Link Figma:** Sử dụng tool `get_design_context` (thuộc `figma_mcp_guide`) để lấy dữ liệu từ link Figma User cung cấp.
2. **Quét Component dùng chung:** 
   - Tham chiếu chéo (Cross-reference) với Design System gốc tại: `https://www.figma.com/design/LEPP6mucy8IwApPlDQ7VAH/-Mobile-App--Design-System?node-id=6-4428`
   - Phân tích xem bản vẽ mục tiêu có chứa các thành phần Foundation (Button, Chip, Alert, Snackbar, Input...) hay không.

## Bước 2: Xây dựng & Quản lý Thư viện dùng chung (The Library)
*Mục tiêu: Đảm bảo tính DRY (Don't Repeat Yourself) - Tái sử dụng code 100%.*
1. **Kiểm tra kho lưu trữ:** Truy xuất thư mục Library nội bộ (ví dụ: `src/components/ui/`, `Shared/UI/`). 
2. **Tạo mới (Nếu chưa tồn tại):** 
   - Nếu bản vẽ có dùng `Button` nhưng trong Library chưa có code của `Button`, AI bắt buộc phải đọc từ file Design System gốc để tạo ra file `Button` chuẩn (hỗ trợ đủ mọi variants/states).
   - Áp dụng nghiêm ngặt `figma-hybrid-rules` để code sinh ra được sạch nhất.
3. **Quy tắc Tái sử dụng vĩnh viễn:** Kể từ bây giờ, khi code bất kỳ màn hình nào, AI BẮT BUỘC phải **import** các Component từ Library này thay vì viết lại mã HTML/Native thô. 
4. **Bảo trì:** Khi có yêu cầu cập nhật (ví dụ: "Đổi màu Button"), AI chỉ được phép vào sửa trực tiếp trong Library, hệ thống sẽ tự động cập nhật lên mọi màn hình.

## Bước 3: Sinh Code Màn hình chính (Screen Generation)
1. **Lập Kế Hoạch (Planning):** Kích hoạt kỹ năng `writing-plans` (thuộc `.dev full/skills/`) để định hình kiến trúc Component Tree của màn hình.
2. **Bóc tách Layout (Structural Parity):** Dịch tư duy Auto-layout của Screen ra cấu trúc code Native/Front-end tương ứng. 
   - *Quy tắc Sinh tử:* **Tôn trọng cấu trúc gốc!** Nếu Figma dùng cấu trúc 2 cột (Two-Column Flex) để căn lề Icon và Text, phải code chính xác 2 cột song song. Tuyệt đối không tự chế lại thành Row-by-Row rồi dùng Padding ảo để "ép lề".
3. **Lắp ráp (Assembly):** Kích hoạt `executing-plans` để gọi và nhúng các Component từ Library vào màn hình chính. 
4. **Quản trị Asset (Asset Management):** Nếu màn hình chứa Icon phức tạp hoặc Illustration dạng SVG/PNG, AI phải yêu cầu User xuất file thủ công lưu vào thư mục `public/assets`. **Không dùng URL tạm thời** (`http://localhost:3845/...`) từ Figma Dev Mode trên Production vì chúng sẽ lỗi ngay khi đóng app Figma.
5. **Trích xuất File:** Lưu code hoàn chỉnh thành file màn hình độc lập (VD: `HomeScreen.tsx` hoặc `HomeScreen.swift`).

## Bước 4: Live Preview & Kiểm định 1:1 trên IDE
*Mục tiêu: Cho phép User nghiệm thu giao diện (Visual QA) ngay tức thì không cần thoát IDE.*
1. **Khởi chạy Môi trường Test (Local Server):** 
   - Tùy thuộc vào Tech Stack (React/Vite/Storybook), AI sẽ tự động đề xuất hoặc dùng `run_command` (có đánh dấu // turbo nếu an toàn) để bật server tại cổng localhost (ví dụ `http://localhost:3000`).
2. **Kích hoạt Auto-Preview:**
   - Thay vì hướng dẫn User, AI BẮT BUỘC phải tự động chạy lệnh mở trình duyệt trỏ tới cổng localhost vừa tạo.
   // turbo
   - Chạy lệnh `open http://localhost:3000` (hoặc cổng tương ứng) để trình duyệt tự động bung lên ngay lập tức. User có thể kéo tab đó vào chia đôi màn hình với IDE.
3. **Ping-pong Feedback & Debugging:** Yêu cầu User đối chiếu UI trên màn hình Preview với Figma gốc. Nếu có sai lệch nhỏ (ví dụ sai khoảng cách, lệch màu, vỡ layout), AI sẽ kích hoạt `systematic-debugging` (từ `.dev full`) để dò lỗi có hệ thống và sửa ngay lập tức. Bước này có thể dùng thêm `verification-before-completion` để đảm bảo chắc chắn Pixel-Perfect trước khi đóng hòm.

---

### 💡 Agent Self-Prompt (Cẩm nang nhẩm trong đầu của AI)
Mỗi khi chạy Workflow này, AI hãy tự nhắc nhở bản thân:
1. *"Khoan vội code màn hình! Phải check xem nó xài Component Foundation nào không. Có thì bóc ra vứt vào thư mục Library trước!"*
2. *"Nhớ dùng `figma-hybrid-rules` để lọc bớt mấy toạ độ tuyệt đối nhảm nhí của Figma, chỉ giữ lại Flexbox/Auto-layout."*
3. *"Cấu trúc Figma thế nào thì Code thế ấy! Đừng có bẻ 2 Cột thành Từng Dòng kẻo spacing lệch tè le!"*
4. *"Mấy cái ảnh Asset từ Dev Mode lát tắt app là hỏng hết, phải nhắc User tải về thư mục local ngay."*
5. *"Code xong phải tìm cách để sếp (User) xem được Preview ngay trên màn hình IDE. Thấy tận mắt mới tin là 1:1 Visual Parity!"*
