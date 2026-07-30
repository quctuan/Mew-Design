---
name: risk_assessment
description: Kỹ năng phân bổ mức độ Rủi ro (Risk) dựa trên việc phân tích tương quan giữa Hạn chót (Due date) và Tiến độ (Status).
---

# Risk Assessment Skill

Năng lực lõi của Jira Logic Analyst. Agent có khả năng "Đánh mùi" rủi ro qua dữ liệu thời gian khô khan.

## Hệ quy chiếu Rủi ro:
1. **Critical (Đỏ):** Task đã quá hạn (Due date < Hôm nay) nhưng Status vẫn chưa "Closed/Done". 
   - *Hành động phân tích:* Cần đánh dấu khẩn cấp, nhắc thẳng tên người được gán (Assignee).
2. **Warning (Cam):** Task chưa quá hạn nhưng nằm im ở trạng thái "To Do" quá 5 ngày, hoặc hạn chót chỉ còn 1-2 ngày nữa.
   - *Hành động phân tích:* Cảnh báo nhẹ nhàng, hỏi thăm xem có bị Blocked (kẹt) phần nào không?
3. **Safe (Xanh):** Đang làm đúng tiến độ, status cập nhật liên tục. Không cần thao tác gì thêm, bỏ qua để làm sạch báo cáo.
