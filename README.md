# 🚀 Chào mừng đến với Workspace GDS-MyVNPT (Agentic AI Workspace)

Chào mừng bạn gia nhập dự án! Đây là một **Không gian làm việc kết hợp Trí tuệ Nhân tạo (Agentic AI Workspace)**, nơi bạn sẽ làm việc cùng trợ lý Antigravity được "trang bị vũ khí" là các quy trình làm việc chuyên nghiệp (Team Frameworks) để giải quyết bài toán từ nghiên cứu, thiết kế đến lập trình phần mềm.

Tài liệu này sẽ hướng dẫn bạn – những thành viên mới – cách tương tác và khai thác tối đa sức mạnh của Antigravity trong dự án này.

---

## 🏗️ 1. Khái Niệm Cốt Lõi: Nhập Vai Tuần Tự (Sequential Role-Playing)

Trong workspace này, chúng ta sử dụng cơ chế **"Một Siêu Đặc Vụ Đội Nhiều Mũ"**.
Thay vì phải dùng các phần mềm phức tạp hay dòng lệnh (Terminal) để mở nhiều màn hình cho nhiều AI chat với nhau, trợ lý Antigravity của bạn có khả năng **Tự động thay đổi vai trò** (Nhập vai tuần tự) để xử lý một bài toán lớn từ đầu đến cuối một cách mượt mà và tập trung.

Antigravity sẽ tự động đọc các "Sổ tay nhân viên" (Role Prompts) của từng bộ phận. Ví dụ: Khi thiết kế tính năng, nó sẽ đóng vai Quản lý (PM) để lập kế hoạch -> Đổi mũ thành UX Designer để vẽ vòng đời sử dụng -> Đổi mũ thành UI Designer để vẽ giao diện -> Cuối cùng đóng vai Quality Reviewer (QR) để tự chấm điểm chéo chính bản vẽ của mình trước khi giao nộp!

---

## 👥 2. Các Đội/Quy Trình (Team Templates) Có Sẵn

Tùy vào tính chất công việc, bạn có thể yêu cầu Antigravity nhập vai và sử dụng chuẩn mực làm việc của một trong các Team sau. Dưới đây là danh sách, vai trò các thành viên và quy trình phối hợp của từng team:

### ✏️ 2.1. Thiết Kế Sản Phẩm (UX/UI Design)
- **Tên team:** `ux-design-team`
- **Mục tiêu:** Phân tích nhu cầu ẩn sâu (Jobs-to-be-done), vẽ luồng người dùng (User Flows), và viết thông số thiết kế (Full-stack Specs) theo chuẩn Design Thinking.
- **Danh sách Vai trò:**
  - **PM (Project Manager):** Quản lý tiến độ, cập nhật WHITEBOARD, và là cầu nối giao tiếp với Boss.
  - **UR (UX Researcher):** Thực hiện bước Empathize & Define. Phân tích JTBD, nghiên cứu đối thủ, xác định nỗi đau của user.
  - **UX (UX Designer):** Thực hiện bước Ideate. Vẽ sơ đồ luồng trải nghiệm (Flowcharts/Mermaid) dựa trên insight từ UR.
  - **TW (Technical Writer):** Viết kỹ thuật & UX Copywriting. Tạo các thông điệp thấu cảm và viết tài liệu Spec chi tiết.
  - **CR (Quality Reviewer):** Thực hiện bước Test. Đánh giá kiểm duyệt cuối cùng theo nguyên tắc MECE và JTBD để đảm bảo chất lượng.
- **Quy trình phối hợp:** Chạy tuần tự theo phương pháp Design Thinking: **PM (Nhận việc) -> UR (Nghiên cứu) -> UX (Thiết kế luồng) -> TW (Viết nội dung) -> CR (Kiểm duyệt) -> PM (Nghiệm thu)**. Mọi tài liệu (Output) của các thành viên phối hợp làm ra đều được đưa tập trung lưu trữ tại `knowledge base`.
- **💡 Mẫu Prompt Giao việc Chuẩn:**
  > *"Tôi cần thiết kế một luồng [Tên tính năng, VD: Đổi mật khẩu]. Hãy kích hoạt `ux-design-team` và lần lượt đóng vai PM -> UR -> UX -> TW -> CR để nghiên cứu JTBD, vẽ flow và viết Specs chuẩn. Nhớ hỏi ý kiến tôi ở mỗi bước đổi role!"*

### 🔍 2.2. Kiểm Định & Audit Trải Nghiệm (UI/UX Audit)
- **Tên team:** `uiux-audit-team`
- **Mục tiêu:** Thẩm định luồng logic, đánh giá Cognitive Load, truy quét Edge Cases, và sửa lỗi UX Writing.
- **Danh sách Vai trò:**
  - **LA (Lead Auditor):** Điều phối quá trình audit, phân công và tổng hợp các lỗi tìm được.
  - **UXE (UX Evaluator):** Đánh giá tính khả dụng (Usability), luồng đi và hành trình tương tác của người dùng.
  - **EC (Edge Case Hunter):** Chuyên tìm kiếm các "góc khuất", lỗi logic hiếm gặp, rủi ro luồng kỹ thuật.
  - **UIA (UI Analyst):** Đánh giá tính nhất quán của giao diện, hệ thống Design System, chuẩn Accessibility.
  - **UXW (UX Writer Auditor):** Rà soát câu chữ, thông báo lỗi, văn phong đàm thoại trên giao diện.
