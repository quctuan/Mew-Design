# GLOBAL WORKSPACE RULES

## OUTPUT RULE (Bắt buộc với tất cả các Team / Agents)
Từ nay, sản phẩm phân tích, file thiết kế, và tài liệu (Output) của TẤT CẢ CÁC AGENTS (UR, UX, TW, CR,...) trong mọi team (ux-design-team, scrum-team, pg-insights-team,...) KHÔNG được lưu ở thư mục cục bộ `docs/` của từng team nữa, mà **BẮT BUỘC** phải được lưu tập trung vào thư mục `knowledge base/` nằm ở thư mục gốc của dự án.

**Lưu ý quan trọng**: Các agent **tự chủ động phân loại và sắp xếp** linh hoạt cấu trúc thư mục bên trong `knowledge base/` sao cho hợp lý, khoa học, dễ tìm kiếm (ví dụ: chia theo tên dự án, tên team, loại tài liệu, feature,...). Không giới hạn một cấu trúc cứng nhắc nào.

*Các agent khi giao tiếp `tm-send` hoặc khi báo cáo lại với Boss cũng phải trỏ đường dẫn theo cấu trúc phân loại mới này.*

## SPECIFICATION TEMPLATE RULE (Quy Chuẩn Viết Spec & Đánh Index)
Từ nay về sau, khi Boss yêu cầu viết/làm Docs/Specs/URD cho bất kỳ tính năng nào, TẤT CẢ các Agent (như TW, PM, UR, BA...) đều **phải mô tả theo định dạng chuẩn "Full-stack Product Spec"** và **áp dụng quy tắc đánh Index bắt buộc**:

1. **Quy tắc đánh Index (Mã tài liệu)**:
   - Mỗi file Spec phải có một mã ID duy nhất theo format: `SPEC-[Số thứ tự 3 chữ số]`. Ví dụ: `SPEC-001`, `SPEC-002`,...
   - Tiêu đề (Heading 1) của file Spec phải được đặt theo chuẩn: `# [SPEC-XXX] Tên tính năng/Tài liệu`
   - Ngay dưới Heading 1, bắt buộc phải có khối Metadata (YAML frontmatter hoặc Markdown list) chứa các trường: `Mã Index`, `Phiên bản`, `Ngày cập nhật`, `Người làm/Owner`.

2. **Template chuẩn (Full-stack Product Spec)**:
   Bản Spec phải đạt tiêu chuẩn gồm đủ 5 mảng:
   - Bối cảnh & Mục tiêu (Business)
   - Trải nghiệm người dùng & Copy (UX/UI)
   - Quy trình Step-by-step
   - Đặc tả Nghiệp vụ & Rule hệ thống ngầm (Backend)
   - Vận hành & Testing

**Template gốc (File mẫu) nằm tại:** 
`knowledge base/templates/full-stack-spec-template.md`

(*Agent phải đọc file template này để lấy form điền thông tin khi được giao task viết tài liệu Specs*).

## CONTINUOUS APPROVAL RULE (Quy tắc Xác nhận Từng Bước)
Từ nay về sau, khi làm việc THEO CHUỖI ROLE (Ví dụ: chạy luồng PM -> UR -> UX -> TW), AI (Antigravity hoặc các Agents) **BẮT BUỘC KHÔNG ĐƯỢC TỰ Ý CHẠY MỘT MẠCH HẾT CÁC BƯỚC**.
Sau khi hoàn thành xong phần việc của *MỖI MỘT ROLE* (ví dụ: UR vừa làm xong báo cáo Research), AI phải **DỪNG LẠI và hỏi ý kiến (permission) của Boss**.
- **Nếu Boss yêu cầu chỉnh sửa:** Phải tiến hành sửa đổi, căn chỉnh tài liệu của Role hiện tại ngay lập tức cho đến khi Boss thực sự hài lòng.
- **Nếu Boss "Duyệt" hoặc "OK":** AI mới được phép thay mũ, chuyển qua đóng vai Role tiếp theo để làm tiến trình công việc kế tiếp.

## WEBSITE / WIKI UPDATE RULE (Quy tắc Kiểm duyệt Nội dung Website)
Từ nay, **KHÔNG BẤT KỲ AGENT, MEMBER NÀO** được phép tự động xuất bản (publish) hay đẩy cập nhật nội dung, tài liệu lên trên Website / Wiki của dự án chạy live.
- Mọi tài liệu dự định đưa lên Website / Wiki **BẮT BUỘC** phải được giữ lại ở file nháp (Draft) hoặc lưu cục bộ nội bộ tại `knowledge base`.
- Quá trình đăng tải/cập nhật lên Website **chỉ được tiến hành** khi đã được **Admin** (Boss/User) trực tiếp rà soát và cho phép phê duyệt (Approved).

## TONE & STYLE RULE (Quy tắc Văn phong)
Từ nay về sau, **TẤT CẢ** các tài liệu, nội dung, báo cáo và giao tiếp trong toàn dự án **BẮT BUỘC** phải tuân thủ nghiêm ngặt quy tắc văn phong sau:
- **Ngắn gọn, súc tích**: Trực tiếp vào vấn đề, không dài dòng, lan man. Sử dụng gạch đầu dòng và định dạng nhấn mạnh (bold, italic) để làm nổi bật từ khóa chính.
- **Phù hợp môi trường doanh nghiệp (Corporate/Professional Tone)**: Sử dụng ngôn từ chuyên nghiệp, lịch sự, khách quan và mang tính hành động (action-oriented). Hạn chế sử dụng từ ngữ cảm thán, văn nói, cách diễn đạt quá thông tục hoặc dịch thuật lủng củng.
