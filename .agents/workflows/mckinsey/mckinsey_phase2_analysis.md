---
description: Pipeline Phân tích - Dành cho McKinsey Analyst xử lý Dữ liệu thô thành Báo cáo.
---

# McKinsey Phase 2: Analysis Workflow

**Vai trò thực hiện:** McKinsey Analyst

**Mục tiêu:** Xử lý file `raw_data.md`, cấu trúc lại bằng Issue Tree, định lượng Market Sizing (nếu cần), suy ra Insight ("So what?") và xuất báo cáo kim tự tháp.

1. **Tiếp nhận Dữ liệu:** Đọc toàn bộ nội dung trong tệp `raw_data.md` do Phase 1 (Researcher) gửi lại. Chỉ dùng Data này, cấm tự ý tưởng tượng số liệu.
2. **Dựng Khung Cấu trúc:** Dùng kỹ năng `mece-structuring`. Chẻ vấn đề cốt lõi thành 3-4 nhánh MECE. Nhóm các Fact tương ứng từ `raw_data.md` vào dưới mỗi nhánh.
3. **Phân tích Định lượng:** Nếu đề bài có yếu tố tính toán doanh thu/độ lớn thị trường, kích hoạt kỹ năng `market-sizing`. Thực hiện đủ Top-Down và Bottom-Up, giải trình các giả định (Assumptions).
4. **Viết Báo cáo Kim tự tháp:** Áp dụng `pyramid-principle`. Bắt đầu soạn phần Executive Summary bằng việc gõ thẳng thông điệp chính/câu trả lời vào dòng đầu tiên. Các luận cứ chứng minh đi theo sau.
5. **Kiểm duyệt Độc lập (Self-QR):** Trước khi xuất file cuối cùng, tự đánh giá lại: Báo cáo có tính Actionable không? Số liệu có chắp vá không? Insight có sắc xảo không?
6. **Bàn giao:** Xuất tệp `final_report.md` và trình bày cho User.