- **Quy trình phối hợp:** **LA (Tiếp nhận màn hình/luồng cần Audit) -> Chuyển giao cho UXE, EC, UIA, UXW (mỗi người "soi" một mảng chuyên môn) -> LA (Tổng hợp lại thành file Report cuối cùng)**.
- **💡 Mẫu Prompt Giao việc Chuẩn:**
  > *"Hãy dùng quy trình của `uiux-audit-team` để kiểm định link Figma sau: [Link Figma]. Các role hãy lướt qua màn hình, tìm ra rủi ro edge cases, tính khả dụng và văn phong. Cuối cùng, LA tổng hợp lại thành 1 file báo cáo Action Items đưa vào knowledge base."*

### � 2.3. Nghiên Cứu & Chiến Lược (McKinsey Research)
- **Tên team:** `mckinsey-research-team`
- **Mục tiêu:** Giải quyết bài toán chiến lược, phân tích thị trường theo chuẩn quy nạp Kim Tự Tháp của McKinsey.
- **Danh sách Vai trò:**
  - **EM (Engagement Manager):** Lập cấu trúc Issue Tree (Cây vấn đề), bóc tách giả thuyết.
  - **RL (Research Lead):** Dẫn dắt định hướng, phân mảnh nguồn thu thập dữ liệu.
  - **PR (Primary Researcher):** Tìm Insight qua dữ liệu sơ cấp (Mô phỏng phỏng vấn, khảo sát).
  - **SR (Secondary Researcher):** Quét dữ liệu thứ cấp (Báo cáo thị trường, bài báo, data có sẵn).
  - **DA (Data Analyst):** Xử lý số liệu, cấu trúc lại biểu bảng, đưa ra pattern.
  - **QR (Quality Reviewer):** Áp dụng MECE rà soát logic, "gọt giũa" thành báo cáo Executive Summary.
- **Quy trình phối hợp:** **EM (Chẻ vấn đề thành nhánh) -> Giao nhánh cho RL, PR, SR, DA đi đào sâu -> Thu thập kết quả ngược lên EM (Tổng luận) -> QR (Phản biện và chốt file Báo cáo chuẩn form McKinsey)**.
- **💡 Mẫu Prompt Giao việc Chuẩn:**
  > *"Doanh nghiệp đang gặp bài toán: [Trình bày bài toán kinh doanh]. Hãy kích hoạt `mckinsey-research-team`. Yêu cầu EM lập cây vấn đề (Issue Tree) MECE, các thành viên khác cùng đào sâu bằng dữ liệu và xuất báo cáo Executive Summary có tính hành động đưa cho tôi."*

### ❤️ 2.4. Nghiên cứu Khách Hàng (PG Insights)
- **Tên team:** `pg-insights-team`
- **Mục tiêu:** Tìm ra sợi dây liên kết cảm xúc giữa người dùng và sản phẩm (Consumer Insight "Goosebumps" - Nổi da gà).
- **Danh sách Vai trò & Quy trình:** Đội ngũ này dùng sức mạnh của các Framework phân tích tâm lý (Needs/Tensions) để bóc tách động cơ ngầm của con người, xây dựng chân dung Persona chuyên sâu trước khi bắt tay làm Branding hoặc Product Marketing. (Đội ngũ vận hành bằng cách thảo luận xoáy sâu vào Why - Why - Why).
- **💡 Mẫu Prompt Giao việc Chuẩn:**
  > *"Tôi đang muốn thiết kế một tính năng/Sản phẩm [Tên sản phẩm] cho App My VNPT. Hãy kích hoạt `pg-insights-team`. Nhập vai tuần tự theo công thức P&G: IM -> MR -> IA -> SL -> QR để giúp tôi tìm ra một Consumer Insight đắt giá và chiến lược thu hút khách hàng."*

### ⏰ 2.5. Thư Ký Quản Lý Tiến Độ (Jira Tracking)
- **Tên team:** `jira-tracking-team`
- **Mục tiêu:** Tự động hóa quá trình theo dõi tiến độ dự án. Trực tiếp kết nối vào API hệ thống Jira (On-premise), phân tích danh sách task đang mở và gửi báo cáo đều đặn mỗi ngày vào Group Telegram.
- **Danh sách Vai trò:** Đội ngũ này hiện thân thông qua 1 tập lệnh Python duy nhất (`jira_reporter.py`) đóng vai trò đan xen 3 kỹ năng:
  - **Scraper (Lấy dữ liệu):** Dùng Access Token chui vào hệ thống Jira móc dữ liệu nguyên bản (JSON).
  - **Analyst (Phân tích):** Bóc tách, làm sạch dữ liệu, loại bỏ những công việc đã Đóng, Hủy.
  - **Reporter (Báo cáo):** Đóng gói format thành bản tin đẹp mắt (HTML Format) và bắn thẳng vào Telegram có tag tên.
