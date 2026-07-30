# Quy hoạch chi tiết: Phân hệ DigiBox (Giải trí & Kết nối Gia đình)

> **Triết lý cốt lõi:** DigiBox không phải là một ứng dụng OTT. DigiBox là **"Hub Quản trị Hệ sinh thái Giải trí Gia đình"** — kết hợp bảng điều khiển thông minh cho MyTV, cỗ máy bán hàng và công cụ tự chăm sóc, được kích hoạt bởi lợi thế hạ tầng độc quyền của VNPT (Quad-play: Mobile + Broadband + TV + Finance).

---

## Entry Point (Từ DigiZone)

Card preview trên trang DigiZone hiển thị:
- Tiêu đề: **"Giải trí & Kết nối Gia đình"**
- Subtitle: "Tận hưởng từng khoảnh khắc trong thời gian rảnh của bạn"
- Các chương trình nổi bật (thumbnail scroll ngang)
- Chương trình sắp diễn ra
- Gói giải trí đang bán chạy (chip filter: Truyền hình | Phim ảnh | Bóng đá)
- CTA chính: **[Khám phá]** → Mở trang DigiBox detail

---

## Cấu trúc trang DigiBox (Detail Page)

Bố cục theo mô hình **Visual Hierarchy hình chữ F**:
> Trạng thái → Tiền bạc/Upsell → Nội dung xem → Tiện ích tự phục vụ

---

### SECTION 1 — Trạng thái & Gói MyTV *(Vùng Nóng — Selfcare + Upsell)*

**Mục đích:** Người dùng biết ngay tình trạng dịch vụ và số tiền phải đóng ngay khi mở màn.

```
┌──────────────────────────────────────────┐
│  🟢 Đường truyền ổn định   HĐ: MTV-12345 │
├──────────────────────────────────────────┤
│  ⭐ MyTV VIP – Tích hợp K+              │
│  Hết hạn: 30/10/2025  •  Còn 17 ngày    │
│  ████████████░░░  (Progress bar)         │
│                                          │
│  [Gia hạn]    [Đổi gói / Nâng cấp]      │
└──────────────────────────────────────────┘
│  Tiền cước tháng này: 150.000đ           │
│  [Thanh toán qua VNPT Money – Giảm 5%]  │
└──────────────────────────────────────────┘
```

**Logic trạng thái:**
- 🔴 Đèn đỏ → CTB mất tín hiệu → Pop-up auto: *"Đường truyền nhà bạn có vẻ không ổn, chẩn đoán ngay?"*
- 🟡 Cước chưa thanh toán → Nút "Thanh toán One-Bill" nhấp nháy

---

### SECTION 2 — Đề xuất cho bạn *(Vùng Trọng điểm Kinh doanh — AI + Upsell)*

**Mục đích:** Contextual upsell đặt ngay dưới hóa đơn — vị trí CTR cao nhất. Được cá nhân hóa theo hành vi xem trên STB và dữ liệu di động.

**Các kịch bản:**

| Tình huống phát hiện | Nội dung hiển thị |
|---|---|
| User mua PPV phim lẻ nhiều lần | 🎁 Nâng lên gói VIP tiết kiệm hơn + Voucher 30% tháng đầu |
| Gói VinaPhone còn < 10% data | 📶 "Nạp data ngày 10k để không đứt phim" |
| Đầu mùa giải bóng đá | ⚽ Gói K+ độc quyền – Ưu đãi chỉ tuần này |
| User có thói quen xem phim Hàn tối thứ 6 | 🎬 Phim bộ Hàn mới cập nhật cuối tuần này |
| Thành viên gia đình < 12 tuổi | 👶 Gói Thiếu nhi – Học tiếng Anh qua hoạt hình |

---

### SECTION 3 — Mở MyTV *(Entry Point Mini App — Content Gateway)*

**Mục đích:** Gateway vào nền tảng xem nội dung thực sự. Không nhúng OTT vào app, mà **mở MyTV như Mini App** để giữ trải nghiệm native của từng nền tảng.

```
┌──────────────────────────────────────────┐
│  📺 MỞ MYTV                              │
│                                          │
│  ┌──────┐  ┌──────┐  ┌──────┐           │
│  │ 🎬  │  │ 📡  │  │ ⚽  │           │
│  │Phim │  │Live │  │Sport│           │
│  └──────┘  └──────┘  └──────┘           │
│                    [Mở MyTV →]           │
└──────────────────────────────────────────┘
```

