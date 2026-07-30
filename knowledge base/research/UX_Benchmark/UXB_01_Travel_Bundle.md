# UX Benchmark: Travel Bundle & Cross-selling (Inbound & Outbound)

## 1. Bối cảnh & Mục tiêu (Context & Objectives)
- **Tính năng / Yêu cầu:** Ý tưởng thiết kế bundle giải pháp Du lịch quốc tế trên app My VNPT cho 2 tập khách hàng: Inbound (khách du lịch đến Việt Nam) và Outbound (khách Việt Nam đi nước ngoài).
- **Mục tiêu Benchmark:** Tìm kiếm các case study thành công trên thế giới về việc cross-sell, upsell các gói cước viễn thông (Roaming, eSIM) kèm các giá trị gia tăng (add-ons) khác trong ngành du lịch/viễn thông.

## 2. Khoảnh khắc Cốt lõi (The Moments) & Pain Points

### A. Segment Inbound (Khách quốc tế đến VN)
- **Hoàn cảnh (When/Where):** Vừa đáp xuống sân bay Nội Bài/Tân Sơn Nhất, cầm điện thoại lên cần tìm xe về khách sạn nhưng không có mạng.
- **Nỗi đau (Pain Point):** Bất đồng ngôn ngữ khi mua SIM vật lý tại quầy; lo sợ bị "chặt chém" giá cước taxi sân bay; cần Internet ngay lập tức để báo bình an cho gia đình.
- **Khao khát:** Một gói "Starter Pack" cài sẵn trước khi bay, đáp máy bay là có mạng và có xe chờ sẵn.

### B. Segment Outbound (Khách VN đi quốc tế)
- **Hoàn cảnh (When/Where):** Đang lên lịch trình đi Thái Lan/Nhật Bản; hoặc chuẩn bị cất cánh/vừa hạ cánh xuống sân bay nước bạn.
- **Nỗi đau (Pain Point):** Nỗi ám ảnh "Bill Shock" (hóa đơn roaming khổng lồ); rủi ro mất đồ, trễ chuyến bay không biết bấu víu vào đâu nếu không có bảo hiểm.
- **Khao khát:** Kiểm soát được chi phí Internet (cước phí cố định) + Yên tâm vui chơi (bảo vệ bởi bảo hiểm).

## 3. Phân tích JTBD (Jobs-to-be-Done)

1. **Inbound:** **Khi** tôi chuẩn bị đến Việt Nam -> **Tôi muốn** mua sẵn eSIM và di chuyển từ sân bay -> **Để tôi** có thể rời sân bay nhanh nhất và kết nối mạng mượt mà không cần xếp hàng mua SIM.
2. **Outbound:** **Khi** tôi ra nước ngoài -> **Tôi muốn** mua một gói cước data cố định kèm bảo hiểm du lịch -> **Để tôi** không lo lắng về cước phát sinh và an tâm nếu có rủi ro về sức khỏe/hành lý.

## 4. Case Study Thực Tế (Global Benchmark)

### Case 1: Klook (Travel Super App) - Chiến lược "The First Mile Bundle"
- **Cách họ làm:** Klook đóng gói các "Travel Essentials" (Khách sạn + Xe đưa đón sân bay + eSIM). 
- **Trigger:** Sau khi user book phòng khách sạn hoặc vé máy bay, Klook đẩy ngay popup gợi ý "Travel Essentials".
- **Insight:** Bán ngay những thứ định hình "sự an tâm" ở dặm đầu tiên của chuyến đi. 

### Case 2: Airalo (Global eSIM) - B2B & "Connectivity as a Security Feature"
- **Cách họ làm:** Airalo không trực tiếp bán bảo hiểm, mà tích hợp API vào các app của công ty Bảo hiểm/Fintech.
- **Insight:** Họ định vị "Internet là thiết yếu để đảm bảo an toàn" (gọi bảo hiểm, khai báo y tế). Khi mua bảo hiểm du lịch, khách hàng được tặng kèm/cross-sell ngay tệp eSIM Airalo.

### Case 3: Grab - Grab Travel Pass
- **Cách họ làm:** Cấp cho khách inbound một gói "Subscription" mua một lần dùng 4 tuần, chứa các voucher discount xe công nghệ (Ride) và Food delivery tại quốc gia bản địa. Gần đây Grab bắt tay với Firsty để tích hợp bán thẳng eSIM trong app.
- **Insight:** Giữ user ở lại hệ sinh thái của mình trọn vẹn từ lúc hạ cánh đến lúc ăn uống, không cần rời app.

### Case 4: Global Telecoms - Predictive Analytics & Real-time Context
- **Cách họ làm:** Dùng DPI (Deep Packet Inspection) để biết khi nào user hạ cánh và kết nối vào mạng nước ngoài.
- **Trigger:** Bắn tin nhắn SMS pre-travel hoặc ngay lúc hạ cánh với thông điệp One-click-to-buy (gói Roaming fix giá). Đặc biệt là kỹ thuật "Nudge" khi data chạm 80% định mức.

## 5. Đề xuất Ý tưởng "Bundle Add-ons" cho My VNPT

Dựa trên benchmark, My VNPT (vốn nằm trong hệ sinh thái số) hoàn toàn có thể bundle các sản phẩm sau:

### Tệp Outbound (Người VN ra nước ngoài)
- **Core Product:** Gói Data Roaming (Fix price, ví dụ Data không giới hạn 5 ngày). Hoặc International eSIM.
- **Cross-sell Add-on:**
  - **Bảo hiểm du lịch (PTI v.v.):** Khớp với định vị "An toàn & Kết nối".
  - **Dịch vụ phòng chờ sân bay (Lounge Access).**
  - **Voucher đổi ngoại tệ hoặc thanh toán quốc tế (VNPT Money).**
- **UX Flow:** Ngay khi khách tra cứu gói cước Roaming -> Hiển thị Bundle: *Gói Data 5 Ngày + Bảo Hiểm Trễ Chuyến = Trọn gói 500k*.

### Tệp Inbound (Khách quốc tế đến VN)
- **Core Product:** Tourist eSIM (Bán online 100%, quét QR là dùng).
- **Cross-sell Add-on:**
  - **Gói Vận chuyển (Mobility):** Voucher Xanh SM / Be đón từ sân bay Nội Bài/Tân Sơn Nhất.
  - **Gói Nội dung/Giải trí:** VNPT Wifi hotspot pass toàn quốc.
  - **Gói Food / Trải nghiệm:** Voucher ẩm thực local.
- **UX Flow:** Tại trang mua Tourist eSIM (Bản tiếng Anh/Hàn/Trung) -> Gợi ý Bundle *eSIM 30 days + Airport Transfer Voucher 20% off*.

## 6. Key Takeaways cho Thiết kế (Do & Don't)
- **DO:** Hiển thị Bundle ngay ở bước đặt mua (Add to Cart / Checkout) - đây là lúc user dễ chi tiền nhất.
- **DO:** Định giá Bundle sao cho người dùng thấy rõ khoản tiết kiệm (ví dụ: Save 15% when bought together).
- **DON'T:** Không bán những Add-on không liên quan đến bối cảnh "hạ cánh/chuẩn bị bay" (đừng cố cross-sell gói truyền hình MyTV cho khách sắp bay ra nước ngoài).
- **DON'T:** Không đưa quá nhiều Bundle gây nhiễu, quy tắc số 3 (chỉ cho phép user chọn 1 trong 3 mức giá/bundle).
