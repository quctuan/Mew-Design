# 📱 UI/UX Architecture: Thực thi "My Travel Hub" trên My VNPT

Dựa trên yêu cầu biến **Travel Pass** thành một cụm feature mang dáng dấp của "Digital Ticket" và "Wallet", việc thực thi thiết kế (Execution) trên App My VNPT cần chia làm 2 giai đoạn hành vi: **Giai đoạn Mua (Pre-trip)** và **Giai đoạn Sử dụng (In-destination)**. 

Tuyệt đối thoát khỏi UI kiểu danh sách gói cước viễn thông truyền thống. Dưới đây là chiến lược quy hoạch UI/UX chi tiết:

---

## 1. Giai đoạn Bán hàng (Pre-trip): Giao diện "Combo Add-on" & Digital Ticket

Mục tiêu ở đây là **Up-sell** (Bán chéo). Khách hàng ban đầu chỉ định vào mua Data Roaming, nhưng UI phải dụ họ mua nguyên 1 cái "Pass" (Vé).

### 🎨 Cấu trúc UI màn hình mua (Purchase Flow)
*   **Hero Banner (Trực quan hóa):** Thay vì để tên gói "Rx_Thai_5GB", hãy thiết kế một tấm vé máy bay (Boarding Pass) đồ họa kỹ thuật số. Hiển thị "Vietnam ✈️ Thailand", kèm hình ảnh minh họa (icon bát Tomyum, xe Tuk-Tuk).
*   **Lựa chọn Base (Nền tảng):** Khách chọn Điểm đến (Destination) và Số ngày (Duration). App tự động tính ra Base Data (VD: 5GB/5 ngày).
*   **The "Add-on Bento Box" (Khu vực Up-sell):**
    *   Sử dụng UI dạng Thẻ (Cards) vuốt ngang hoặc Toggle Switch (Bật/Tắt).
    *   *Card 1: 🚕 Đón Sân Bay Grab (Thêm 150k)*
    *   *Card 2: ☕ Voucher Phòng Chờ thương gia (Thêm 300k)*
    *   *Card 3: 🛡️ Bảo hiểm trễ chuyến (Thêm 50k)*
*   **Giao diện "Build your Ticket":** Khi khách tick chọn Add-on nào, cái "Digital Ticket" ở trên cùng sẽ tự động kẹp thêm Icon của dịch vụ đó vào, và tổng tiền "Summary" nhảy số real-time với hiệu ứng Animation mượt mà.
*   **Micro-copy:** Dùng từ ngữ kích thích như "Unlock VIP Experience", "Best for Families", thay vì "Đăng ký dịch vụ".

---

## 2. Giai đoạn Sử dụng (In-Destination): Màn hình siêu tiếp cận "My Travel Hub"

Khi khách hàng hạ cánh và máy nhận sóng Roaming (hoặc đối với Inbound là eSIM kích hoạt), App My VNPT phải "Biến hình" (Context-Aware). Giao diện nạp thẻ, đóng tiền điện nước thông thường phải được giấu đi, nhường chỗ cho **"My Travel Hub"**.

### 🎨 Cấu trúc UI của "My Travel Hub"
Màn hình này được thiết kế theo tư duy **Apple Wallet** kết hợp **Super-App Dashboard**, ưu tiên tối đa thao tác 1 chạm (One-tap) hoặc vuốt (Swipe).

*   **Zone 1: The Digital Pass (Tấm vé quyền năng - Nửa trên màn hình)**
    *   Trung tâm là 1 tấm thẻ ảo mang tên "Thai Travel Pass".
    *   Hiển thị Real-time: Data còn lại (Xanh lá/Đỏ), Thời tiết hiện tại ở Bangkok, Tỷ giá VNĐ/THB chênh lệch hôm nay.
    *   Có thể hiện một mã QR to (hoặc Barcode) trên thẻ lấp lánh (Hologram effect) để nhân viên đối tác (như Lounge, Klook) quét xác nhận quyền lợi.

*   **Zone 2: Quick Action Bar (Thanh công cụ khẩn cấp - Giữa màn hình)**
    *   Thiết kế dạng Floating Button tròn, to, dễ bấm khi đang vừa xách vali vừa thao tác:
      1.  \[ 🆘 ] **Cấp Cứu** (Gọi 112 / ĐSQ)
      2.  \[ 💳 ] **Quét QR** (Mở camera thanh toán VNPT Money ngay lập tức)
      3.  \[ 🚗 ] **Gọi Xe** (Deep-link bung Mini-app Grab/Uber)
      4.  \[ 🗺️ ] **Bản Đồ** (Mở bản đồ tàu điện/Google Maps offline)

*   **Zone 3: Voucher Wallet (Ví quà tặng - Nửa dưới màn hình)**
    *   Thay vì giấu voucher vào sâu trong phần "Ưu đãi", hãy hiển thị chúng dưới dạng Xếp Lớp (Stack) như trong Apple Wallet.
    *   Chỉ hiển thị các voucher liên quan đến Quốc gia đang đến.
    *   **Thao tác (Interaction):** Chạm vào để phóng to thẻ -> **Vuốt (Swipe-to-redeem)** từ trái sang phải để đưa cho thu ngân quét. Vuốt xong thẻ lật sếp xó (Animation) báo hiệu đã sử dụng. (Giúp giải quyết sự cập rập, luống cuống khi đứng trước quầy thanh toán nước bạn).

---

## 3. Điều Hướng (Navigation) & Triger

Làm sao để khách hàng vào được "My Travel Hub" siêu nhanh mà không cần tìm kiếm trong Menu?

1.  **Contextual Trigger (Ngữ cảnh tự động):** App tự động phát hiện IP quốc tế hoặc mạng di động chuyển sang Roaming Code -> Hiển thị 1 Pop-up toàn màn hình hoặc đẩy 1 Push Notification: *"Welcome to Thailand! Tap to open your Travel Hub"*.
2.  **Floating Bubble (Bong bóng nổi):** Suốt chuyến đi, My VNPT cung cấp 1 shortcut dạng bong bóng nổi trên màn hình chính (Giống chathead Messenger), bấm vào là bung giao diện Hub.
3.  **Dynamic Bottom Tab:** Thanh Navigation Bar dưới đáy của app My VNPT (Home | Shop | Support | Profile) sẽ geç thay đổi tạm thời, mục "Shop" có thể biến thành "Travel Hub" với icon máy bay phát sáng trong suốt thời gian chuyến đi.

### Kết Luận
Việc quy hoạch thành 1 "Hub" riêng biệt với UX tối giản (Vuốt thả, 1 chạm, icon to) giúp giảm tải nhận thức (Cognitive Load) cho khách hàng trong môi trường đầy áp lực (lạ nước, lạ cái, gấp gáp tiếng lóng). Nó không còn là App viễn thông, nó là một "Người dẫn đường" bỏ túi.
