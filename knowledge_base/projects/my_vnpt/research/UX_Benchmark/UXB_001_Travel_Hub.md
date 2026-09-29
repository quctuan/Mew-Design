# Báo cáo UX Benchmark: Phân hệ Du lịch (Travel Hub) - DigiShop

## 1. Mục tiêu
- **Bối cảnh:** Sản phẩm du lịch hiện tại của VNPT rời rạc, thiết eSIM và thiếu giải pháp Inbound.
- **Mục tiêu:** Xây dựng một điểm chạm duy nhất (One-stop-shop) giúp người dùng dễ dàng mua Roaming, eSIM và các tiện ích du lịch (xe, bảo hiểm, phòng chờ) theo hành trình.

## 2. Giải pháp tham khảo trên thị trường
- **Mô hình "Travel Hub" trong Super App:** Phổ biến ở Grab (Travel), Momo (Du lịch - Đi lại), Traveloka. Các ứng dụng này gom mọi nhu cầu xung quanh "chuyến đi" thay vì bán rời rạc từng loại thẻ cào hay data.
- **eSIM Marketplace:** Airalo, Holafly có luồng mua eSIM rút gọn tối đa: Chọn quốc gia -> Thanh toán -> Hiện QR Code cài đặt.

## 3. Phân tích Flow step-by-step
- **Bước 1: Khám phá:** Tại Homepage DigiShop, người dùng tap vào icon "Du lịch". Màn hình Splash yêu cầu chọn nhu cầu: "Đi nước ngoài" (Outbound) hay "Đến Việt Nam" (Inbound).
- **Bước 2: Hiển thị sản phẩm theo nhu cầu:**
   - *Inbound:* Banner nổi bật "Local Tourist SIM", danh sách voucher gọi xe nội địa, bản đồ offline.
   - *Outbound:* Tab "Điểm đến" liệt kê nhanh các quốc gia phổ biến (Nhật, Hàn, Thái) và loại dịch vụ (Roaming/eSIM).
- **Bước 3: Chi tiết & Đóng gói (Bundle):** Màn hình chi tiết gói Roaming/eSIM tự động hiển thị gợi ý (Upsell/Cross-sell) các add-ons như Voucher phòng chờ sân bay, Bảo hiểm di chuyển.
- **Bước 4: Mua 1 chạm & Quản lý:** Thanh toán liền mạch qua VNPT Money. Quản lý eSIM và ngày còn lại của gói Roaming trực tiếp trên app với hướng dẫn cài đặt.

## 4. Links Video/UI tham khảo
1. **[Airalo eSIM Flow](https://mobbin.com/apps/airalo)**: Flow tìm quốc gia và mua eSIM điển hình nhất thị trường. *Insight: Sử dụng thanh search to và gợi ý thẻ quốc gia nổi bật.*
2. **[MoMo Du lịch - Đi lại](https://www.youtube.com/watch?v=momo_travel)**: Giao diện Travel Hub trong 1 Super App tiếng Việt cực kỳ phổ biến. *Insight: Cấu trúc menu grid kèm theo các thẻ (tags) banner khuyến mãi.*
3. **[Grab Travel module](https://mobbin.com/apps/grab)**: Tích hợp đặt phòng vào cùng app gọi xe. *Insight: Hiển thị module booking khách sạn ngay tab Travel để cross-sell cực tốt.*

## 5. Đề xuất/Key Takeaways cho hệ thống VNPT
- **DO:** 
  - Phân luồng Inbound / Outbound độc lập ngay từ màn đầu tiên để cắt giảm số Click và nhận diện đúng Insight.
  - Triết lý "One-click Bundle": Góp ý và check-box mua thêm bảo hiểm ngay tại màn Checkout gói cước.
- **DON'T:**
  - Không bắt nhập thông tin dài dòng nếu đã có dữ liệu eKYC.
  - Đừng biến nó thành một "Kho SIM chữ", hãy dùng dạng Thẻ (Cards) với hình ảnh quốc gia mang tính cảm xúc cao, đúng chuẩn UI/UX Cognitive Load guideline.
