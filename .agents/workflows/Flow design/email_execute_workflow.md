---
description: Pipeline Xuyên Mạch - Xử lý Yêu cầu Cải tiến từ nguồn Input là Link Email (6 Bước + HITL)
---

# Quy trình Xử lý Yêu cầu Cải tiến từ Email (Email PYC Workflow)

Quy trình này tự động hóa việc phân tích yêu cầu từ một liên kết (Link) Email nội bộ hoặc khách hàng, tạo bản Research cốt lõi, lên chiến lược giải pháp và xuất ra thiết kế UX Flow & Spec cuối cùng.
Quy trình yêu cầu sự giám sát và phê duyệt của con người (HITL - Human In The Loop) ở các điểm chạm quan trọng để đảm bảo chất lượng đầu ra.

## Bước 1: Kích hoạt & Hỏi đáp Dữ liệu (Trigger & Interactive Fetch)
1. **Action:** Gọi Agent `@Email Requirements Analyst` để bắt đầu quy trình thu thập dữ liệu (HITL).
2. **Task 1.1 (Lấy Nội dung Email):** Agent chủ động đặt **Câu hỏi 1** cho Boss: *"Vui lòng cung cấp nội dung text của Email"*. Dừng lại chờ Boss phản hồi.
3. **Task 1.2 (Lấy File Đính kèm):** Sau khi nhận được thông tin câu 1, Agent tiếp tục đặt **Câu hỏi 2**: *"Vui lòng cung cấp nội dung hoặc tải lên các tài liệu đính kèm (Nếu không có, vui lòng phản hồi 'Bỏ qua')"*. Dừng lại chờ Boss phản hồi.
4. **Task 1.3 (Tổng hợp):** Khi đã thu thập đủ 2 luồng thông tin, Agent sử dụng kỹ năng `/email_parsing_rules` để đọc hiểu bối cảnh cốt lõi, loại bỏ các đoạn hội thoại rác và trích xuất thông tin từ tài liệu đính kèm.
5. **Output:** Dữ liệu này được gộp lại thành **Master Input** để chuyển sang Bước 2.

## Bước 2: Phân tích Thấu cảm (Empathy Analysis)
1. **Action:** Chuyển Master Input cho Agent `@PG-UX Researcher` (`pg_ux_researcher.md`).
2. **Task 2.1:** Kích hoạt kỹ năng `/ethnographic-research` để xác định Bối cảnh thực tế (When/Where), Trạng thái cảm xúc (Emotional State), và Cách người dùng đang làm thủ công (Current Workaround). **Bắt buộc phải tìm ra "Nỗi đau" (Pain Point).**
3. **Task 2.2:** Kích hoạt kỹ năng `/jtbd-analysis` để viết các câu Jobs-to-be-Done cô đọng (Tối đa 3 câu).

## Bước 3: Kiểm định Chất lượng Dữ liệu (HITL - Data Quality Check)
1. **Condition:** Nếu `Master Input` ở Bước 1 quá ngắn, chung chung, hoặc thiếu ngữ cảnh từ Email để hoàn thành Bước 2 một cách có ý nghĩa:
2. **Action:** Agent TẠM DỪNG quy trình. Đặt câu hỏi cụ thể cho Boss để yêu cầu bổ sung thông tin (hoặc tải trực tiếp file đính kèm nếu link bị lỗi).

## Bước 4: Khởi tạo Insight & Phê duyệt (Insight Generation - HITL 1)
1. **Action:** `@PG-UX Researcher` tổng hợp kết quả Bước 2.
2. **Output Formatting:**
   - Tạo một file MỚI trong thư mục `research` của Knowledge Base.
   - **Tên file:** `RS[index]_[Tiêu đề Email rút gọn].md`.
   - **Nội dung:** Bắt buộc bao gồm Tóm tắt yêu cầu từ Email, kết quả Ethnographic và JTBD.
3. **Review:** Dừng lại chờ Người Dùng (Boss) phê duyệt file **Đạt** (Proceed) mới đi tiếp.

## Bước 5: Lên Thiết kế Chiến lược & Phê duyệt (Strategy Generation - HITL 2)
1. **Action:** Sau khi được phê duyệt ở Bước 4, tự động gọi Agent `@Empathy Strategist` (`empathy_strategist.md`).
2. **Task:** Đọc file `RSxx...md` vừa tạo, kích hoạt kỹ năng `/goosebumps-validation`.
3. **Output Formatting:** **Ghi đè/Bổ sung (Append)** "Ý tưởng Giải pháp" (Vế Logic & Vế Emotion) trực tiếp vào *CUỐI* file `RSxx...md` đó. Tuyệt đối không tạo file mới.
4. **Review:** Dừng lại chờ Boss duyệt (HITL) ý tưởng chiến lược này.

## Bước 6: Chế tác Flow & Specs (Design & Spec Generation)
1. **Action:** Sau khi chiến lược được duyệt, tự động gọi Agent `@UX Designer & Writer` (`ux_designer_writer.md`).
2. **Task 6.1:** Áp dụng kỹ năng `/mermaid-optimization` để vẽ sơ đồ luồng UX (UX Flow).
3. **Task 6.2:** Áp dụng kỹ năng `/ux-writing-tone` để viết bảng UI Copywriting và Edge Cases.
4. **Output Formatting:** 
   - Tạo một file MỚI dựa trên `ux_spec_template.md`.
   - Lưu vào thư mục `specs` của Knowledge Base.
   - **Tên file:** `URD[index]_[Tiêu đề Email rút gọn].md`.

---
*(Quy trình Kết thúc tại đây, toàn bộ Tài nguyên của 1 Task được lưu trữ gọn gàng trong 1 file `RS..` và 1 file `URD..`)*
