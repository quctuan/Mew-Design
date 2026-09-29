# Quy hoạch Phân hệ MyVNPT - Theo Định hướng Vertical Slices (Dịch vụ)

Cách chia này được gọi là **Vertical Slicing (Cắt dọc theo dịch vụ)** hay mô hình **Mini-CEO**. Trong đó, mỗi Product Owner (PO) sẽ làm chủ trọn vẹn một "Line of Business" (Ví dụ: Mảng Di động, Mảng Internet). PO này sẽ sở hữu toàn bộ phễu **AARRR** của dịch vụ đó, từ lúc tìm kiếm khách hàng mới cho đến lúc thu tiền và chăm sóc khách hàng cũ.

Cấu trúc này cực kỳ hiệu quả nếu công ty đang hạch toán doanh thu và chi phí riêng biệt cho từng mảng kinh doanh.

---

## 1. Domain: Dịch vụ Di động (Mobile Business)
**Vai trò PO:** Đóng vai trò "Giám đốc chi nhánh Di động số". Chịu trách nhiệm toàn bộ vòng đời của thuê bao VinaPhone trên app.

- **Acquisition (Bán mới):** Mua SIM mới, Đơn hàng SIM, Tra cứu đơn SIM, Gói cước 4G/5G, Mua thêm data.
- **Activation (Kích hoạt):** Kích hoạt SIM chính chủ, Đổi eSIM, Đăng ký eSIM watch.
- **Retention (Giữ chân & Self-care):** Quản lý thuê bao di động, Thông tin/Tra cứu thuê bao, Chuyển đổi SIM 4G, Quản lý cuộc gọi thông minh (báo bận, chữ ký, lời nhắn, cuộc gọi nhỡ).
- **Revenue (Doanh thu & Thanh toán):** Nạp điện thoại, Nạp qua thẻ/Mã thẻ, Chuyển trả trước sang trả sau, Quản lý Multi-SIM, Chuyển vùng quốc tế (Roaming).

---

## 2. Domain: Dịch vụ Cố định & Hộ gia đình (Home & Broadband)
**Vai trò PO:** Đóng vai trò "Giám đốc chi nhánh Hộ gia đình". Trọng tâm là bán các gói Combo và số hóa trải nghiệm chẩn đoán mạng, quản lý router tại nhà khách hàng.

- **Acquisition (Bán mới):** Mua SIM/Internet/MyTV (Combo), Đơn hàng Internet.
- **Activation (Kích hoạt):** Ký hợp đồng điện tử, Quản lý hợp đồng (dành riêng cho băng rộng).
- **Retention (Giữ chân & Self-care):** Thuê bao Internet, Quản lý Home Combo, Quản lý thiết bị, Quản lý Wi-Fi (Đặt lịch, Đổi tên/Pass, Khởi động), Kiểm tra tốc độ Internet.
- **Revenue (Doanh thu & Up-sell):** Mua thêm băng thông.
- **Referral (Lan tỏa):** Chia sẻ Wi-Fi (Tạo trải nghiệm liền mạch cho các thành viên trong gia đình).

---

## 3. Domain: Thanh toán & Tiện ích (Financial & Utility Services)
**Vai trò PO:** Quản lý "Ví/Nền tảng thanh toán" của người dùng. Tập trung vào việc xuất hóa đơn viễn thông và mở rộng hệ sinh thái thu hộ (Non-Telco).

- **Acquisition (Lôi kéo dùng ví):** (Tích hợp các banner dịch vụ điện, nước ra trang chủ).
- **Activation (Onboarding hóa đơn):** Nhắc nợ tự động, Thông báo cước.
- **Retention (Quản lý hóa đơn):** Tra cứu cước viễn thông, Xem chi tiết cước / Xem chi tiết hoá đơn / Xuất hoá đơn, Lịch sử đóng cước.
- **Revenue (Xử lý giao dịch):** Đóng cước viễn thông (Đóng cước tháng, Đóng trước cước), Đóng tiền điện, Đóng tiền nước, Đóng phí môi trường, Thanh toán VETC.

---

## 4. Domain: Hệ sinh thái Ưu đãi & Giải trí (Ecosystem & Partnerships)
**Vai trò PO:** Tăng giá trị cộng thêm cho toàn bộ nền tảng, kéo người dùng vào app để giải trí và sử dụng điểm thưởng từ Domain 1 & 2.

- **Acquisition & Activation:** Trưng bày các tiện ích đối tác thứ 3.
- **Retention (Daily Habit):** Vietlott Vinaphone, Vietlott SMS, VTV Cab, VNPT SmartCA.
- **Referral (Lòng trung thành):** VinClub, VinaPhone Plus, Voucher ưu đãi.

---

## 5. Domain: Nền tảng Core & Hỗ trợ (Platform CX & Support)
**Vai trò PO:** Vì chia dọc theo dịch vụ, sẽ luôn có những tính năng "Cắt ngang" (Horizontal) phục vụ chung cho cả mảng Di động, Internet và Thanh toán. PO này quản lý trải nghiệm nền tảng lõi.

- **Quản lý Đơn hàng chung:** Quản lý đơn hàng (Nơi tập trung theo dõi tracking cho cả SIM, Internet, Hàng hóa).
- **Trung tâm CSKH chung:** Trung tâm hỗ trợ, Tổng đài, Hướng dẫn.
- **Tracking chung:** Lịch sử hoạt động.
