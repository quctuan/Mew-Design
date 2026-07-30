---
description: Pipeline Xuyên Mạch - Kích hoạt tự động chuỗi UI/UX Audit (2 Phases + HITL)
---

# UI/UX Audit Master Workflow

**Mục tiêu:** Luồng gọi lệnh chóp bu (Master Command) tự động hóa gọi 2 Sub-agents (Team Soi Logic và Team Soi Giao diện) ra kiểm duyệt thiết kế tuần tự. Cả quá trình vận hành Human-in-the-Loop giữ chặt tiến độ.

1. **Khởi Trình:** Yêu cầu User đưa link dự án, hình ảnh, Figma hoặc Description.
// turbo-all
2. **Kích hoạt Phase 1 (Check Móng & Luồng):**
   - Đóng vai `UX Flow Auditor`.
   - Chạy workflow tại `/.agents/workflows/UIUX Audit/audit_uiux_phase1_flow.md`.
   - Báo hiệu: `[HITL 1] Mời Boss duyệt tệp ux_findings.md`. (Dừng chờ lệnh Approve).
3. **Kích hoạt Phase 2 (Check Sơn & Nội thất):**
   - Đóng vai `UI Visual Auditor`.
   - Kế thừa lại thông tin, chạy workflow tại `/.agents/workflows/UIUX Audit/audit_uiux_phase2_visual.md`.
   - Báo hiệu: `[HITL 2] Mời Boss duyệt tệp ui_findings.md`. (Dừng chờ lệnh Approve).
4. **Gom Báo Cáo:**
   - Khi Boss Ok, hệ thống tự động gom cả `ux_findings.md` và `ui_findings.md` lại trộn thành Siêu văn bản `Final_Audit_Report.md`. Đây là file cuối cho Dev và Designer mang về xử lý (Fix bugs).
