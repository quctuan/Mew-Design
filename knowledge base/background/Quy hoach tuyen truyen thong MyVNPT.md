# Quy hoạch các tuyến truyền thông (Communication & Notification Strategy) trên MyVNPT

Tài liệu này đánh giá hiện trạng quy hoạch các nhóm Use-case truyền thông trên ứng dụng MyVNPT và đề xuất mở rộng, chiến lược phân bổ kênh (channels) cũng như nguyên tắc gửi thông báo để đảm bảo trải nghiệm người dùng tối ưu (UX).

---

## 1. Audit & Nhận xét về Đề xuất Hiện trạng

Đề xuất hiện tại của team đã phân chia thành 5 nhóm rất logic, bám sát các giai đoạn của một vòng đời khách hàng và các dịch vụ đặc thù của VNPT. Đặc biệt, việc đưa Nhóm 4 (Báo cáo Smart home, Gamification) vào cho thấy tư duy vượt ra ngoài "quản lý cước" thông thường để hướng tới "Digital Assistant".

**Tuy nhiên, để hoàn thiện và đưa cho team Dev/UIUX triển khai, Bản quy hoạch hiện tại đang thiếu 3 yếu tố then chốt (Missing points):**

1.  **Thiếu "Kênh hiển thị" (Touchpoints/Channels):** Đã biết nên gửi nội dung gì, nhưng chưa quy định nội dung đó sẽ xuất hiện ở đâu (Push Notification có rung, Pop-up chặn màn hình, hay chỉ là 1 chấm đỏ trong Hộp thư?).
2.  **Thiếu "Tần suất và Độ ưu tiên" (Priority & Frequency):** Việc nào là "Alert" chen ngang luồng user, việc nào là "Update" im lặng. Nếu không kiểm soát, app sẽ biến thành cỗ máy Spam.
3.  **Thiếu "Tính hành động" (Call to Action / Deep-link):** Báo cáo xong thì người dùng bấm vào đâu? Truyền thông cần tạo ra Conversion (chuyển đổi).
4.  **Thiếu các Use-case Nhạy cảm/Bảo mật:** Biến động số dư tài khoản/điểm, cảnh báo đăng nhập...

---

## 2. Gợi ý Bổ sung Use-case cho 5 Nhóm Hiện tại

Dưới đây là các use-case nên được cân nhắc thêm vào để cover đủ hành trình khách hàng:

### Nhóm 1: Nhóm nhắc nhở / Cảnh báo (Urgent & Alert)
*   **Hệ thống hiện tại:** Nhắc đóng cước, Cập nhật TTTB, TK chính hết hạn.
*   **Bổ sung thêm:**
    *   **Cảnh báo Data/Phút gọi:** Thuê bao đã dùng mức 80%, 95% hoặc vắt kiệt dung lượng gói.
    *   **Cảnh báo Bảo mật Cấp 1:** Đăng nhập MyVNPT từ thiết bị/IP mới; Thay đổi mật khẩu thành công.
    *   **Cảnh báo Cước:** Biến động số dư (Trừ tiền mua dịch vụ lớn), gia hạn gói cước thất bại do không đủ tiền.
    *   **Nhắc lịch trình:** Sắp tới hạn kỹ thuật viên VNPT đến nhà lắp mạng/sửa Internet.

### Nhóm 2: Nhóm Follow Up (Cập nhật tiến trình)
*   **Hệ thống hiện tại:** Đơn hàng, Ticket hỗ trợ.
*   **Bổ sung thêm:**
    *   **Cập nhật EKYC:** Trạng thái chuẩn hóa thông tin thuê bao (Thành công/Từ chối sửa).
    *   **Giao dịch điểm VPlus:** Đổi quà thành công, trạng thái vận chuyển quà vật lý VPlus.
    *   **Follow-up Survey (NPS):** Ngay sau khi Ticket kỹ thuật đóng -> Lời mời đánh giá chất lượng sửa mạng (rất quan trọng để cải thiện dịch vụ).

### Nhóm 3: Nhóm Recommend (Tư duy cá nhân hóa & Upsell)
*   **Hệ thống hiện tại:** Gói cước, Tính năng, Nội dung giải trí phù hợp.
*   **Bổ sung thêm:**
    *   **Trigger-based Recommend:** Khi phát hiện thuê bao ra nước ngoài -> Gợi ý mua Roaming.
    *   **Smart Analytics Đỉnh cao:** Tháng trước phát sinh cước ngoại mạng nhiều -> "Gợi ý gói cước kèm thoại ngoại mạng để tiết kiệm 30%".
    *   **Cross-sell gia đình:** Mời thành viên vào Family Group khi phát hiện chung địa chỉ lắp Internet.

### Nhóm 4: Nhóm Thông báo, Báo cáo (Insight & Report)
*   **Hệ thống hiện tại:** Thiết bị lạ vô mạng nhà, Internet con cái, Gamification.
*   **Bổ sung thêm:**
    *   **Báo cáo Điểm Loyalty:** Số điểm VinaPhone Plus chuẩn bị hết hạn vào cuối kỳ (kích thích user đổi quà cháy túi).
    *   **Monthly Bill Summary:** Tổng hợp chi tiêu viễn thông hàng tháng (như Spotify Wrapped/Banking Recap).

