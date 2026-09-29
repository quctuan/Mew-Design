# 🔍 UX Research Insight: Trải nghiệm "In-Destination" (Khi Khách Hàng Ở Nước Ngoài)

- **Jira Task:** [Nghiên cứu Hành trình In-Destination & Value-Add Services cho My VNPT]
- **Tóm tắt Yêu cầu:** Phân tích nhu cầu, Use Cases (ngoài việc bán SIM/Gói data) của khách du lịch khi đang ở nước ngoài. Benchmark các Super App (Alipay, WeChat, Revolut) để đề xuất các sản phẩm/dịch vụ giá trị gia tăng (VAS) có thể tích hợp vào My VNPT.

---

## 1. Hành Trình "In-Destination" Của Du Khách Outbound

Gạt bỏ yếu tố viễn thông (Data/Roaming), khi du khách hạ cánh xuống một quốc gia khác, hành trình của họ xoay quanh 4 trục nhu cầu chính: **Di chuyển (Mobility) - Chi tiêu (Finance) - Trải nghiệm (Lifestyle) - An toàn (Safety).**

### Các "Pain Points" Lệch Chuẩn (Beyond Connectivity)
1. **Lạc lõng tại sân bay (Airport Anxiety):** Chuyến bay delay mệt mỏi không có chỗ nghỉ; Rảo bước tìm phương tiện di chuyển về nội đô trong sợ hãi bị "chặt chém".
2. **Rào cản thanh toán & Ngôn ngữ:** Không biết tỷ giá, xót ruột vì phí chuyển đổi ngoại tệ (FX fees) của thẻ tín dụng; Cầm hóa đơn VAT ở nước ngoài nhưng lười làm thủ tục hoàn thuế (Tax Refund) tại sân bay vì quá rườm rà.
3. **Mất phương hướng khi khẩn cấp:** Mất hộ chiếu, ốm đau không biết số điện thoại cảnh sát địa phương hay đại sứ quán Việt Nam ở đâu.

---

## 2. Benchmark Các Super App Toàn Cầu

### 2.1. Nhóm Fintech / Banking App (Revolut, Monzo)
- **Feature: Thiết kế trải nghiệm "Chống mệt mỏi tại sân bay"**
  - **SmartDelay:** Revolut từng áp dụng tính năng cực kỳ thông minh: Nếu hệ thống ghi nhận chuyến bay của khách bị delay quá thời gian quy định (vd: 1 tiếng), app **tự động phát hành Voucher vào phòng chờ sân bay (Lounge Access)** miễn phí cho khách. (Đây là một dạng Micro-insurance tác động cực mạnh vào cảm xúc).
  - **Experiences:** Ngay trên app ngân hàng, khách có thể book tour, vé bảo tàng tại điểm đến (giống Klook) và thanh toán với tỷ giá liên ngân hàng cực tốt.

### 2.2. Nhóm Payment Super App (Alipay, WeChat Pay)
- **Feature: "Hoàn thuế (VAT Refund) Trong Lòng Bàn Tay"**
  - **Mini Program We TaxFree / Alipay Tax Refund:** Giải quyết triệt để nỗi đau hoàn thuế. Khách hàng mua sắm tại Châu Âu/Hàn/Nhật, quét QR Code hóa đơn vào App. Khi ra sân bay chỉ cần hải quan đóng dấu là tiền hoàn thuế sẽ "Pinh" thẳng vào ví điện tử Alipay/WeChat Pay bằng đồng nội tệ (RMB) lập tức, thay vì phải chờ đợi hoặc nhận tiền mặt ngoại tệ không dùng đến.
  - **Location-based Offers:** Vừa xuống sân bay Narita (Nhật Bản), Alipay sẽ tự đổi giao diện "Travel Center", push mã giảm giá của các cửa hàng Don Quijote, Takashimaya xung quanh.

### 2.3. Nhóm Mobility Super App (Grab, Uber)
- **Feature: Grab Travel Pass (Voucher Bundle)**
  - Grab không bán data, họ bán "Sự quen thuộc". Khi khách sang Thái/Sin, Grab tự chuyển đổi ngôn ngữ/bản đồ. Họ bán các gói **Travel Pass** (vd: Mua 100k VND được bộ 5 voucher giảm giá cuốc xe GrabCar và GrabFood tại Thái Lan).

