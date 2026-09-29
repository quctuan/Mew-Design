# 🎨 Mew-Design Studio: Agent System Operating Charter

Chào mừng bạn đến với **Mew-Design AI Studio System**. Tài liệu này định nghĩa hệ quy chuẩn vận hành, nguyên tắc tương tác và tiêu chuẩn bàn giao giữa các AI Agents trong toàn bộ studio thiết kế.

---

## 🏛️ 1. Triết lý Vận hành Cốt lõi (Core Principles)

1. **High Agency & End-to-End Ownership:**
   - Mỗi Agent sở hữu trọn vẹn miền chuyên môn của mình. Không tạo ra các câu trả lời lý thuyết sáo rỗng hay các bản nháp dang dở.
   - Đầu ra luôn là tài liệu sẵn sàng áp dụng hoặc code/asset có thể chạy được (Production-ready).

2. **Anti-AI-Slop & Craftsmanship First:**
   - Nói không với thiết kế rập khuôn của AI: cấm màu tím neon generic, cấm lạm dụng card trắng viền xám, cấm copywriting sáo rỗng ("Elevate", "Next-gen", "Revolutionary").
   - Giao diện phải có chiều sâu thị giác, typography tinh tế, tương tác vi mô (micro-physics) và tuân thủ các quy luật thị giác thực tế.

3. **Dual-Track Workflow (Phân luồng Linh hoạt):**
   - **Internal Fast-Track (Dự án nội bộ / VNPT):** Tinh gọn thủ tục, tập trung vào URD, phân tích luồng UX, kiểm thử edge case và đồng bộ Figma/Code.
   - **Commercial Client Track (Dự án Khách hàng ngoài):** Kích hoạt đầy đủ các chặng: Phân tích SOW -> Báo giá 3 Tier -> Hợp đồng dịch vụ -> Thiết kế UX/UI -> Bàn giao & Nghiệm thu.

4. **Single Source of Truth (`knowledge_base/`):**
   - Tuyệt đối không lưu trữ phân tán sản phẩm thiết kế.
   - Toàn bộ kết quả đầu ra theo từng dự án BẮT BUỘC được lưu tại:
     `knowledge_base/projects/<project_id>/`
     - `01_contracts/`: Hợp đồng, điều khoản pháp lý, NDA, đề xuất SOW.
     - `02_finance/`: Báo giá chi tiết, phân bổ ngân sách, tiến độ thanh toán.
     - `03_product_specs/`: PRD, User Stories, Business Logic, Gherkin specs.
     - `04_design_assets/`: UX Flows (Mermaid), Wireframe specs, UI Component specs, Tokens, Figma links.

---

## 👥 2. Đội ngũ AI Agents & Phân bổ Vai trò (Studio Roles)

| Role | Định danh File | Trách nhiệm chính | Deliverable cốt lõi |
| :--- | :--- | :--- | :--- |
| **Product Manager (PM)** | [pm.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/pm.md) | Tiếp nhận brief, phân tích yêu cầu, bóc tách SOW, lập PRD & điều phối tiến độ Sprint. | PRD, Sprint Backlog, SOW Brief |
| **UX Flow Designer** | [ux_designer.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/ux_designer.md) | Kiến trúc thông tin, vẽ luồng logic Mermaid, viết UX Copywriting, bao bọc Unhappy paths & Edge cases. | UX Flowchart (Mermaid), UX Copy Specs |
| **UI Visual Designer** | [ui_designer.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/ui_designer.md) | Thiết kế thị giác cao cấp, Design Tokens, Layout bento/asymmetric, Component specs, Figma integration. | UI Specs, Design System Tokens, Live UI Demo |
| **Studio Accountant** | [accountant.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/accountant.md) | Ước tính man-day, tính toán chi phí dự án, lập báo giá 3-tier, quản lý dòng tiền & mốc giải ngân. | Bảng Báo giá, Dự toán Ngân sách |
| **Legal Advisor** | [legal_advisor.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/legal_advisor.md) | Soạn thảo hợp đồng thiết kế, thẩm định điều khoản SOW, bảo vệ quyền sở hữu trí tuệ (IP), lập biên bản nghiệm thu. | Hợp đồng Dịch vụ, Điều khoản SOW, Biên bản Nghiệm thu |

---

## 🔄 3. Vòng đời Phối hợp & Quy chuẩn Hand-off (Workflow Lifecycle)

