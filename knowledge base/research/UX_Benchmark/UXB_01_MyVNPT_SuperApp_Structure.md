# 🏷 UX Benchmark: My VNPT Super App Structure
- **ID:** UXB_01_MyVNPT_SuperApp
- **Tên Tính năng:** Cấu trúc Phân hệ Super App
- **Nguồn Tham khảo:** MyIM3 (Indosat Ooredoo), MoMo, Zalo, Grab.

## 1. Phân tích Đối thủ Key (Benchmarking)

### 🔴 MyIM3 (Benchmark chính):
- **Cấu trúc:** Tách biệt rõ "Account" (trái) và "Lifestyle/Kios" (phải).
- **Điểm mạnh:** Sử dụng Dashboard với các thẻ (Cards) có thể tương tác nhanh. Tích hợp "Missions" ngay màn chính để tạo thói quen mở app hàng ngày.
- **Bài học:** Các dịch vụ giải trí không được nằm quá sâu. Cần có một "Bento-grid" nhỏ ở Home để giới thiệu DigiZone.

### 🔵 MoMo (Fintech Super App):
- **Cấu trúc:** Phân loại dịch vụ cực mạnh bằng Icon (Grid 4xN).
- **Điểm mạnh:** Thanh tìm kiếm (Search bar) là "trái tim" của app. Tích hợp AI để gợi ý "Dịch vụ bạn có thể cần".
- **Bài học:** Tab Quick Action của My VNPT nên mô phỏng thanh tìm kiếm đa năng này nhưng thông minh hơn nhờ AI.

---

## 2. Cấu trúc Section đề xuất (Section-by-Section)

### A. Trang chủ: My VNPT (Self-care & Telco)
1. **Header:** Profile, Notification, QR Scanner.
2. **Dashboard Account:** Số dư Main Balance, Data Quota (Visual ring/progress bar), Hạn dùng.
3. **Quick Telco Actions:** Nạp tiền, Đổi SIM, Gói cước hot (Carousel).
4. **Bento Discovery (DigiZone Insight):** 2-3 ô nội dung giải trí/smart home đang hot nhất.
5. **Community Signals:** "Hôm nay 50,000 người VNPT đã tham gia nâng cấp gói 5G".

### B. DigiZone (Smart home, Entertainment, Health)
1. **IoT Dashboard:** Trạng thái các thiết bị (Đèn, Khóa, Camera) - Chỉ hiển thị nếu user có dùng.
2. **Entertainment Hub:** Movie, Music, News (Thumpnails lớn, mượt).
3. **Daily Health:** Đếm bước chân (Sync với Google Fit/HealthKit), Chỉ số sức khỏe.
4. **Community Tips:** Video hướng dẫn dùng Smart Home từ TikTok/YouTube cộng đồng.

### C. VNPT Shop (E-commerce & Shopping)
1. **Search & Category Grid:** Smartphones, Phụ kiện, Vouchers, Sim số đẹp.
2. **Flash Sales:** Các khung giờ giảm giá sốc cho thiết bị viễn thông.
3. **Personalized Picks:** "Sản phẩm dành cho bạn" (Dựa trên lịch sử tiêu dùng).
4. **Subtle Community:** Đánh giá thật của người dùng kèm ảnh.

### D. Rewards (Loyalty & Gamification)
1. **Points Overview:** Số điểm hiện có, Hạng hội viên (Gold/Silver/Platinum).
2. **Burn Points:** Đổi voucher ăn uống, mua sắm (Phân loại theo Brand).
3. **Earn Points (Missions):** "Xem 1 bộ phim trên DigiZone", "Mời bạn dùng My VNPT".
4. **Rankings:** BXH người dùng năng nổ trong cộng đồng (Gamified).

### E. Trang Quick Action (On-demand & AI)
1. **AI Chat Interface (Semi-translucent):** Trợ lý đa năng (Hỏi cước, hỏi phim, yêu cầu hỗ trợ).
2. **Frequent Shortcuts:** Các tác vụ user hay dùng (Nạp tiền cho mẹ, Đóng cước nhà).
3. **Trending Now:** Top các tìm kiếm/tác vụ cộng đồng đang thực hiện.

---

## 3. Chiến lược "Cộng đồng ẩn" (Shadow Community)
- **Review Layer:** Tích hợp đánh giá 5 sao vào mọi dịch vụ ở DigiZone và Shop.
- **Social Proof:** Hiển thị "Hot" hoặc "Trending" dựa trên dữ liệu thật của User base.
- **Q&A Section:** Ở mỗi trang chi tiết sản phẩm/gói cước, có phần "Hỏi đáp cộng đồng" thay vì chỉ là FAQ cứng nhắc.

---
## 4. Key Takeaways (Do & Don't)
- **Do:** Giữ tab Home (Viễn thông) cực kỳ tinh gọn, phản hồi nhanh.
- **Do:** Sử dụng hình ảnh (Visuals) chất lượng cao cho DigiZone để tạo cảm giác Lifestyle.
- **Don't:** Ép người dùng vào trang Cộng đồng dạng Social Feed (như Facebook) - sẽ gây loãng. Chỉ dùng Cộng đồng để củng cố niềm tin (Trust builder).
