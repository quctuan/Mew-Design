# 🗺️ Phân tách Journey & Flow: Inbound vs Outbound

**Mục tiêu:** Áp dụng 5 giải pháp lõi (Travel Pass, QR Payment, Virtual Transit, Insurance, Safety Alerts) vào thực tế hành trình từ lúc Xem -> Mua SIM -> Thanh toán -> Sử dụng tại nước ngoài. Chúng ta sẽ lọc và tùy biến giải pháp sao cho sát nhất với insight của từng tệp khách hàng.

---

## 🟢 BẢN 1: THE OUTBOUND JOURNEY (Khách Việt Nam sang nước ngoài)
*Thị trường ví dụ: Khách Việt Nam du lịch Thái Lan/Singapore.*
*Đặc điểm: Cần quản lý chi phí chặt (sợ Bill Shock, FX Fee) và cần bảo mật/bảo vệ rủi ro.*

### 1. Xem SIM & Mua Sắm (Pre-Trip)
*   **Điểm chạm (Touchpoint):** Khách mở app My VNPT -> Mục "Chuyển vùng Quốc tế (Roaming)".
*   **Trải nghiệm xem:** App hiển thị gói "Data Roaming Thái Lan 5 Ngày - 150k".
*   **Bán chéo 1 (Cart Interception - Cấy giỏ hàng):** Ngay dưới nút "Chọn gói này", thuật toán hiện thông điệp kích thích: *"Bạn sợ máy bay delay? Tích ✓ để **Mua Bảo hiểm du lịch PTI (Chỉ 50k)** - Tự động đền ngay 500k nếu delay quá 2 tiếng."*
*   **Bán chéo 2 (Piggyback - Đính kèm Pass):** Chuyển sang màn hình Thanh toán, tung đòn chốt hạ: *"Bạn từ sân bay về khách sạn bằng gì? Nâng cấp lên **Thai Explorer Pass (+80k)** để lấy trọn bộ eSIM + 3 Voucher Grab đón tại trạm Suvarnabhumi + Voucher 7-Eleven."*
*   **Thanh toán:** Khách trả 280k bằng VNPT Money. Đóng gói xong toàn bộ lo âu trước chuyến bay. (App nhắc nhẹ: Nhớ nạp sẵn tiền vào VNPT Money để qua kia tiêu không tốn phí chuyển đổi nhé).

### 2. Kích hoạt & Sử dụng thực tế (In-Destination)
*   **Hạ cánh (Arrival):** Tắt chế độ máy bay, My VNPT tự động bật sang **Travel Mode**. 
    *   *Giải pháp Safety:* Push notification đầu tiên: *"Chào mừng đến Thái Lan. Hãy lưu số Đại sứ quán VN (+66...) và Cảnh sát Du lịch (1155)."*
    *   *Giải pháp Pass:* Push notification thứ 2: *"Cần gọi xe về khách sạn? Lấy mã Grab trong thẻ Travel Pass của bạn ngay nhé."*
*   **Thiết lập Di chuyển (Mobility):** Tại nhà ga tàu điện BTS/MRT, thay vì đi xếp hàng mua xu nhựa, khách ấn nút **"Tạo thẻ Transit Ảo"** trên app My VNPT. Chỉ việc đập điện thoại (NFC/Mã vạch QR) vào cửa ga từ để đi.
*   **Thanh toán Ăn uống / Mua sắm (Finance):** Tại chợ đêm Jodd Fairs, quán ăn không quẹt thẻ tín dụng. Khách bấm nút **"Quét mã QR bằng VNPT Money"** -> Quét mã ThaiQR của bà chủ quán. Tiền trừ thẳng bằng VNĐ (Zero-FX fee). Không cần cầm một tờ Baht Thái nào trong tay.

---

## 🔵 BẢN 2: THE INBOUND JOURNEY (Du khách Nước Ngoài vào Việt Nam)
*Thị trường ví dụ: Khách Tây Ba Lô, Khách Hàn/Nhật nhập cảnh Nội Bài/Tân Sơn Nhất.*
*Đặc điểm: Rất ngợp về giao thông, sợ bị taxi chặt chém, khó khăn thanh toán (không có số TK ngân hàng VN).*

