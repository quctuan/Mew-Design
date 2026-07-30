---
hide:
  - toc
---
# ⚙️ Nguyên Lý Làm Việc & Cách Vận Hành Workspace

Tài liệu này giải thích cơ chế cốt lõi của không gian làm việc này và cách bạn tương tác với trợ lý Agentic AI để khai phá sức mạnh tối ưu nhất.

## 🏗️ 1. Khái Niệm Cốt Lõi: Nhập Vai Tuần Tự (Sequential Role-Playing)

Trong workspace này, chúng ta sử dụng cơ chế **"Một Siêu Đặc Vụ Đội Nhiều Mũ"**. Tập hợp Agentic ở đây đóng vai trò như một Team ảo làm việc trên Máy Khách của bạn.

Thay vì phải dùng các cấu trúc hạ tầng phức tạp hay giao diện thiết lập nhiều màn hình cửa sổ (như Multi-agents qua Terminal/Tmux truyền thống), trợ lý Antigravity được trang bị khả năng **Tự động thay đổi vai trò** (Nhập vai tuần tự) để xử lý một tiến trình lớn từ đầu đến cuối một cách mượt mà nhất.

Antigravity sẽ tự động đọc các "Sổ tay nhân viên" (Role Prompts) của từng tổ đội (Teams) khai báo sẵn.
> **Ví dụ:** Khi bạn kích hoạt chế độ "ux-design-team", nó sẽ chủ động đóng vai *Quản lý (PM)* để lập kế hoạch -> Đổi mũ thành vòng *UX Researcher (UR)* để thực hiện nghiên cứu người dùng -> Tự đổi mũ sang *UX Designer* để vẽ sơ đồ luồng -> Cuối cùng nhập vai *Technical Writer (TW)* để tổng hợp tài liệu đặc tả (Specs) hoàn chỉnh.

Bạn sở hữu nguyên tổ chức nhân sự đầy đủ vòng chỉ trên đúng duy nhất 1 luồng chat AI!

---

## � 2. Danh Sách Các Đội Nhóm (Teams)

Dưới đây là giới thiệu về các đội ngũ Agentic AI sẵn sàng nhận nhiệm vụ. Tùy thuộc bài toán đang gặp, hãy chọn tổ đội phù hợp:

<div class="features-grid">
  <div class="feature-card">
    <div class="icon">✏️</div>
    <h3>UX Design Team</h3>
    <p>Phân tích Insight JTBD, vẽ luồng hành vi và lên Full-stack Specs.</p>
    <a href="../teams/ux-design/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">🔍</div>
    <h3>UI/UX Audit Team</h3>
    <p>Soi xét Cognitive Load, xử lý triệt để Edge Cases và kiểm định ngôn ngữ UI.</p>
    <a href="../teams/uiux-audit/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">📊</div>
    <h3>McKinsey Research Team</h3>
    <p>Nghiên cứu thị trường từ xa, phân tích cấu trúc bài toán và xuất báo cáo Action.</p>
    <a href="../teams/mckinsey-research/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">❤️</div>
    <h3>PG Insights Team</h3>
    <p>Nghiên cứu Tensions, đúc kết sợi dây liên kết cảm xúc đắt giá nhất của người dùng.</p>
    <a href="../teams/pg-insights/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">⏰</div>
    <h3>Jira Tracking Team</h3>
    <p>Tự động hoá tổng hợp thông tin Ticket và gửi báo cáo về Telegram.</p>
    <a href="../teams/jira-tracking/" class="md-button md-button--primary">Chi tiết</a>
  </div>
</div>

---

## �🛑 3. Nguyên Lý Kiểm Duyệt HITL (Human-in-the-Loop)

Trái với xu hướng hiện tại là ủy thác hoàn toàn cho AI từ đầu đến cuối, dễ dẫn đến hiện tượng "ảo giác" (Hallucination) và lỗi hệ thống khó kiểm soát, một số bộ tổ chức cốt lõi trong workspace này tuân thủ nguyên tắc **Kiểm duyệt chốt chặn tại mọi nút giao (Mandatory HITL)**:

- Khi một "nhân sự AI" hoàn thành xong 1 mốc công việc (Ví dụ: UR cày xong tài liệu gốc). Project Manager (PM) KHÔNG được tự ý chuyển giao nhiệm vụ cho bộ phận thiết kế UX khi chưa có sự phê duyệt.
- Tiến trình sẽ **tạm dừng (Pause)** hoàn toàn. Trợ lý sẽ đặt câu hỏi lên màn hình thông báo cho Quản trị viên (Admin/PO) để **Review (Phê duyệt)** tài liệu đó.
- Chỉ khi bạn xem qua, nếu phát hiện sai sót, bạn có thể đưa ra yêu cầu chỉnh sửa tức thời. Nếu kết quả đã đạt tiêu chuẩn, hãy nhập lệnh `>>> Approved` (Phê duyệt) và nhấn gửi. Lúc đó, hệ thống (PM) mới được phép điều hướng công việc cho nhân sự tiếp theo.

