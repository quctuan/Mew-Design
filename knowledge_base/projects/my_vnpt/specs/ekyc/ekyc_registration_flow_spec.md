# [SPEC-002] Full-stack Product Spec: Luồng Đăng ký & Cập nhật Thông tin Thuê bao (eKYC)

**Mã Index:** SPEC-002
**Dự án:** MyVNPT App - Tối ưu hóa Luồng Cập nhật Thông tin
**Đội ngũ thực hiện:** UX Design Team x P&G Insights Team (Quy trình VietDoc)
**Phiên bản:** 1.0
**Ngày cập nhật:** 26/02/2026

---

## 1. Tổng quan sản phẩm (Product Overview)

### 1.1 Mục tiêu kinh doanh & Cảm xúc (Business & Emotional Goals)
**Business Goal:** Tăng tỷ lệ hoàn thành (Success Rate) đăng ký thông tin thuê bao trực tuyến, giảm tải cho quầy giao dịch và giảm tỷ lệ thoát (Drop-off Rate) ở các bước chụp giấy tờ. Đảm bảo tuân thủ nghị định viễn thông.
**Emotional Goal:** Xóa bỏ cảm giác áp lực, hành chính hóa khi "bị ép" khai báo thông tin. Mang đến trải nghiệm quét eKYC **khoan dung, bảo vệ, thấu cảm**. Người dùng cảm thấy nhẹ nhõm và tự hào vì vừa bảo vệ được danh tính số của mình thông qua "Trợ lý bảo mật" MyVNPT.

### 1.2 Nguyên tắc thiết kế (Core Design Principles)
- **Zero-click Capture:** Hủy bỏ nút [Chụp]. Thay bằng công nghệ Auto-capture. Tự động nhận diện đạt chuẩn (khung, sáng, nét) và chụp liền tay.
- **Interactive Fallback (Hướng dẫn gỡ lỗi AR):** Thay thế những thông báo báo lỗi tĩnh, khô khan ("Ảnh mờ", "Bị chói"). Áp dụng AR Overlay - khoanh vùng lỗi trực tiếp trên màn hình camera theo thời gian thực (real-time) để hướng dẫn khách hàng tự sửa tư thế chụp.
- **Conversational Tone-of-Voice:** Thay đổi văn phong từ mệnh lệnh ("Vui lòng chụp lại", "Yêu cầu...") thành ngôn ngữ khích lệ, trò chuyện ("Chỉ một chút nữa thôi!", "Chỗ này hơi lóa, bạn nghiêng máy xíu nhé!").

---

## 2. Bản vẽ Luồng Người Dùng (User Flow)

Dưới đây là sơ đồ luồng trải nghiệm (The "How"), mô tả các điểm chạm kết hợp cảm xúc người dùng (được thiết kế bởi **UX Designer**):

```mermaid
graph TD
    classDef start fill:#f9f,stroke:#333,stroke-width:2px;
    classDef normal fill:#fff,stroke:#333,stroke-width:1px;
    classDef emotion fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;
    
    A([Mở App MyVNPT / Web]) --> B{Kiểm tra trạng thái TTTB}:::normal
    B -->|Đang chờ chuẩn hóa/Mới| C[Màn hình Welcome: <br>Trợ lý Bảo mật Danh tính]:::emotion
    B -->|Đã chuẩn hóa| X([Kết thúc luồng])
    
    C --> D[Màn hình Hướng dẫn chụp giấy tờ <br> Minh họa animation ngắn]:::normal
    D --> E[Bật Camera & Khung nhận diện]:::normal
    
    E --> F{Hệ thống tự động đánh giá <br> AR Overlay thời gian thực}:::normal
    F -->|Lỗi lóa/mờ/thiếu góc| G[Khoanh đỏ vùng lỗi trên màn hình <br> Text: Cảnh báo cụ thể]:::emotion
    G --> E
    
    F -->|Đạt chuẩn| H[Auto-Capture: Tự động chụp! <br> Chuyển xanh lá + Rung haptic]:::success
    H --> I[Chụp mặt sau CCCD]:::normal
    I --> J{Đánh giá tương tự}:::normal
    J -->|Lỗi| K[Gợi ý khắc phục]:::emotion
    K --> I
    J -->|Đạt chuẩn| L[Auto-Capture thành công]:::success
    
    L --> M[Nhận diện khuôn mặt chân dung]:::normal
    M --> N{Thực hiện yêu cầu Liveness}:::normal
    N -->|Gật/Nháy mắt đạt| O[Xác thực khuôn mặt thành công]:::success
    N -->|Lỗi môi trường| P[Feedback: Mời lại gần/Đủ sáng]:::emotion
    P --> M
    
    O --> Q[Màn hình Xác nhận Thông tin (OCR) <br> Cho phép User sửa lỗi cơ bản]:::normal
    Q --> R[Ký tên điện tử / Confirm]:::normal
    R --> S([Hoàn tất: Chúc mừng! Tài sản số đã an toàn]):::success

    %% Tooltips (thể hiện cảm xúc)
    click C "Khách hàng gỡ bỏ sự phòng vệ, chuyển sang tâm lý an tâm"
    click H "Khoảnh khắc 'Nổi da gà': Máy tự chụp nhanh và mượt mà"
    click G "Cảm thấy được ứng dụng 'Cầm tay chỉ việc' thay vì mắng mỏ"
    click S "Cảm giác nhẹ nhõm (Phew!), tự hào vì đã hoàn thành nhiệm vụ khó khăn"
```

---

