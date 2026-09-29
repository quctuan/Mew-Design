# 📁 Cấu trúc Thư mục Mẫu Dự án (Project Folder Template)

Thư mục này là **bộ khung mẫu (Scaffold)** dành cho mọi dự án thiết kế mới trong Mew-Design Studio.

---

## 🚀 Hướng dẫn Khởi tạo Dự án Mới

Khi tiếp nhận một khách hàng hoặc dự án mới, hãy nhân bản (duplicate) toàn bộ thư mục `_sample_project` này và đổi tên theo cú pháp:
`knowledge_base/projects/<ma_du_an>_tên_du_an/` (Ví dụ: `knowledge_base/projects/prj_fintech_superapp/`)

---

## 📂 Ý nghĩa các Thư mục Con & Phân quyền Phụ trách

```
projects/<project_name>/
├── 01_contracts/          # ⚖️ Phụ trách: Legal Advisor & PM
│   ├── hop_dong_dich_vu.md        # Lấy mẫu từ knowledge_base/_templates/design_contract_template.md
│   ├── bien_ban_nghiem_thu.md     # Lấy mẫu từ knowledge_base/_templates/handover_acceptance_template.md
│   └── nda_bao_mat.md             # Thỏa thuận bảo mật thông tin (nếu có)
│
├── 02_finance/            # 💰 Phụ trách: Studio Accountant
│   ├── bang_bao_gia_3_tier.md     # Lấy mẫu từ knowledge_base/_templates/quotation_template.md
│   └── theo_doi_thanh_toan.md     # Lịch sử các đợt giải ngân, hóa đơn, công nợ
│
├── 03_product_specs/      # 📋 Phụ trách: Product Manager (PM)
│   ├── PRD_<project_name>.md      # Lấy mẫu từ knowledge_base/_templates/prd_template.md
│   └── sprint_backlog.md          # Phân rã WBS và danh sách User Stories
│
└── 04_design_assets/      # 🎨 Phụ trách: UX & UI Designers
    ├── UX_flows_mermaid.md        # Lấy mẫu từ knowledge_base/_templates/ux_spec_template.md
    ├── UI_design_tokens.json      # Xuất khẩu tokens màu, font, spacing
    ├── UI_specs.md                # Lấy mẫu từ knowledge_base/_templates/ui_spec_template.md
    └── figma_links.md             # Liên kết trực tiếp đến file Figma chính thức
```

---

## 🛡️ Nguyên tắc Lưu trữ Bắt buộc
1. **Không tạo thư mục ngoài luồng:** Mọi tài liệu và sản phẩm thiết kế của dự án phải nằm trọn vẹn trong 4 thư mục trên.
2. **Đồng bộ liên tục:** Khi hoàn thành một giai đoạn, Agent phụ trách phải cập nhật trạng thái nghiệm thu vào tài liệu tương ứng để chuyển giao cho Role tiếp theo.
