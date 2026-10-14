# 🔍 UX Research Insight: Điều chỉnh nghiệp vụ đổi eSIM trên My VNPT
- **Jira Task:** [IT360-1585542] Điều chỉnh nghiệp vụ đổi eSIM trên My VNPT
- **Tóm tắt Yêu cầu:** Bổ sung nội dung cảnh báo (nhắc nhở khách hàng cài đặt eSIM ngay và báo thời hạn xử lý khiếu nại là trong 72 giờ) tại 2 điểm chạm: Màn hình báo đổi eSIM thành công trên App My VNPT và trong Email gửi mã QR eSIM.

## 1. Khoảnh khắc Cốt lõi (The Moments) & Nỗi đau
- **Hoàn cảnh (When/Where):** Khách hàng vừa mới thực hiện thanh toán online thành công và vừa mới nhận được chiếc mã QR eSIM mới toanh trên màn hình App hoặc trong hòm thư cá nhân.
- **Cảm xúc (Emotional State):** Thỏa mãn vì đã mua xong, nhưng lại sinh ra tâm lý chủ quan, nghĩ rằng mã QR lưu đó rồi lúc nào rảnh hoặc tiện tay thì quét cài đặt cũng được.
- **Cách làm hiện tại (Current Workaround):** Khách hàng thường chỉ chụp nhanh màn hình (screenshot) hoặc để ngâm email đó qua nhiều ngày mà không add (quét) quét mã vào thiết bị vật lý ngay lúc đó.
- **Nỗi đau (Pain Point):** Nếu mã QR bị người khác nhìn trộm/lấy mất, hoặc để quá thời gian (hơn 72 giờ) gây ra rủi ro lỗi mã, khách hàng sẽ mất tiền oan và gọi điện khiếu nại gay gắt lên trung tâm CSKH. Căn nguyên nỗi đau là khách hàng **thiếu yếu tố "Thúc giục cấp bách" (Sense of Urgency)** và **không lường trước giới hạn trách nhiệm 72 giờ** ngay tại thời điểm chạm nhận mã QR.

## 2. Phân tích JTBD (Tối đa 3 câu)
1. **Khi** tôi vừa nhận được mã QR eSIM mới trên App/Email -> **Tôi muốn** được hệ thống nhắc nhở rõ ràng lập tức về các rủi ro bảo mật phòng tránh mất cắp và thời hạn giới hạn khắc phục sự cố -> **Để tôi có thể** ý thức được sự gấp gáp, cài đặt mã QR ngay lập tức vào máy nhằm đảm bảo quyền lợi cá nhân.

## 3. Khoảng trống cơ hội (Opportunities)
- Vấn đề cốt lõi chưa được giải quyết tốt nhất ở đâu?
Yêu cầu gạch đầu dòng của PRD Jira khá thô cứng: "bổ sung thông báo". Cơ hội của thiết kế (Design Opportunities) ở đây không chỉ đơn thuần là nhét thêm một đoạn Text dài dòng (vì khách hàng thường lười đọc chữ), mà cần làm **nổi bật từ khóa "72 GIỜ"** (in đậm, màu đỏ). Có thể xem xét dùng **Icon Cảnh Báo (Warning)** và đi kèm với **Nút CTA trực diện "Hướng dẫn cài đặt ngay"** để điều phối thói quen hành vi khách hàng thay vì chỉ thông báo suông.

---

# Empathy Strategy Blueprint: Cảnh báo rủi ro 72H đổi eSIM

## 1. Insight Cốt tử
"Sự tiện lợi của việc nhận mã QR Online ngay lập tức lại trở thành cái bẫy ru ngủ sự đề phòng của khách hàng; họ cần một 'cú hích' cảnh báo bằng thị giác để bừng tỉnh và cài đặt ngay thay vì vứt mã QR đó vào dĩ vãng."

## 2. Giải pháp Đề xuất (The Idea)
- **Vế Logic (Trí não):** Thay vì thả một đoạn văn bản (Text Notice) bằng chữ thường ở cuối màn hình/email, ta sẽ đóng gói đoạn cảnh báo này vào một component UI `Alert Banner` (hoặc `Call-out box`) màu cam/đỏ. Từ khóa **72 GIỜ** phải được in đậm. Bên dưới dòng chữ này, gắn thẳng một Nút CTA phụ (Secondary Button) hoặc Text Link: *"Xem hướng dẫn cài đặt eSIM vào máy"*.
- **Vế Emotion (Trái tim):** Chuyển hóa trạng thái Khách hàng từ "Thảnh thơi/Rảnh rỗi" sang trạng thái "Chú ý nhẹ/Hành động". Sự rõ ràng trong thời hạn 72H giúp họ cảm thấy VNPT minh bạch, sòng phẳng ngay từ đầu chứ không giấu giếm điều khoản để phủi trách nhiệm.

## 3. Goosebumps Validation (Pass / Fail)
- **Tính Người (Human-Centricity): [PASS]** Không cộc lốc đổ lỗi cho người dùng. Khéo léo nhắc nhở rủi ro "lộ mã QR" như một người đồng hành bảo vệ tài sản cho khách hàng.
- **Tính Vượt trội (Superiority): [PASS]** Biến một dòng thông báo pháp lý khô khan thành một điểm chạm hướng dẫn hành vi (Navigating Behavior) qua việc gắn kèm link/nút Hướng dẫn cài đặt.
- **Chạm Cảm xúc (Emotional Resonance): [PASS]** Đủ mức độ răn đe (Urgency) nhưng vẫn giữ được sự lịch sự của dịch vụ CSKH. Đem đến cảm giác an tâm vì được nhắc nhở.
