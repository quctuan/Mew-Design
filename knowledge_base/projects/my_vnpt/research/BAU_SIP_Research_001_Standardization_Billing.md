# BAU_SIP_Research_001_Standardization_Billing

## 1. Tóm tắt Đề bài (Master Input)
- **Mục tiêu**: Chuẩn hóa quy trình thu cước Đa kênh (MyVNPT, VNPT Money, Landing Page QR).
- **KPI**: Tăng tỷ lệ thanh toán online từ 21%.
- **Nỗi đau chính**: 
    - Thông tin cước không đồng bộ giữa OneBss & CCBS.
    - Spam thông báo (Zalo OA tỉnh, SMS).
    - Landing page thiếu tin cậy, thiếu chăm sóc sau thanh toán.
    - Trải nghiệm thanh toán qua các điểm chạm đều khác nhau
    - Chưa dồng nhất về branding VNPT
    Nhân viên thường chủ động thu cước qua QR cá nhân mà không qua kênh chính thống
## 2. Phân tích Thấu cảm (Empathy Analysis)

### 2.1 Bối cảnh & Hành vi (Ethnographic)
- **Hành vi**: Khách hàng thường mở link từ SMS/Zalo để thanh toán nhanh. Tuy nhiên, thông tin chưa đầy đủ để khách hàng có thể yên tâm thực hiện thanh toán
- **Trạng thái cảm xúc**: Lo lắng khi đã đóng tiền nhưng vẫn nhận thông báo nợ. Hoài nghi khi landing trang thanh toán trông quá đơn giản, không hiển thị chi tiết sử dụng.

### 2.2 Nỗi đau (Pain Points)
- "Tôi đã trả tiền rồi, sao vẫn cứ nhắn tin đòi nợ?"
- "Cùng là VNPT mà lúc xem ở app MyVNPT một giá, lúc xem ở landing QR lại thấy một thông tin khác."
- "Giao diện thanh toán qua QR trông như trang lừa đảo, không có logo hay thông tin chi tiết gói cước của tôi."

### 2.3 Công việc cần thực hiện (JTBD)
- **JTBD 1**: "Khi đến kỳ hóa đơn, tôi muốn thấy tổng tất cả các nợ cước (di động, internet, TV) tại một nơi duy nhất để tôi có thể thanh toán tất cả trong 1 lần."
- **JTBD 2**: "Khi tôi đã thanh toán, tôi muốn hệ thống xác nhận ngay lập tức và cam kết dừng mọi thông báo nhắc nợ, để tôi an tâm là nợ đã được xóa."
- **JTBD 3**: "Khi sử dụng landing page không đăng nhập, tôi vẫn muốn thấy lịch sử và chi tiết cước của mình một cách chuyên nghiệp để đảm bảo tôi đang trả đúng số tiền tôi đã dùng."

## 3. Kết quả UX Benchmark (Tham chiếu Quốc tế)
- **Globe (Philippines)**: Áp dụng "Safeguard Mode" - chặn phát sinh cước ngay khi hết gói.
- **Telkomsel (Indonesia)**: Dashboard thông minh hiển thị chi tiết "Remaining Quota" ngay bên cạnh nút "Pay Now".
- **UX Pattern cho Async Data**: Sử dụng trạng thái "Đã nhận thanh toán - Đang cập nhật hệ thống gạch nợ" để trấn an người dùng thay vì chỉ hiển thị "Chưa thanh toán".