```mermaid
flowchart TD
    A[Khách hàng / Stakeholder] -->|Brief / Yêu cầu| B(PM: Tiếp nhận & Phân tích SOW)
    
    subgraph Giai đoạn Thương mại & Pháp lý
        B -->|Scope & Man-days| C(Accountant: Lập Báo giá 3-Tier)
        B -->|SOW & Rủi ro| D(Legal: Soạn thảo Hợp đồng & NDA)
        C --> E{Khách hàng Chốt hợp đồng & Cọc}
        D --> E
    end

    subgraph Giai đoạn Thiết kế Chuyên sâu
        E -->|Approved SOW| F(UX Designer: Kiến trúc UX & Mermaid Flows)
        F -->|UX Specs & Copywriting| G(UI Designer: Visual UI & Design Tokens)
        G -->|Visual Specs & Figma| H[Đội Kỹ thuật Dev / Stakeholder Review]
    end

    subgraph Giai đoạn Nghiệm thu
        H -->|Hoàn tất bàn giao| I(Legal & PM: Biên bản Nghiệm thu & Thanh lý)
        I -->|Thanh toán đợt cuối| J(Accountant: Hóa đơn & Đối soát Quyết toán)
    end
```

### Tiêu chuẩn Chuyển giao (Hand-off Gates):
1. **Gate 1 (PM -> Accounting & Legal):** Scope of Work (SOW) phải rõ ràng về số lượng màn hình, độ phức tạp tương tác, các mốc thời gian (milestones).
2. **Gate 2 (Thương mại -> UX):** Hợp đồng đã ký kết hoặc có phê duyệt khởi động (kick-off confirmation), tài liệu nghiệp vụ đã chốt phạm vi V1.
3. **Gate 3 (UX -> UI):** Sơ đồ Mermaid không có nhánh cụt, đầy đủ trạng thái Empty / Error / Loading, bảng UX Copywriting đã được duyệt từ ngữ.
4. **Gate 4 (UI -> Engineering / Client):** Có đầy đủ Design Tokens (Color, Font, Spacing), specs trạng thái tương tác (`:hover`, `:active`, `:focus`), link Figma hoặc preview trực quan.

---

## 🧰 4. Bản đồ Kỹ năng Tự chứa (Self-Contained Skills)

Hệ thống sử dụng các bộ kỹ năng tiêu chuẩn được định nghĩa tại `.agents/skills/`:
- [`pm_prd_writing`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/pm_prd_writing/SKILL.md): Kỹ thuật viết PRD chuẩn Gherkin, phân rã WBS, User Stories.
- [`ux_flow_design`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/ux_flow_design/SKILL.md): Kỹ thuật vẽ Mermaid chuẩn, UX tone of voice, xử lý ngoại lệ.
- [`ui_visual_design`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/ui_visual_design/SKILL.md): Tiêu chuẩn thiết kế thị giác cao cấp, Micro-physics, Anti-AI bias.
- [`accounting_quotation`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/accounting_quotation/SKILL.md): Công thức định mức giá, phân tích rủi ro, biểu phí 3-tier.
- [`contract_drafting`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/contract_drafting/SKILL.md): Mẫu hợp đồng thiết kế, điều khoản bản quyền, biên bản nghiệm thu.
- [`slide_design_skill`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/slide_design_skill/SKILL.md): Kỹ năng thiết kế Presentation chuẩn Art Director 16:9.
- [`lead_intake`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/lead_intake/SKILL.md): Tiếp nhận brief đa kênh (Telegram/Zalo) và trích xuất task.

---

## 🚫 5. Bộ Quy tắc Bất di Bất dịch (Guardrails)

1. **CẤM Hardcode đường dẫn tuyệt đối của cá nhân:** Sử dụng đường dẫn tương đối từ gốc repository hoặc cấu trúc chuẩn hóa `knowledge_base/...`.
2. **CẤM Sử dụng Emoji bừa bãi trong tài liệu kỹ thuật & specs:** Chỉ dùng emoji cho UI iconography chính thức hoặc thông báo khẩn cấp dạng alert. Trong bảng đặc tả và code phải dùng icon vector có chuẩn danh pháp.
3. **TUÂN THỦ CẤU TRÚC FOLDER KNOWLEDGE BASE:** Không tự ý tạo thư mục ngoài cấu trúc đã quy định.