---

## 3. Phân Tích JTBD (Jobs-to-be-Done tại In-Destination)

1. **Khi** chuyến bay của tôi bị delay hoặc tôi cần ra sân bay chờ lâu -> **Tôi muốn** có chỗ nghỉ ngơi thoải mái mà không tốn kém -> **Để tôi** giữ được sức khỏe và tinh thần tốt nhất cho chuyến đi.
2. **Khi** tôi mua sắm hàng hiệu ở nước ngoài -> **Tôi muốn** thủ tục hoàn thuế diễn ra tự động trên điện thoại và nhận tiền về tài khoản quen thuộc ở VN -> **Để tôi** thao tác nhanh gọn, lấy lại được tiền rủng rỉnh mà không cần đứng xếp hàng điền giấy ở sân bay.
3. **Khi** tôi gặp sự cố rơi mất hộ chiếu ở nước ngoài -> **Tôi muốn** mở điện thoại ra là có ngay hướng dẫn tiếng Việt hoặc nút gọi đại sứ quán -> **Để tôi** có thể xử lý khủng hoảng ngay lập tức.

---

## 4. Đề Xuất Value-Add Services (VAS) Cho My VNPT Dành Riêng Cho Du Khách Outbound

My VNPT với lợi thế là app Viễn Thông (có kết nối Data) và có ví VNPT Money (Tài chính) hoàn toàn có thể xây dựng một **"Travel Dashboard"** tự động kích hoạt khi nhận diện khách chuyển vùng quốc tế:

### Giải pháp 1: Bundle "An Toàn & Khẩn Cấp" (Safe Travel Companion)
- **SOS Button (Luôn có sẵn mạng):** Tích hợp một module "Emergency" trong My VNPT: 
  - Nơi duy nhất tra cứu *Nút gọi nhanh Đại sứ quán Việt Nam* tại quốc gia đó (Gọi VoIP free qua mạng của VNPT).
  - Tích hợp Mini-App "Dịch thuật khẩn cấp" AI.
- **Micro-Insurance Bundle (SmartDelay Insight):** Phối hợp với đối tác Phòng chờ (như DragonPass/Priority Pass) + Bảo hiểm để tạo gói Cước Roaming VIP: *Nếu chuyến bay bị delay > 2 tiếng, My VNPT tự động tặng khách 1 vé vào Phòng chờ sân bay quốc tế.*

### Giải pháp 2: Fin-Tech Travel Bundle (Tích hợp VNPT Money)
- **My VNPT Tax Refund FastTrack:** Nếu VNPT Money có thể bắt tay hợp tác với Global Blue (Hệ thống hoàn thuế toàn cầu), cho phép khách hàng quét mã hoàn thuế và nhận tiền trực tiếp về ví VNPT Money (bằng VNĐ). Khách khỏi cần ra quầy xếp hàng -> Đây là **Killer Feature**.
- **No-FX Fee Wallet:** Thúc đẩy ví điện tử VNPT Money qua Apple Pay/Google Pay để khách thanh toán không mất phí chuyển đổi ngoại tệ cao.

### Giải pháp 3: "Partner In-Destination Experience" (Klook/Grab Liên kết)
- **Tích điểm My VNPT Point ở nước ngoài:** Khách đang ở Thái Lan, app push notification thông báo: *"Dùng điểm VNPT đổi Voucher GrabCar Thái Lan"*.
- **Marketplace Mini-app:** Dành hẳn một tab trên Travel Dashboard tích hợp Klook / Traveloka API để khách mua vé tàu điện ngầm (Suica, T-money), vé bảo tàng, e-ticket bằng tài khoản My VNPT ngay khi đang dạo chơi.

---
## Kết Luận:
Du khách không chỉ cần "Sóng di động". Sóng di động chỉ là nền tảng (Infrastructure). Cái họ cần là một "Người bạn đồng hành số" giúp họ thấy An Toàn, Tiết Kiệm (Hoàn Thuế/Grab Pass) và Giải Quyết Khủng Hoảng (Delay/Mất đồ). Đó mới là tương lai của một Super App khi đem khách hàng ra khỏi biên giới.
