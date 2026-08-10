---
description: Pipeline Khởi chạy URD Mapper - Tương tác hỏi đáp từng bước để lấy Input từ User (Figma & URD)
---

# WORKFLOW: URD MAPPER (INTERACTIVE MODE)

**Mục tiêu:** Workflow này định tuyến quá trình thu thập thông tin đầu vào từ người dùng một cách chặt chẽ theo từng bước, sau đó tự động gọi Kỹ năng URD Mapper để đồng bộ ảnh từ Figma vào bảng Đặc tả.

## CÁC BƯỚC THỰC THI (Tương tác từng bước)

**Bước 1: Thu thập Figma URL**
- Agent tự động hỏi người dùng: 
  *"Chào bạn, để bắt đầu quá trình Đồng bộ giao diện, vui lòng cung cấp link **Figma URL** (link file hoặc Section thiết kế chứa các màn hình cần lấy ảnh)."*
- **!! QUAN TRỌNG:** Agent phải DỪNG LẠI và chờ người dùng nhập link. Không chuyển sang Bước 2 khi chưa nhận được URL hợp lệ.

**Bước 2: Thu thập Nội dung URD**
- Sau khi xác nhận đã nhận link Figma, Agent tiếp tục hỏi: 
  *"Đã nhận link Figma. Tiếp theo, vui lòng cung cấp nội dung hoặc đính kèm file **Bảng URD Input** (Bảng đặc tả này cần có sẵn các mã ở cột **[Mã màn hình]** để làm cơ sở truy xuất)."*
- **!! QUAN TRỌNG:** Agent phải DỪNG LẠI và chờ người dùng cung cấp bảng URD / file nội dung.

**Bước 3: Xác nhận thông tin và Khởi chạy Mapping**
- Agent tổng hợp lại 2 dữ liệu đã nhận được và in ra màn hình để người dùng kiểm tra thông tin.
- Hỏi người dùng: *"Thông tin đầu vào đã đầy đủ. Bạn đã sẵn sàng để hệ thống tự động quét Figma tìm ảnh và chép vào URD chưa? (Yes/No)"*
- Nếu người dùng đồng ý (Yes), Agent bắt đầu áp dụng các quy tắc/system prompt tại file `.agents/roles/URD mapper/figma_urd_mapper.md` để thực thi công việc. Quá trình xử lý nội bộ ẩn với người dùng để tránh nhiễu thông tin.

**Bước 4: Trả Biểu mẫu Kết quả URD Final**
- Sau khi kỹ năng/Agent URD Mapper xử lý xong, in ra Bảng URD đã được cập nhật hoàn chỉnh.
- Đảm bảo cột `[Giao diện]` đã được điền các thumbnail ảnh (cú pháp Markdown `![Mã màn hình](image_url)`) hoặc các thông báo `[KHÔNG_TÌM_THẤY_TRÊN_FIGMA]`/`[LỖI_XUẤT_ẢNH]` (nếu có lỗi như quy định của Role).
- Hỏi người dùng có muốn ghi đè kết quả vừa tạo vào file URD gốc hay chỉ xem tạm thời.
