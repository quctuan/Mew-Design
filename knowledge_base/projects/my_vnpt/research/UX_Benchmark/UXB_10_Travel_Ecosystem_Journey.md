# 🗺️ Master Flow & Journey: My VNPT Travel Ecosystem

**Mục tiêu:** Tích hợp 5 giải pháp lõi (Travel Pass, QR Payment, Virtual Transit Card, Travel Insurance, Safety/SOS Alerts) vào một luồng trải nghiệm duy nhất cho khách hàng Outbound. Biến My VNPT từ một app Viễn thông thành một Siêu ứng dụng Du lịch (Travel Super App).

---

## The Master Customer Journey (Outbound Persona)

### Phase 1: Pre-Trip (Giai đoạn hoạch định & Mua sắm)
*Mục đích: Móc nối và Bán chéo (Cross-sell) các dịch vụ phi viễn thông dựa trên hành vi mua Data Roaming.*

1.  **Trigger:** Khách hàng vào app My VNPT tìm mua gói Data Roaming đi Thái Lan cho 5 ngày.
2.  **Upsell "Bảo hiểm Du Lịch":** Ngay tại màn hình thanh toán Data, hệ thống check-box sẵn lựa chọn: *"Thêm Bảo hiểm du lịch PTI (Chỉ 50.000đ) - Tự động bồi thường 500k nếu chuyến bay delay quá 2 giờ"* -> Rất dễ chốt sale vì rẻ và gãi đúng nỗi đau delay.
3.  **Upsell "Travel Pass Combo":** Sau khi thanh toán xong Data + Bảo hiểm, hiện Pop-up: *"Bạn đã có mạng, nhưng bạn đi từ sân bay Suvarnabhumi về khách sạn bằng gì? Mua thêm **Bangkok Essentials Pass** (+80.000đ): Tặng mớ 3 voucher Grab 25% + 1 mã ưu đãi ăn uống 7-Eleven"*.
4.  **Wallet Activation:** Nhắc nhở nạp tiền vào VNPT Money với lời tựa: *"Nạp sẵn 2 triệu VND để qua Thái quét QR không mất phí chuyển đổi ngoại tệ!"*

---

### Phase 2: Arrival (Khoảnh khắc hạ cánh - The "Aha" Moment)
*Mục đích: Giải tỏa tâm lý lo âu khi đến nơi xứ lạ, khẳng định sự đồng hành.*

1.  **Trigger:** Khách hạ cánh, tắt chế độ máy bay. My VNPT bắt được sóng Roaming tại Thái Lan.
2.  **Context-Aware UI Switch:** App My VNPT tự động đổi từ "Chế độ Thường" sang **"Travel Mode"** (Toàn bộ thao tác nạp thẻ cào nội địa bị giấu đi, nhường chỗ cho Travel Dashboard).
3.  **Push Notification 1 (Welcome & Safety):** *"Chào mừng đến Bangkok! Nếu cần hỗ trợ khẩn cấp, số Cảnh sát du lịch sở tại là 1155. Đại sứ quán VN: +66 2 251 5836."*
4.  **Push Notification 2 (First Mile Mobility):** *"Đường truyền của bạn đã ổn định. Mở Travel Vault lấy voucher Grab để gọi xe về khách sạn ngay nhé!"*

---

### Phase 3: In-Destination (Tiêu dùng & Trải nghiệm nội địa)
*Mục đích: Giữ chân khách hàng dùng App liên tục (High Frequency) trong suốt chuyến đi bằng tiện ích thanh toán và di chuyển.*

1.  **Dùng Virtual Transit Card (Tàu điện/Bus):** 
    *   Khách đi BTS Skytrain. Thay vì xếp hàng mua xu nhựa, khách mở My VNPT -> Tab Di chuyển -> Nhấp **"Thẻ Transit Thái Lan"**. 
    *   App hiện một mã QR (hoặc tích hợp NFC). Khách đập điện thoại vào cổng từ sân ga để đi qua. Tiền trừ thẳng vào VNPT Money.
2.  **Dùng QR Payment (Ăn uống/Mua sắm):** 
    *   Khách ăn Tomyum tại chợ đêm Jodd Fairs. Quán không xài thẻ Visa, chỉ có bảng QR ThaiPay.
    *   Khách mở quét QR của VNPT Money quét mã. App hiển thị: *"Thanh toán 150 Baht = 105.000 VND. Tỷ giá 1:700 (0% FX Fee)"*.
    *   Khách bấm xác nhận. Giao dịch liền mạch, không lo giữ tiền lẻ.
3.  **Hệ thống Cảnh báo An toàn (Safety Alerts):** 
    *   Khách đi vào khu vực Sukhumvit ban đêm. GPS ghi nhận.
    *   App tự đẩy Notification: *"⚠️ Cảnh báo: Bạn đang ở khu vực có mật độ móc túi cao, hãy chú ý giữ gìn đồ đạc cá nhân. Bấm nút SOS đỏ trên màn hình 3 giây nếu cần trợ giúp khẩn gấp."*

---

### Phase 4: Resolution & Post-Trip (Xử lý sự cố & Kết thúc)
*Mục đích: Xây dựng lòng trung thành thông qua xử lý khẩn cấp và hậu mãi.*

1.  **Xử lý sự cố bay (Delay/Hủy chuyến):**
    *   Hệ thống API nhận diện chuyến bay của khách về VN bị delay 3 tiếng. 
    *   Do khách đã mua Bảo Hiểm PTI ở Phase 1, My VNPT lập tức nháy Notification: *"Chuyến bay của bạn bị trễ. PTI đã bồi thường nóng 500.000đ vào ví VNPT Money của bạn. Bạn muốn mua 1 vé vào phòng chờ VIP sân bay nghỉ ngơi không?"*
2.  **Nhắc nhở kết thúc hành trình:**
    *   Chuẩn bị lên máy bay về nước, hệ thống đo lường khách chưa xài hết dung lượng Data hoặc Voucher Grab.
    *   App thông báo: *"Dung lượng chưa xài hết sẽ được tự động quy đổi thành 500 điểm VinaPhone Plus. Hẹn gặp lại bạn ở quê nhà!"*
3.  **Trở về Normal Mode:** Hạ cánh Việt Nam, App tự động tắt "Travel Mode", trở lại giao diện Viễn thông bình thường.

---

## 🎨 Architecture of "My Travel Hub" Screen (UI Layout)
Khi App vào chế độ **Travel Mode (Phase 2 & 3)**, giao diện sẽ được tổ chức như sau:

*   **Zone 1: Dynamic Data Widget (Top)** - Vòng tròn cước data metering (Còn bao nhiêu MB), nút gạt "Nạp thêm Data khẩn cấp".
*   **Zone 2: Smart Financial & Transit (Mid-High)** - Nút Quét QR thanh toán to bự (Zero-FX), bên cạnh là Nút Mở thẻ Virtual Transit để đi qua trạm tàu điện.
*   **Zone 3: Voucher Vault & Travel Pass (Mid-Low)** - Hiển thị dưới dạng thẻ (Cards) các Voucher Grab, Klook, 7-Eleven khách đã mua từ trước. Vuốt (Swipe) để xài.
*   **Zone 4: The Safety Bar (Bottom Floating)** - Một thanh màu đỏ cực kỳ nổi bật bám đáy màn hình: Chứa nút gọi Cảnh sát địa phương / Gọi VoIP cho hotline Đại sứ quán VN / Nút kêu gọi bảo hiểm y tế.
