# 🧩 Hướng Dẫn Vận Hành Hệ Thống URD Mapper

Tài liệu này giải thích cách thức hoạt động của URD Mapper, hệ thống quy chuẩn ánh xạ thiết kế Figma vào tài liệu URD (User Requirement Document).

---

## 1. 👥 Các Thành Viên Khung (AI Agents)

Hệ thống Mapper được điều phối bởi một tác nhân chính chuyên xử lý Specs:

**🎯 Figma URD Mapper (`roles/URD mapper/figma_urd_mapper.md`):**
- **Vai trò:** Chuyên viên Đồng bộ URD-Figma.
- **Nhiệm vụ:** Hiểu quy tắc đặt tên Figma, quét 'Mã màn hình' do PO điền sẵn trong URD, đối chiếu chính xác (Exact Match), bỏ qua Anti-patterns, xuất ảnh tự động từ Figma và chèn vào cột 'Giao diện' trong URD.
- **Đầu ra:** Bảng URD đã được lấp đầy cột hình ảnh giao diện chuẩn xác.

---

## 2. 🚀 Các Quy Trình Vận Hành (Workflows) & Kỹ Năng

URD Mapper hoạt động tuân thủ nguyên tắc `NO HALLUCINATION` (Không ảo giác) thông qua bộ quy tắc nghiêm ngặt:

### 📐 Kỹ năng Ánh xạ & Xuất ảnh (`Figma_To_URD_Image_Mapper_And_Validator`)
Đây là bộ khung xử lý cốt lõi, bắt buộc tuân theo:

**1. Quy tắc đặt tên (Naming Conventions):**
- Cú pháp chuẩn: `[Tiền tố loại] - [Tên Màn Hình] - [Trạng thái] - [Số thứ tự]`.
- Màn hình đúng chuẩn (Ví dụ: `SCR-Login-Default`, `POP-ConfirmDelete-1`).
- Agent sẽ tự động **BỎ QUA** các màn hình bắt đầu bằng `Z_` (Bản nháp), chứa khoảng trắng, gắn version (`-v2`), hoặc có tiếng Việt có dấu.

**2. Quá trình Thực thi (Execution Steps):**
- **Bước 1:** Đọc bảng URD đầu vào từ PO để trích xuất mảng `[Mã màn hình]`.
- **Bước 2:** Dùng `Figma_MCP` quét file thiết kế, lọc bỏ rác/bản nháp theo quy tắc Naming Convention để ra danh sách `Valid_Figma_Nodes`.
- **Bước 3:** So khớp chính xác 100% (Exact String Match) mã URD với tên màn hình Figma hợp lệ. Khớp thì gọi lệnh Export Image để lấy link ảnh thu nhỏ.
- **Bước 4:** Gắn ảnh vào cột `[Giao diện]` dạng Markdown Thumbnail. Nếu không tìm thấy, ghi rõ in đậm `[KHÔNG_TÌM_THẤY_TRÊN_FIGMA]`.

### 🔄 Pipeling với Workflow URD (`urd_mcp_figma_matcher`)
Quy trình URD Mapper thường chạy nối tiếp với quy trình phân tích yêu cầu (PYC Execute):
- **Giai đoạn 1:** Chạy quy trình PYC Execute để phân tích nghiệp vụ, sinh ra Bảng URD Khung (Có text mã màn hình, nhưng cột ảnh trống).
- **Giai đoạn 2:** Gọi URD Mapper đính kèm Link Figma. Mapper sẽ nuốt trọn bảng URD Khung, cắm ảnh vào và nhả ra bản URD Final 100% hoàn thiện.
