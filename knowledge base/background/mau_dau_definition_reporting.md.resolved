# Tài liệu Định nghĩa và Yêu cầu Báo cáo MAU/DAU 2026

## 1. Định nghĩa MAU & DAU

### 1.1. Khái niệm cơ bản
*   **DAU (Daily Active Users):** Số lượng người dùng hoạt động duy nhất trong một ngày (24 giờ).
*   **MAU (Monthly Active Users):** Số lượng người dùng hoạt động duy nhất trong một tháng (30 ngày gần nhất).

### 1.2. Tiêu chuẩn xác định "Active User"
Để đảm bảo tính thực chất, một người dùng chỉ được tính là Active khi thỏa mãn đồng thời các điều kiện sau:

*   **Trạng thái hoạt động (Foreground Only):** Chỉ tính những tương tác khi ứng dụng đang mở trên màn hình thiết bị. Không tính các hoạt động chạy ngầm (background refresh), tự động đăng nhập (auto-login) hoặc tin nhắn đẩy (silent push).
*   **Tương tác có ý nghĩa (Meaningful Engagement):** Phải gắn liền với nhu cầu thực tế của khách hàng (Ví dụ: Tra cứu cước, thanh toán, kiểm tra lưu lượng, đổi gói cước, nạp thẻ...).
*   **Định danh rõ ràng:** Phải xác định được MSISDN (Số điện thoại), Customer ID hoặc Account ID của người dùng.

### 1.3. Quy tắc "1-1" (Bắt buộc)
Một bản ghi dữ liệu được tính là 1 Active User (DAU/MAU) khi trong phiên truy cập đó xuất hiện:
1.  **Ít nhất 1 hành vi thuộc nhóm Core Session:** App Start, Login thành công, Landing Home...
2.  **VÀ Ít nhất 1 hành vi thuộc nhóm Engagement:** Click tra cứu, Click giao dịch, Click sử dụng dịch vụ...

### 1.4. Nguyên tắc định danh
*   **Duy nhất theo số thuê bao:** 1 SĐT = 1 User. Nếu một khách hàng đăng nhập trên nhiều thiết bị khác nhau trong cùng một khoảng thời gian báo cáo, hệ thống chỉ đếm là 1 User.
*   **Mở rộng bộ đếm (Growth Hack):** Việc đăng nhập và sử dụng dịch vụ trên **Lean Website** (truy cập từ Zalo OA) cũng được tính là 1 đơn vị MAU cho ứng dụng MyVNPT.

---

## 2. Tiêu chuẩn Phân tích MAU (MAU Breakdown)

Để phục vụ công tác tăng trưởng (Growth), MAU được bóc tách thành 3 nhóm:
*   **New A30:** Người dùng mới sử dụng App lần đầu trong 30 ngày.
*   **Retention A30:** Người dùng đã từng active trước đó 30 ngày và quay lại tiếp tục sử dụng.
*   **Resurrected A30 (Hồi sinh):** Người dùng đã "ngủ đông" (không hoạt động > 30 ngày) nhưng quay trở lại trong tháng báo cáo.

**Công thức tổng quát:** `MAU = New A30 + Retention A30 + Resurrected A30`

---

## 3. Yêu cầu Báo cáo theo dõi DAU/MAU

### 3.1. Báo cáo Tần suất Ngày (Daily Report - DAU Focus)
Mục tiêu: Giám sát sức khỏe vận hành và độ ổn định của dịch vụ.

*   **Chỉ số chính:** Tổng DAU, Tỷ lệ DAU/MAU (Stickiness).
*   **Phân tích sự biến động:** So sánh DAU ngày hiện tại với cùng kỳ tuần trước (DoW) và trung bình 7 ngày gần nhất.
*   **Top Dịch vụ hoạt động:** Danh sách 5-10 dịch vụ có lượng người dùng tương tác cao nhất trong ngày.

### 3.2. Báo cáo Tần suất Tháng (Monthly Report - MAU & Growth Focus)
Mục tiêu: Đánh giá hiệu quả chiến lược và các kịch bản tăng trưởng.

*   **Phân tích Cơ cấu MAU:** Tỷ lệ % đóng góp của New vs. Retention vs. Resurrected.
*   **Hiệu quả 80/20 (Pareto):** Theo dõi MAU của 20% nhóm dịch vụ cốt lõi đóng góp 80% MAU tổng (Gói cước di động, Thu cước viễn thông, v.v.).
*   **Động cơ Tăng trưởng (Growth Engines):**
    *   **Referral:** Số lượng Inviter/Invitee, tỷ lệ chuyển đổi sang thanh toán.
    *   **Group Buy:** Số phòng tạo, số phòng hoàn thành, số lượng user mua chung.
    *   **Lean Website:** Số MAU đóng góp từ kênh Zalo OA -> Lean Web.

### 3.3. Quy tắc làm sạch dữ liệu (Data Cleansing Rules)
Trong mọi báo cáo, phải áp dụng bộ lọc:
*   `Excluding False Events`: Loại bỏ các sự kiện lỗi hệ thống hoặc sự kiện ảo.
*   `Foreground Duration`: Lọc các phiên truy cập có thời gian Foreground > 0 giây.
*   `Identify Check`: Đảm bảo trường dữ liệu MSISDN không bị trống.