## 4. Đề xuất Hướng đi (Insight)
- **Insight 1**: Cơ chế "Thanh toán nối tiếp" (Serial Payment): Do hệ thống chưa cho phép gộp cước, UX sẽ đóng vai trò "Điều phối viên" để khách hàng thực hiện trả nợ trả sau trước, sau đó tự động dẫn hướng (Auto-redirect) sang trang gia hạn gói trả trước.
- **Insight 2**: Cơ chế "Xác nhận gạch nợ tức thì cấp độ UI" (UI-level instant clearing) để giải quyết xung đột dữ liệu OneBss/CCBS.
- **Insight 3**: Tích hợp Gamification (Vòng quay, Điểm thưởng VinaPhone Plus) ngay tại màn hình "Cảm ơn" để tăng Engagement.
- **Insight 4**: Chuẩn hóa Branding "VNPT One-Look": Đảm bảo mọi điểm chạm (App, Landing, SMS) đều có chung ngôn ngữ thiết kế và nhận diện thương hiệu để tạo sự chuyên nghiệp và tin cậy tuyệt đối.
- **Insight 5**: Chính thống hóa kênh thanh toán: Chuyển dịch thói quen dùng QR cá nhân của nhân viên sang QR động (Dynamic QR) được sinh ra từ hệ thống VNPT, có gắn mã định danh nhân viên hỗ trợ để vẫn đảm bảo KPI thu cước cho nhân viên nhưng tiền chảy về kênh chính thống.

---

## 5. Danh mục Tiện ích & Tính năng cho Landing Page (Willingness-to-Pay)

Để khách hàng sẵn lòng thanh toán trên Landing Page thay vì các kênh truyền thống/cá nhân, trang cần đáp ứng 3 trụ cột: **Tin cậy - Minh bạch - Tiện lợi.**

### 5.1 Các yếu tố tạo Lòng tin (Trust Building)
- **Chứng thực Chính chủ**: Logo VNPT chuẩn, dấu tick xanh "Verified by VNPT", Chứng chỉ bảo mật (PCI DSS, SSL) hiển thị rõ ràng.
- **Xác thực OTP/Mã định danh**: Quy trình truy cập qua Số điện thoại + OTP giúp khách hàng cảm thấy dữ liệu cá nhân được bảo vệ dù không cần đăng nhập App.
- **Thông tin liên hệ chính thức**: Chân trang gồm Hotline 18001166, địa chỉ trụ sở và liên kết tới các trang MXH chính thức của VNPT.

### 5.2 Các yếu tố Minh bạch & Phân tầng Thông tin (3-tier Info Access)
Để tối ưu tỷ lệ chuyển đổi (Conversion Rate) và thúc đẩy cài App, thông tin được phân làm 3 tầng:
- **Tầng 1 - Công khai (Public - Không cần OTP)**:
    - Tổng tiền, Hạn thanh toán, Trạng thái nợ.
    - *Mục tiêu*: Thanh toán NHANH.
- **Tầng 2 - Riêng tư (Private - Cần xác thực OTP)**:
    - Chi tiết cước (Bill Breakdown) kỳ hiện tại.
    - Lịch sử dùng (Cuộc gọi, Data) ngắn hạn.
    - *Mục tiêu*: Phục vụ nhu cầu soát xét tại chỗ.
- **Tầng 3 - Nâng cao (Advanced - Yêu cầu chuyển sang App MyVNPT)**:
    - Lịch sử chi tiết thời gian dài (>3 tháng).
    - Biểu đồ xu hướng tiêu dùng, phân tích AI.
    - *Mục tiêu*: Chuyển đổi (Migration) người dùng lên App chính thức.

### 2.3 Các yếu tố Tiện lợi & Động lực (Convenience & Motivation)
- **Thanh toán 1-chạm**: Hỗ trợ đa dạng phương thức (VNPT Money, QR Bank, Thẻ nội địa/quốc tế) với luồng thanh toán tối giản.
- **Ưu đãi tức thì**: Hiển thị rõ số điểm VinaPhone Plus sẽ nhận được hoặc áp dụng mã giảm giá ngay khi thanh toán.
- **Tính năng Autopay**: Gợi ý đăng ký thanh toán tự động cho kỳ sau với ưu đãi "Chiết khấu X%" để giữ chân khách hàng lâu dài.
- **Hỗ trợ 24/7**: Nút Chat hoặc gọi lại nhanh (Request Call) ngay tại chân trang nếu khách hàng gặp lỗi thanh toán.

---

## 6. Phân tầng Ưu tiên Kênh Thanh toán

Việc phân tầng nhằm mục đích chuyển dịch lưu lượng từ các kênh "Thu hộ" (chi phí cao, mất dữ liệu) sang kênh "Chính chủ" (chi phí thấp, giàu dữ liệu, tăng lòng trung thành).

