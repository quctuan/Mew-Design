# 🔍 UX Research Insight: Du lịch Quốc tế (Inbound & Outbound)
- **Jira Task:** [Đề xuất Giải pháp Bundling Sản phẩm Du lịch trên My VNPT]
- **Tóm tắt Yêu cầu:** Xây dựng chân dung khách hàng chi tiết, phân tích Jobs-to-be-Done (JTBD), Usecase, và Insight từ social/internet cho tính năng Bán chéo (Cross-sell) dịch vụ viễn thông du lịch cho tệp Inbound và Outbound.

---

## PHẦN 1: TỆP INBOUND (Khách quốc tế đến Việt Nam)

### 1.1. Chân dung Khách hàng & Hoàn cảnh (The Moments)
- **Đối tượng:** Khách du lịch quốc tế (Khách lẻ FIT, Tây balo, khách châu Á như Hàn, Trung...) đến VN công tác hoặc du lịch.
- **Hoàn cảnh (When/Where):** Vừa đáp xuống cổng đến tại sân bay Nội Bài / Tân Sơn Nhất. Hành lý cồng kềnh, mệt mỏi sau chuyến bay dài. Không có WiFi 4G.
- **Cảm xúc (Emotional State):** Háo hức nhưng **Căng thẳng, Bối rối, Mất phương hướng**. Sợ bị taxi dù lừa đảo (scam).

### 1.2. Cách làm hiện tại (Current Workarounds) & Nỗi đau (Pain Points)
*(Tổng hợp từ Insight Reddit, TripAdvisor, TrustPilot)*
- **Mua SIM Vật lý tại Sân bay:**
  - *Workaround:* Đứng xếp hàng tại các quầy Kiosk mạng viễn thông.
  - *Pain Point:* Bất đồng ngôn ngữ; Nhân viên yêu cầu đưa Passport để scan (vi phạm privacy, rườm rà); Giá tại sân bay cao gấp 3-4 lần bên ngoài cửa hàng nội đô (Tourist Trap); Đặc biệt rủi ro đánh rơi SIM gốc của nước sở tại khi tháo lắp khay SIM.
- **Sử dụng Travel eSIM (Airalo, Mobimatter...):**
  - *Workaround:* Mua qua App trước khi bay. Đến nơi active.
  - *Pain Point:* Khách thất bại khi Scan QR (Do lỗi mạng, màn hình chói, phần mềm cũ); Quên không bật "Data Roaming" làm eSIM không bắt sóng được. Đặc biệt, **eSIM Data-only** khiến du khách KHÔNG THỂ tạo tài khoản Grab (yêu cầu nhận OTP qua SMS) để bắt taxi, hoặc không gọi được nhà hàng địa phương.

### 1.3. Usecase & Gợi ý Bundle (Từ Pain Points)
- **Usecase Cốt lõi:** Landing -> Cần Mạng -> Cần xe về Khách sạn an toàn -> Cần gọi điện thoại/Xác thực App.
- **Giải pháp Bundle (Starter Pack):** Bán **Tourist eSIM (Có sẵn một số phút gọi Local Voice / SMS)** + **Tích hợp sẵn Data** + Bundle voucher Xanh SM / Grab / Be Airport Transfer. Setup 100% Digital trước khi lên máy bay.

### 1.4. Phân tích JTBD (Tệp Inbound)
1. **Khi** tôi vừa hạ cánh xuống sân bay lạ -> **Tôi muốn** điện thoại có mạng 4G ngay lập tức mà không cần tháo lắp khay SIM hay xếp hàng -> **Để tôi** có thể book Grab an toàn về khách sạn giá rẻ và nhắn tin báo bình an cho gia đình.
2. **Khi** tôi cần đặt chỗ nhà hàng/tour local ở Việt Nam -> **Tôi muốn** eSIM của tôi có số điện thoại Việt Nam thay vì chỉ có Data -> **Để tôi** có thể nhận OTP xác thực các App local hoặc nghe shipper gọi giao đồ ăn.

