# Hướng dẫn sử dụng Web App Quản lý Công việc (Task Manager)

Tài liệu này cung cấp hướng dẫn chi tiết dành cho các thành viên mới (Onboarding) để nắm bắt và sử dụng hiệu quả hệ thống **Web App Quản lý Công việc** đồng bộ thời gian thực với Google Sheets của team GDS-MyVNPT.

---

## 🌟 1. Giới thiệu chung
Web App Quản lý Công việc hiện đóng vai trò là "Trung tâm điều khiển" (Control Center) giúp các team theo dõi, khởi tạo và cập nhật tiến độ công việc một cách trực quan nhất. Thiết kế của App hoạt động độc lập với Google Sheets nhưng **đồng bộ dữ liệu 2 chiều** vào Database. Bất kỳ thay đổi nào trên Web cũng sẽ được ghi nhận xuống Sheets, và ngược lại.

**Lợi ích cốt lõi:**

- ⚡ **Tập trung hóa:** Không cần mở nhiều tab Google Sheets, mọi thứ nằm trên một giao diện thống nhất.
- 🎯 **Cảnh báo sớm:** Dashboard thông minh tự động chỉ điểm các Task sắp tới hạn hoặc vượt quá deadline `URD` / `Release`.
- ✏️ **Thao tác nhanh:** Hỗ trợ Inline-Edit (nhấn đúp để sửa) ngay trên lưới dữ liệu giống hệt Excel.

---

## 🗂 2. Cấu trúc các Trang (Phân hệ)

Menu điều hướng bên trái cung cấp các view dữ liệu chuyên biệt phân tầng cho từng đội nhóm và chiến dịch:

1. **Dashboard Phân tích:** Trang tổng quan (Overview) với hệ thống Scorecards đếm số lượng công việc Đang chạy, Tỷ lệ hoàn thành, và các cảnh báo **Sắp tới hạn / Quá hạn**. Cung cấp biểu đồ workload phân bổ theo nhân sự.
2. **Kế hoạch tháng:** Danh mục tổng thầu các công việc trọng tâm được đưa vào Sprint/Tháng hiện tại.
3. **Roadmap BAU / SIP / VNP:** Theo dõi vòng đời của sản phẩm, cấu trúc chẻ nhỏ công việc đường dài theo từng dự án lớn để báo cáo giám sát.
4. **Phát sinh (Ad-hoc):** Nơi xử lý rác/vấn đề phát sinh hàng ngày. Cụ thể là các Yêu cầu cải tiến (PYC) từ Jira, Nhiệm vụ Hỗ trợ (Support) hoặc xử lý Bugs. Chứa tính năng Lọc theo Tab độc quyền.

---

## 💻 3. Hướng dẫn Thao tác cơ bản

### 3.1. Thêm mới công việc (Create Task)
- **Bước 1:** Tại bất kỳ trang danh sách nào, nhấn nút **"+ Thêm Mới"** màu xanh đen ở góc trên bên phải.
- **Bước 2:** Điền các thông tin trong Modal xuất hiện. Chú ý các trường quan trọng:
    - **Nguồn (Source):** Web sẽ tự động thiết lập nguồn tương ứng với trang bạn đang đứng (Ví dụ: bấm + Thêm mới khi đang ở trang `Roadmap BAU` thì Task sẽ gán thẳng vào Sheet BAU).
    - **URD Date:** Ngày hẹn chốt Tài liệu Đặc tả Yêu cầu (URD). Format ngày được hiển thị qua Date Picker chọn lịch siêu nhanh gọn.
    - **Start / End Date:** Ngày khai mạc dự án và Ngày triển khai lên môi trường Live (Release) của Task.
- **Bước 3:** Bấm **Lưu Task**. Hệ thống sẽ hiển thị biểu tượng Loading xoay tròn và nhả ra Toast thông báo góc dưới khi dữ liệu đã được nạp qua API Google Sheets thành công.

### 3.2. Cập nhật tiến độ siêu tốc (Inline Edit)
Tuyệt tác tinh gọn nhất của Web App chính là tính năng Sửa Nhanh trên Lưới:
- 🖱 **Sửa Status/Trạng thái:** Bấm thẳng vào chữ Tình trạng ở cột cuối (ví dụ `In Progress`, `0%`, `Done`) để gõ Update tiến độ hiện tại. Enter để lưu.
- 📅 **Đổi Ngày tháng:** Bấm vào Text ô Ngày ở các cột Start, End, URD Date. Lập tức một Popup lịch phụ (Datepicker) sẽ hiện ra để bạn trượt thả vào ngày mới. Cực kì tiện.
- 👤 **Chuyển Assignee:** Bấm vào Tên người hiện tại để đổi qua tên thành viên khác đang gánh Task.

!!! warning "Lưu ý Đồng bộ"
    Mọi thao tác Edit sửa đổi trên Grid sẽ tốn khoảng 1-2s để đồng bộ tín hiệu tự động thông qua Background xuống Google Sheets. Hãy lưu ý **không đóng tab vội** trước khi Toast thông báo màu Xanh lá cây ("Đã cập nhật!") nổi lên!

### 3.3. Xóa Task (Delete)
Nếu thao tác nhầm hoặc Task đã thoái vốn, hãy tìm biểu tượng **Thùng rác** (Màu đỏ) ở góc ngoài cùng bên phải của Row Task đó. Nhấn xác nhận để vĩnh viễn xóa sạch dữ liệu khỏi lưới Web và DB Google Sheet.

---

## 🚨 4. Đọc hiểu Cảnh báo Dashboard (Top Alert)

Giao diện **Dashboard Phân tích** là nơi các Team Leader và Member bắt buộc phải Check-in vào mỗi buổi sáng. Tình hình Sức khoẻ dự án được thể hiện qua các thẻ cảnh giới cao nhất:

- 🟧 **Sắp tới hạn URD (5 ngày):** Các task có `URD Date` đếm ngược còn `<= 5 ngày`. Team làm tài liệu cần hối thúc chốt phương án.
- 🟨 **Sắp Release (7 ngày):** Các task có vòng đời sắp khép lại (`End date` <= 7 ngày). Dev, QC chuẩn bị test chót để đấm lên Live.
- 🟥 **Quá hạn URD / Quá hạn Release:** Báo động đỏ chót. Những task đã rớt deadline lùi về trước Ngày Hôm Nay (Today).
- 📜 **Bảng Danh sách Chậm URD:** Khu vực tập hợp Top các công việc trễ hạn lặp lại (Sort theo khoảng cách trễ nặng nhất lên đầu). Nơi công khai để bêu tên Member nắm Task. Đừng để bản thân bị treo tên lên bảng vàng này!

!!! tip "Thiết lập Nhắc việc"
    Hãy luôn đảm bảo trường **URD date** và **End date** được điền chính xác khi lập Task ban đầu. Nếu bỏ trống trường này, luồng Dashboard Algorithm sẽ không tính toán cảnh báo giúp team được!

---

## 🔍 5. Tiện ích Tìm kiếm (Search)
Không cần Ctrl + F lằng nhằng, ở phía trên giao diện mỗi bảng List luôn có khung **Tìm Kiếm Task (Search)**. Nhập cú pháp văn bản, Task Code, tên Mem... hệ thống sẽ lập tức Lọc (Filter) dữ liệu tại chỗ ngay thời gian thực (Real-time).

Hi vọng Cẩm nang này giúp các chiến binh mới (Newbies) của nhà GDS-MyVNPT chinh phục dễ dàng tiến độ dự án mà không cần nhờ đến quản đốc! Chúc các bạn làm việc hiệu quả và ra số bùng nổ! 🚀
