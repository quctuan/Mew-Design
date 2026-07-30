# [SPEC-001] [URD] Tính năng Mua gói cước di động
**Mã Index:** SPEC-001
**Phiên bản (Version):** v1.0
**Ngày cập nhật:** 25/02/2026
**Người làm (Owner):** Antigravity UX Design Team (UR, UX, TW, CR)

---

## Phần I: Bối cảnh & Mục tiêu (Business Perspective)
- **Mục tiêu kinh doanh (Business Goals):** 
  - Đơn giản hóa quá trình mua gói cước, giải quyết tình trạng "nghịch lý sự lựa chọn" (quá nhiều gói làm người dùng bối rối).
  - Tăng tỷ lệ mua thành công (conversion rate) với luồng thanh toán 1 chạm (One-tap checkout).
  - Tăng tỷ lệ duy trì (retention) và sự an tâm của khách hàng bằng việc minh bạch tính năng "Tự động gia hạn".
- **Lộ trình triển khai (Rollout Plan):** 
  - Đội ngũ Testing nội bộ chạy luồng Beta với nhân viên VNPT trong vòng 1 tuần trước khi phân phối dần (Canary release) cho 10% tập khách hàng thật và sau đó là Go-live toàn bộ.

---

## Phần II: Trải nghiệm Người dùng (UX & Copywriting)
- **User Stories (Hành trình trải nghiệm):** 
  - **US.1:** Là khách hàng đang lướt mạng và đột ngột hết dung lượng, tôi muốn thấy nút nạp gói cước cứu trợ ngay ngoài trang chủ để tôi không bị gián đoạn trải nghiệm quá lâu.
  - **US.2:** Là khách hàng mở mục "Gói cước", tôi muốn thấy các gói "Gợi ý cho bạn" dựa trên thói quen (xem video, chơi game) để tôi dễ dàng ra quyết định mua ngay.
  - **US.3:** Là khách hàng xem chi tiết gói, tôi muốn biết gói này xài thực tế được bao nhiêu tiếng TikTok/YouTube thay vì con số GB tối nghĩa. Tôi cũng muốn thấy rõ nút "Tự động gia hạn" để kịp thời TẮT đi nếu không có nhu cầu chu kỳ sau, tránh cảm giác bị trừ tiền ngầm.
  - **US.4:** Là người mua hàng, tôi muốn chốt thanh toán bằng FaceID/Vân tay nhanh chóng và ngay sau đó được ăn mừng (Celebration) kèm đồng hồ báo dung lượng mới cập nhật.

- **Sơ đồ UX (User Flow / Wireframe):** 
  - *(Luồng chi tiết đã được vẽ bằng Mermaid map).* 
  - Luồng tắt (Shortcut): Trang Chủ -> Phát hiện hết Data -> Sticky Bar Cứu Trợ -> Xác thực Mua -> Thành công.
  - Luồng chuẩn: Màn hình Gói Cước -> Tab Gợi Ý -> Chi tiết gói (Có nút chặn tự gia hạn) -> Thanh Toán -> Thành Công.

- **Copywriting (Nội dung thấu cảm):**
  - *Cảnh báo sắp cạn Data:* "⚠️ Bạn sắp cạn Data rồi! Mua nhanh Gói Cứu Trợ 1 Ngày để xem phim không gián đoạn."
  - *Thuyết minh quy đổi Data:* "~ 2 tiếng thỏa thích xem TikTok" hoặc "Phù hợp Cày Video, gọi Zalo cháy máy."
  - *Message Tắt gia hạn:* "Hệ thống sẽ không tự động trừ tiền bạn vào kỳ hạn sau."
  - *Lỗi Thanh toán:* "Oops! Giao dịch bị từ chối từ phía ngân hàng. Bạn thử thanh toán lại bằng Số dư Tài khoản chính xem sao?"
  - *Thành công (Celebration):* "🎉 Nạp Data Thành công! 7GB/Tuần đã ở trong kho của bạn. Trải nghiệm ngay thôi!"

---

