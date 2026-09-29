# 🎫 UX Benchmark & Ideation: My VNPT Travel Pass

**Mục tiêu:** Phân tích sâu mô hình "Travel Pass" (Gói Voucher Tiện Ích Du Lịch), xây dựng Customer Journey và các ý tưởng (Ideation) để tích hợp chéo với dịch vụ Roaming của VNPT nhằm gia tăng giá trị vào 3 nhu cầu chính: Di chuyển (Mobility), Ăn uống (F&B), và Vui chơi (Entertainment).

---

## 1. Bản chất của "Travel Pass" là gì?

"Travel Pass" không phải là một tính năng kỹ thuật mạng. Nó là một **"Pre-paid Bundle" (Gói cước trả trước dạng Voucher)** mà khách hàng mua hoặc được tặng *trước* khi chuyến đi bắt đầu. 

**Tại sao mô hình này lại thành công (Tâm lý học hành vi)?**
*   **Sự an tâm về ngân sách (Budget Certainty):** Khách hàng "khóa" trước một khoản chi phí di chuyển/ăn uống với giá hời để không lo biến động giá tại nước ngoài.
*   **Hiệu ứng chim mồi gài chéo (Cross-sell Hook):** "Chỉ cần mua SIM/Roaming của tôi, bạn sẽ được bao đi xe / ăn uống". Điều này biến Data Roaming từ một mức giá đắt đỏ thành một "Món hời".
*   **Sự điều hướng hành vi (Behavioral Guidance):** Khi đã cầm trong tay gói giảm giá Grab/Uber/Klook, khách hàng sẽ chủ động tìm kiếm các dịch vụ này trong app My VNPT thay vì tự ra ngoài tải app khác.

---

## 1.5. Benchmark: Cách Grab & Klook "Bán khéo" Travel Pass
Hai "ông trùm" này tuyệt đối không nhồi nhét hay spam người dùng mua Pass. Họ dùng nghệ thuật **"Contextual Upselling" (Bán trúng ngữ cảnh)**:

### 🌟 Chiến thuật của Grab (Bán theo Vị trí & Cảm xúc)
*   **The Airport Trigger (Đánh kích rào cản đầu tiên):** Khi khách mở app gọi xe đi *ra* sân bay Tân Sơn Nhất, thuật toán Grab biết khách sắp bay. Ngay lập tức pop-up: *"Sắp bay sang Thái hả? Mua gói Thailand Grab Pass chỉ 25k (Giữ giá cước 5 chuyến từ Sân bay Bangkok về khách sạn)"*. Họ chốt deal dựa trên nỗi sợ "bị chém giá hớ" khi vừa đáp xuống xứ lạ.
*   **Voucher Tiers (Chia gói rõ ràng):** Không bán voucher lẻ, Grab gói thành "Lite, Standard, Premium". Khách mua cái "Quyền" được giảm giá. Ví dụ: Bỏ 100k mua Pass, được 5 mã giảm mỗi mã 50k. Khách nhẩm tính "Lãi ngay 150k" nên bấm mua không hối tiếc.

### 🌟 Chiến thuật của Klook (Bán Kèm & Bán Combo Mẫu)
*   **Cart Interception (Bán cấy vào giỏ hàng):** Klook KHÔNG ép khách mua Travel Pass từ màn hình chính. Khi khách chọn mua *1 Vé Universal Studios Japan* (Sản phẩm lõi), ở màn hình checkout sẽ có Check-box sáng bừng: *"Thêm 150k nâng cấp thành Osaka Pass: Đi Universal + Thêm 1 vé Tàu Nhanh Express dỡ phải xếp hàng"*. Khách dễ dàng "móc mành" thêm tiền vì đang hứng thú.
*   **The "Choose 2 out of 30" (Bán quyền tự chọn):** Klook Pass không bắt khách chốt lịch trình ngay lúc mua. Khách chỉ cần mua "Klook Pass Singapore - Hạng 3 khu vui chơi". Sau đó khách được quyền tự do kích hoạt 3 trong 30 khu vui chơi tùy ý khi đến nơi. Vừa được cam kết giảm 45%, vừa giữ được sự tự do (Flexibility) cho lịch trình đi du lịch.

---

## 2. Customer Journey: "The Travel Pass Flow" (Split by Segment)

Mô hình Travel Pass sẽ có kịch bản hoàn toàn khác nhau tùy thuộc vào định hướng tệp khách hàng.

### 2.1. The Outbound Journey (Khách Việt Nam sang nước ngoài)
*Ví dụ: Khách Việt Nam sang du lịch Thái Lan.*

*   **Phase 1: Pre-Trip (Upsell lúc mua Data)**
    *   *Touchpoint:* Khách hàng lên My VNPT mua gói Data Roaming Thái Lan.
    *   *Action:* Màn hình thanh toán gài thêm tuỳ chọn "Nâng cấp lên **Outbound Thai Explorer Pass** (+50.000đ): Nhận ngay 3 mã giảm 25% xe Grab đón tại Bangkok và 1 voucher 100 Baht tại 7-Eleven".
    *   *Emotion:* Cảm thấy hời ngay từ lúc ở nhà, yên tâm về mặt đi lại nơi xứ lạ.

