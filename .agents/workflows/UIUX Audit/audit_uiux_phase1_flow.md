---
description: Phân tích Cấu trúc Luồng & Cognitive Load (Phase 1/2)
---

# UI/UX Audit Phase 1: Logic & Flow Workflow

**Vai trò thực hiện:** UX Flow Auditor

**Mục tiêu:** Xác định đúng gốc rễ công việc (JTBD), tự bước vào trong luồng để tìm điểm kẹt nhận thức và đánh giá Missing Edge Cases.

1. **Nhận Scope:** Mở file thiết kế hoặc yêu cầu luồng.
2. **Khảo sát Nguồn tin:** 
   - Đặt câu hỏi `JTBD-analysis` cho tính năng hiện tại. Phải qua được bài test "Người dùng đạt được mục tiêu" không.
   - Thử `cognitive-walkthrough` qua các màn hình, chọc ngoáy vào nút bấm "What if" để xem Cognitive Load mức nào.
3. **Quét Rẽ nhánh:** Lôi bộ `edge-case-analysis` để xem thiếu Empty State/Error Form nào không.
4. **Viết Báo cáo Logic:** Xuất file trung gian định dạng Markdown `ux_findings.md`. Trong đó nêu rõ Lỗi (Severity) và Hướng xử lý.
5. **🛑 CHỜ PHÊ DUYỆT (HITL 1):** Tạm ngưng toàn bộ quá trình. Trình cho Boss bản `ux_findings.md`. Nếu Boss gõ `Approved` / `Duyệt` thì hệ thống mới cho phép đi qua Phase 2.
