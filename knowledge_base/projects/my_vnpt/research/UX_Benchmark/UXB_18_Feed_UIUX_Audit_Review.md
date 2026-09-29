# Báo cáo UI/UX Audit: My VNPT "Conversational Feed" Mockup

Dựa trên nguyên tắc thiết kế **Agentic UX** và **Cấu trúc Feed Hội thoại**, dưới đây là bản đánh giá chi tiết định dạng UI được cung cấp, đi kèm các đề xuất tái cấu trúc nhằm giảm thiểu "Cognitive Load" (Tải nhận thức) và cá nhân hóa giọng điệu.

---

## 1. Phân tích Trực quan & Cấu trúc (Visual & Architecture Audit)

### 🌟 Điểm Sáng (What works well)
- **Thẩm mỹ (Aesthetics):** Các khối Card (Bento Box) được bo góc mềm mại, đổ bóng (drop shadow) mượt mà kết hợp với nền gradient tạo chiều sâu tốt (Liquid Glass vibe).
- **Trạng thái tài nguyên (Resource Status):** Nêu bật việc giảm giá (Giảm 32.000đ) và tích hợp nút "Nạp ngay" nội tuyến rất trực quan và kích thích chuyển đổi (Call-to-Action).

### 🚨 Lỗi Cấu trúc (Architectural Flaws & Clutter)
1. **Lỗi "Phình to" (Bloated Quick Actions):** Khối 8 icon Quick Actions (Nạp điện thoại, Chuyển vùng...) chiếm đến 1/4 diện tích màn hình. Việc này đẩy luồng Feed "cá nhân hóa" xuống quá thấp (Below the fold). Đây là di chứng của lối thiết kế Sitemap truyền thống, đi ngược lại triết lý "Trợ lý chủ động dọn đường".
2. **Tab Chia rẽ (Dành cho bạn / Bản tin):** Cắt đứt luồng chảy (Endless Feed). AI Feed chuẩn mực phải là một luồng (Single-scroll), tin tức nổi bật phải được Agent chèn khéo léo đan xen vào giữa các thẻ báo cáo tài khoản cá nhân.
3. **Biểu đồ thị giác gây quá tải (Data Bar Chart):** Tại phần "Tần suất dùng data", việc vứt một biểu đồ hình cột chi chít nến xanh/nến đỏ như biểu đồ chứng khoán lên màn hình Home tạo ra **Cognitive Load (Áp lực nhận thức) ở mức báo động**. Khách hàng thông thường không có nhu cầu "phân tích dữ liệu" hàng ngày của mình bằng mắt.

---

## 2. Re-write: Đại tu Ngôn ngữ Giao tiếp (UX Writing Shift)

Mockup hiện tại đang bị mắc kẹt giữa việc ghép hình một cô Gái (Emi) vào bản báo cáo hệ thống. Theo góc độ UX chuẩn, **Tiêu đề khối (Section Titles) cần duy trì sự cố định** để luồng mắt người dùng dễ định vị, không bị nhảy lung tung làm hỏng mắt chóp cấu trúc. Tuy nhiên, thay vì dùng từ ngữ "Kỹ thuật báo cáo khô khan", ta sẽ dùng "Ngôn ngữ đời thường" (Human-centric language) để giữ vibe thân thiện.