*   **Phase 2: Arrival (Bảo chứng First Mile khi hạ cánh)**
    *   *Touchpoint:* Tắt chế độ máy bay tại sân bay Suvarnabhumi, sóng Roaming được kích hoạt.
    *   *Action:* App tự đẩy Push Notification: *"Chào mừng đến Bangkok 🇹🇭! Bạn đã có đường truyền ổn định. Bấm vào mở Travel Vault lấy mã Grab gọi xe về khách sạn ngay nhé"*.
    *   *Emotion:* Nhận được sự chăm sóc kịp thời, giải tỏa áp suất tâm lý tìm phương tiện di chuyển.

*   **Phase 3: In-Destination (Hòa nhập và Tiêu dùng)**
    *   *Touchpoint:* Ăn uống và đi lại trong nội ô Bangkok.
    *   *Action:* Mở My VNPT để dùng mã quét ThaiQR Payment từ VNPT Money (không mất phí chuyển đổi ngoại tệ - Zero FX fee), hoặc đổi điểm My VNPT Point lấy vé tàu BTS qua cổng Klook tích hợp.
    *   *Emotion:* Dễ dàng thao tác qua 1 super app duy nhất mà không bị phân tán.

*   **Phase 4: Post-Trip (Gamification / Retention)**
    *   *Touchpoint:* Khách quay về Việt Nam.
    *   *Action:* Số lượng mã ưu đãi/Voucher di chuyển chưa xài hết được My VNPT tự động "bồi hoàn" thành điểm VinaPhone Plus.
    *   *Emotion:* Cảm giác không bị lãng phí tiền bạc, tăng hứng thú sử dụng My VNPT cho các tiện ích trong nước.

---

### 2.2. The Inbound Journey (Khách quốc tế / Việt Kiều nhập cảnh Việt Nam)
*Ví dụ: Du khách phương Tây hoặc Việt Kiều hạ cánh tại Tân Sơn Nhất / Nội Bài.*

*   **Phase 1: Pre-Trip (Mua trực tuyến trước khi cất cánh)**
    *   *Touchpoint:* Khách mua "eSIM Du lịch Việt Nam" qua Web/App (bản Tiếng Anh).
    *   *Action:* Web gợi ý gói combo **Welcome to Vietnam Pass**: Bao gồm 1 Tourist eSIM (10GB) + Tặng 3 chuyến xe XanhSM / Be đón từ sân bay + Tặng 1 ly Cà phê Phin Highlands để trải nghiệm văn hóa.
    *   *Emotion:* Thoáng đãng và thấy an tâm vì lo xong việc thiết yếu (Mạng + Phương tiện) ngay trước chuyến bay.

*   **Phase 2: Arrival (Vượt ải "Taxi Dù" sân bay)**
    *   *Touchpoint:* Khách scan mã QR eSIM thành công khi vừa lấy hành lý băng chuyền.
    *   *Action:* Giao diện app (hoặc zalo/SMS từ tổng đài) hiện link hướng dẫn gọi xe Be/XanhSM qua Mini-app tích hợp. Hướng dẫn khách điểm đỗ xe rõ ràng.
    *   *Emotion:* Cực kỳ an tâm, loại bỏ ngay điểm mù "bắt chẹt" taxi dù - pain point lớn nhất ở các cửa ngõ Việt Nam.

*   **Phase 3: In-Destination (Di chuyển tham quan Nội Địa)**
    *   *Touchpoint:* Cần khám phá thành phố, di chuyển các điểm di tích.
    *   *Action:* Khách mở My VNPT dùng Travel Pass quét mã QR điện tử bước lên xa bus 2 tầng (Hop-on Hop-off) thuận tiện. My VNPT Location-based thông báo các nhà hàng chấp nhận dùng mã thanh toán điện tử an toàn.
    *   *Emotion:* Trải nghiệm Seamless, du lịch không cần quá bận tâm rút tiền mặt (chống lừa đảo, trộm cắp).

*   **Phase 4: Post-Trip (Hồi hương & Lan tỏa)**
    *   *Touchpoint:* Trở lại máy bay rời khỏi Việt Nam.
    *   *Action:* Gửi thiệp điện tử lưu giữ kỷ niệm (Digital Memory), tặng mã giảm giá gia hạn eSIM/số điện thoại ảo để giữ số nhận báo cáo / OTP phục vụ kinh doanh sau này v.v.
    *   *Emotion:* Ấn tượng chuyên nghiệp về Dịch vụ số của Việt Nam.

---

## 3. Ideation: Mở Rộng Ý Tưởng Khai Thác Travel Pass Cho My VNPT