**Shortcuts nhanh:**
- **Xem phim** → deeplink vào danh mục phim trên MyTV
- **Trực tiếp** → deeplink vào kênh live đang phát
- **Thể thao** → deeplink vào khu thể thao
- **[Mở MyTV →]** → Launch full Mini App MyTV

**Continue Watching (đồng bộ từ STB):**
- Carousel ngang các nội dung đang xem dở trên TV
- Badge `📺 Xem trên TV` phân biệt với lịch sử điện thoại
- Hiển thị: Progress bar + Tên tập + Thời gian còn lại
- Tap → Xem tiếp trên điện thoại hoặc điều hướng TV từ xa

---

### SECTION 4 — Lịch phát sóng & Sự kiện sắp chiếu

**Mục đích:** Thay thế thói quen xem lịch TV truyền thống. Là công cụ giữ chân user quay lại app thường xuyên.

- Timeline ngang theo giờ trong ngày (real-time)
- Highlight khung giờ đang phát (pulse animation)
- Nút 🔔 **Nhắc tôi** → Push notification tới giờ phát
- Tùy chọn: STB tự động chuyển kênh đúng giờ
- Filter: `Tất cả` · `Đang theo dõi` · `Bóng đá` · `Phim` · `Thiếu nhi`

**Sự kiện PPV sắp tới:**
```
🔥 Sự kiện đặc biệt – 3 ngày nữa
Real Madrid vs Man City  |  Thứ 7 • 02:00
Chỉ 20.000đ  |  [Đặt mua ngay]  [Dùng điểm VNP+]
```

---

### SECTION 5 — Gợi ý cho Gia đình *(Behavior-based Distribution)*

**Mục đích:** Phân phối nội dung dựa trên hành vi xem thực tế từ thiết bị đầu cuối MyTV — đây là dữ liệu mà TV360/VieON/Netflix không có.

```
👨 Dành cho Bố     →  Serie bóng đá Champions League tập mới
👩 Dành cho Mẹ     →  Phim Hàn "Hương vị tình nhân" – Tập mới hôm nay
👨‍👩‍👧‍👦 Cả nhà xem   →  Chương trình cuối tuần hot – Anh trai vượt ngàn chông gai
👧 Cho bé          →  Doraemon lồng tiếng + Khóa học tiếng Anh
```

- Label contextual: *"Vì bạn hay xem vào tối thứ 6"* / *"Phổ biến với gia đình ở TP.HCM"*
- Dữ liệu nguồn: Lịch sử xem trên STB + Profile thành viên

---

### SECTION 6 — Công cụ Tự phục vụ *(Quick Action Grid — Selfcare)*

**Mục đích:** Đưa các pain point thường gặp ra ngoài thành lưới icon chạm nhanh. Giảm cuộc gọi hotline.

```
Grid 2×3:

[📺 Quản lý thiết bị]     [📱 Quét QR đăng nhập TV]
[🔒 Khóa trẻ em / PIN]    [⏰ Nhắc lịch trực tiếp]
[📶 Chẩn đoán đường truyền][👨‍🔧 Đặt lịch kỹ thuật viên]
```

**Chi tiết từng tool:**

| Icon | Tên | Chức năng |
|---|---|---|
| 📺 | Quản lý thiết bị | Danh sách STB/SmartTV/điện thoại; đăng xuất từ xa; reboot STB |
| 📱 | Quét QR đăng nhập | Xuất QR từ app, quét lên SmartTV thay vì gõ remote |
| 🔒 | Khóa trẻ em | PIN mua hàng; khóa STB theo giờ; kiểm soát thời lượng xem |
| ⏰ | Nhắc lịch | Cài alert sự kiện trực tiếp; STB tự chuyển kênh đúng giờ |
| 📶 | Chẩn đoán mạng | Auto-ping ONT → STB; báo lỗi phần cứng tự động; deeplink sang DigiZone Network |
| 👨‍🔧 | Đặt lịch KTV | Chọn khung giờ rảnh; live-tracking vị trí kỹ thuật viên |

---

