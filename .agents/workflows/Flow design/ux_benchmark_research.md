---
description: Tìm kiếm, phân tích và tổng hợp Báo cáo UX Benchmark (Phase 2/2)
---
# Workflow UX Benchmark Phase 2: Tìm kiếm & Đóng gói Báo cáo

**Mô tả:** Pipeline tự động hóa luồng tìm kiếm và tổng hợp tư liệu UI/UX dựa trên "Đề bài UX Benchmark cuối cùng" đã chốt ở Phase 1. Quy trình này đòi hỏi Agent tự động sử dụng Web Browser để tìm kiếm trên thị trường.

## Đầu vào (Input)
Bản **"Đề bài UX Benchmark cuối cùng"** đã được thống nhất và chốt hạ từ quy trình Phase 1 (`/requirement_specify`). Nếu chạy độc lập quy trình này, NGƯỜI DÙNG cần cung cấp trực tiếp bản Đề bài đã có đầy đủ bối cảnh (Painpoint, Goal, JTBD...).

## Bước 1: Tìm kiếm giải pháp và tính năng tương đương
1. **[System]** Kích hoạt Agent **`UX Benchmarker`** và nhắc Agent chắc chắn đã đọc nội dung Skill **`/web-benchmark`**.
2. **`UX Benchmarker`** tự động trích xuất các keyword chính từ "Đề bài UX Benchmark", sau đó chủ động **dịch sang tiếng Anh** để tối ưu phạm vi và chất lượng khi tìm kiếm trên Web.
3. **`UX Benchmarker`** sử dụng trình duyệt để duyệt web và tìm kiếm:
   - Các lý thuyết hoặc phương pháp đang được sử dụng để giải quyết vấn đề/painpoint đó.
   - Các tính năng / module trên các ứng dụng khác ứng dụng giải pháp tương đương (tìm kiếm rộng trên toàn bộ thị trường, không giới hạn lĩnh vực nào, miễn là giải quyết được vấn đề).

## Bước 2: Đào sâu tìm kiếm nguồn trải nghiệm UI/UX
Dựa trên dàn features / apps vừa tìm được, **`UX Benchmarker`** tiếp tục dùng quy tắc của Skill **`/web-benchmark`** để rẽ nhánh tìm kiếm thêm URL các tư liệu UI/UX.
1. Mục tiêu tìm kiếm bao phủ các nguồn sau:
   - **Articles / Reports:** Medium, UX Collective, NN/g, các case study step-by-step.
   - **Videos:** Link Youtube, Tiktok review hoặc demo tính năng (chỉ lấy URL, Title và Description/insight đi kèm).
   - **UI Flow / Visuals:** Nguồn từ Mobbin, Behance, Dribbble, UI8...
2. **Quy định số lượng:** Mỗi nhóm hạng mục (Bài viết / Video / UI Flow) cực kỳ cẩn thận thu thập **tối thiểu là 3** và **tối đa là 10** examples để đảm bảo danh sách vừa đủ độ đa dạng, không bị quá tải thông tin.

## Bước 3: Tổng hợp & Tạo tài liệu UX Benchmark
1. **`UX Benchmarker`** tổng hợp toàn bộ thông tin từ Bước 1 và Bước 2 thành file Markdown theo đúng định dạng được quy định trong Skill **`/web-benchmark`**.
2. Quy tắc đặt tên file: `UXB_[ID]_[Tên_tính_năng].md` (ví dụ `UXB_001_Dang_nhap_eSIM.md`). Nếu chưa có ID thì xin NGƯỜI DÙNG hoặc tự đánh số tiếp theo.
3. **Cấu trúc tài liệu (Format bắt buộc):**
   - **1. Mục tiêu:** Trình bày bối cảnh và mục tiêu (lấy từ bản Đề bài Bước 1).
   - **2. Giải pháp tham khảo trên thị trường:** Thông tin các logic/cách giải quyết từ Bước 1 tìm kiếm.
   - **3. Phân tích Flow step-by-step:** Phác thảo luồng UX cơ bản tham khảo được.
   - **4. Links Video/UI tham khảo:** Danh sách URL được gom nhóm gọn gàng (kèm mô tả).
   - **5. Đề xuất/Key Takeaways cho hệ thống VNPT:** Những bài học rút ra, do & don't để áp dụng vào luồng sản phẩm hiện tại.
4. Lưu tài liệu bằng tool `write_to_file` vào đúng đường dẫn thư mục:
   - File Markdown: `/Users/Shared/Previously Relocated Items/Security/Documents/GDS-MyVNPT/knowledge base/research/UX_Benchmark/UXB_[ID]_[Tên_tính_năng].md`
5. **Xuất file HTML trình bày:**
   - Dựa trên nội dung bản Markdown vừa hoàn thiện, tự động chuyển đổi sang định dạng HTML với CSS styling đẹp mắt (hỗ trợ hiển thị rõ ràng heading, bullet list, in đậm, hình ảnh, link, v.v.).
   - Lưu thành file HTML có cùng tên `UXB_[ID]_[Tên_tính_năng].html` tại cùng thư mục `UX_Benchmark` để phục vụ việc trình bày cho teammate xem trực tiếp trên trình duyệt.
