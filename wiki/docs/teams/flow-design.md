# 🎨 Hướng Dẫn Vận Hành Đội Ngũ Flow Design & UX

Tài liệu này giải thích cách thức hoạt động của đội ngũ AI chuyên trách việc nghiên cứu trải nghiệm người dùng, xây dựng chiến lược thấu cảm và thiết kế luồng (UX/UI Flow).

---

## 1. 👥 Các Thành Viên Khung (AI Agents)

Đội ngũ Flow Design bao gồm ba vai trò chính, hoạt động tiếp nối nhau tạo thành một phễu ý tưởng:

**🕵️‍♂️ PG-UX Researcher (`roles/Flow design/pg_ux_researcher.md`):**
- **Vai trò:** Người tìm kiếm Thấu cảm.
- **Nhiệm vụ:** Thấu hiểu bối cảnh người dùng, định hình "khoảnh khắc đáng giá" (moments that matter) thông qua phương pháp Jobs-to-be-Done (JTBD).
- **Đầu vào:** Nhận yêu cầu từ Jira (Quy trình cải tiến PYC) hoặc tài liệu PRD (Quy trình tính năng mới).
- **Đầu ra:** File Research Insight chứa Nỗi đau (Pain Point) và phân tích JTBD.

**🧠 Empathy Strategist (`roles/Flow design/empathy_strategist.md`):**
- **Vai trò:** Chiến lược gia Thấu cảm.
- **Nhiệm vụ:** Đọc các Insight từ Researcher, chắp nối nỗi đau với giải pháp một cách "Có tình Người". Đóng vai trò gác cổng chất lượng (Quality Reviewer).
- **Đầu ra:** File Empathy Strategy Blueprint chứa the Idea (ý tưởng lõi) đáp ứng cả hai khía cạnh: Logic và Cảm xúc, vượt qua bài kiểm tra "Goosebumps Validation" (Độ nổi da gà).

**✍️ UX Designer & Writer (`roles/Flow design/ux_designer_writer.md`):**
- **Vai trò:** Nghệ nhân Chế tác.
- **Nhiệm vụ:** Lấy "Ý tưởng lớn" từ Strategist và chuyển hóa nó thành Flow logic, thông số kỹ thuật (Tech Specs) và nội dung Copywriting mượt mà. Đảm bảo xử lý các Edge Cases (luồng ngoại lệ).
- **Đầu ra:** Các file `ux_flow_mermaid` và `ui_copywriting_specs` sẵn sàng bàn giao cho đội Dev.

---

## 2. 🚀 Các Quy Trình Vận Hành (Workflows)

Hệ thống cung cấp các Workflow tương ứng với từng giai đoạn hình thành sản phẩm:

### 💡 `create_workflow_phase1_moments` 
- **Mục đích:** Khảo sát Hành vi Gốc rễ & Nỗi đau Cảm xúc.
- **Cách làm:** Kích hoạt vai trò PG-UX Researcher tìm kiếm Insight và định hình JTBD.

### 🎯 `create_workflow_phase2_strategy`
- **Mục đích:** Định hình Ý tưởng Giải pháp & Lọc Cảm xúc.
- **Cách làm:** Kích hoạt Empathy Strategist sáng tạo chiến lược dựa trên Insight từ Phase 1.

### 📐 `create_workflow_phase3_spec_design`
- **Mục đích:** Thiết kế UX Flow và Spec Giao diện.
- **Cách làm:** Giao việc cho UX Designer & Writer để hệ thống hóa ý tưởng thành bản thiết kế chi tiết.

### 🎁 Master Workflow (`create_workflow_master`)
- Đây là chuỗi Super UX Pipeline tự động nối tiếp 3 giai đoạn trên (Moments -> Strategy -> Specs Design). 
- Gọi lệnh `/create_workflow_master` để AI tự động chạy luồng xuyên suốt, có điểm dừng chờ User duyệt (HITL - Human in the Loop) ở giữa các bước quan trọng.
