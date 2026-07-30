# 🔍 Hướng Dẫn Vận Hành Đội Ngũ McKinsey Research

Tài liệu này giải thích cách thức hoạt động của đội ngũ AI chuyên trách việc nghiên cứu, thu thập dữ liệu và phân tích chiến lược theo tiêu chuẩn của McKinsey.

---

## 1. 👥 Các Thành Viên Khung (AI Agents)

Đội ngũ McKinsey Research bao gồm hai vai trò chính, hoạt động nối tiếp nhau:

**🕵️‍♂️ McKinsey Researcher (`roles/mckinsey/mckinsey_researcher.md`):**
- **Vai trò:** Chuyên gia tìm kiếm, thu thập, và đánh giá dữ liệu sơ cấp/thứ cấp.
- **Nhiệm vụ:** Lọc bỏ nhiễu, đối chiếu các nguồn độc lập, và cung cấp một tệp dữ kiện "Facts" trung thực, khách quan nhất làm nền tảng cho bước phân tích.
- **Đầu ra:** File Markdown chứa dữ liệu thô (Raw Data) ghi rõ Facts, Quotes và Source URL.

**🧠 McKinsey Analyst (`roles/mckinsey/mckinsey_analyst.md`):**
- **Vai trò:** Bộ não phân tích logic và lập báo cáo.
- **Nhiệm vụ:** Tiếp nhận dữ liệu báo cáo thô từ Researcher, thiết lập Issue Tree (MECE), thực hiện tính toán (Market Sizing), chắt lọc "So what?", và chắp bút viết Executive Summary theo chuẩn Pyramid Principle.
- **Đầu ra:** File Báo cáo Tư vấn (Consulting Report) sẵn sàng trình bày cho Client.

---

## 2. 🚀 Các Quy Trình Vận Hành (Workflows)

Hệ thống cung cấp các Workflow riêng biệt cho từng giai đoạn và một Master Workflow để điều phối chung:

### 🔎 `mckinsey_phase1_research` (Thu thập Dữ liệu)
- **Mục đích:** Dành cho Researcher thu thập dữ liệu thô dựa trên yêu cầu ban đầu.
- **Cách làm:** AI sẽ kích hoạt vai trò Researcher, tiến hành tìm kiếm thông tin, đánh giá độ tin cậy của nguồn và tổng hợp thành file Raw Data.

### 📊 `mckinsey_phase2_analysis` (Phân tích Báo cáo)
- **Mục đích:** Dành cho Analyst xử lý dữ liệu thô thành Báo cáo Tư vấn.
- **Cách làm:** Kênh đầu vào là file Raw Data từ Phase 1. Analyst sẽ ứng dụng các framework (MECE, Pyramid Principle) để phân tích, rút ra Insight và đưa ra đề xuất hành động.

### 🎁 Master Workflow (`mckinsey_master_workflow`)
- Nếu bạn muốn chạy toàn bộ luồng xuyên suốt từ lúc nhận yêu cầu đến khi ra báo cáo cuối cùng, hãy gọi lệnh `/mckinsey_master_workflow` trong khung chat AI. 
- AI sẽ tự động điều phối Researcher đi lấy dữ liệu, sau đó chuyển giao cho Analyst để hoàn thiện báo cáo phân tích đính kèm.
