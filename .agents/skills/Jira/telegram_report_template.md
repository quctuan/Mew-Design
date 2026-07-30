# Telegram Report Template (Recap)

File này chứa cấu trúc (Format) mặc định của một tin nhắn Báo cáo (Recap) sẽ được gửi lên nhóm Telegram. Bạn có thể tự do chỉnh sửa tiêu đề, emoji, hoặc câu chữ dưới đây. `Jira Logic Analyst` sẽ copy y hệt khung này để điền số liệu vào.

---
**[KHUNG TEMPLATE]**

🚀 **[TIÊU ĐỀ: BÁO CÁO CÔNG VIỆC {TÊN_NHÓM_INDEX} (PYC hoặc Support)]**

Thân gửi Team, báo cáo tiến độ các hạng mục {TÊN_NHÓM_INDEX} hiện tại như sau:

**1. 🗂 Trạng thái Tổng Quan (Đang thụ lý)**
- Tổng số Task đang mở: `{Tổng_Số}`
- Phân bổ theo Nhóm Nghiệp vụ (Bước 2):
  - 📱 Di động: `{Số}` tasks
  - 🌐 Băng rộng cố định: `{Số}` tasks
  - 💳 Thanh toán: `{Số}` tasks
  - 📦 Khác: `{Số}` tasks

- Phân bổ theo Assignee: 
  - {Tên_Assignee_1}: `{Số}` tasks
  - {Tên_Assignee_2}: `{Số}` tasks

**2. 🚨 Báo Động Đỏ (Gần Deadline < 7 ngày)**
*(Quy tắc: Liệt kê các task sắp hạn chót. Nếu không có thì ghi: "Trống / Mọi thứ an toàn")*
- `[{ID_Task}]` {Tên_Tóm_Tắt_Task} - Phụ trách: {Assignee} - *Due: {Số} ngày nữa*

**3. 🆕 Nhiệm Vụ Mới Nhận (< 24H)**
*(Quy tắc: Task vừa được gán. Nếu không có thì ghi: "Chưa có task mới phát sinh")*
- `[{ID_Task}]` {Tên_Tóm_Tắt_Task} - Phụ trách: {Assignee}

---
*(Cầu xin Hà và Mai để ý để ko bị VNP spam nhé :D)*