### 1. Xem SIM & Mua Sắm (Pre-Trip)
*   **Điểm chạm (Touchpoint):** Khách mua qua Website tiếng Anh của VinaPhone (Shop.vnpt.vn) từ khi còn ở nước nhà.
*   **Trải nghiệm xem:** Web hiển thị gói "Welcome to Vietnam Tourist eSIM".
*   **Bán chéo (The "Survival" Pass):** Thay vì bán riêng SIM, nhồi luôn thành một combo sống còn cực kỳ hấp dẫn: **"Vietnam City Pass (chỉ $15)"**. Khách được ôm luôn 3 món:
    *   1 Tourist eSIM (Không giới hạn Data).
    *   3 Voucher gọi XanhSM/Be từ sân bay về phố cổ (Trị giá $10).
    *   1 Voucher uống Cà phê Phin Highlands để trải nghiệm văn hóa.
    *   *(Không bán Bảo hiểm du lịch cho luồng này vì khách nước ngoài thường mua bảo hiểm toàn cầu ở nước họ rồi).*
*   **Thanh toán:** Khách cào thẻ Visa/Mastercard thanh toán quốc tế qua cổng Stripe/Paypal. Web trả về mã QR của eSIM gửi vào Email.

### 2. Kích hoạt & Sử dụng thực tế (In-Destination)
*   **Hạ cánh (Arrival):** Khách scan eSIM lấy mạng thành công ngay băng chuyền hành lý. 
    *   *Giải pháp Safety:* Push Notification tới bằng tiếng Anh: *"Beware of fake taxis! (Cẩn thận Taxi dù). Use the Be/XanhSM voucher in your Vietnam Pass to go to your hotel safely. If emergencies, call Tourist Police at 113."*
*   **Thiết lập Thanh toán (Finance - eWallet cho khách Tây):** Để giải quyết việc khách đi ăn Bún chả không thể xài thẻ Visa, App hướng dẫn khách **"Add Visa card to VNPT Money Tourist Wallet"**. Từ lúc này, khách dùng My VNPT (bản tiếng Anh) để giơ máy **Quét mã VietQR** tại xe nước mía, quán bún chả. Tiền tự động charge qua Visa của họ. Trải nghiệm Seamless hòa nhập bản địa vô bờ bến.
*   **Trải nghiệm Di chuyển (Mobility):** Dùng tính năng **"Virtual Transit Card"**, nhưng không phải để đi MRT (do làn xe buýt VN chưa phủ mạnh thẻ từ), mà tích hợp thành chức năng: **Vé xe Bus 2 Tầng (Hop-on Hop-off) điện tử**. Khách bước lên xe bus mui trần, chỉ cần chìa cái vé dạng Barcode trong hệ sinh thái My VNPT ra cho lơ xe quét.

---

## Tổng kết so sánh việc "Áp dụng 5 Giải pháp"

| Giải pháp Lõi | Luồng Outbound (Khách Việt đi xứ người) | Luồng Inbound (Tây vào Việt Nam) |
| :--- | :--- | :--- |
| **1. Travel Pass** | Bán combo Data + Voucher Grab Nước Ngoài + 7-Eleven | Bán combo eSIM + Voucher XanhSM/Be + Cà phê Highlands |
| **2. Thanh toán QR** | Quét QR điểm đến (ThaiQR/Alipay), trừ ví VNPT Money (Zero FX). | Liên kết thẻ Visa/Amex của khách vào VNPT Money để quét VietQR nội địa. |
| **3. Virtual Transit** | Dùng thẻ ảo (NFC/QR) đập cửa chui ga tàu điện (BTS/MRT). | Dùng vé quét Barcode đi xe bus 2 tầng du lịch (Hop-on Hop-off). |
| **4. Bảo hiểm** | Upsell mạnh lúc mua Data: Bồi thường Delay, mất hành lý. | Không áp dụng (hoặc chỉ bán kèm gói Bảo hiểm tai nạn giao thông xe máy rất nhỏ). |
| **5. Cảnh báo Safety** | Tự động báo số ĐSQ Việt Nam ở nước ngoài và số Cảnh sát nội địa. | Cảnh báo Scam/Taxi dù và hiển thị số 113, 115 bằng tiếng Anh. |
