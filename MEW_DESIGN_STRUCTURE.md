# 📐 Mew-Design: Phân tích Cấu trúc Hiện tại & Định hướng Tái cấu trúc (Design Studio Agent System)

## 📌 1. Bức tranh Tổng quan Thư mục gốc (`Mew-Design`)

Hiện tại, repository `Mew-Design` chứa nhiều phần được phát triển qua các giai đoạn khác nhau (dự án My VNPT, Audit UI/UX, McKinsey Research, MkDocs Wiki, và ứng dụng Web Toolcraft).

```
Mew-Design/
├── .agents/                 # 🤖 TRỌNG TÂM: Hệ thống AI Agents, Roles, Skills, Workflows
├── knowledge base/          # 📚 Nơi chứa tri thức & đầu ra (hiện chứa hỗn hợp nhiều dự án)
├── design-docs/             # 🎨 Thư mục preview & script tải màn hình UI (Python/HTML)
├── frameworks/              # 📖 Tài liệu nghiên cứu quy trình (McKinsey, Market Research)
├── sample_team/             # 👥 Thư mục lưu mẫu một team (uiux-audit-team)
├── wiki/                    # 🌐 Dự án MkDocs để xuất bản trang tri thức nội bộ
├── ui-library-building/     # 💻 App Web Toolcraft Studio (Soft 3D Stylizer)
├── preview-app/             # 💻 App preview phụ
├── CLAUDE.md / README.md    # 📄 Các file hướng dẫn & onboarding agent
└── package.json             # ⚙️ Cấu hình Node.js dependencies
```

---

## 🤖 2. Phân tích Chi tiết Thư mục `.agents/` (Hệ thống AI Agents)

Thư mục `.agents/` hiện tại đang được chia thành **5 nhánh chính**:

```
.agents/
├── core/                    # Quy tắc cốt lõi & prompt tạo team
│   ├── commands/            # Các lệnh tùy chỉnh
│   ├── hooks/               # Trình bắt sự kiện
│   └── team-creator.md      # Prompt/Guide cốt lõi để AI đóng vai khởi tạo 1 team
│
├── roles/                   # 定義 VAI TRÒ của các Agent (Agent Personas)
│   ├── Design Ops/          # Agent Quản lý quy trình & vận hành thiết kế
│   ├── Flow design/         # Agent Thiết kế Luồng thao tác (UX Flow)
│   ├── UI Design/           # Agent Thiết kế Giao diện (UI)
│   ├── UIUX Audit/          # Agent Đánh giá & Audit UI/UX
│   ├── Jira/                # Agent Quản lý công việc (Task Tracking)
│   └── mckinsey/            # Agent Nghiên cứu Chiến lược
│
├── skills/                  # 各 BỘ KỸ NĂNG (Instructions, Rules & Templates)
│   ├── Flow design/         # Chứa mẫu ux_spec_template.md, quy tắc vẽ Mermaid
│   ├── visual_design_skill/ # Quy tắc thiết kế UI
│   ├── slide_design_skill/  # Quy tắc thiết kế Slide
│   ├── UIUX Audit/          # Bộ skill đánh giá UI/UX
│   ├── design_ops/          # Bộ skill vận hành thiết kế
│   ├── figma_mcp_guide/     # Hướng dẫn kết nối Figma MCP
│   ├── Jira/                # Bộ skill tương tác Jira
│   └── mckinsey/            # Bộ skill nghiên cứu McKinsey
│
├── workflows/               # LUỒNG CÔNG VIỆC phối hợp giữa các Agent
│   ├── Design Ops/
│   ├── Flow design/
│   ├── UIUX Audit/
│   ├── Jira/
│   ├── Wiki/
│   └── mckinsey/
│
└── scripts/                 # Các script tự động hóa helper
```

### 🔍 Nhược điểm & Tồn tại của cấu trúc `.agents/` hiện tại:

1. **Bị phân tán 3 nơi (`roles/`, `skills/`, `workflows/`)**:
   - Cùng 1 nghiệp vụ (ví dụ: *Flow Design* hay *UIUX Audit*) nhưng file lại nằm rải rác ở cả 3 thư mục `.agents/roles/`, `.agents/skills/`, và `.agents/workflows/`.
   - Trong chuẩn **Agent Skills Standard** mới, mỗi Skill nên là **1 thư mục độc lập (Self-Contained)** chứa đầy đủ: Hướng dẫn (`SKILL.md`), biểu mẫu (`templates/`), quy tắc (`rules/`) và luồng xử lý (`workflows/`).
2. **Đặt tên thư mục chưa chuẩn hóa**:
   - Có thư mục chứa khoảng trắng (`Flow design`, `UI Design`, `UIUX Audit`), có thư mục viết thường (`design_ops`, `mckinsey`), có thư mục dùng gạch dưới (`visual_design_skill`).
3. **Thư mục rác / Dữ liệu mẫu thừa**:
   - `sample_team/`, `frameworks/` bị tách rời bên ngoài root thay vì gom vào cấu trúc chung.
   - Thư mục `knowledge base/` hiện chưa phân theo từng Dự án (Project-based).

---

## 🎯 3. Định hướng Cấu trúc Mục tiêu (Target Architecture cho Design Studio)

Mục tiêu xây dựng Agent System cho **Design Studio**:
1. **Đội ngũ AI Agents Studio**:
   - **Product Manager (PM)**: Nhận yêu cầu, phân tích URD/PRD, chia nhỏ Sprint Task.
   - **Design Team**: 
     - *UX Flow Designer*: Vẽ luồng Mermaid, UX writing, Edge cases.
     - *UI Visual Designer*: Design System, Component specs, Layouts.
   - **Kế toán (Accounting / Finance)**: Tính toán chi phí, Báo giá dự án, Quản lý thu chi.
   - **Hợp đồng (Legal / Contracts)**: Soạn thảo hợp đồng, Điều khoản pháp lý, Biên bản thanh lý.
2. **Bộ Skills tương ứng**.
3. **Knowledge Base phân theo từng Folder Dự án (`knowledge_base/projects/<project_name>/`)**.

---

### 📐 Mô hình Cấu trúc Thư mục Mục tiêu (Đề xuất chuẩn hóa):

```
Mew-Design/
├── .agents/                           # 🤖 TRUNG TÂM AI AGENTS
│   ├── AGENTS.md                      # System Prompt & Quy định chung cho toàn studio
│   ├── roles/                         # Persona định danh từng nhân sự AI
│   │   ├── pm.md                      # Agent Product Manager
│   │   ├── ux_designer.md             # Agent UX Flow Designer
│   │   ├── ui_designer.md             # Agent UI Visual Designer
│   │   ├── accountant.md              # Agent Kế toán Studio
│   │   └── legal_advisor.md           # Agent Pháp lý / Hợp đồng
│   │
│   └── skills/                        # BỘ KỸ NĂNG TỰ CHỨA (Self-Contained Skills)
│       ├── pm_prd_writing/            # Skill: Viết PRD & Chia Task
│       ├── ux_flow_design/            # Skill: Thiết kế Luồng UX & Copywriting
│       ├── ui_visual_design/          # Skill: Thiết kế Giao diện & Design System
│       ├── accounting_quotation/      # Skill: Lập Báo giá & Tính toán Chi phí
│       └── contract_drafting/         # Skill: Soạn thảo & Thẩm định Hợp đồng
│
├── knowledge_base/                    # 📚 NƠI LƯU TRI THỨC THEO DỰ ÁN
│   ├── _templates/                    # Biểu mẫu dùng chung (Mẫu hợp đồng, Báo giá, PRD)
│   ├── studio_internal/               # Tri thức nội bộ (Bảng giá chuẩn, Quy trình làm việc)
│   └── projects/                      # MỖI DỰ ÁN LÀ 1 FOLDER RIÊNG
│       ├── project_client_a/          # Dự án A
│       │   ├── 01_contracts/          # Hợp đồng, Đề xuất
│       │   ├── 02_finance/            # Báo giá, Hóa đơn
│       │   ├── 03_product_specs/      # PRD, URD, User Stories
│       │   └── 04_design_assets/      # UX Specs, UI Specs, Figma links
│       └── project_client_b/          # Dự án B
│
└── apps/                              # 💻 CÁC ỨNG DỤNG & TOOLING
    └── ui-library-building/           # Toolcraft Web App (Soft 3D Stylizer Studio)
```

