# Đánh giá Trải nghiệm và Giao diện (UI/UX) - Luồng Đăng ký Mobile Money

*Dựa trên việc kiểm tra trực quan các màn hình thiết kế trên Figma.*

## 1. Đánh giá UI (Giao diện người dùng)

### Tính thẩm mỹ (Aesthetics)
- **Hình ảnh thương hiệu:** Giao diện bám sát nhận diện thương hiệu của VNPT với tông màu xanh-trắng chủ đạo, tạo cảm giác chuyên nghiệp, an toàn và sạch sẽ - yếu tố cực kỳ quan trọng đối với các dịch vụ tài chính.
- **Thị giác (Visual Design):** Độ tương phản giữa chữ và nền tốt, kiểu chữ dễ đọc, phân cấp thông tin rõ ràng giữa tiêu đề chính, mô tả phụ và các trường nhập liệu. 

### Quy ước và Heuristic (Heuristics)
- **Tính nhất quán (Consistency):** Các thành phần giao diện như nút bấm (button), tiêu đề header, và các form nhập liệu được đồng bộ xuyên suốt từ màn hình định danh đến xác thực khuôn mặt.
- **Phòng ngừa lỗi (Error Prevention):** 
  - Tại bước **Bổ sung thông tin cá nhân MM**, nút "Tiếp tục" được thiết kế ở trạng thái vô hiệu hóa (disabled) khi người dùng chưa điền đủ các trường bắt buộc, giúp ngăn chặn lỗi do bỏ sót thông tin.
  - Khi có sự cố về **thông tin thuê bao không khớp**, hệ thống chặn lại bằng một thông báo (modal) trực quan, từ chối cho đi tiếp và hướng dẫn người dùng cách xử lý ngoại tuyến hiệu quả.

---

## 2. Đánh giá UX (Trải nghiệm người dùng)

### Khả năng khám phá (Discoverability)
- **Điểm truy cập:** Tùy chọn mở Mobile Money nằm ngay trong màn hình **Phương thức thanh toán**, xếp chung với các tùy chọn phổ biến như Ví điện tử hay Thẻ ngân hàng. Điều này giúp người dùng dễ dàng nhận thấy dịch vụ mới ngay trong luồng thanh toán quen thuộc mà không cần tìm kiếm sâu trong các tab ẩn.

### Khả năng hiểu (Comprehension)
- **Phản hồi lỗi rõ ràng:** Thông báo lỗi được viết bằng ngôn ngữ tự nhiên, mạch lạc, không dùng từ ngữ kỹ thuật (VD: *"Số điện thoại bạn cung cấp không trùng khớp với thông tin chính chủ..."*). Nó cũng cung cấp giải pháp cụ thể hướng dẫn người dùng ra điểm giao dịch GNPT có kèm cả địa chỉ và biểu tượng bản đồ giúp tăng cường khả năng định hướng tới điểm chỉ định.
- **Khẩu lệnh trực quan:** Màn hình **Xác thực khuôn mặt** cung cấp khung ovan hướng dẫn và câu lệnh rõ ràng *"Vui lòng giữ điện thoại ngang tầm mắt..."* giúp người dùng ngay lập tức hiểu điều họ cần làm.

### Khả năng học hỏi (Learnability)
- **Kế thừa các UI pattern thân thuộc:** Luồng đăng ký tái sử dụng lại các mô hình nhập liệu quen thuộc trên mobile (VD: Selector lựa chọn địa chỉ Tỉnh/Thành -> Quận/Huyện, Checkbox đồng ý cam kết). Người dùng không mất thời gian học cách dùng các tương tác giao diện phức tạp và có thể hoàn thành form một cách nhanh chóng.

### Sự định hướng (Orientation)
- **Tiêu đề theo ngữ cảnh:** Mỗi màn hình đều có một Header rất rõ ràng gắn với nhiệm vụ tại bước đó như *"Xác nhận thông tin thuê bao"*, hay *"Bổ sung thông tin cá nhân MM"*.
- **Theo lộ trình tuyến tính:** Quy trình diễn ra một cách tự nhiên và logic (Xem thông tin -> Bổ sung -> Xác thực sinh trắc học). Cấu trúc này không khiến người dùng bị lạc lối hay nhầm lẫn tiến trình.
