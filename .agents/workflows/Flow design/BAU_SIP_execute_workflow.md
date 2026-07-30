---
description: Quy trình Xuyên mạch BAU/SIP - Từ Khảo sát Định hướng đến Thiết kế Spec cuối cùng (6 Bước + HITL)
---

# Quy trình Xử lý Yêu cầu BAU/SIP (BAU/SIP Workflow)

Quy trình này tự động hóa việc tiếp nhận yêu cầu BAU/SIP (Business As Usual / Service Improvement Plan), từ việc đào sâu tìm hiểu yêu cầu gốc thông qua tương tác trực tiếp, nghiên cứu thị trường, nhận diện nỗi đau, định hình chiến lược cho đến khi xuất ra bản thiết kế UX Flow & Spec cuối cùng.
Quy trình yêu cầu sự giám sát và phê duyệt của con người (HITL - Human In The Loop) ở các điểm chạm quan trọng để đảm bảo chất lượng đầu ra.

## Bước 1: Tiền Nghiên Cứu & Chốt Đề Bài (Trigger)
1. **Action:** Hệ thống kích hoạt quy trình `/requirement_specify` (`requirement_specify.md`).
2. **Task:** Agent không yêu cầu một đoạn văn bản (text) từ đầu mà sẽ **chủ động đặt câu hỏi** với NGƯỜI DÙNG để khai thác bối cảnh, hiểu rõ User Painpoint, Business Goal, JTBD, v.v.
3. **Output:** Một "Đề bài UX Benchmark cuối cùng" súc tích và hoàn chỉnh.
4. **HITL:** Dừng lại chờ NGƯỜI DÙNG xác nhận chốt Đề bài. Đề bài này sẽ làm **Master Input** cho Bước 2 và Bước 3.

## Bước 2 & Bước 3: Đào sâu Phân tích (Thực thi Song song)
*Hai nhiệm vụ thực hiện Nghiên cứu thị trường và Phân tích thấu cảm nội tại sẽ được các Agent tiến hành đồng thời (song song) để tối ưu hóa thời gian chạy.*

### Bước 2: Tìm kiếm & Phân tích Thị trường (UX Benchmark)
1. **Action:** Giao Master Input cho `UX Benchmarker` thực thi tiếp quy trình `/ux_benchmark_research` (`ux_benchmark_research.md`).
2. **Task:** Agent tự động tìm kiếm Web, trích xuất tính năng tương đương, screenshot, video, flow và các bài viết phân tích UI/UX từ thị trường.
3. **Output:** Một báo cáo UX Benchmark hoàn chỉnh lưu tại `Knowledge Base/research/UX_Benchmark/UXB_[ID]_[Tên_tính_năng].md`.

### Bước 3: Phân tích Thấu cảm (Empathy Analysis)
1. **Action:** Giao Master Input cho Agent `@PG-UX Researcher` (`pg_ux_researcher.md`).
2. **Task 3.1:** Kích hoạt kỹ năng `/ethnographic-research` để xác định Bối cảnh thực tế (When/Where), Trạng thái cảm xúc (Emotional State) và Cách người dùng đang làm thủ công (Current Workaround). **Bắt buộc phải tìm ra "Nỗi đau" (Pain Point).**
3. **Task 3.2:** Kích hoạt kỹ năng `/jtbd-analysis` để viết các câu Jobs-to-be-Done cô đọng (Tối đa 3 câu).
4. **Output:** Phân tích Ethnographic & JTBD chuyên sâu.

---
**[HITL Tổng hợp]**
Sau khi hệ thống hoàn thành CẢ Bước 2 và Bước 3, Agent dừng lại trình bày kết quả của cả hai mảng Nghiên cứu thị trường & Phân tích Thấu cảm để người dùng (Boss) phê duyệt (Approve) và chỉnh sửa nếu cần trước khi sang Bước 4.

## Bước 4: Khởi tạo Insight & Phê duyệt (Insight Generation - HITL 1)
1. **Action:** `@PG-UX Researcher` đối chiếu và kết hợp dữ liệu từ Master Input (Bước 1) và Kết quả Thấu cảm (Bước 3).
2. **Output Formatting:**
   - Tạo một file MỚI trong thư mục `research` của Knowledge Base.
   - **Tên file mặc định:** `BAU_SIP_Research_[index]_[Tên_tính_năng].md` (Ví dụ: `BAU_SIP_Research_001_Gamification_Center.md`). *(Ghi chú: Đổi dấu gạch chéo `/` trong cụm BAU/SIP thành dấu gạch dưới `_` để bảo toàn cấu trúc tệp hệ điều hành, tránh vô tình tạo ra thư mục BAU).*
   - **Nội dung:** Bắt buộc bao gồm Tóm tắt Đề bài (từ Bước 1), kết quả Ethnographic và JTBD (từ Bước 3).
3. **Review:** Dừng lại chờ Người Dùng (Boss) phê duyệt file **Đạt** (Proceed) mới đi tiếp.

## Bước 5: Lên Thiết kế Chiến lược & Phê duyệt (Strategy Generation - HITL 2)
1. **Action:** Sau khi được phê duyệt ở Bước 4, tự động gọi Agent `@Empathy Strategist` (`empathy_strategist.md`).
2. **Task:** Đọc file `BAU_SIP_Research_[index]...md` vừa tạo, kích hoạt kỹ năng `/goosebumps-validation`.
3. **Output Formatting:** **Ghi đè/Bổ sung (Append)** "Ý tưởng Giải pháp" (Vế Logic & Vế Emotion) trực tiếp vào *CUỐI* file `BAU_SIP_Research_[index]...md` đó. Tuyệt đối không tạo file mới.
4. **Review:** Dừng lại chờ Người Dùng duyệt (HITL) ý tưởng chiến lược.

## Bước 6: Chế tác Flow & Specs (Design & Spec Generation)
1. **Action 1:** Sau khi chiến lược được duyệt, tự động gọi Agent `@UX Designer & Writer` (`ux_designer_writer.md`).
2. **Task 6.1 (Tham chiếu UX Benchmark):** Đọc kỹ hồ sơ Phân tích thị trường `UXB_[ID]...md` từ **Bước 2** để tìm cảm hứng, đánh giá mức độ khả thi và chắt lọc các ưu/nhược điểm có thể áp dụng vào Flow hiện tại.
3. **Task 6.2:** Áp dụng kỹ năng `/mermaid-optimization` để vẽ sơ đồ luồng UX (UX Flow).
4. **Task 6.3:** Áp dụng kỹ năng `/ux-writing-tone` để viết bảng UI Copywriting và Edge Cases.
5. **Output Formatting:** 
   - Tạo một file MỚI vào thư mục `specs` của Knowledge Base.
   - **Tên file:** `BAU_SIP_Spec_[index]_[Tên_tính_năng].md` (Ví dụ: `BAU_SIP_Spec_001_Gamification_Center.md`).
   - **Yêu cầu bắt buộc Content:** Trong file Spec này **PHẢI** đính kèm đường link Markdown tới file Benchmark `UXB...md` để lấy dẫn chứng minh họa trực quan cho các quyết định lập sơ đồ Flow và tham chiếu UI cho Team lập trình/thiết kế UI.

---
*(Quy trình Kết thúc tại đây, toàn bộ Tài nguyên của 1 Yêu cầu được lưu trữ chuẩn hóa thành 1 file báo cáo Research Insight và 1 file Spec thiết kế)*