---

## 🚀 4. Kế hoạch Thực thi Dọn dẹp & Tái cấu trúc (Đã Triển khai Hoàn tất ✅)

- [x] **Bước 1 (Cleanup & Hạ tầng thư mục)**:
  - Đổi tên & chuẩn hóa `knowledge base/` thành [`knowledge_base/`](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base). Tạo symlink `knowledge base -> knowledge_base` để duy trì tương thích ngược 100%.
  - Gom các tài liệu nghiên cứu `frameworks/` vào `knowledge_base/studio_internal/frameworks/`.
  - Phân loại tài liệu hiện có vào dự án [`knowledge_base/projects/my_vnpt/`](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/projects/my_vnpt).
  - Chuẩn hóa thư mục [`apps/ui-library-building/`](file:///Users/tuanvuong/Documents/Mew-Design/apps/ui-library-building).

- [x] **Bước 2 (Restructure `.agents/`)**:
  - Khởi tạo [`.agents/AGENTS.md`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/AGENTS.md) - System Prompt & Operating Charter chung cho toàn bộ Studio.
  - Chuẩn hóa 5 Core Roles:
    - [pm.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/pm.md): Product Manager & Studio Producer
    - [ux_designer.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/ux_designer.md): Senior UX Flow Designer & Information Architect
    - [ui_designer.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/ui%20design/ui_designer.md): Senior UI/UX Engineer & Design System Designer
    - [accountant.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/accountant.md): Studio Accountant & Financial Estimator
    - [legal_advisor.md](file:///Users/tuanvuong/Documents/Mew-Design/.agents/roles/legal_advisor.md): Studio Legal Advisor & Contract Specialist
  - Xây dựng 5 Self-Contained Skills:
    - [`pm_prd_writing`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/pm_prd_writing/SKILL.md): Kỹ thuật viết PRD chuẩn Gherkin & quản lý Sprint WBS
    - [`ux_flow_design`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/ux_flow_design/SKILL.md): Sơ đồ luồng Mermaid, UX writing thấu cảm, ma trận 4 trạng thái
    - [`ui_visual_design`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/ui_visual_design/SKILL.md): Visual cao cấp, Bento 2.0, Design Tokens, Anti-AI-slop
    - [`accounting_quotation`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/accounting_quotation/SKILL.md): Báo giá 3-tier, tính man-day, lịch giải ngân
    - [`contract_drafting`](file:///Users/tuanvuong/Documents/Mew-Design/.agents/skills/contract_drafting/SKILL.md): Hợp đồng dịch vụ thiết kế, bảo vệ SHTT, biên bản nghiệm thu
  - Lưu trữ an toàn các roles/skills cũ tại `.agents/roles/_archive/` và `.agents/skills/_archive/`.

- [x] **Bước 3 (Build Project Knowledge Base & Templates)**:
  - Khởi tạo bộ 6 biểu mẫu chuẩn tại [`knowledge_base/_templates/`](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates):
    - [prd_template.md](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates/prd_template.md): Mẫu PRD & User Stories
    - [ux_spec_template.md](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates/ux_spec_template.md): Mẫu đặc tả UX Flows Mermaid & Micro-copy
    - [ui_spec_template.md](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates/ui_spec_template.md): Mẫu đặc tả Visual UI & Design Tokens
    - [quotation_template.md](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates/quotation_template.md): Mẫu bảng báo giá thương mại 3-tier
    - [design_contract_template.md](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates/design_contract_template.md): Mẫu hợp đồng thiết kế dịch vụ UI/UX
    - [handover_acceptance_template.md](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/_templates/handover_acceptance_template.md): Mẫu biên bản bàn giao & nghiệm thu
  - Xây dựng bộ khung dự án mẫu chuẩn tại [`knowledge_base/projects/_sample_project/`](file:///Users/tuanvuong/Documents/Mew-Design/knowledge_base/projects/_sample_project).
