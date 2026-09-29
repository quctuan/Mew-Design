# 🛡️ UI/UX Audit Report: My VNPT Homepage (Wireframe 799-6977)

**Auditor:** UX Flow Auditor + UI Visual Auditor
**Scope:** Màn hình Homepage (Tab 1) trong tổ hợp Super App.
**Ngữ cảnh đối chiếu:** Dựa trên "Tầm nhìn Hệ sinh thái Phục vụ Hộ gia đình" (AIOps, Proactive Care, Seamless Experience).

---

## 1. Định vị JTBD cốt lõi của Homepage
- **Job cốt lõi của User trên Home:** "Tôi muốn kiểm tra ngay băng thông/tài khoản và giải quyết nhanh các tác vụ cấp bách (đóng tiền, mua thêm data) ngay khi mở app".
- **Nhận định thiết kế hiện tại:** Khung wireframe màn "My VNPT" (Tab 1 bên trái cùng) đang bị kéo dài tới khoảng 8-10 sections (Scroll > 4 lần chiều dài màn hình). Thiết kế đang nhầm lẫn giữa **"Homepage (Trang chủ)"** và **"Sitemap (Mục lục)"**. Việc dàn trải toàn bộ tiện ích viễn thông, Shop, và DigiZone ra Home làm lu mờ hoàn toàn JTBD cốt lõi.

---

## 2. Rào cản Nhận thức & Logic (Cognitive Roadblocks)

### 🔴 Vấn đề 1: Trội Cognitive Load & Scroll Fatigue (Định luật Hick)
- **Chuẩn đoán:** Màn hình đang cố trưng bày tất cả mọi thứ cùng một lúc. Khi người dùng mở app lên, họ đối mặt với một bức tường thông tin. Theo định luật Hick, quá nhiều CTA (Call-to-Action) ngang hàng sẽ làm tê liệt khả năng ra quyết định.
- **Hệ quả:** User Feedback đã chỉ rõ: *"Nhiều nội dung gây rối. Phải scroll quá nhiều để xem hết"*. Những tính năng nằm ở cuộn thứ 3 (below the fold) gần như có Tỷ lệ nhấp (CTR) = 0%.
- **Severity (Mức độ nghiệm trọng):** 🔴 Critical (Hủy hoại luồng chuyển đổi).
- **Đề xuất sửa chữa:** Áp dụng nguyên lý *Progressive Disclosure (Mở thông tin dần dần)*. Gọt bỏ 50% section bên dưới. Homepage chỉ giữ lại: Đầu trang là Dashboard Cá nhân (Data/Tiền), Dưới đó là Quick Actions (4-8 icons), và Dưới cùng là KHÔNG GIAN DYNAMIC (Sẽ đề cập ở Vấn đề 2). Hàng hóa và tiện ích chuyên sâu phải bị đẩy sang **Tab DigiZone** hoặc **Tab Shop**.

### 🔴 Vấn đề 2: Tính tĩnh lặng (Static) của Hệ sinh thái AI
- **Chuẩn đoán:** Trong file triết lý "Định hướng Quy hoạch tổng quan" có ghi mũi nhọn Giai đoạn 2 là "Proactive Care - Hỗ trợ chủ động nhờ AIOps". Tuy nhiên, wireframe hiện tại hoàn toàn là "Nội dung Tĩnh" (Ai mở lên cũng thấy bố cục y hệt nhau), điều này phản tác dụng và gây rác mắt user.
- **Severity (Mức độ nghiệm trọng):** 🔴 Critical (Trái ngược tầm nhìn Super App).
- **Đề xuất: The "Context-Aware" Dynamic Architecture:**
  Đập bỏ các section block cứng nhắc, chuyển sang hệ thống **Card Widget Động (Bento Box)** điều khiển bằng CDP/AI.

---

## 3. Kiến trúc Đề xuất: "Dynamic & Contextual Homepage"
Để giải quyết triệt để 2 feedback của User, Homepage cần tái cấu trúc theo mô hình "Ưu tiên Ngữ cảnh" (Context-first). Layout mới chỉ ngắn gọn bằng đúng 1.5 lần màn hình (chỉ cuộn nửa trang):

### Lớp 1: The Personal Dashboard (Tĩnh - Luôn xuất hiện)
*Vị trí: Bám chặt trên cùng.*
* Giao diện Glassmorphism với avatar khách hàng, Lời chào cá nhân hóa.
* Hiển thị To, Rõ các Job quan trọng nhất: Số dư tài khoản, Dung lượng 4G/5G còn lại (Thiết kế dạng Vòng tròn/Bar chart trực quan).

### Lớp 2: The Action Bar (Tĩnh - Luôn xuất hiện)
*Vị trí: Ngay dưới Dashboard.*
* 4-6 Quick Actions (Nạp tiền, Đóng cước, Đổi sim, Lịch sử). Các icon này có thể cho user tự "Pin" (Ghim) những tính năng họ hay dùng nhất.

