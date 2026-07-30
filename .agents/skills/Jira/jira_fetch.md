---
name: jira_fetch
description: Kỹ năng móc nối (Fetch) dữ liệu đầu vào (Input) từ hệ thống Jira nội bộ thông qua API.
---

# Jira Fetch API Skill

Kỹ năng chuyên biệt dành cho Operations Bot đọc và trích xuất dữ liệu rác (Raw Data) từ board Jira của nhóm. 

## Nguyên tắc Vận hành:
- Kéo danh sách Task thông qua câu lệnh bộ lọc (JQL).
- **Chỉ lấy dữ liệu Cần thiết:** Status (Trạng thái), Assignee (Người được giao), Due Date (Hạn chót tính bằng Date), và Summary (Tiêu đề).
- **Tuyệt đối không:** Không suy đoán ý nghĩa dữ liệu. Nhiệm vụ chỉ là kéo Raw Data về dạng mảng (Array) hoặc JSON để chuyển giao cho Agent não bộ (Logic Analyst) đọc hiểu tiếp.
- Bỏ qua cảnh báo Tự cấp SSL (InsecureRequestWarning) nếu hệ thống nằm trong dải IP On-premise VNPT nội bộ.
