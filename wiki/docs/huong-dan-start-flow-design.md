# Hướng dẫn sử dụng Master Workflow: Start Flow Design

Đây là tài liệu Onboarding dành cho các thành viên trong đội ngũ Product & Design GDS-MyVNPT. Tài liệu này hướng dẫn cách sử dụng lệnh khởi tạo **Start Flow Design** - xương sống của toàn bộ hệ sinh thái thiết kế Trải nghiệm Người dùng tự động.

<div align="center" style="margin: 2.5rem 0;">
  <a href="../slide-master-workflow.html" class="md-button md-button--primary" style="font-size: 1.1rem; padding: 0.8rem 2.5rem; border-radius: 8px; font-weight: bold;">
    ▶️ Xem Master Flow Slide (Trình bày)
  </a>
</div>

---

## 🚀 1. Giới thiệu chung

Thay vì phải nhớ quá nhiều câu lệnh riêng lẻ cho từng tình huống (Jira, Email, Khảo sát mới), giờ đây bạn chỉ cần tương tác duy nhất với một **Master Menu** đóng vai trò như cô "Tiếp tân AI" của hệ thống. Master Menu sẽ dẫn dắt bạn đi từ lúc nhận yêu cầu thô sơ, cho đến khi xuất bản và đóng gói hoàn chỉnh tài liệu Spec Màn hình giao diện.

*   **Câu lệnh kích hoạt (Slash Command):** `/start_flow_design`

---

## 🛠 2. Quy trình Hoạt động (Step-by-Step)

### Giai đoạn 1: Mở phiên làm việc & Điều hướng
1. Tại khung chat, bạn gõ lệnh: `/start_flow_design`
2. Hệ thống chào mừng và hiển thị Menu 3 lựa chọn nguồn gốc yêu cầu:
   - **[1] Xử lý Yêu cầu từ Jira (PYC)**
   - **[2] Xử lý Yêu cầu từ Email / File đính kèm**
   - **[3] Yêu cầu khảo sát từ đầu (Nghiệp vụ BAU/SIP)**
3. Bạn **gõ phím số tương ứng (1, 2 hoặc 3)**.
4. Tuỳ thuộc vào lựa chọn của bạn, Hệ thống sẽ lịch sự xin thông tin tương ứng (VD: Xin Link Jira, hoặc xin Text Email). Nếu bạn chọn số [3], hệ thống sẽ tự động bắt đầu phỏng vấn bạn thay vì bắt bạn nộp link.
5. Hệ thống âm thầm đóng vai trò trung chuyển, đẩy dữ liệu của bạn sang 1 trong 3 nhà máy xử lý chuyên biệt.

*Trong lúc này, bạn đi uống một cốc nước và chờ đợi Agent làm việc: Phân tích Nỗi đau (Painpoint), lập Jobs-to-be-Done, nghiên cứu thị trường UX Benchmark, nặn ý tưởng, vẽ Flow và viết Copywriting...*

---

### Giai đoạn 2: Hậu xử lý & Đóng gói (Post-Processing)

Khi đã rặn ra được **bản Spec (URD)** hoàn chỉnh, Master Menu sẽ thức tỉnh và "nắm tay" bạn đi nốt 3 chặng cuối cùng để đóng gói sản phẩm hoàn hảo:

#### 📌 Chặng 1: Đồng bộ lên Google Docs
*   Hệ thống hỏi bạn có muốn đẩy file Spec này lên Google Docs không?
*   Gõ **Có**, Hệ thống sẽ chạy công cụ đồng bộ và trả về cho bạn 1 đường Link Google Docs xanh mướt (nhớ cấp quyền đăng nhập tài khoản Google nếu là lần đầu).

#### 📌 Chặng 2: Khai báo Mã Màn Hình
*   Hệ thống nhắc nhở bạn mở cái Link Google Docs vừa tạo ở trên ra. 
*   Tìm đến cái bảng "Chi tiết User Flow", tự tay điền **Mã Màn hình** hoặc **Tên Màn hình** vào cột tương ứng.
*   Xong xuôi, quay lại chat và gõ **"Done"** hoặc **"Đã điền xong"**.

#### 📌 Chặng 3: Dán Ảnh Figma Tự động
*   Hệ thống xin bạn **Link Figma** chứa thiết kế của tính năng tương ứng.
*   Dán link Figma vào. Lúc này Phép màu xảy ra: Hệ thống tự động cắt ghép screenshot từ Figma và dán ngay ngắn vào thẳng bản Google Docs của bạn rải đều theo từng Step flow.
*   Bạn ngồi ngắm lại ảnh trên Docs, thấy mượt rồi thì gõ **"Đã map ảnh xong"**.

#### 📌 Chặng 4: Sinh mã sự kiện Event Tracking
*   Chặng cuối cùng, Hệ thống hỏi bạn có muốn cắm **Tracking Event** (để đo lường bấm nút) cho luồng này không.
*   Gõ **Có**, Hệ thống lấy chính bản Google Docs chuẩn chỉ vừa nãy quét một lượt từ đầu đến cuối để đẻ ra bảng danh sách Gắn Tracking theo chuẩn Taxonomy 2026.
*   Kiểm tra lại ưng ý rồi là xong! Hệ thống chào tạm biệt và đóng phiên làm việc.

---

## 🎯 3. Lưu ý quan trọng (Best Practices)
*   **Luôn tương tác trực tiếp (HITL - Human in the Loop):** Quy trình được thiết kế đan xen các điểm dừng để chờ con người (là bạn) đọc và duyệt. Đừng vứt đó để Agent tự biên tự diễn.
*   **Linh hoạt thoát ngang:** Ở các chặng Hậu xử lý, bạn luôn có quyền gõ **"Không"** nếu bạn cảm thấy chưa cần đi tiếp (ví dụ Spec này quá nháp, chưa cần đẩy lên Docs hay xin Tracking). Hệ thống sẽ tự động đóng ngay lập tức các chặng sau.

Chúc các bạn có những nét vẽ trải nghiệm xuất chúng với Hệ sinh thái Flow Design!
