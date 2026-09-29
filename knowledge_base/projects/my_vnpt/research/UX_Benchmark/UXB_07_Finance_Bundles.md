# 💰 Concept Packaging: Trục Tiêu Dùng & Tài Chính (Finance)

Phân tích sâu các điểm chạm tài chính (Payment & Finance) trong hành trình In-Destination thông qua nền tảng VNPT Money được tích hợp bên trong My VNPT. Ý tưởng được chia tách rõ rệt dựa trên 2 tệp khách hàng.

---

## 1. Hành Trình Tài Chính: OUTBOUND (Người Việt ra nước ngoài)
*Pain point cốt lõi: Phí chuyển đổi ngoại tệ (FX Fee) của thẻ tín dụng quá đắt, cầm nhiều tiền mặt thì sợ mất, thủ tục hoàn thuế (Tax Refund) ở sân bay cực kỳ phiền toái.*

### 🚀 Idea 1: Giao Dịch Không Biên Giới (Cross-border QR Payment)
*   **Bối cảnh:** Các nước châu Á (Thái Lan, TQ, Hàn, Sing) đang cực kỳ chuộng quét QR code (PromptPay, WeChat, Alipay).
*   **Sản phẩm:** My VNPT mở tính năng "Quét Mã Du Lịch". VNPT Money liên minh với các mạng lưới thanh toán quốc gia sở tại.
*   **Trải nghiệm (UX):** Khách hàng mua xôi xoài bên Thái, mở My VNPT quét mã ThaiQR của bà chủ quán. App tự động hiển thị số tiền quy đổi sang VNĐ (với tỷ giá liên ngân hàng tốt nhất) và trừ thẳng vào số dư VNPT Money. **Cam kết Zero-FX Fee (Miễn phí chuyển đổi ngoại tệ)** – Tính năng "sát thủ" thu hút khách sử dụng thay vì quẹt thẻ Visa.

### 🚀 Idea 2: Hoàn Thuế Tức Thì Trong Lòng Bàn Tay (Digital VAT Fast-Track)
*   **Bối cảnh:** Mua sắm hàng hiệu (hóa đơn lớn) được hoàn thuế 7-10% nhưng phải ra quầy hải quan sân bay chờ đợi, điền form, và bù trừ bằng tỷ giá tệ của sân bay.
*   **Sản phẩm:** Hợp tác với các đơn vị như Global Blue.
*   **Trải nghiệm (UX):** Khách mua xong hàng, mở tab "Tax Refund" trên My VNPT, quét Barcode hóa đơn. Máy chủ ghi nhận. Khi ra sân bay chỉ cần hải quan scan xác nhận đồ, tiền hoàn thuế sẽ lập tức "Ting ting" trả về ví VNPT Money (bằng VNĐ) thay vì tiền mặt nước bạn hay đợi hoàn vào thẻ tín dụng sau 30 ngày.

### 🚀 Idea 3: "Campuchia" Xuyên Quốc Gia (Group Split Bill)
*   **Sản phẩm:** Giải quyết bài toán ăn uống theo nhóm (Family/Group).
*   **Trải nghiệm (UX):** Trưởng nhóm thanh toán hóa đơn bữa tối bằng cách quét QR. Trên lịch sử giao dịch hiển thị nút "Chia tiền (Split)". My VNPT sẽ gửi thông báo (Push) đến các thành viên trong nhóm đòi tiền (theo tỷ lệ chia đều hoặc tùy chỉnh), tự động quy đổi thành VNĐ để dễ dàng chuyển trả cho nhau bằng VNPT Money.

---

## 2. Hành Trình Tài Chính: INBOUND (Người nước ngoài vào Việt Nam)
*Pain point cốt lõi: Việt Nam là quốc gia đi theo hướng "Cashless" mã QR ở mọi nơi (VietQR từ quán trà đá đến nhà hàng), nhưng du khách nước ngoài không thể mở ví MoMo/ZaloPay/VNPay vì không có thẻ ngân hàng nội địa Việt Nam. Đổi tiền mặt thì dễ bị lầm giá hoặc đưa tiền rách.*

### 🚀 Idea 1: Ví Du Lịch Vãng Lai (Tourist Virtual E-Wallet)
*   **Sản phẩm:** Khi khách Tây mua eSIM (Vietnam Pass) trên web My VNPT, họ được kích hoạt đồng thời một Ví điện tử (Tourist E-Wallet) giới hạn định danh.
*   **Trải nghiệm (UX):** Khách có thể dùng chính thẻ Visa/Mastercard quốc tế của mình (hoặc Paypal/Apple Pay) để **"Top-up" (Nạp tiền trước)** vào Ví My VNPT bằng một số tiền ngân sách (ví dụ: Nạp $100 -> Tự quy đổi thành 2.500.000 VNĐ trong ví). 

### 🚀 Idea 2: Local QR Scanner (Thanh toán hẻm phố như người bản địa)
*   **Bối cảnh:** Ngồi uống cà phê bệt hay ăn hủ tiếu gõ, chủ quán chỉ nhận quét mã VietQR.
*   **Sản phẩm:** Khách Tây rút App My VNPT ra quét mã VietQR của tiệm hủ tiếu. Tiền trừ đi từ số dư của "Tourist E-Wallet".
*   **Trải nghiệm (UX):** Giao diện khi quét QR sẽ hiện TO RÕ con số quy đổi ra đồng tiền của đất nước họ (VD: Bill 50.000 VNĐ -> Bên dưới hiện "~ $2.00"). Khách cảm thấy rõ ràng, không bị chém giá, hòa nhập 100% vào văn hóa người bản địa (Local lifestyle).

### 🚀 Idea 3: Hoàn Tiền Hậu Chuyến Đi (Post-trip Refund)
*   **Bối cảnh:** Kết thúc chuyến đi Việt Nam, khách còn thừa 300.000 VNĐ trong ví ảo, bỏ đi thì tiếc.
*   **Sản phẩm:** Nút "Cash out to Card" (Rút tiền về thẻ quốc tế lúc đầu nạp vào).
*   **Trải nghiệm (UX):** Mở ra một vòng lặp tốt, tạo uy tín lớn về sự tử tế của dịch vụ Việt Nam. (Khách có thể quyên góp vào quỹ từ thiện VNPT hoặc rút tiền về thẻ gốc với 1 mức phí nhỏ).

---

### Khái Lược Hóa (Summary)

Khung trục Finance mở ra cái nhìn "Hệ sinh thái My VNPT = Telco + Fintech".

*   **Với Outbound (Người Việt):** VNPT bán nền tảng đi vay mượn của nước ngoài (QR Cross-border, Tax Refund) nhưng giao dịch thu về là VNĐ quen thuộc, tạo cảm giác an tâm.
*   **Với Inbound (Khách Tây):** VNPT cấp công cụ số để họ thâm nhập sâu vào nếp sống Việt Nam (quét QR ăn lề đường) mà không cần lo lắng thủ tục rườm rà. Viễn thông (eSIM) lúc này chính là cầu nối định danh để có Ví điện tử.