### Lớp 3: The "Magic" Dynamic Zone (Tùy biến 100% bằng AI) (Quan trọng nhất)
*Vị trí: Nửa dưới của màn hình Homepage.*
Khu vực này sẽ thay đổi nội dung hoàn toàn dựa trên 4 yếu tố ngữ cảnh:

1.  **Ngữ cảnh Hóa đơn (Billing Context):** 
    - *Bình thường:* Trống rỗng, không hiện gì.
    - *Đến kỳ cước (Ngày 15 hàng tháng):* Nổi lên một Widget to đùng màu vàng cảnh báo: *"Ban có 1 hóa đơn Internet 250k chờ thanh toán"*. Kèm nút bấm 1 chạm thanh toán ngay.
2.  **Ngữ cảnh Vị trí (Location Context - Travel Hub):**
    - Nhận diện khách tới Sân bay hoặc Nước ngoài: Đẩy toàn bộ giao diện cước viễn thông xuống, thay bằng Widget **"Chế độ Du lịch"** (Mua eSIM, Cảnh báo tỷ giá ngoại tệ, Gọi SOS).
3.  **Ngữ cảnh Thời gian & Gia đình (DigiBox/DigiHome Context):**
    - *8h tối Thứ 7:* Hệ thống biết khách đang ở nhà. Kéo Widget giải trí lên: *"Phim bom tấn đang chiếu trên MyTV tối nay"*.
    - Thiết bị Wifi (Mesh) báo có dấu hiệu rớt mạng: Nổi Widget Đỏ báo hiệu: *"Phát hiện sóng Wifi nhà bạn đang yếu. Chạy chẩn đoán lỗi ngay (Auto-Troubleshooting)?"*
4.  **Ngữ cảnh Chăm sóc Tự động (Proactive Care):**
    - Hệ thống phát hiện gói Data 4G sắp hết dung lượng. Thay vì bắt khách vào Tab Shop để tự mò, khu vực này nảy lên Banner: *"Gói của bạn còn <1GB, chạm để đăng ký gia hạn thêm 1.5GB giá hời"*.

### Lớp 4: The Endless "Shadow Community" Feed (Cuộn vô tận)
*Vị trí: Bắt đầu từ cuối nếp gấp trang và cuộn vô tận xuống dưới.*

Khu vực này được thiết kế như một **Bảng tin (Personalized Feed)** giống thuật toán Discovery của Tiktok/Facebook. Không có 2 khách hàng nào nhìn thấy Feed giống hệt nhau:
- **Zero-UI Social Flow:** Khách hàng lướt xem nội dung 1 cách vô thức, tự nhiên thay vì cảm giác bị bắt ép vào một "mạng xã hội nội bộ" khô khan.
- **Dynamic Content Types (Đa dạng hóa nội dung):**
  - *Tips/Lifehacks:* Mẹo tối ưu sóng Wifi, cách tiết kiệm pin, Review phim bản quyền trên MyTV.
  - *User-Generated Content (UGC):* Bài viết chia sẻ từ cộng đồng khách hàng VNPT (ví dụ: "Review kinh nghiệm du lịch Đà Lạt dùng eSIM VNPT").
  - *Native Ads & Micro-Upselling:* Quảng cáo gói cước, mua sắm rạp chiếu phim được bọc dưới vỏ bọc một bài viết hấp dẫn ("Cách mình vượt qua chuyến đi Thái Lan 0 đồng roaming...").
  - *Gamification:* Nêm nếm thêm voucher ẩn, các minigame tặng điểm VinaPhone Plus chèn ngay giữa các bài viết.
- **Mục tiêu UX:** Tạo ra **"Engagement Loop" (Vòng lặp thu hút)**. Kể cả khi user không có nhu cầu trả tiền cước hay mua gói, Feed này chính là mỏ vàng để tăng "Time on App", giữ chân người dùng và tạo thói quen mở ứng dụng mỗi ngày.

---

## 4. Action Items cho Flow & Visual Designer
- [ ] **CHẶT CỤT MÀN HÌNH:** Xóa bỏ toàn bộ các Section liệt kê Gói cước, Danh sách thiết bị, Danh sách phim dài thòng lọng ra khỏi màn Home. Đẩy chúng về Tab Shop và Tab DigiZone.
- [ ] **THIẾT KẾ XƯƠNG WIDGET:** Thiết kế 1 bộ UI Kit chuẩn cho các "Dynamic Widget" (Kích thước dạng Bento 1x1, 1x2, 2x2) để lập trình viên có thể bắn dữ liệu và ráp khối linh hoạt theo từng ngữ cảnh ở Lớp số 3.
- [ ] Gọt bỏ hệ màu rườm rà. Dùng khoảng trắng (White space - Law of Proximity) để tách cụm nội dung thay vì dùng border nét liền dày cộp.