### Nhóm 5: Nhóm Truyền thông Quảng cáo
*   **Hệ thống hiện tại:** Chương trình khuyến mại, Scheme.
*   **Bổ sung thêm:**
    *   **Partner Ecosystem Deals:** Các mã giảm giá liên kết (F&B, Du lịch, Shopee) lấy từ hạng Hội viên VNPT.
    *   **Flash Sale:** Giờ vàng nạp thẻ.

### Nhóm 6: Nhóm Thông báo Hệ thống & Chăm sóc khách hàng (System & CS)
*Nhóm Mass Broadcast (diện rộng) hoặc điều hướng người dùng.*
*   **Sự cố mạng lưới:** "Khu vực của bạn đang bị ảnh hưởng bởi sự cố hạ tầng/đứt cáp", "Bảo trì trạm/hệ thống thanh toán trong khoảng thời gian X".
*   **Nâng cấp Ứng dụng:** Yêu cầu cập nhật bản MyVNPT mới (Force Update / Optional).

### Nhóm 7: Nhóm Tương tác Xã hội & Gia đình (Social & Peer-to-Peer)
*Nhóm này cực kì quan trọng nếu app định hướng Emi & Family (1 người quản lý nhiều người).*
*   **Yêu cầu thanh toán hộ:** "Thuê bao 091x... (Con trai) vừa gửi yêu cầu bạn thanh toán giúp cước tháng này".
*   **Chia sẻ tài nguyên:** "Chồng bạn vừa chia sẻ thành công 2GB Data vào quỹ dùng chung của gia đình".
*   **Trao quyền truy cập:** "Người thân yêu cầu quyền xem camera an ninh tại Phòng khách".

### Nhóm 8: Nhóm Dẫn dắt & Đào tạo người dùng (Onboarding & Education)
*Nhóm hỗ trợ người dùng mới làm quen với App hoặc kích cầu tính năng ẩn.*
*   **Welcome Message:** Chuỗi tin nhắn chào mừng ngay khi tạo tài khoản sinh trắc học thành công, kèm quà tặng Tân thủ.
*   **Feature Discovery:** Khi app ra mắt tính năng mới: *"MyVNPT vừa ra mắt tính năng Gọi thợ chuyên nghiệp tận nhà, khám phá ngay!"*
*   **Edu-tips:** *"💡 Bạn có biết: Có thể dùng điểm VinaPhone Plus dư thừa để thanh toán hóa đơn Internet?"*

---

## 3. Quy hoạch CHUẨN UX: Kênh và Touchpoint (Truyền thông ở đâu?)

Đây là bước cực kỳ quan trọng. Cần xây dựng "Ma trận điểm chạm" dựa trên độ ưu tiên.

### A. OS Push Notification (Gửi từ hệ thống máy)
*Đây là kênh nhạy cảm, dễ làm người dùng ghét và tắt luôn Push của App.*
*   **Active Push (Có chuông / Rung màn hình):** Chỉ dùng cho **Nhóm 1 (Urgent)** (Cắt mạng tới nơi, Trừ tiền cước lớn, OTP).
*   **Silent Push (Chỉ hiện trên Lockscreen, im lặng):** Dùng cho **Nhóm 2 và Nhóm 4**.
*   **Marketing Push:** Hạn chế tối đa gửi Push cho **Nhóm 3 và Nhóm 5**. Nếu gửi, chỉ được gửi 1 lần/tuần và phải Target đúng luồng (đỉnh cao là gửi Push kèm hình ảnh Rich-push).

### B. In-app Pop-up / Modal
*Chắn chình ình giữa màn hình khi người dùng vừa mở App MyVNPT.*
*   **Chỉ định:** Cực hiếm. Chỉ dành cho **Nhóm 1 (Loại chặn đường)**. Ví dụ: Bị khóa 1 chiều bắt buộc EKYC, bắt buộc Update App thì mới cho dùng, hoặc là Flash sale Khủng 1 năm có 1 lần.
*   *Lưu ý:* Tuyệt đối không nhét Quảng cáo gói cước lẻ tẻ vào Pop-up, gây bực mình.

### C. In-app Inbox (Hộp thư App)
*Nơi lưu trữ lịch sử truyền thông.*
*   **Quy hoạch UI:** Không được để chung 1 list dài vô tận. Hộp thư cần chia Tab:
    1.  *Giao dịch / Cảnh báo (Cá nhân)* -> Nhóm 1, Nhóm 2.
    2.  *Hóa đơn / Báo cáo* -> Nhóm 4.
    3.  *Ưu đãi / Tin VNPT* -> Nhóm 3, Nhóm 5.

### D. In-app Banner & Carousel (Trang chủ / Cửa hàng)
*   Kênh chuyên dụng cho **Nhóm 3 và Nhóm 5**. Không dùng Banner để thông báo nhắc nợ hay trạng thái đơn. Banner phải đẹp, là đất của Marketing.

