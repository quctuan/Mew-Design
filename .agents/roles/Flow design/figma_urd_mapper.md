---
skill_name: Figma_To_URD_Image_Mapper_And_Validator
description: "Kỹ năng Đồng bộ URD-Figma: Hiểu quy tắc đặt tên Figma, quét 'Mã màn hình' do PO điền sẵn trong URD, đối chiếu chính xác (Exact Match), bỏ qua Anti-patterns, xuất ảnh và chèn vào cột 'Giao diện'."
required_tools: [Figma_MCP]
---

# SKILL: ÁNH XẠ MÃ MÀN HÌNH VÀ XUẤT ẢNH UI VÀO URD

## 1. KNOWLEDGE: QUY TẮC ĐẶT TÊN FIGMA (NAMING CONVENTION RULES)
Agent BẮT BUỘC ghi nhớ bộ quy tắc này để nhận diện, lọc node hợp lệ và loại bỏ các node rác khi quét file Figma.

**1.1. Công thức bắt buộc (Phân tách bằng gạch ngang `-`):**
`[Tiền tố loại] - [Tên Màn Hình] - [Trạng thái] - [Số thứ tự]`
*(Trong đó Trạng thái và Số thứ tự là tùy chọn).*

**1.2. Bảng Tiền Tố Quy Ước (Prefixes):**
- `SCR`: Screen (Màn hình chính, full thiết bị). VD: SCR-Login-Default
- `POP`: Pop-up/ Modal (Hộp thoại nổi). VD: POP-ConfirmDelete-1
- `BTS`: Bottom Sheet (Cửa sổ trượt từ dưới lên).
- `Z_`: Archive / Draft (Bản nháp). BẮT BUỘC BỎ QUA.

**1.3. Các Anti-Patterns (Lỗi vi phạm BẮT BUỘC bỏ qua hoặc cảnh báo):**
- **Khoảng trắng vô tội vạ:** Tên màn hình hợp lệ không chứa khoảng trắng (VD: `login-screen` là đúng, `Login screen final` là sai).
- **Gắn version vào tên:** Tên màn hình là bất biến (Immutable). (VD: `SCR-Home` là đúng, `SCR-Home-v2` là sai).
- **Tiếng Việt có dấu:** Các tên chứa ký tự có dấu (VD: `SCR-HồSơ`) có thể gây lỗi.

---

## 2. TRIGGERS (ĐIỀU KIỆN KÍCH HOẠT)
Kích hoạt tự động khi người dùng (User/PO) cung cấp đồng thời 2 dữ liệu sau:
1. **Bảng URD Input:** Đã được điền sẵn các giá trị tại cột `[Mã màn hình]`.
2. **Figma URL:** Link của Section/File thiết kế chứa các màn hình đó.

---

## 3. EXECUTION STEPS (CÁC BƯỚC THỰC THI)

**Bước 1: Parse URD Targets (Lấy danh sách mã cần tìm)**
- Đọc bảng URD đầu vào.
- Trích xuất toàn bộ các chuỗi text nằm trong cột `[Mã màn hình]` thành một mảng mục tiêu (Ví dụ: `["SCR-Login-Default", "POP-ConfirmDelete-1"]`).
- Bỏ qua các hàng (row) có cột `[Mã màn hình]` bị bỏ trống.

**Bước 2: Fetch & Validate Figma Nodes (Quét và Xác thực dữ liệu thiết kế)**
- Sử dụng công cụ `Figma_MCP` để truy cập vào Figma URL được cung cấp.
- Lấy danh sách toàn bộ các Frame/Node cấp cao nhất (Top-level nodes) nằm trong link đó.
- **Tiền xử lý (Lọc rác):** Áp dụng Mục 1.2 và 1.3 để lọc dữ liệu. TỰ ĐỘNG BỎ QUA các node bắt đầu bằng `Z_` hoặc vi phạm Anti-Patterns (có chứa khoảng trắng, có gắn version v2/v3). Tạo ra danh sách `Valid_Figma_Nodes`.

**Bước 3: Exact Match & Export Image (So khớp 1-1 và Xuất ảnh)**
- Với mỗi mã màn hình lấy được từ Bước 1, dò tìm trong danh sách `Valid_Figma_Nodes` (Bước 2).
- **YÊU CẦU SO KHỚP CHÍNH XÁC (Exact String Match):** Tên node trên Figma phải giống y hệt 100% mã trong bảng URD (phân biệt hoa thường, KHÔNG tự ý đoán).
- **Nếu KHỚP:** Lấy `node_id` của màn hình đó, gọi lệnh Export Image qua `Figma_MCP` để lấy đường link ảnh thu nhỏ (`image_url`).

**Bước 4: Populate Output (Hoàn thiện bảng URD)**
- Giữ nguyên toàn bộ nội dung, cấu trúc và các cột khác của bảng URD gốc do PO cung cấp.
- Tại cột `[Giao diện]`: 
  - Chèn hình ảnh thu được từ Bước 3 dưới dạng Markdown thumbnail: `<img width="200" src="image_url" alt="Tên mã màn hình"/>` (Hoặc cú pháp `![Mã màn hình](image_url)` tuỳ thuộc hệ thống render).

---

## 4. STRICT GUARDRAILS & ERROR HANDLING (XỬ LÝ LỖI & CHỐNG ẢO GIÁC)
- **NO HALLUCINATION:** Tuyệt đối không tự sửa lỗi chính tả hay tự đoán tên màn hình. Chỉ dùng đúng chuỗi PO đã nhập.
- **KHÔNG TÌM THẤY:** Nếu một `[Mã màn hình]` trong URD không có node nào khớp trên Figma (hoặc node đó bị loại do vi phạm Anti-Pattern), BẮT BUỘC điền text in đậm **`[KHÔNG_TÌM_THẤY_TRÊN_FIGMA]`** vào cột `[Giao diện]`. Không được tự lấy ảnh màn hình khác đắp vào.
- **LỖI RENDER:** Nếu tìm thấy màn hình nhưng `Figma_MCP` báo lỗi không xuất được ảnh (do file quá nặng), điền **`[LỖI_XUẤT_ẢNH]`**.

---

## 5. HƯỚNG DẪN KẾT HỢP AGENT (PIPELINE)
Kỹ năng (Skill) này được thiết kế để hoạt động độc lập hoặc **chạy nối tiếp (Pipeline)** cùng với **Agent PYC Execute**. Khi thao tác, các PO hãy làm theo lưu trình sau:

1. **Giai đoạn 1 (Tạo URD Khung):** Gọi Agent PYC Execute để AI phân tích nghiệp vụ và tự động sinh ra bảng Đặc tả Kỹ thuật (Bao gồm các cột: Bước, Điểm chạm, Hành động, Mã màn hình...). Lúc này cột `[Giao diện]` sẽ để trống.
2. **Giai đoạn 2 (Fill Ảnh tự động):** Gọi ngay Agent URD Mapper này (đính kèm link Figma của team Design). Agent này sẽ nhận đầu vào là cái Bảng URD Khung vừa sinh ở Bước 1, tự động rà quét mã màn hình trên Figma và Fill toàn bộ ảnh Screenshot vào cột `[Giao diện]`, hoàn tất bản URD Final 100%.