# Kiến trúc Nội dung Conversational Feed: Chiến lược 3 Lớp Khách hàng Đầu cuối

Để Agent "Emi" (hoặc Mya/Vivi) thực sự trở thành linh hồn của hệ sinh thái My VNPT theo đúng định hướng **Chủ thể Số (Digital Entity)**, giao diện màn hình Trang chủ (Homepage) không thể là một Sitemap tĩnh dùng chung cho mọi người. 

Trang chủ là một **"Dòng chảy AI Feed"**, nơi nội dung được nhào nặn và thả vào màn hình hoàn toàn dựa trên 3 vai trò (Roles) trong một Hộ gia đình Số (Smart Household).

---

## 1. Dòng Feed cho Nhóm Quản lý (Home Admin - Khách hàng Trọng tâm)
* **Keyword cốt lõi:** Bức tranh toàn cảnh (Bird's-eye view), Phân bổ tài nguyên, Cảnh báo sớm.
* **Tư duy thiết kế Feed:** Không bắt Home Admin đi tìm thông tin, Agent sẽ gom mọi "rủi ro" hoặc "đề xuất thay đổi" thành các Thẻ (Card) đặt lên đầu luồng.

### Các tuyến nội dung hiển thị trên Magic Zone / Agent Chat:
1. **Báo cáo Sức khỏe Hệ sinh thái:** 
   - *Thẻ Cảnh báo tài nguyên:* "Gói 4G của Mẹ sắp hết lúc 14:00, dung lượng chung của nhà mình còn dư 5GB. Emi chia sẻ sang cho mẹ luôn nhé?"
   - *Thẻ Sóng Wifi/Thiết bị:* "Emi phát hiện camera ngoài hiên mất kết nối lúc 2h sáng. Admin kiểm tra lại nguồn điện nhé!"
2. **Đề xuất Tối ưu Tài chính (Proactive Finance):** 
   - "Tháng vừa rồi hóa đơn lẻ của bố, mẹ và Admin mua Data gói ngày hơi nhiều (tổng 150k). Emi tìm thấy gói Home Combo X giúp cả nhà tiết kiệm được 100k/tháng. Đổi gói nhé?"
3. **Thanh toán & Chu kỳ (Actionable Bills):**
   - Thẻ Thanh toán 1-chạm gom toàn bộ cước phí viễn thông, truyền hình của cả đại gia đình, có chèn sẵn mã giảm giá phù hợp nhất.

---

## 2. Dòng Feed cho Nhóm Thụ hưởng Thụ động (Home Dependents)
* **Keyword cốt lõi:** Tối giản (Simplicity), Gỡ rối tự động (Auto-troubleshoot), Giải trí cá nhân hóa.
* **Tư duy thiết kế Feed:** Cực kỳ ít nút bấm. Chữ to, câu từ ấm áp. Triệt tiêu 100% các từ ngữ kỹ thuật viễn thông phức tạp.

### Các tuyến nội dung hiển thị trên Magic Zone / Agent Chat:
1. **Nút "Cứu hộ" (One-tap Troubleshoot):**
   - Thay vì hiện biểu đồ ping mạng, Feed chỉ hiện: "Ông bà thấy tivi MyTV bị giật? Bấm vào đây để Emi khởi động lại cục Wifi tự động nhé."
2. **Ủy quyền Yêu cầu (Delegation Requests):**
   - "Ông bà muốn xem phim bộ mới nhưng kênh này yêu cầu mua thêm gói. Emi đã gửi yêu cầu xin phép sang máy của Admin (Ba/Mẹ) rồi ạ. Ông bà đợi 5 phút nha!"
3. **Giải trí Y tế & An toàn (Care-as-a-Service):**
   - Thẻ hiển thị Cảnh báo lừa đảo: "Số điện thoại lạ 088... vừa gọi là số chuyên lừa đảo đã bị report. Emi tự động chặn số này cho ông bà nhé."
   - Thẻ Đề xuất MyTV: Gợi ý các kênh Sức khỏe, Thể dục buổi sáng, Cải lương phù hợp với nhân khẩu học lớn tuổi.

---

## 3. Dòng Feed cho Thế hệ số (Digital Natives)
* **Keyword cốt lõi:** Năng động (Dynamic), Theo Trend (Trendy), Quyền lực cá nhân (Self-serve).
* **Tư duy thiết kế Feed:** Xóa bỏ sự "già cỗi" của nhà mạng. Ứng dụng trông phải giống như một siêu ứng dụng mua sắm/giải trí hiện đại.

### Các tuyến nội dung hiển thị trên Magic Zone / Agent Chat:
1. **Gợi ý Tiêu dùng "Cắt lát" (Micro-transactions & OTT):**
   - "Đêm nay CKTG Liên Minh Huyền Thoại nhé. Emi gợi ý gói Data Đêm Tốc độ cao 5k/10 tiếng để combat mượt không ping nè."
   - Gợi ý mua gói vé Netflix / Spotify / Voucher Game trừ thẳng vào tiền điện thoại.
2. **Cộng đồng "Shadow Community" & Gamification:**
   - Đẩy mạnh các Thẻ Nhiệm vụ / Check-in: "Emi thách bạn đi bộ 5,000 bước ngày hôm nay để nhận 50 Point đổi voucher trà sữa đêyyy!"
   - Review sản phẩm: Thẻ chứa các bài review "1 phút" bằng định dạng Tiktok/Reel về tai nghe Bluetooth, Sim du lịch trên DigiShop để kích thích chốt đơn.
3. **Thanh lý tài nguyên chưa xài (Data Trading):**
   - Tính năng tự động định giá: "Tháng này dư 10GB Data lận, đổi lấy 2 voucher giảm giá Shopee nhé?"

---

### Tóm lại (Key Takeaway)
Kiến trúc **Conversational Feed** không yêu cầu người dùng phải "đi tìm" ứng dụng để làm gì. Mọi luồng thông tin sẽ được đẩy trực tiếp đến trang chủ từ các phân hệ ngầm (DigiBox, DigiShop, Tín hiệu Wifi) sao cho **đúng người, đúng ngữ cảnh nhất**. Trang chủ của mỗi thành viên trong gia đình sẽ trông khác nhau hoàn toàn.