| Vị trí | UX Writing Hiện tại (Khô cứng) | UX Writing Đề xuất (Cố định nhưng Rất "Người") | Lý do thay đổi |
| :--- | :--- | :--- | :--- |
| **Thanh Voice Search** | *Chỉ với 1 chạm nhờ vào câu lệnh, mọi thứ để Emi lo* | *"Bạn cần Mya giúp gì hôm nay?"* | Ngắn gọn tuyệt đối. Câu cũ quá dài và mang tính "slogan quảng cáo" lỗi thời. |
| **Tiêu đề khối Dashboard** | *Tình trạng thuê bao > Di động* | *"Tài nguyên của bạn"* hoặc *"Tình hình sử dụng"* | Rũ bỏ từ khóa kỹ thuật nặng nề "Thuê bao", "Tình trạng". Dùng từ mang lại cảm giác sở hữu nhẹ nhàng. |
| **Tiêu đề khối Data** | *Tần suất dùng Data tháng 4* | *"Thói quen lướt mạng"* | Đổi góc nhìn: Khách hàng không ngồi đếm "Tần suất Data" như kỹ sư viễn thông, họ quan tấm đến việc "Lướt mạng". |
| **Các khối Cross-sell** | *Emi gợi ý các gói cước tối ưu hơn* | *"Mya gợi ý riêng cho bạn"* | Vừa xưng danh từ Agent chân xưng, vừa khẳng định sự độc bản (riêng cho bạn) một cách tự nhiên. |
| **Khối Banner Quảng cáo**| *My VNPT có gì mới?* | *"Có thể bạn sẽ thích"* hoặc *"Góc rinh ưu đãi"* | Thu hút chú ý bằng lợi ích cá nhân, không tạo cảm giác ứng dụng đang nhồi nhét tin tức PR nội bộ. |
| **Khối Lịch phát sóng / Giải trí**| *Chương trình sắp diễn ra* | *"Góc giải trí"* hoặc *"Lịch xem của bạn"* | Tiêu đề cũ nghe như lịch phát sóng nhà đài rập khuôn. Từ mới tạo cảm giác nội dung được thiết kế riêng theo gu giải trí của khách hàng. |
| **Khối Trung tâm Hỗ trợ (CSKH)**| *Bạn cần Emi hỗ trợ?* | *"Cần trợ giúp?"* hoặc *"Kết nối với Emi (Mya)"* | Tiêu đề khối nên ngắn gọn nhất có thể để mắt dễ lướt. "Cần trợ giúp?" là chuẩn mực mắt quét dễ nhất, nội dung chi tiết để Agent thả thẻ (Card). |

> **Quy tắc vàng:** **Tiêu đề khối thì cố định**, nhưng phần text tóm tắt bên dưới (Subtitle) nằm trong từng khối Thẻ Card thì sẽ là nơi để Agent **phát ngôn động**. (VD: Tiêu đề là *"Thói quen lướt mạng"*, nội dung Thẻ bên trong sẽ là: *"Tháng này bạn cày Youtube tăng đột biến 12% so với tháng trước nha"*).

---

## 3. Đề xuất Cải thiện Layout (Actionable Solutions)

Để thiết kế này "chuẩn vị" siêu ứng dụng AI của 2026:

1. **Rút gọn Quick Actions thành "Dynamic Bar":** 
   - Thay vì ép chết 8 icon, nên gộp lại thành 4 icon.
   - **Tính động (Dynamic):** 4 icon này do thuật toán tự bốc lên đưa ra theo thói quen của user đó (Ví dụ: Chuyển vùng quốc tế chỉ hiện ra khi định vị user đang ở sân bay).
2. **Dẹp bỏ Hình minh họa Emi chiếm chỗ:** 
   - Xóa bỏ khối hình hoạt hình Emi tốn kém không gian chiều học dọc. Sự hiện diện của "Emi" được xác thực bằng Ngôn từ (UX Writing) ở ngay trên các tiêu đề Thẻ (Card).
3. **Chuyển Biểu đồ Data thành Thẻ Hành Động (Action Card):** 
   - Bỏ hoàn toàn Bar Chart. Nếu muốn báo user dùng nhiều data (Tăng 12%), hãy ghi 1 dòng text và kèm theo nút [Nâng cấp gói Data tháng tới] ngay lập tức để hái ra tiền (Profit Center), thay vì bắt họ xem biểu đồ rồi thôi.
4. **Thay Banner truyền thống thành Card:**
   - Thay vì cắm một banner ads hình chữ nhật ngang ("Đặt vé Vietlott..."), hãy biến nó thành một Thẻ Bento bo góc vuông vức nằm xen kẽ: *"Hôm nay thứ 5, Emi vừa săn được mã giảm giá vé Vietlott cho Tuấn, thử hên xem sao!"*