### SECTION 7 — Quản lý Gói Add-on & Lịch sử giao dịch

**Mục đích:** Minh bạch hóa toàn bộ chi tiêu giải trí, gỡ bỏ cảm giác "bị trừ tiền oan".

- **Gói đang bật:** K+ Sport · HBO Go · Galaxy Play (Toggle ON/OFF)
- **Gói có thể thêm:** VTVcab · ON Sports · Disney+ Hotstar *(cross-sell)*
- **Lịch sử PPV:** Danh sách phim/sự kiện đã mua lẻ
- **Auto-pay:** Bật/tắt gia hạn tự động từng gói
- **Nhắc gia hạn:** Cài push notification trước X ngày hết hạn

---

### SECTION 8 — Hồ sơ Gia đình *(Profile & Parental Control)*

**Mục đích:** Trao quyền kiểm soát toàn diện cho chủ hợp đồng.

- **Danh sách thành viên:** Avatar + tên + độ tuổi
- **Cấu hình từng profile:** Nội dung phù hợp theo độ tuổi
- **Chế độ Trẻ em:** One-tap switch — ẩn nội dung 18+, giới hạn giờ xem
- **Thống kê:** "Bé đã xem 2 tiếng hôm nay" / "Bố hay xem khuya"

---

### FLOATING BUTTON — Hỗ trợ nhanh *(Selfcare Bọc hậu)*

- Nút nổi góc phải: 💬 **Chat VNPT** (VNPT Chatbot / chuyển agent)
- Khi mọi công cụ tự phục vụ thất bại → chat trực tiếp, không cần thoát app gọi hotline

---

## Tóm tắt kiến trúc Visual

```
┌─────────────────────────────────────────────┐
│  DIGIBOX – Giải trí & Kết nối Gia đình      │
├─────────────────────────────────────────────┤
│  S1: Trạng thái gói + Thanh toán            │ ← SELFCARE
│  S2: Đề xuất cá nhân hóa (AI Upsell)        │ ← SALES ENGINE
│  S3: Mở MyTV + Continue Watching            │ ← CONTENT GATEWAY
│  S4: Lịch phát sóng + PPV sự kiện           │ ← ENGAGEMENT
│  S5: Gợi ý cho gia đình (Behavior AI)       │ ← PERSONALIZATION
│  S6: Quick Action Grid (Tự phục vụ)         │ ← SELFCARE TOOLS
│  S7: Gói Add-on & Lịch sử giao dịch         │ ← COMMERCE
│  S8: Hồ sơ gia đình & Parental Control      │ ← PROFILE MGMT
│  [💬 Chat VNPT]                             │ ← SUPPORT FALLBACK
└─────────────────────────────────────────────┘
```

---

## Lộ trình Triển khai (Roadmap)

| Phase | Tên | Nội dung |
|---|---|---|
| **Phase 1 – MVP** | Hiện diện | Sync hợp đồng; Trạng thái gói; Hóa đơn; Hotline/Ticket |
| **Phase 2 – Giao dịch** | Tự phục vụ | Mua Add-on; Auto-pay; Quản lý thiết bị; QR đăng nhập; Parental Control |
| **Phase 3 – Thông minh** | Khai thác tăng trưởng | Chẩn đoán mạng; Recommendation Engine; Upsell tự động |
| **Phase 4 – Hội tụ** | Ecosystem Convergence | One-Bill; Điểm VNP+; Ưu tiên băng thông; Mini App MyTV |

---

## Lợi thế độc quyền so với OTT thuần (Netflix, VieON, TV360)

| Tính năng | Netflix | VieON | TV360 | **DigiBox** |
|---|---|---|---|---|
| Quản lý STB từ xa | ❌ | ❌ | ❌ | ✅ |
| Reboot Set-top Box | ❌ | ❌ | ❌ | ✅ |
| Chẩn đoán đường truyền | ❌ | ❌ | ❌ | ✅ |
| Gói tích hợp Internet + TV + Mobile | ❌ | ❌ | ❌ | ✅ |
| Dùng điểm SIM mua phim | ❌ | ❌ | ❌ | ✅ |
| Đồng bộ lịch sử từ STB thật | ❌ | ❌ | ❌ | ✅ |
| Personalization từ hành vi TV thực | ❌ | Một phần | Một phần | ✅ |