### 1.5. Tổng hợp User Needs (Nhu cầu thực sự của Inbound)
Dựa trên phân tích JTBD và Pain points, nhu cầu thực sự của du khách quốc tế vượt xa việc chỉ mua gói cước viễn thông:
*   **Need 1: Connectivity ASAP (Kết nối cấp tốc):** Nhu cầu có mạng internet ngay giây phút hạ cánh hòng xóa bỏ sự bơ vơ và sợ hãi. Họ cần quy trình mua số hóa 100%, không cần xếp hàng, không đưa Passport gốc cho người lạ.
*   **Need 2: Local Integration (Hòa nhập bản địa):** Nhu cầu sử dụng các tiện ích nội địa (Grab gọi xe, ShopeeFood, VietQR thanh toán) mà không gặp rào cản về việc thiếu "Số điện thoại Việt Nam" hoặc "Tài khoản ngân hàng Việt Nam".
*   **Need 3: Safety & Assurance (Sự an tâm bảo vệ):** Nhu cầu được hướng dẫn, cảnh báo các rủi ro (Scam taxi, móc túi) và liên lạc khẩn cấp (Tourist Police) nếu có sự cố bất đồng ngôn ngữ.
*   **Need 4: Seamless Economy (Kinh tế liền mạch):** Nhu cầu thanh toán minh bạch, không bị lừa đảo tỷ giá, không muốn giữ nhiều tiền lẻ tiền giấy lạ lẫm.
*   **Need 5: AI Concierge & Language Bridge (Phiên dịch & Trợ lý thông tin):** Rào cản lớn nhất khi ra đường phố là giao tiếp. Khách rất cần một "Local Guide" bỏ túi, dịch thuật tức thời Menu quán ăn bằng camera, hoặc hệ thống nhắn tin tự động dịch ngôn ngữ khi liên hệ với dịch vụ nội địa (giống Grab Chat).
*   **Need 6: Logistics Freedom (Tự do hành lý):** Giờ check-in khách sạn thường là 14:00 trong khi khách hạ cánh lúc 9:00 sáng. Họ cần dịch vụ gửi/giao hành lý thẳng về khách sạn (như LuggAgent) để rảnh tay đi chơi ngay lập tức mà không phải khệ nệ vali.

---

## PHẦN 2: TỆP OUTBOUND (Người Việt Nam đi Quốc tế)

### 2.1. Chân dung Khách hàng & Hoàn cảnh (The Moments)
- **Đối tượng:** Người Việt đi du lịch tự túc, đi công tác nước ngoài (Hàn, Nhật, Thái, Châu Âu...).
- **Hoàn cảnh (When/Where):** 
  - (1) Đang ở nhà soạn Vali, lướt điện thoại tìm hiểu mua SIM.
  - (2) Ngày cuối ở nước ngoài bị hết dung lượng giữa đường lướt Google Maps tìm đường ra ga tàu.
- **Cảm xúc (Emotional State):** **Sợ hãi (Sợ lạc đường), Bực bội (Hết dung lượng), Xót tiền (Sợ Bill Shock).**

### 2.2. Cách làm hiện tại (Current Workarounds) & Nỗi đau (Pain Points)
*(Tổng hợp từ Insight Facebook Group Du Lịch, Tiktok)*
- **Thuê Cục Phát WiFi (Pocket WiFi):**
  - *Workaround:* Thuê tại VN mang đi, hoặc nhận cục WiFi tại sân bay KIX, Narita.
  - *Pain Point:* Phải mang vác lỉnh kỉnh, thêm 1 cục sạc dự phòng vì thiết bị rất tốn pin. Phải xếp hàng lấy/trả thiết bị mất thời gian. Đi tách nhóm là những người còn lại mất mạng.
- **Mua Sim Local nước bạn (Qua Shopee/Klook):**
  - *Workaround:* Mua SIM Thái (DTAC, AIS), SIM Nhật giao tận nhà trước.
  - *Pain Point:* Phải tháo SIM chính VN ra -> **LÀM MẤT KHẢ NĂNG NHẬN OTP NGÂN HÀNG**. Khi quẹt thẻ tín dụng ở nước ngoài bị lỗi không có cách nào nhận SMS từ ngân hàng VN để xử lý.
- **Sử dụng Data Roaming mạng VNPT/Viettel:**
  - *Workaround:* Bật Roaming Data vì tiện, giữ được SIM chính.
  - *Pain Point:* Nỗi ám ảnh kinh hoàng về **"Bill Shock" (Hóa đơn cước phí hàng chục triệu)** do không kiểm soát được dung lượng ngầm update app; App My VNPT thiết kế luồng tra cứu dung lượng Roaming chậm chạm, hết data tốc độ cao không báo trước khiến khách hàng bị trừ cước ngoài gói phát sinh vô tội vạ.

### 2.3. Usecase & Gợi ý Bundle (Từ Pain Points)
- **Usecase Cốt lõi:** Sắp bay/Khởi hành -> Cần kết nối Internet ổn định ở nước bạn -> Cần nhận OTP thanh toán thẻ -> Cần cảm giác An Toàn.
- **Giải pháp Bundle (Safe & Connect):** Bán Gói cước Roaming **(Cơ chế Fixed-Price, cam kết 100% không Bill Shock - chặn sài lố cước)** + **Tương thích Wifi Calling (Voice over Wifi)** để nhận OTP free + Combo **Bảo Hiểm Du lịch PTI cover rủi ro chuyến bay**. Hỗ trợ pop-up Nudge khi xài đến 80% dung lượng Data để giới thiệu gói Upsell nhỏ.

