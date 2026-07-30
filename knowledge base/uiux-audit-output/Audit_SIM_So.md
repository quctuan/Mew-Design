# Báo Cáo Kiểm Định UI/UX (Audit Report)
**Tính năng**: Tìm kiếm, Mua và Kích hoạt SIM Số
**Nguồn thiết kế**: Figma (Dự án SIM Số)
**Thực hiện bởi**: UI/UX Audit Team (LA, UXE, EC, UIA, UXW)
**Ngày thực hiện**: 26/02/2026

---

## 1. TỔNG QUAN (Từ LA - Lead Auditor)
Dựa trên triết lý **Jobs-To-Be-Done (JTBD)**, luồng này sinh ra để giúp người dùng "Thuê" (hire) hệ thống nhằm mục đích:
- **Main JTBD:** "Tôi muốn dễ dàng tìm được một số điện thoại đẹp, hợp phong thủy hoặc dễ nhớ, và hoàn tất thủ tục mua (giao tận nhà hoặc E-SIM) một cách nhanh gọn, hợp pháp mà không phải ra quầy giao dịch."
- **Key Pain Points (Nỗi đau lớn nhất):**
  - Sợ bị lỗi ở vòng EKYC (Chụp CCCD/Khuôn mặt bị mờ, không khớp).
  - Rối rắm ở khâu chọn loại SIM (Vật lý vs. E-SIM) không rõ thiết bị mình có hỗ trợ E-SIM hay không.
  - Sợ bị giam tiền khi đơn hàng bị hủy hoặc lỗi hệ thống.

---

## 2. KẾT QUẢ AUDIT CHI TIẾT (Từ các Chuyên gia)

### 🧑‍💻 UXE (UX Evaluator) - Khả năng sử dụng & Luồng đi:
- 🟡 **Minor Issue (Luồng tìm kiếm):** Bộ lọc (Filter) tìm số khá đa dạng nhưng có thể gây quá tải nhận thức (Cognitive Load). Cần bổ sung tính năng "Lưu bộ lọc" hoặc hiển thị các "Tag gợi ý sẵn" (Ví dụ: Số tiến, Số lặp) để người dùng chạm nhanh thay vì phải tự gõ logic tìm kiếm.
- 🟠 **Major Issue (Luồng E-SIM):** Đang thiếu một bước quan trọng là "Kiểm tra thiết bị có hỗ trợ E-SIM không" trước khi cho phép người dùng thanh toán mua E-SIM. Nếu mua xong không quét được mã QR, UX sẽ rất tệ.
- 🟢 **Good Point:** Sắp xếp tách biệt luồng Trả trước / Trả sau và luồng Kích hoạt là rất rõ ràng, định hướng người dùng tốt.

### 🕵️‍♂️ EC (Edge Case Hunter) - Rủi ro & Góc khuất:
- 🔴 **Critical Issue (EKYC Failure):** Trong khung `Sub-flows EKYC`, nếu hệ thống bên thứ 3 (như VNPT EKYC) phản hồi quá chậm (Timeout) hoặc rớt mạng ở bước Video Call, thiết kế hiện tại thiếu màn hình "Lưu nháp hồ sơ". Khách hàng có nguy cơ phải chụp lại CCCD từ đầu -> Cần luồng "Resume" (Tiếp tục đơn hàng đang dang dở).
- 🟠 **Major Issue (SLA 30 phút rớt hạn):** Mô tả có nhắc đến SLA Video call 30 phút. Nếu quá 30 phút mà nhân viên không bắt máy Call Center thì màn hình sẽ báo gì? Phải có UI cho phép "Hẹn gọi lại sau" hoặc chuyển sang luồng duyệt tay truyền thống (Upload ảnh cầm CCCD).

### 🎨 UIA (UI Analyst) - Giao diện & Hiển thị:
- 🟡 **Minor Issue (Accessibility chữ):** Ở các thẻ (Card) hiển thị số điện thoại, sự tương phản chữ (Contrast ratio) của các Tag (ví dụ "E-SIM", "Số đẹp") cần đảm bảo tỷ lệ WCAG tối thiểu 4.5:1 với nền.
- 🟡 **Minor Issue (Empty State):** Màn hình "Tra cứu đơn hàng" đang thiếu trạng thái khi không có đơn (Empty State) với một hình minh họa thân thiện và nút "Đi mua SIM ngay".

### ✍️ UXW (UX Writer Auditor) - Câu chữ & Ngôn từ:
- 🟠 **Major Issue (Lỗi đe dọa):** Ở màn hình mã lỗi "Kết thúc", cần tránh dùng những từ ngữ tiêu cực kiểu như "Giao dịch thất bại do lỗi CMND/CCCD". 
  - *Sửa thành (Thấu cảm):* "Oops! Khung hình bị mờ nên hệ thống chưa nhận diện rõ thẻ của bạn. Hãy thử chụp lại ở nơi sáng hơn nhé!"
- 🟡 **Minor Issue (Nút CTA):** Nút gọi Video Call hiện tại nếu chỉ viết "Gọi Video" thì hơi khô khan.
  - *Sửa thành:* "Bắt đầu Gọi Video (Sẽ mất khoảng X phút)" để quản trị kỳ vọng thời gian của người dùng.

---

## 3. TỔNG HỢP ACTION ITEMS (Dành cho Team Design & Dev)

| Mức độ | Lỗi phát hiện | Hướng khắc phục (Action Item) | Người nhận |
|---|---|---|---|
| 🔴 Critical | Thiếu rẽ nhánh Lưu nháp hồ sơ khi rớt mạng/Timeout ở bước EKYC. | Thiết kế thêm màn hình Resume đơn hàng nháp trong mục Quản lý. | UX Designer |
| 🟠 Major | Thiếu bước Check tương thích E-SIM trước lúc mua. | Bật Popup cảnh báo "Vui lòng xem danh sách điện thoại hỗ trợ E-SIM trước khi thanh toán". | UX Designer |
| 🟠 Major | UX Writing: Tone of voice ở màn hình Lỗi đang quá "người máy". | Viết lại các mã lỗi sang giọng điệu thân thiện, có Call-to-action đi kèm thay vì bỏ ngỏ. | TW / UX Writer |
| 🟠 Major | Quá hạn SLA 30 phút ở luồng Video Call. | Vẽ thêm màn hình "Trạm nghỉ": Cho phép đặt lịch hẹn giờ gọi lại hoặc Upload hình offline. | UX Designer |
| 🟡 Minor | Bổ sung Empty State cho Quản lý đơn hàng. | Thêm hình Graphic vui vẻ + Nút Call-to-Action về trang Tìm SIM. | UI Designer |

---
*(Tài liệu này được lưu tự động theo quy chuẩn của workspace tại thư mục knowledge base).*