Điều này biến AI thành một "đội ngũ chuyên viên phác thảo tự động", còn quyền Lắp ráp, Đánh giá (Decision Making) vẫn phải thuộc về tư duy của Con người. Chất lượng đầu ra nhờ vậy mà sát cực độ với kỳ vọng nghiệp vụ.

---

## 🛠️ 4. Thao Tác Cơ Bản Điều Phối Các Tổ Đội

Bạn không cần bấm nhấp nháy chuyển tab phức tạp, các thao tác điều phối và quản lý đều được thực hiện thông qua một giao diện duy nhất:

### Bước 1: Giao Nhiệm Vụ Và Định Hướng (Briefing)
Hãy gửi vào khung chat màn hình nội dung Yêu cầu - Chỉ định Team phù hợp và thiết lập các mốc kiểm duyệt:
> *"Đây là bài toán: Thiết kế luồng Mua Gói Cước 4G trên MyVNPT. Tôi muốn tích hợp xác thực sinh trắc học và thanh toán nhanh.*
> *Hãy kích hoạt quy trình của `ux-design-team` để thực thi nhiệm vụ này. Bạn hãy lần lượt nhập vai qua tuần tự: PM -> UR -> UX -> TW -> CR. Vui lòng báo cáo và chờ phê duyệt ở từng giai đoạn chuyển giao."*

### Bước 2: Theo Dõi Tiến Trình Làm Việc Của Các Agent
- AI Antigravity sẽ vạch ra "Chuỗi tư duy" của nó trên màn hình. Hệ thống sẽ tự động quét quy định của tổ đội tương ứng, sau đó bắt đầu khởi tạo các tệp tài liệu, từ bản nháp (Draft) đến bản hoàn thiện (Final).
- Agent sẽ liên tục cập nhật trạng thái: "Báo cáo: Tôi đã hoàn thành luồng giao diện (UX Flow), vui lòng xem xét và phê duyệt file tài liệu..."

### Bước 3: Yêu Cầu Chỉnh Sửa Qua Vòng Lặp Phản Hồi (Feedback Loops)
Khi Antigravity đề xuất bản nháp, bạn đọc nhanh và cung cấp Feedback để hệ thống điều chỉnh:
> *"Hãy bổ sung bước xác minh Email vào màn hình xác thực (OTP) do quy trình hiện tại đang bị thiếu sót."*
> -> AI sẽ ngay lập tức cập nhật lại luồng thiết kế. Bạn duy trì các vòng lặp phản hồi này cho đến khi kết quả đạt chuẩn và dự án (Sprint) có thể khép lại.

---

## 📁 5. Cấu Trúc Thư Mục Cốt Lõi

- `/sample_team`: Kho lưu trữ hệ thống quy định và cấu hình nghiệp vụ chuyên môn (System/Role Prompts) chi tiết của các Team (Nghiên cứu thị trường, Thiết kế UIUX, Jira Tracking,...). Vui lòng **không tự ý thay đổi hoặc xóa bỏ các tệp tin trong khu vực này**.
- `/.agents/skills/SKILL.md`: Đây tệp tin cấu hình trọng yêú. Tài liệu chứa danh mục hệ sinh thái giúp Antigravity tra cứu kỹ năng, nhiệm vụ và vai trò nhanh chóng.
- `/knowledge base`: Kho tàng tri thức (Output Zone) dùng chung. Toàn bộ tài liệu thiết kế, thông số nghiên cứu, báo cáo Audit thành phẩm đều lưu tại đây để đồng bộ xuất bản.

---

## 🌐 6. Cập Nhật Tài Liệu Lên Website (Auto-Deploy)

Website (Wiki) nội bộ của dự án đã được tích hợp luồng Vercel CI/CD mở rộng tại máy chủ. **TUYỆT ĐỐI** AI không có quyền tự tiện đẩy code lên mạng nếu tài liệu chưa được Human (Boss) đồng ý xác minh.

Khi bạn muốn Cập nhật/Phát hành (Publish) phiên bản tài liệu mới nhất từ Kho `/knowledge base` trôi lên Website chính thức:

1. Bạn không cần tự gõ bất kỳ lệnh Code / Terminal Git phức tạp nào.
2. Vẫn tại giao diện Khung Chat AI hàng ngày, bạn gửi đúng 1 lệnh kích hoạt **Slash Command (Workflow)** sau cho nó:

   > `/deploy-website`

3. Trợ lý Antigravity sẽ đọc ngay workflow deploy, tiến hành dò tìm tài liệu nào vừa tạo, tự động đóng gói nội dung và Commit mã nguồn lên GitHub. Sau khoảng 20-30 giây, Vercel Cloud Server sẽ tự động nhận diện bản cập nhật và bài viết mới sẽ xuất hiện chính thức trên nền tảng Wiki Live!
