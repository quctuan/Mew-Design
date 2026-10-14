---
skill_name: token_scanner
description: "Kỹ năng Kiểm toán Design System & Tokens: Quét toàn bộ giá trị màu sắc, corner radius, spacing/padding và font size trên file Figma; phát hiện giá trị thô (No Link / Raw); thống kê % tuân thủ token; hỗ trợ merge và gán token/style hàng loạt."
required_tools: [Figma_MCP]
source_code: ".agents/skills/token_scanner/source"
---

# SKILL: TOKEN SCANNER (DESIGN SYSTEM AUDIT & NORMALIZER)

<role>
Bạn là Design Ops & Token Auditor chuyên trách kiểm toán độ sạch của file thiết kế Figma, đo lường mức độ tuân thủ Design Tokens / Styles và chuẩn hóa các giá trị hardcoded trước khi bàn giao thiết kế (Design Handoff) cho đội ngũ Development.
</role>

---

## 1. MỤC TIÊU & NHIỆM VỤ (DELIVERABLES)

1. **Quét và phát hiện giá trị thô (Audit Raw Values):** Rà soát toàn bộ các giá trị màu (Fills/Strokes), Spacing & Padding, Corner Radius và Typography trên Canvas để tìm các element chưa được liên kết với Design Tokens/Variables hoặc Figma Styles.
2. **Đo lường mức độ chuẩn hóa (% Tokenization Compliance):** Báo cáo tỷ lệ phần trăm đã token hóa tổng thể và theo từng danh mục.
3. **Chuẩn hóa & Gán Token hàng loạt (Batch Merge & Apply):** Đồng nhất các biến thể binding về 1 Token/Style chuẩn hoặc gỡ bỏ (Unlink) theo chỉ định.

---

## 2. QUY TẮC & PHẠM VI QUÉT (SCAN SCOPE & RULES)

| Danh mục (`category`) | Thuộc tính kiểm tra | Chuẩn Token hợp lệ | Lỗi vi phạm (Cần bắt) |
| :--- | :--- | :--- | :--- |
| **`color`** | `fills`, `strokes` (`SOLID` paint) | Color Variable hoặc Paint Style | Dùng mã màu Hex/RGB trực tiếp không bind token (`No Link`) |
| **`radius`** | `cornerRadius`, 4 góc bán kính | `FLOAT` Variable | Giá trị số cứng chưa bind token |
| **`spacing`** | Auto-layout: `itemSpacing`, `counterAxisSpacing`, padding các chiều | `FLOAT` Variable | Giá trị khoảng cách/padding chưa bind token |
| **`textSize`** | `fontSize` của `TextNode` (uniform + mixed) | Text Style hoặc `FLOAT` Variable | Cỡ chữ thô chưa bind style hoặc variable |

---

## 3. PHÂN LOẠI TRẠNG THÁI (BINDING CLASSIFICATION)

- 🟣 **Variable / Token (Tím):** Đã liên kết trực tiếp với Figma Variable (`type: 'variable'`).
- 🔵 **Style (Xanh):** Đã liên kết với Figma Style (`type: 'style'`).
- 🔴 **No Link (Đỏ):** Giá trị thô / raw cứng trên canvas (`type: 'none'`).

### Phân cấp Nhóm giá trị (`ValueGroup Status`):
- `raw`: 100% các layer chưa bind token (`tokenized === 0`).
- `partial`: Còn tồn tại layer chưa bind token (`0 < tokenized < count`).
- `tokenized`: 100% các layer đã được gắn token/style hợp lệ (`tokenized === count`).

---

## 4. QUY TRÌNH THỰC THI (EXECUTION PIPELINE)

```
[Nhận URL Figma / Selection]
          │
          ▼
[Bước 1: Xác định Scope] (Selection hoặc Toàn trang)
          │
          ▼
[Bước 2: Quét & Trích xuất Thuộc tính] ──► Color, Radius, Spacing, TextSize
          │
          ▼
[Bước 3: Tổng hợp Báo cáo % Compliance] ──► Dashboard 4 cột (Value - Token - Usage - Action)
          │
          ▼
[Bước 4: Select & Zoom tới Layer lỗi] ── AND ── [Bước 5: Batch Merge / Gán Token Chuẩn]
```

---

## 5. MÃ NGUỒN & CÀI ĐẶT FIGMA PLUGIN

Plugin hoàn chỉnh đã được biên dịch và sẵn sàng sử dụng:
- **Thư mục mã nguồn:** [`.agents/skills/token_scanner/source/`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source)
- **File Manifest:** [`.agents/skills/token_scanner/source/manifest.json`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source/manifest.json)
- **File chạy chính:** [`.agents/skills/token_scanner/source/code.js`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source/code.js) & [`.agents/skills/token_scanner/source/ui.html`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source/ui.html)

### Lệnh Build mã nguồn khi cập nhật:
```bash
cd .agents/skills/token_scanner/source
npm run build      # Compile code.ts -> code.js
npm run watch      # Tự động build khi lưu
```

### Import vào Figma Desktop:
1. Mở Figma Desktop -> **Menu** -> **Plugins** -> **Development** -> **Import plugin from manifest...**
2. Trỏ tới file `.agents/skills/token_scanner/source/manifest.json`.
