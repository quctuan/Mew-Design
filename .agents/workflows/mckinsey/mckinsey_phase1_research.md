---
description: Pipeline Khảo sát - Dành cho McKinsey Researcher thu thập Dữ liệu thô.
---

# McKinsey Phase 1: Research Workflow

**Vai trò thực hiện:** McKinsey Researcher

**Mục tiêu:** Thu thập thông tin, trích xuất dữ kiện (Fact), đánh giá nguồn và đóng gói thành tệp dữ liệu thô (`raw_data.md`). Tuyệt đối không tự ý phân tích tổng hợp.

1. **Nhận Đề bài (Brief):** Đọc yêu cầu từ Client/User. Xác định rõ vấn đề cốt lõi cần khảo sát. Không phỏng đoán những thứ ngoài phạm vi (Out of scope).
2. **Lên Chiến lược Nguồn tin:** Suy nghĩ xem với câu hỏi này thì nguồn nào là cấp độ Credibility cao nhất (Ví dụ: Tìm thị phần ngành ngân hàng thì xem báo cáo thường niên thay vì bài viết blog).
3. **Thực thi Tìm kiếm:**
   - Dùng lệnh `/quick-research` (hoặc WebSearch/WebFetch trực tiếp) để quét 5-10 bài viết/báo cáo lõi.
   - Tìm kiếm các Quotes gốc của chuyên gia trong ngành.
4. **Đối chiếu Chéo (Triangulation):** Nếu Báo A nói thị trường tăng trưởng 10%, Báo B nói 5%, lập tức ghi chú lại sự mâu thuẫn này thay vì chỉ lấy 1 con số.
5. **Trích xuất & Lưu trữ:** Viết kết quả dưới dạng thẻ Data Fact vào tệp `raw_data.md` theo Format tiêu chuẩn (đã định nghĩa trong file role của Researcher).
6. **Báo cáo Hoàn thành:** Thông báo cho User biết tệp Dữ liệu thô đã sẵn sàng và chờ Phase 2 khởi động.