### E. Assistant Feed/Widget (Giao diện trợ lý/Trang chủ)
*   Một dòng Feed UI sinh động hiển thị ở đầu trang chủ: *"Chào Minh, tài khoản sắp hết Hạn, nạp thẻ ngay nhé"*, hay *"Có vé xem phim Beta rẻ lắm nè"*.
*   Phục vụ cho **Nhóm 1 (nhẹ), Nhóm 3, Nhóm 4**. Giúp giao diện App bớt cứng nhắc và giống một trợ lý thật thụ (Emi Concept).

---

## 4. Các Nguyên Tắc "Vàng" Khi Thiết Kế Hệ Thống Thông Báo

1.  **Rule & Frequency Capping (Giới hạn tần suất):** Đặt luật: 1 user không nhận quá X thông báo Marketing trong 1 tuần (Tránh Burn-out).
2.  **No Dead-end (Mọi con đường phải có ngã rẽ):** Mội thông báo (dù là Inbox hay Push) **bắt buộc phải có URI Deep-link** trỏ tới màn hình tiếp theo. (VD: Nhắc đóng cước -> Click mở màn Thanh Toán; Nhắc Ticket -> Click mở màn xem tiến trình Kỹ thuật viên).
3.  **Human/Empathetic Copywriting:** Tránh ngôn ngữ robot/hành chính (VD: "Quy khách đã sử dụng hết lưu lượng gói MAX"). Thay vào đó: *"Data sắp cạn rồi bạn ơi, bổ sung thêm gói X để không gián đoạn xem phim nhé!"*.
4.  **Tôn trọng Opt-out:** Phải có màn hình cho phép người dùng tick chọn: *"Tôi không muốn nhận thông báo Quảng Cáo"*, nhưng giữ lại thông báo *"Biến động số dư"*. Đây là chuẩn mực của các Super App.

---

## 5. Bảng Ma trận Tổng hợp Quy hoạch (Notification Matrix)

Dưới đây là bảng tổng hợp ánh xạ giữa Nhóm nội dung, Độ ưu tiên, Kênh hiển thị và Hành động (dùng làm Spec cho đội Dev/Sytem).

| Nhóm Nội Dung | Ví dụ Tiêu biểu | Độ Ưu Tiên | Kênh Chính (Primary) | Kênh Phụ (Secondary) | Tần suất Max | Hành động (CTA) / Deep-link |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **1. Urgent / Cảnh báo** | Nợ cước, Cạn Data, OTP, Login lạ | **Cao (P1)** | Active Push (Có chuông) | Popup (Nếu cắt mạng) / Inbox | Khi sinh Event | Link -> Thanh toán / Đổi MK |
| **2. Follow-up / Tiến trình**| Xử lý Đơn hàng, Ticket Kỹ thuật | **Cao (P1)** | Silent Push | Inbox (Tab Giao dịch) | Khi đổi Trạng thái | Link -> Chi tiết đơn / Ticket |
| **3. Recommend / Upsell** | Gợi ý Roaming, Cấu trúc lại gói | **Vừa (P2)** | Dòng Feed Trợ lý (Home) | Banner / Inbox (Tab Ưu đãi) | 1-2 lần/tuần | Link -> Chi tiết Gói cước |
| **4. Report / Insight** | Điểm VPlus sắp hết, Báo cáo cước | **Vừa (P2)** | Silent Push | Inbox (Tab Báo cáo) | 1 lần/kỳ (Tháng) | Link -> Trang Lịch sử / Loyalty |
| **5. Marketing / Quảng cáo** | Flash Sale, Deal Đối tác F&B | **Thấp (P3)** | Banner Home / Carousel | Inbox (Tab Khuyến mại) | 1-2 lần/tuần | Link -> Landing Page chiến dịch |
| **6. System / Sự cố** | Bảo trì trạm, Đứt cáp quang | **Cao (P1)** | Cảnh báo đỏ tại Home | Inbox (Tab Hệ thống) | Theo sự cố | Link -> Bài viết Cáo lỗi |
| **7. Social / Chia sẻ** | Trả hộ cước, Xin Data, Xin share Cam | **Vừa (P2)** | Silent Push / Active Push| Inbox (Tab Giao dịch) | Khi sinh Event | Nút -> Trả hộ / Cấp quyền |
| **8. Onboarding / Hướng dẫn**| Welcome Tân thủ, Mới ra chức năng | **Thấp (P3)** | In-app Modal (Hiếm) | Dòng Feed Trợ lý | 1 lần/tính năngmới | Nút -> Bắt đầu trải nghiệm |

---
**Kết luận:** Đề xuất ban đầu của bạn đã có bộ khung tốt. Hãy kết hợp bộ khung đó với "Ma trận Điểm chạm" (Ở trên) và "Điều kiện Trigger" (Hành vi) để ra được bản **Notification Spec / URD** hoàn chỉnh nhất cho Dev và Marketing.