## 3. Bản vẽ Phân rã Màn Hình & Copywriting (Technical Specs)

(*Được viết bởi **TW (Technical Writer)** dựa trên Flow của UX và Insights của P&G*)

### Màn hình 1: Khởi động / Welcome Screen (Point of Entry)
* **Visual:** Hình ảnh mô phỏng một "Tấm khiên" hoặc biểu tượng bảo mật an toàn thay vì icon chứng minh thư nhàm chán. Nút (Button) nổi bật dạng Call-to-action (CTA).
* **Copywriting:**
  * ToV (Tone of Voice): Động viên, trao quyền bảo vệ.
  * Headline: "Chỉ 1.5 phút để bảo vệ số điện thoại số 1 của bạn!"
  * Sub-text: "Thông tin của bạn sẽ được mã hóa an toàn. Hãy để MyVNPT giúp bạn hoàn thành việc quét thẻ tự động mà không cần nỗ lực."
  * Button CTA: "Khởi động Trợ lý quét (Bắt đầu)" thay vì "Chụp ảnh".

### Màn hình 2 & 3: Quét tự động (Auto-capture) mặt Trước/Sau
* **Visual:** Camera view toàn màn hình. Có khung overlay trong suốt (khung form CCCD).
* **Behavior:** User KHÔNG CẦN BẤM NÚT "CHỤP". 
* **Logic:** Khi 4 góc thẻ lọt vào khung và độ chói lõi (Glare Score) < ngưỡng cho phép, AI tự kích hoạt chụp ảnh -> Hiệu ứng lóe sáng "Scan" màu xanh lá chạy ngang màn hình để thông báo máy đã tự chụp xong -> Rung máy (Haptic feedback nhẹ).
* **Copywriting (Interactive Fallback):**
  * Nếu AI phát hiện mờ do tay rung: Text xuất hiện trên màn hình camera *"Cố gắng giữ điện thoại tĩnh một lát nhé!"*
  * Nếu dính ánh đèn chói: Áp dụng hiệu ứng Dimming (làm tối nhẹ) tại vùng bị chói và hiện Text khoanh đỏ ngay vùng chói: *"Khu vực này đang bị lóa sáng, bạn nghiêng một xíu nhé!"*
  * Khi tự chụp thành công: *"Tuyệt vời! Thông tin rất sắc nét."* (Tạo cảm giác người dùng đang làm rất tốt việc của mình).

### Màn hình 4: Xác thực khuôn mặt (Liveness)
* **Visual:** Khung Oval chân dung với luồng khung viền tiến độ.
* **Logic:** Hoàn thành nhiệm vụ nhìn thẳng, mỉm cười, quay trái/phải.
* **Copywriting:**
  * ToV: Nhẹ nhàng, như lúc chụp ảnh selfie.
  * Hướng dẫn: "Hãy để gương mặt lọt vào khung hình nhé." / "Tuyệt, giờ hãy nhìn sang trái một chút nào!"

### Màn hình 5: Xác nhận thông tin (Extracted Data Review)
* **Visual:** Hiển thị thẻ card thông tin đã được trích xuất (OCR) sạch sẽ, phân chia vùng (Thông tin cá nhân, Địa chỉ, Thẻ).
* **Logic:** Cho phép sửa các trường dữ liệu dễ sai (Như địa chỉ hẹp) thông qua Inline-edit.
* **Copywriting:**
  * Headline: "Hãy kiểm tra lại thông tin, Trợ lý đã quét xong!"
  * Dòng trạng thái (Toast): "Dữ liệu được OCR trích xuất với độ chính xác 98%."

### Màn hình 6: Chúc Mừng (Success Screen)
* **Visual:** Hình ảnh pháo hoa, huy hiệu (Badge) check-mark xanh. Không sử dụng màn hình trắng chứa một file giấy tờ.
* **Copywriting:**
  * ToV: Tuyên dương, nâng tầm cảm xúc khách hàng.
  * Headline: "Phew! Hoàn thành xuất sắc!" 
  * Sub-text: "Thông tin của bạn đã được đối soát thành công và định danh số điện thoại được đưa vào trạng thái Bảo vệ 100%. "
  * Button CTA: "Đóng cửa sổ" hoặc "Trở về Trang chủ".

---

## 4. Kiểm duyệt & Đánh giá (Quality Review)

(*Báo cáo từ **CR (Quality Reviewer)** trước khi bàn giao Code*)
- [x] **JTBD Check:** Giải quyết được nhu cầu thao tác quét eKYC nhanh ở bất kỳ đâu (do có hướng dẫn xử lý chói đèn, mờ). Rút ngắn thao tác chạm.
- [x] **Brand Insight Check:** Không còn sắc thái "Đe dọa khóa SIM" ở các thông báo báo lỗi. Toàn bộ ngôn ngữ đều đóng vai Trợ lý bảo vệ danh tính, đúng chuẩn định hướng P&G Insight.
- [x] **Feasibility Check:** AI xử lý Auto-capture (Zero-tap) có trong tầm với của các SDK eKYC hiện hành. Tính năng quét điểm chói theo thời gian thực (Glare Detection Layer) hoàn toàn khả thi về mặt Front-end.

**-> Kết luận CR:** Bản Full-stack Product Specification này **PASSED**. Sẵn sàng bàn giao cho đội ngũ Dev (Lập trình - Front-end/Back-end) triển khai. 

---
*(Kết thúc Master Workflow)*


<!-- gdoc_id: 10hEc8YIAt48yRBIW4V00TsbGY7o0Wn_3RNucDaOR6XM -->