Để biến My VNPT thành hub trung tâm, chúng ta có thể thiết kế các lớp "Pass" dưới dạng Component cấu trúc (để bán chéo):

### Ý tưởng 1: The "Zero-to-Hero" Mobility Pass (Pack Đưa Đón)
*   **Nhu cầu:** Cú shock lớn nhất là từ Sân Bay Nước Ngoài về Khách Sạn. 
*   **Tích hợp (Partnership):** Hợp tác với các hãng gọi xe (Grab/Uber) hoặc các dịch vụ Airport Transfer toàn cầu (Klook/Traveloka).
*   **Sản phẩm:** Xây dựng một Mini-tool trên My VNPT: Gõ mã chuyến bay -> Ứng dụng tự đặt trước xe đón tại cửa sân bay điểm đến kèm Data Roaming trọn gói. 

### Ý tưởng 2: The "City Explorer" Lifestyle Pass (Dành cho Inbound/Outbound)
*    **Cấu trúc Package:** 
    *   **Inbound (Tây vào VN):** Bán "Vietnam Pass" (eSIM VNPT + Voucher gọi ứng dụng BE + Voucher Highlands Coffee + Vé Bus 2 tầng Hop-on Hop-off). Bán cái này ngay tại website khách mua eSIM trước khi bay.
    *   **Outbound (Việt ra Tây):** Đổi điểm VNPT để nhận chùm Voucher chuỗi cửa hàng tiện lợi phổ biến ở nước ngoài (vd: 7-Eleven Thái/Nhật, Lawson, GS25 Hàn). 

### Ý tưởng 3: Financial "Pay-As-You-Go" Pass (QR Xuyên Biên Giới)
*   **Nhu cầu:** Ẩm thực đường phố thường không nhận thẻ tín dụng, chỉ xài tiền mặt hoặc mã QR nội địa.
*   **Tích hợp:** Nếu VNPT Money mở rộng được liên minh QR (như VietQR đã quét được ThaiQR/PromptPay).
*   **Sản phẩm:** Chức năng "Du Lịch Quét Mã". Mở My VNPT ra, camera quét mã QR của hàng xiên nướng bên Thái Lan, tự động quy đổi tỷ giá sang tiền Việt và trừ vào Ví điện tử VNPT Money. Không cần mua ngoại tệ hay cầm tiền mặt lỉnh kỉnh.

### Ý tưởng 4: The "Family/Group" Shareable Pass
*   **Nhu cầu:** Đi du lịch gia đình người lớn tuổi hoặc đi theo nhóm bạn bè. Thường có một "Trưởng nhóm" đứng ra lo liệu mạng mẽo, gọi xe và trả tiền ăn uống cho cả hội. Nhóm hay gặp tinh trạng thất lạc nhau ở chỗ đông người hoặc khó chia tiền lẻ ngoại tệ.
*   **Sản phẩm (Tính năng mở rộng):**
    *   **Data & Voucher Sharing:** Trưởng nhóm mua 1 gói "Family Pass" dung lượng lớn. My VNPT cho phép "Chia sóng Roaming" cho các số phụ, hoặc "Bắn Voucher Grab/Klook" thẳng sang số điện thoại của bố mẹ qua SMS/Zalo để tự chủ động dùng.
    *   **Family Dashboard (Kiểm soát chéo):** Trưởng nhóm có một bảng điều khiển trên My VNPT để theo dõi dung lượng Roaming còn lại của các máy thành viên, tránh tình trạng có người lỡ xài lố Data bị trừ tiền ngoài gói (Bill Shock).
    *   **Family Safety / Radar:** Khi các thành viên trong nhóm cùng kết nối vào gói Family Pass, tích hợp tính năng định vị an toàn. Nếu bố mẹ đi lạc ở Pasar Malam (Chợ đêm), con cái có thể mở App để tìm vị trí hoặc nhấn nút "Ping" báo động tìm nhau.
    *   **"Campuchia" (Split Bill):** Tích hợp tính năng chia tiền của VNPT Money. Nhóm ăn xong quán hải sản, trưởng nhóm quét mã thanh toán ThaiQR bằng VNPT Money, sau đó bấm "Split Bill" -> App tự động gửi push notification đòi tiền từng thành viên trong nhóm theo VNĐ.

---

## Kết Luận cho Thiết Kế UI/UX:
Gói **Travel Pass** cần được thiết kế (UI) như một **Tấm Hộ Chiếu Số / Vé Điện Tử (Digital Ticket)**. 
- Trên giao diện bán Roaming, nó phải được trình bày theo dạng "Combo Add-on" với thiết kế đồ họa sinh động (dùng nhiều icon Phương tiện, Món ăn).
- Ở chiều sử dụng (Wallet), nó phải được gom vào một màn hình siêu tiếp cận tên là **"My Travel Hub"** với UX tối giản (Vuốt để dùng voucher, Quét QR để thanh toán) để phản hồi nhanh ngay cả khi ở nước ngoài đang gấp gáp.
