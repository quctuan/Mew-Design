# 🔍 Hướng Dẫn Vận Hành Đội Ngũ UI/UX Audit

Tài liệu này giải thích cách thức hoạt động của đội ngũ AI chuyên trách việc tự động kiểm định, phát hiện lỗi và đánh giá chất lượng sản phẩm về mặt trải nghiệm người dùng (UX) và giao diện trực quan, câu chữ (UI/Microcopy).

---

## 1. 👥 Các Thành Viên Khung (AI Agents)

Hệ thống Audit chia làm 2 tầng kiểm định độc lập để soi xét sản phẩm từ tổng thể đến chi tiết:

**🧠 UX Flow Auditor (`roles/UIUX Audit/ux_flow_auditor.md`):**
- **Vai trò:** Chuyên gia rà soát Tầng Logic.
- **Nhiệm vụ:** Đọc Flow/Màn hình để soi xét cấu trúc, định vị mục tiêu lõi (JTBD), thử nghiệm bước đi đóng vai người dùng và "vạch lá tìm sâu" các lỗi rẽ nhánh (Unhappy Paths). Tổng hợp Data để chốt hạ mức độ nghiêm trọng (Severity).
- **Đầu ra:** Bản báo cáo Phát hiện Lỗi Logic (UX Findings) và Báo cáo Audit Cuối cùng.

**👁️ UI Visual Auditor (`roles/UIUX Audit/ui_visual_auditor.md`):**
- **Vai trò:** Chuyên gia rà soát Tầng Giao diện (Thị giác & Câu chữ).
- **Nhiệm vụ:** Không cho phép để lọt bất kỳ thiết kế nào vi phạm tính tương thích (WCAG), độ khó đọc, hay dùng từ ngữ tối nghĩa, sai chính tả trên hệ thống (UX Writing/Microcopy).
- **Đầu ra:** Bản báo cáo Phát hiện Lỗi Giao diện (UI Findings).

---

## 2. 🚀 Các Quy Trình Vận Hành (Workflows)

Hệ thống Audit vận hành theo các Workflows cụ thể để quét toàn diện một sản phẩm/tính năng:

### 🧩 `audit_uiux_phase1_flow` (Soát lỗi Logic)
- **Mục đích:** Phân tích Cấu trúc Luồng & Rào cản Nhận thức (Cognitive Load).
- **Cách làm:** Kênh đầu vào là File Specs/Figma cần Audit. UX Flow Auditor sẽ kiểm tra các nhánh logic, đảm bảo luồng đi không có ngõ cụt và bám sát JTBD.

### 🎨 `audit_uiux_phase2_visual` (Soát lỗi Thẩm mỹ & Microcopy)
- **Mục đích:** Đánh giá Giao diện Visual, chuẩn WCAG & Copywriting.
- **Cách làm:** UI Visual Auditor soi xét tỉ mỉ từng câu chữ, khoảng cách, màu sắc và độ tương phản của mẫu thiết kế.

### 🎁 Master Workflow (`audit_uiux_master`)
- Đây là Pipeline Xuyên mạch kích hoạt tự động toàn bộ chuỗi UI/UX Audit.
- Gọi lệnh `/audit_uiux_master`, AI sẽ tự động chạy song song, hoặc nối tiếp các Phase ở trên có điểm dừng (HITL) và xuất ra **Bản báo cáo Audit Nhất định cuối cùng (Final Audit Report)** với đầy đủ phân loại rủi ro (Critical/Major/Minor) cho đội ngũ Thiết kế & Lập trình sửa chữa.