| Tầng | Nhóm kênh | Ưu tiên | Lý do chiến lược |
| :--- | :--- | :--- | :--- |
| **P1** | **Hệ sinh thái VNPT (App)** | **Chiến lược** | Là "pháo đài" giữ chân khách hàng. App cho phép chăm sóc liên tục (push notification), cá nhân hóa ưu đãi (AI), và có chi phí giao dịch thấp nhất. |
| **P2** | **Landing Page QR** | **Tăng trưởng** | Là "cửa ngõ" thu hút khách hàng chưa tải app. Cung cấp trải nghiệm 1-chạm cực nhanh, tạo niềm tin bước đầu để từ đó "up-sell" khách hàng cài đặt App. |
| **P3** | **App Thu hộ (Bank/Ví ngoài)** | **Duy trì** | Chỉ đóng vai trò là "tiện ích phủ sóng". Cần duy trì để đảm bảo khách hàng có chỗ thanh toán, nhưng không khuyến khích vì mất phí hoa hồng và không kiểm soát được trải nghiệm sau thanh toán. |

---

## 7. Bộ khung Trải nghiệm Thống nhất (VNPT Unified Billing Framework)

Để kéo khách hàng về kênh P1 & P2, chúng ta cần một bộ khung trải nghiệm đồng nhất, khiến khách hàng cảm thấy "Thanh toán qua VNPT là sướng nhất/tin cậy nhất".

### 7.1 Cấu trúc Luồng & Hành trình (Customer Journey Map)

#### 7.1.1 Giai đoạn Trước thanh toán (Pre-payment)
- **Thông báo Nhắc cước**: Hợp nhất thông báo (SMS/Zalo/Push) từ một đầu số duy nhất. Nội dung tin nhắn gồm: [Lời chào] + [Số nợ] + [Dẫn link Landing Page P2].
- **Tra cứu sơ cấp (P0)**: Khách hàng click link → Vào Landing Page thấy ngay số tiền cần trả mà không cần đăng nhập/OTP. Điều này đáp ứng tâm lý muốn "xử lý nhanh cho xong".
- **Hành vi kiểm tra**: Nếu khách hoài nghi về số tiền → Cung cấp nút "Tại sao tôi phải trả số tiền này?" dẫn đến yêu cầu OTP để xem chi tiết (Tầng 2).

#### 7.1.2 Giai đoạn Trong thanh toán (Payment Execution)
- Luồng thanh toán 1-chạm: Giảm thiểu các bước nhập liệu, ưu tiên tự động điền (Auto-fill) thông tin thanh toán.

#### 7.1.3 Giai đoạn Sau thanh toán (Post-payment)
- **Xác nhận tức thì**: Hiển thị trạng thái "Thanh toán thành công" kèm cam kết "Dừng nhắc nợ ngay lập tức".
- **Tri ân & Phần thưởng**: Hiển thị số điểm VinaPhone Plus vừa tích lũy. Tặng kèm "Voucher chúc mừng" (ví dụ: Giảm giá data).
- **Tiện ích hóa đơn**: Cung cấp nút "Tải hóa đơn điện tử" hoặc "Gửi hóa đơn qua Email".
- **Chuyển đổi (Conversion)**: Gợi ý cài App MyVNPT hoặc đăng ký Autopay để "Kỳ sau không cần làm gì cả".

#### 7.1.4 Phân biệt Trả trước và Trả sau trong mã thanh toán chung
Dù được gom vào cùng một lần trả tiền, ứng xử của hệ thống cần phân tách để khách hàng nắm rõ:

| Tiêu chí | Hóa đơn Trả sau (Post-paid) | Hóa đơn Trả trước/Gói cước (Pre-paid) |
| :--- | :--- | :--- |
| **Bản chất hiển thị** | Là khoản nợ đã phát sinh từ việc sử dụng. | Là khoản phí gia hạn để tiếp tục sử dụng. |
| **Minh bạch cấp 2** | Phân rã theo cước thuê bao, cước sử dụng vượt gói. | Hiển thị tên gói cước (ví dụ: VD149) và thời hạn sử dụng mới sau khi đóng. |
| **Xác nhận (Post-pay)** | "Đã thanh toán nợ kỳ tháng X" + Mã giao dịch. | "Đã gia hạn thành công gói Y - Hạn dùng đến ngày Z". |
| **Care đặc thù** | Nhắc nhở đăng ký Autopay để tránh bị chặn 1 chiều. | Gợi ý nâng cấp gói cước cao hơn (Up-sell) dựa trên hành vi dùng cũ. |

#### 7.1.5 Xử lý kịch bản Chuyển đổi (Trả trước -> Trả sau do quá hạn)
Do hạn chế hệ thống không cho phép gộp 2 loại cước vào 1 giao dịch, quy trình sẽ được xử lý theo luồng **Thanh toán nối tiếp (Serial Payment)**:

1. **Lớp Cảnh báo (Trước khi chuyển)**: Nhắc nợ sớm 3 ngày.
2. **Lớp Nhận diện (Khi đã nợ)**: Hiển thị "Giỏ nợ tạm thời" bao gồm 2 mục riêng biệt:
    - Mục A: Cước trả sau phát sinh (Bắt buộc trả trước).
    - Mục B: Gói cước trả trước cần gia hạn.
3. **Lớp Giải pháp - Luồng "Một hành trình - Hai giao dịch"**:
    - **Bước 1**: Khách hàng chọn "Thanh toán xóa nợ" (Mục A).
    - **Bước 2 (Giao dịch 1)**: Thực hiện thanh toán cước trả sau.
    - **Bước 3 (Chuyển tiếp UX)**: Ngay sau khi Giao dịch 1 thành công, hiển thị màn hình: "Tuyệt vời! Bạn đã xóa nợ thành công. Hãy gia hạn ngay gói [Tên gói] để tiết kiệm chi phí sử dụng!" + Nút "Gia hạn ngay".
    - **Bước 4 (Giao dịch 2)**: Thực hiện gia hạn gói trả trước.
    - *Lưu ý*: Sử dụng tính năng "Ghi nhớ phương thức thanh toán" để Giao dịch 2 diễn ra trong 1-chạm, giảm bớt sự phiền hà cho khách hàng.

---

### 7.2 Các quy tắc thiết kế "Níu chân" khách hàng
- **Branding nhất quán**: Landing Page và App phải dùng chung bộ ICON, Màu sắc (VNPT Blue), và Tone of Voice (Thân thiện, tin cậy).
- **Lợi ích độc quyền**: Chỉ khi thanh toán qua kênh VNPT mới được tặng điểm VinaPhone Plus hoặc tham gia Gamification (Vòng quay may mắn).
- **Hỗ trợ gạch nợ tức thì**: Cam kết gạch nợ trong 30s hoặc cam kết "Không nhắc nợ sai" sau khi thanh toán qua kênh chính chủ.


---

## 8. Danh mục Xử lý Lỗi (Error Handling Strategy)

Để duy trì trải nghiệm liền mạch và sự tin cậy, quy trình cần có các phương án xử lý lỗi chủ động (Proactive Error Handling):

### 8.1 Lỗi Hệ thống & Dữ liệu (Backend Errors)
- **Lỗi Async OneBss/CCBS**: Nếu khách đã thanh toán nhưng CCBS chưa cập nhật kịp.
    - *Xử lý*: Hiển thị trạng thái "Đã nhận yêu cầu - Đang gạch nợ tự động" kèm thời gian cam kết hoàn tất. Nếu quá thời gian, khách nhận được SMS xác nhận nợ đã xóa.
- **Lỗi Hệ thống Tra cứu Downtime**: Không thể lấy thông tin hóa đơn.
    - *Xử lý*: Hiển thị thông báo "Hệ thống đang bảo trì để nâng cấp trải nghiệm. Bạn có thể để lại SĐT, chúng tôi sẽ nhắc cước ngay khi hệ thống hoạt động trở lại."