### 2.4. Phân tích JTBD (Tệp Outbound)
1. **Khi** tôi chuẩn bị ra nước ngoài -> **Tôi muốn** điện thoại có sẵn mạng Data mà vẫn giữ được SIM gốc Việt Nam -> **Để tôi** có thể nhận được tin nhắn SMS OTP từ ngân hàng khi quẹt thẻ mua sắm.
2. **Khi** tôi sử dụng Data Roaming ở nước bạn -> **Tôi muốn** chặn toàn bộ rủi ro cước phát sinh thụ động và được cảnh báo rõ ràng khi sắp hết gói -> **Để tôi** không phải nhận hóa đơn hàng triệu đồng khi về nước (Bill Shock).
3. **Khi** tôi lên lịch trình khởi hành đi du lịch -> **Tôi muốn** mua Data Roaming và Bảo hiểm du lịch trong cùng một nút bấm -> **Để tôi** an tâm tuyệt đối về mặt sức khỏe và liên lạc với chi phí tối ưu nhất.

### 2.5. Tổng hợp User Needs (Nhu cầu thực sự của Outbound)
Người Việt Nam khi đi du lịch nước ngoài mang theo tâm lý phòng vệ cao, vì vậy các User Needs tập trung mạnh vào rào cản chi phí và an toàn:
*   **Need 1: Financial Transparency & Control (Kiểm soát cước phi tuyệt đối):** Nhu cầu gạt bỏ nỗi sợ "Bill Shock" 100%. Họ cần một công-tơ-mét đo thời gian thực rõ ràng, các cảnh báo trước khi hết gói (80%, 90%), và cam kết ngắt mạng thay vì tự động trừ cước vượt lưu lượng.
*   **Need 2: Cross-border Financial Utility (Thanh toán xuyên biên giới giá rẻ):** Nhu cầu quẹt thẻ, quét QR thanh toán nước ngoài bằng chính dòng tiền VNĐ của mình mà không bị tính phí FX Charge đắt đỏ (Zero-FX fees). Hoàn thuế (Tax Refund) trực tiếp tự động không qua rườm rà giấy tờ.
*   **Need 3: OTP Accessibility (Duy trì liên lạc gốc):** Khát khao dùng SIM chính ở nước ngoài không chỉ để nghe gọi, mà là để đảm bảo mạch máu tài chính (Nhận OTP ngân hàng VN, xác thực mã ví điện tử).
*   **Need 4: Group Synchronization (Sự đồng bộ của nhóm/gia đình):** Nhu cầu chia sẻ tài nguyên (Data, Vouchers) và kiểm tra sự an tòan của đồng bọn/người thân bị lạc (Radar) trong một hệ sinh thái app dễ sử dụng.
*   **Need 5: Disruption Mitigation (Chống chấn thương tâm lý biến cố):** Năm 2024, tình trạng delay chuyến bay, mất hành lý xảy ra cực nhiều. Khách hàng khao khát được "bồi thường tức thì" (như tặng vé vào phòng chờ VIP ngay khi phát hiện máy bay delay) mà không qua thủ tục đòi tiền bảo hiểm lằng nhằng.
*   **Need 6: Itinerary & Document Vault (Gom gọn thủ tục offline):** Sự quá tải thông tin (Information overload) khi đi xa. Họ cần một "Két sắt Offline" ngay trong app My VNPT để gom chung: Vé máy bay điện tử, Email Booking Agoda/Booking.com, QR Code Klook, và ảnh chụp Passport. Tránh việc đang đứng ở hải quan mà mạng yếu không load được Google Drive.

---

## 3. KHOẢNG TRỐNG CƠ HỘI CHO MY VNPT (Opportunities)
- Vấn đề lõi chưa được ai giải quyết triệt để: Sự nhập nhằng và **Nỗi sợ Bill Shock** của Roaming. Nền tảng My VNPT hoàn toàn có thể tái thiết kế lại UX phần Roaming thành "The Safe Roaming System" (Công tắc bật/tắt chống phát sinh gói cước, Dashboard realtime theo dõi % data Roaming) từ đó làm đòn bẩy **Bán chéo Bảo hiểm PTI**, tái định vị My VNPT thành "Companion App" cho du khách Việt. Lấy lòng tin khách hàng bằng sự minh bạch sẽ tạo ra conversion rate mua Bundle cực kỳ cao.
- Đối với Inbound: Không ai muốn đăng ký My VNPT chỉ để mua SIM. UX cần thiết kế dạng **"Guest Checkout"** - mua trên nền Web quét QR trả qua Apple Pay/Visa trong 3 cú click rước khi tải App, và dùng App My VNPT để tracking Data Inbound.
