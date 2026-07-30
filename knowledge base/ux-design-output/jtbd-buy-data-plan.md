# Ngiên cứu Trải nghiệm Người dùng (UX Research)
**Tính năng**: Mua gói cước di động
**Người chịu trách nhiệm (Role)**: UR (UX Researcher)
**Framework**: Jobs-to-be-Done (JTBD) & Competitor Analysis

---

## 1. Phân tích Jobs-to-be-Done (JTBD)

Thay vì thiết kế tính năng "Hiển thị danh sách gói cước và nút mua", chúng ta cần giải quyết công việc (Job) mà người dùng thực sự đang cố gắng hoàn thành.

*   **Core Job (Nhu cầu cốt lõi):** "Khi tôi đang sử dụng điện thoại mà đột ngột hết Data, tôi muốn tìm và mua một gói cước phù hợp ngay lập tức để *không bị gián đoạn trải nghiệm* (đang xem phim, gọi video, hoặc tìm đường)."
*   **Emotional Job (Nhu cầu Cảm xúc):** "Tôi muốn cảm thấy mình *tiêu tiền thông minh*, mua được gói hời nhất. Tôi cực kỳ ghét cảm giác bị lừa vì các điều kiện ẩn (tự động gia hạn trừ tiền ngầm)."
*   **Social Job (Nhu cầu Xã hội):** "Tôi muốn có thể mua hộ data cho người thân (bố mẹ lớn tuổi) một cách dễ dàng."

**Chân dung & Hoàn cảnh (Contexts):**
1.  **Người dùng chủ động:** Lên app mỗi tháng để mua gói tháng/năm. (Cần thông tin đầy đủ, rõ ràng, so sánh giá).
2.  **Người dùng "chữa cháy":** Đang đi trên đường hoặc mất Wifi, cần data gấp. (Cần nhanh, 1 chạm mua ngay gói ngày, không cần đọc nhiều).
3.  **Người dùng mù mờ:** Không biết 1GB, 4GB là nhiều hay ít. (Cần app gợi ý theo thói quen: Xem Tiktok nhiều hay lướt web).

---

## 2. Phân tích Đối thủ (Competitor Benchmark - Việt Nam)

Nhìn ra thị trường Việt Nam hiện tại, các app mạng lưới viễn thông và ví điện tử đang giải quyết bài toán này như thế nào?

### 2.1. Nhóm App Viễn thông (MyViettel, MyMobiFone)
*   **Ưu điểm (Pros):** Hệ sinh thái phong phú, nhiều loại gói cước chia theo ngành nghề, game, tiện ích.
*   **Nhược điểm (Cons):** 
    *   *Nghịch lý sự lựa chọn (Paradox of Choice):* Quá nhiều gói cước (thường >50 gói), tên gói khó nhớ (V120, ST15K...). Người dùng bị choáng ngợp và không biết chọn gói nào.
    *   *Giao diện thẻ (Card) chật chội:* Thông tin nhồi nhét, khó so sánh giữa 2 gói với nhau.
    *   *Sợ hãi ngầm:* Tích chọn "Tự động gia hạn" thường bị ẩn hoặc đặt mặc định, gây mất thiện cảm.

### 2.2. Nhóm Mạng Ảo (Wintel, iTel)
*   **Ưu điểm (Pros):** Thông điệp cực kỳ rõ ràng, đơn giản: "Win60 - Data Không giới hạn". Bán sự an tâm tuyệt đối thay vì bán dung lượng.
*   **Nhược điểm (Cons):** Chưa cá nhân hóa mạnh, ít gói cước linh hoạt.

### 2.3. Nhóm Ví Điện Tử (MoMo, ZaloPay - Mua hộ data)
*   **Ưu điểm (Pros):** 
    *   Cực kỳ nhanh (Fast Checkout). Luồng thanh toán mượt mà chỉ qua 1 chạm vân tay/FaceID.
    *   Giao diện gọn gàng, hiển thị nhãn (Tag) như: *Bán chạy*, *Gói ngày*, *Combo*.
*   **Nhược điểm (Cons):** Không giám sát được lưu lượng sau khi mua (do tích hợp bên thứ ba).

---

## 3. Định hướng Thiết kế "Tốt nhất Việt Nam" cho Mua Gói Cước

Từ phân tích trên, UX flow của chúng ta TRÁNH vết xe đổ của các nhà mạng cũ (nhồi nhét) và kế thừa tốc độ của MoMo, sự rõ ràng của Wintel. Cụ thể:

1.  **Cá nhân hóa (Smart Recommendation):** 
    *   Thay vì đập vào mắt 100 gói cước, chỉ hiển thị **"Gợi ý cho Bạn"** (Gồm 3 gói: 1 gói chuyên dùng Data, 1 gói gọi+data, 1 gói ngắn hạn chữa cháy) dựa trên lịch sử dùng của họ.
2.  **Trực quan hóa Dung lượng (Data Visualization):** 
    *   Dịch thông số kỹ thuật (Ví dụ: 2GB/ngày) thành ngôn ngữ "Con người": *(Tương đương 4 giờ xem TikTok / 10 giờ Lướt web).*
3.  **Chi phí minh bạch (Transparent Pricing):** 
    *   Hiển thị rõ: *Chi phí thực tế là ... VNĐ / 1 ngày*. 
    *   Chức năng Tự động Gia hạn (Auto-renew) phải được để **nổi bật, cho phép TẮT ngay trên màn hình mua** thay vì giấu giếm.
4.  **Luồng thanh toán 1-chạm (1-Click Checkout):** 
    *   Tích hợp thanh toán bằng tài khoản viễn thông (nếu đủ tiền) làm mặc định ưu tiên. Nếu thiếu, hiển thị Apple Pay / Google Pay / Ví điện tử nổi bật ở bước kế sau để bấm là mua được luôn, không nhập thẻ thủ công.
5.  **Micro-interactions (Vi tương tác):** 
    *   Hiệu ứng *Ăn mừng (Celebration)* nhỏ xinh ngay khi giao dịch thành công và đồng hồ báo thời gian thực dung lượng vừa được cộng vào.

---
*(Tài liệu này là chuẩn đầu vào để thiết kế flow)*
