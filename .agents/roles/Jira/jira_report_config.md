# Jira Report Configuration (Config)

File này chứa cấu hình tham số mặc định cho Jira Operations Bot và Jira Logic Analyst khi thực thi luồng tổng hợp Recap. **Người dùng (User) có thể tự do thêm hoặc sửa các giá trị tại đây.**

## 1. Màng lọc ban đầu (Filter)
- **Assignees:** 
  - An Vũ Nhật Minh
  - Hồ Phạm Quỳnh Mai
  - Nguyễn Việt Hà
*(Luật: Cứ không thuộc 1 trong 3 người này thì loại bỏ).*

- **Exclude Statuses (Loại trừ trạng thái):** 
  - Đóng yêu cầu (Closed / Done)
  - Đã xử lý (Resolved)

## 2. Tiêu chí thời gian (Time Metrics)
- **Nhiệm vụ Sắp hết hạn (Deadline Alert):** `Due date < 7 ngày` tính từ thời điểm chạy báo cáo.
- **Nhiệm vụ Mới nhận (New Assignment):** Ngày tạo (Created) hoặc Ngày Assign `trong vòng 24 giờ` qua.

## 3. Cấu hình Telegram (Thông tin kết nối)
- **Token Bot:** `8757329276:AAG5zL8re4xprBhFPuJQ-yr0DS6FxUesWK4` (Mặc định)
- **Group Chat ID:** `-4580999681` (Tên Nhóm: PO-UIUX MyVNPT)