### 8.2 Lỗi Thanh toán (Payment Errors)
- **Giao dịch bị từ chối/Lỗi ngân hàng**:
    - *Xử lý*: Không chỉ báo lỗi chung chung. Cần gợi ý phương thức thay thế ngay tại chỗ (Ví dụ: "Thẻ của bạn không đủ số dư, hãy thử thanh toán qua QR Ngân hàng hoặc Ví VNPT Money để nhận thêm ưu đãi").
- **Lỗi "Thanh toán nối tiếp" (Giao dịch 2 bị lỗi sau khi Giao dịch 1 thành công)**:
    - *Xử lý*: Đây là lỗi nhạy cảm nhất. Hệ thống cần lưu trạng thái: "Bạn đã xóa nợ thành công, chỉ còn bước gia hạn gói để tối ưu chi phí. [Nút gia hạn lại]". Gửi đồng thời link thanh toán gói cước qua SMS/Push để khách có thể thực hiện lại sau.

### 8.3 Lỗi Người dùng & Bảo mật (User/Security Errors)
- **Nhập sai SĐT/OTP**:
    - *Xử lý*: Gợi ý kiểm tra lại số hoặc liên hệ hotline. Nếu sai OTP quá 3 lần, tạm khóa 5 phút để bảo mật và cung cấp nút liên hệ chăm sóc khách hàng.
- **Truy cập link đã hết hạn**: (SMS nhắc cước cũ).
    - *Xử lý*: Tự động cập nhật cước mới nhất và hiển thị: "Hóa đơn cũ đã được thanh toán hoặc hết hạn, dưới đây là thông tin cước mới nhất của bạn."

---

## 9. Thiết kế Chiến lược (Goosebumps Validation)

### 6.1 Vế Logic (Giải quyết Nỗi đau Chức năng)
- **Cơ chế "Gạch nợ Ảo" (Virtual Instant Clearing)**: Ngay sau khi khách hàng thanh toán thành công, UI sẽ chuyển trạng thái hóa đơn thành "Đã thanh toán (Đang cập nhật hệ thống)". Điều này giúp ngăn chặn việc hệ thống gửi thông báo nhắc nợ sai trong thời gian OneBss và CCBS đang đồng bộ.
- **Cổng thanh toán QR Động (Dynamic QR Gateway)**: Thay thế QR cá nhân của nhân viên bằng QR được sinh ra từ hệ thống VNPT Money/MyVNPT. QR này chứa: Mã hóa đơn + Mã định danh nhân viên hỗ trợ. Tiền sẽ chảy trực tiếp vào tài khoản tập đoàn, nhưng nhân viên vẫn được ghi nhận công sức thu cước.
- **Trung tâm điều hành thông báo (Notification Hub)**: Gom tất cả các tin nhắn Zalo OA tỉnh và SMS vào một đầu số/kênh duy nhất "VNPT Billing". Áp dụng thuật toán tần suất để đảm bảo không gửi quá 3 thông báo/kỳ cước.

### 6.2 Vế Cảm xúc (Giải quyết Nỗi đau Tâm lý)
- **Huy hiệu "VNPT Verified" & Chứng chỉ Bảo mật**: Trên landing page thanh toán, bổ sung các biểu tượng bảo mật và dấu tick xanh chính chủ VNPT ở vị trí trang trọng để đập tan sự hoài nghi "Landing lừa đảo".
- **Chiến lược "Niềm vui sau thanh toán" (Post-payment Joy)**: Màn hình Thank-you không chỉ là thông báo thành công khô khan. Thay vào đó là:
    - Hiệu ứng pháo hoa nhẹ nhàng.
    - Thông báo số điểm VinaPhone Plus vừa nhận được.
    - Một "Hộp quà bí mật" chứa voucher khuyến mãi hoặc recommendation gói cước phù hợp (Upsell).
- **Sự thấu cảm qua Minh bạch**: Hiển thị bảng chi tiết cước (Bill Breakdown) rõ ràng, giải thích các khoản phí "tận răng" bằng ngôn ngữ bình dân thay vì mã kỹ thuật, giúp khách hàng cảm thấy mình được tôn trọng và không bị "móc túi ngầm".
