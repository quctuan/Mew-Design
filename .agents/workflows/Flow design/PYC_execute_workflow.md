---
description: Pipeline Xuyên Mạch - Xử lý Yêu cầu Cải tiến (PYC) từ Jira đến khi ra bản thiết kế Spec cuối cùng (6 Bước + HITL)
---

# Quy trình Xử lý Yêu cầu Cải tiến (PYC Workflow)

Quy trình này tự động hóa việc phân tích yêu cầu từ Jira, tạo bản Research cốt lõi, lên chiến lược giải pháp và xuất ra thiết kế UX Flow & Spec cuối cùng.
Quy trình yêu cầu sự giám sát và phê duyệt của con người (HITL - Human In The Loop) ở các điểm chạm quan trọng để đảm bảo chất lượng đầu ra.

## Bước 1: Kích hoạt & Trích xuất Dữ liệu (Trigger & Fetch)
1. **Input:** Người dùng cung cấp một link Jira Task (Ví dụ: `https://cntt.vnpt.vn/browse/IT360-1585542`).
2. **Action 1 (Kéo Dữ liệu):** Gọi Agent `@Jira Operations Bot` (`jira_operations_bot.md`).
3. **Task 1.1:** Bot sử dụng kỹ năng `/jira_fetch` kết hợp với **Personal Access Token (PAT)** đã cấu hình trong biến môi trường hệ thống để gọi API trực tiếp vào Jira VNPT.
4. **Task 1.2:** Bot trích xuất trường `Description` và nội dung văn bản (Text) từ các `Attachment` mới nhất của Task đó, xuất ra raw data (Dữ liệu thô).
5. **Action 2 (Phân tích Logic):** Bàn giao raw data cho Agent `@Jira Logic Analyst` (`jira_logic_analyst.md`).
6. **Task 2.1:** Logic Analyst sử dụng kỹ năng `/jira_classify` (`jira_classification_rules.md`) để đọc hiểu và phân loại dữ liệu gốc.
7. **Output:** Dữ liệu sau khi dọn dẹp và phân loại được gọi là **Master Input** để chuyển sang Bước 2.

## Bước 2: Phân tích Thấu cảm (Empathy Analysis)
1. **Action:** Chuyển Master Input cho Agent `@PG-UX Researcher` (`pg_ux_researcher.md`).
2. **Task 2.1:** Kích hoạt kỹ năng `/ethnographic-research` để xác định Bối cảnh thực tế (When/Where), Trạng thái cảm xúc (Emotional State), và Cách người dùng đang làm thủ công (Current Workaround). **Bắt buộc phải tìm ra "Nỗi đau" (Pain Point).**
3. **Task 2.2:** Kích hoạt kỹ năng `/jtbd-analysis` để viết các câu Jobs-to-be-Done cô đọng (Tối đa 3 câu).

## Bước 3: Kiểm định Chất lượng Dữ liệu (HITL - Data Quality Check)
1. **Condition:** Nếu `Master Input` ở Bước 1 quá ngắn, chung chung, hoặc thiếu ngữ cảnh để hoàn thành Bước 2 một cách có ý nghĩa:
2. **Action:** Agent TẠM DỪNG quy trình. Đặt câu hỏi cụ thể cho Người Dùng (Boss) để yêu cầu bổ sung thông tin.

## Bước 4: Khởi tạo Insight & Phê duyệt (Insight Generation - HITL 1)
1. **Action:** `@PG-UX Researcher` tổng hợp kết quả Bước 2.
2. **Output Formatting:**
   - Tạo một file MỚI trong thư mục `research` của Knowledge Base.
   - **Tên file:** `RS[index]_[Mã Task Jira]_[Tên Task đục lỗ].md` (Ví dụ: `RS01_[IT360-1587543]_Yeu_cau_bo_sung_chuc_nang.md`).
   - **Nội dung:** Bắt buộc bao gồm Tóm tắt yêu cầu từ Jira, kết quả Ethnographic và JTBD.
3. **Review:** Dừng lại chờ Người Dùng (Boss) phê duyệt file **Đạt** (Proceed) mới đi tiếp.

## Bước 5: Lên Thiết kế Chiến lược & Phê duyệt (Strategy Generation - HITL 2)
1. **Action:** Sau khi được phê duyệt ở Bước 4, tự động gọi Agent `@Empathy Strategist` (`empathy_strategist.md`).
2. **Task:** Đọc file `RSxx...md` vừa tạo, kích hoạt kỹ năng `/goosebumps-validation`.
3. **Output Formatting:** **Ghi đè/Bổ sung (Append)** "Ý tưởng Giải pháp" (Vế Logic & Vế Emotion) trực tiếp vào *CUỐI* file `RSxx...md` đó. Tuyệt đối không tạo file mới.
4. **Review:** Dừng lại chờ Người Dùng duyệt (HITL) ý tưởng chiến lược này.

## Bước 6: Chế tác Flow & Specs (Design & Spec Generation)
1. **Action 1:** Sau khi chiến lược được duyệt, tự động gọi Agent `@UX Designer & Writer` (`ux_designer_writer.md`).
2. **Task 6.1:** Áp dụng kỹ năng `/mermaid-optimization` để vẽ sơ đồ luồng UX (UX Flow).
3. **Task 6.2:** Áp dụng kỹ năng `/ux-writing-tone` để viết bảng UI Copywriting và Edge Cases.
4. **Output Formatting:** 
   - Tạo một file MỚI dựa trên `ux_spec_template.md`.
   - Lưu vào thư mục `specs` của Knowledge Base.
   - **Tên file:** `URD[index]_[Mã Task Jira]_[Tên Task đục lỗ].md` (Ví dụ: `URD01_IT360-1587543_Yeu_cau_bo_sung_chuc_nang.md`).

---
*(Quy trình Kết thúc tại đây, toàn bộ Tài nguyên của 1 Task được lưu trữ gọn gàng trong 1 file `RS..` và 1 file `URD..`)*