- **Quy trình phối hợp:** Chạy "không người lái" 100%. Không cần đổi mũ role phức tạp. Báo cáo sẽ được lên lịch gọi dậy bằng hệ thống Cronjob của thiết bị (Ví dụ: 8h30 sáng mỗi ngày).
- **💡 Mẫu Prompt Giao việc Chuẩn:**
  > *(Đây là team tự động chạy ngầm nên Boss không cần phải gõ Prompt giao việc hàng ngày. Nếu muốn team này **chạy đột xuất**, hãy tự mở Terminal và gõ lệnh sau: `/usr/bin/python3 "sample_team/jira-tracking-team/jira_reporter.py"`)*

---

## 🛠️ 3. Hướng Dẫn Sử Dụng (Dành Cho Thành Viên Mới)

Sử dụng môi trường Antigravity cực kỳ nhẹ nhàng, không cần cài đặt phần mềm bên thứ 3 (không Tmux) hay lo tốn RAM. Bạn chỉ cần làm theo các bước sau:

### Bước 1: Ra Lệnh & Giao Việc (Briefing)
Hãy gửi vào khung chat của Antigravity một Prompt (yêu cầu) mang tính "Giao quyền":
> *"Đây là bài toán: Thiết kế luồng Mua Gói Cước 4G trên MyVNPT. Tài liệu đầu vào tôi đã để ở `docs/xxx.md`.*
*Hãy sử dụng quy trình của `ux-design-team` để thực hiện nhiệm vụ này. Bạn hãy tự đọc các file trong `sample_team/ux-design-team/prompts`, nhập vai tuần tự từ PM -> UX -> UI -> UT -> QR để hoàn thành các tài liệu tương ứng."*

### Bước 2: Quan Sát Siêu Đặc Vụ (Antigravity) Làm Việc
- Lập tức, Antigravity sẽ hình thành một "Chuỗi tư duy". Nó sẽ dùng bộ công cụ của nó truy cập thư mục của team được gọi, đọc luật của từng vai trò và bắt tay vào tạo file.
- Bạn có thể thấy nó tạo file `Design_Brief.md`, sau đó lấy luôn nội dung file đó làm đầu vào để viết tiếp `JTBD_Map.md`... Y như một đội ngũ chuyên nghiệp nhưng tập trung tại 1 tiến trình máy tính duy nhất!
- Antigravity sẽ tuần tự báo cáo tiến độ với bạn và rà soát ý kiến.

### Bước 3: Đánh Giá & Feedbacks
Khi Antigravity ra bản nháp, nếu có chỗ chưa ưng ý, bạn phản hồi thẳng trong Chat:
> *"Sửa lại phần Màn hình 2 theo ý A, B, C giúp anh."*

*(💡 Lưu ý: Trợ lý Antigravity không chạy đa luồng ẩn dưới nền như các nền tảng khác. Khi nó thông báo làm xong việc, tự nó sẽ trả lại RAM cho máy, bạn cứ làm việc bình thường, không cần tìm gõ lệnh Kill Session hay Tắt Team).*

---

## 🔒 4. Quy Tắc Xuất Bản Lên Website / Wiki (Quan trọng)

**KHÔNG BẤT KỲ THÀNH VIÊN NÀO** (kể cả Agent AI) được phép tự động xuất bản (publish) hay đẩy cập nhật nội dung, tài liệu thẳng lên trên Website / Wiki của dự án đang chạy live.

- Mọi tài liệu dự định đưa lên Website / Wiki **BẮT BUỘC** phải được giữ lại ở file nháp (Draft) hoặc lưu cục bộ nội bộ tại thư mục `knowledge base`.
- Quá trình đăng tải/cập nhật lên Website **chỉ được tiến hành** khi đã được **Admin** (Boss/User) trực tiếp rà soát và cho phép phê duyệt (Approved).

---

## 📁 5. Cấu Trúc Thư Mục Quan Trọng Cần Biết

Là người mới, bạn không cần phải chạy file Terminal nào cả, nhưng bạn cần biết kho chứa quy trình/tài sản nằm ở đâu:

- `/sample_team`: Kho chứa các "Sổ tay nhập vai" (Prompts) của từng Team. Antigravity dùng các file Markdown trong thư mục `prompts` của mỗi Team để học hỏi tính cách chuyên gia. Xin đừng tự ý xóa thư mục này nhé.
- `/.agents/skills/SKILL.md`: Đây là "Sách Khải Huyền" của Antigravity. File này dạy cho Antigravity biết những Teams nào đang tồn tại.
- `/sample_team/.../WHITEBOARD.md`: Nếu dự án kéo dài nhiều ngày, Antigravity có thể sử dụng file Bảng Trắng này như một bảng lưu trữ công việc (Kanban) thay mặt bạn.

---

**Chúc bạn có những giờ phút điều phối Trợ lý AI thật hiệu quả và nhàn nhã!**