## Phần III: Quy trình & UI Logic (Step-by-step)
| Bước | Màn hình | Hành động của người dùng (User Action) | Phản hồi của hệ thống (System Response / UI Changes) |
|---|---|---|---|
| 1 | Trang Chủ | Người dùng mở App My VNPT | Hệ thống call API kiểm tra số dư Data. Nếu <10MB, hiển thị Sticky bar "Cứu trợ gói D5". Nếu >10MB, ẩn thanh này. |
| 2 | Màn hình Gói Cước | Người dùng bấm vào mục chọn "Gói cước" | Hiển thị 2 Tab: "Gợi ý cho Bạn" (Mặc định) và "Tất cả". Tab Gợi ý render 3 thẻ gói P0/P1/P2 từ API Recommend Data. |
| 3 | Chi tiết Gói | Chọn 1 gói cứu trợ (ví dụ ST30K) | Mở màn hình Bottom Sheet. Hiện mô tả quy đổi thông minh (Ví dụ: Xem 4h Tiktok). Cụm công tắc "Tự động gia hạn" hiển thị ngay dưới nút Mua, cho phép gạt BẬT/TẮT tự do. |
| 4 | Thanh Toán | Bấm nút "Mua Ngay (30.000đ)" | App kiểm tra số dư TK Chính (Core Billing). Nếu ĐỦ -> Gọi popup xác thực sinh trắc học (FaceID/Vân tay). Nếu KHÔNG ĐỦ -> Bật Action Sheet chọn nguồn ngoài (Momo/Apple Pay/ZaloPay). |
| 5 | Hoàn Thành | Xác thực vân tay/khuôn mặt thành công | Đóng luồng thanh toán tạm, load ngay màn hình Success với hiệu ứng Pháo hoa (Lottie animation). Hiển thị Widget đếm ngược dung lượng Data thực tế (Ví dụ: 7.00/7.00 GB). |

---

## Phần IV: Đặc tả Nghiệp vụ & Kỹ thuật (Backend Logic)
- **Luật kinh doanh (Business Rules):** 
  - Gói liệt kê trong tab "Gợi Ý" phải khớp với hồ sơ hành vi của thuê bao (Dựa vào AI mô hình Customer Segmentation bên Backend để trả ra mã gói).
  - Thuê bao phải đang hoạt động 2 chiều mới cho nạp gói cước. Mọi khách hàng đang bị khóa/chặn do cước không được phép thực hiện giao dịch sinh tiền này.
- **Quy tắc hệ thống quy đổi (Algorithm):** 
  - Quy tắc dịch Data sang từ ngữ người dùng cần được ánh xạ động (Dynamic Map) từ CMS chứ không fix cứng. (VD: 1GB Data = 1h xem Video HD = 2h lướt TikTok).
- **Xử lý Ngoại lệ (Edge Cases / Exception Handling):** 
  - **Mất mạng Internet khi hết Data:** Đảm bảo toàn bộ request API của App My VNPT liên quan kết nối Mua Gói nằm trong danh sách "Zero-rating" (Miễn cước Data) từ trạm phát (BTS) để users luôn mở được App và mua tính năng này cứu mạng ngay lúc đường cùng.
  - **Lỗi API trừ tiền (Timeout):** Nếu Core Viễn Thông báo timeout (do nghẽn), tạm thời Hold giao dịch trạng thái "Đang xử lý". Không hiển thị "Lỗi" vội, không cho phép bấm mua lại để chặn rủi ro trừ tiền 2 lần (Double Charge).
- **Tác vụ ngầm (Background Jobs):** 
  - Job đồng bộ tính năng "Auto-Renew" vào DB của hệ thống Billing Viễn thông. Nếu người dùng chọn TẮT tự gia hạn, trạng thái đồng bộ về trạm phải là False.

---

## Phần V: Kiểm thử & Vận hành (Testing/Operation)
- **Kịch bản Test (Test Scenarios):** 
  - *Luồng Dương:* Sim còn tiền -> Xem gợi ý -> Mua -> FaceID -> Thành công -> API Data cộng đúng 1GB -> Giao diện F5 đúng số dư.
  - *Luồng Âm (Hết tiền):* Nhảy cổng Momo -> Trả về lỗi hủy từ Momo -> App phải back lại màn thanh toán, khuyên nạp tiền chứ không Crash/Văng App.
  - *Luồng Đặc Thù Zero-rating:* Cố tình tắt WiFi, xài Sim vừa hết sạch tiền & 100% dung lượng Data -> Test xem mở App có fetch được list gói cước lên màn hình không?
- **Cấu hình CMS/Admin Toolkit:** 
  - Portal Admin cho phép tự định nghĩa (Config) câu thông điệp đính kèm gói (Ví dụ đổi từ "Cày Youtube" sang "Săn Sale Shopee" vào mùa Sale) mà không cần Frontend release lại (Live Update).
- **Tracking & Analytics:** 
  - Đo lường (Event Tracking) sự tương tác với nút gạt "Gia hạn tự động". Đếm xem tỷ lệ khách hàng chủ động Tắt đi là bao nhiêu % -> Rút gọn khoảng cách Mis-trust của khách.
  - Đo độ rụng rớt (Drop-off Rate) ở bước "Giao dịch không thành công với ví" đi tiếp tới đâu.
