---
description: Master Pipeline - Kích hoạt tự động chuỗi McKinsey 2-Subagent Architecture.
---

# McKinsey Master Workflow

**Mục tiêu:** Workflow tự động hóa toàn bộ quy trình từ yêu cầu ban đầu cho đến báo cáo tư vấn chuyên sâu, thông qua việc điều phối tuần tự 2 Agent (Researcher và Analyst).

1. **Lấy đầu bài:** Yêu cầu User cung cấp thông tin bài toán/thị trường cần khảo sát.
// turbo-all
2. **Khởi động Phase 1 (Researcher):** 
   - Kích hoạt Role McKinsey Researcher.
   - Yêu cầu Agent này chạy file `/.agents/workflows/mckinsey/mckinsey_phase1_research.md`.
   - Kết quả bắt buộc: Agent này tự động tạo ra file `workspace/engagements/raw_data.md` (đường dẫn tuỳ theo ngữ cảnh dự án) và gửi thông báo hoàn tất.
3. **Nghiệm thu trung gian:** Tạm dừng một chút để User có quyền ngó qua tệp `raw_data.md`. Nếu User không phản hồi gì, tự động sang bước tiếp theo.
4. **Khởi động Phase 2 (Analyst):**
   - Kích hoạt Role McKinsey Analyst.
   - Yêu cầu Agent này đọc tệp `raw_data.md` vừa sinh ra và chạy file `/.agents/workflows/mckinsey/mckinsey_phase2_analysis.md`.
   - Kết quả bắt buộc: Trả về bản Báo cáo Chiến lược Kim tự tháp hoàn chỉnh (Final Report).
5. **Thuyết trình:** Agent tương tác với User để tóm tắt 3 kết luận (Actionable items) chắt lọc nhất từ Final Report.
