---
name: token_scanner
description: Kỹ năng kiểm toán (Audit), đo lường tỷ lệ token-hoá (% compliance) và chuẩn hóa Design Tokens / Styles trong Figma. Quét màu (fills/strokes), corner radius, spacing/padding, typography và gán token hàng loạt.
---

# Token Scanner Skill (Figma Design System Audit & Tokenizer)

Kỹ năng chuyên biệt cho **Design Ops** và **UI/UX Designer** nhằm tự động kiểm toán (Audit), đo lường mức độ tuân thủ Design System (% tokenization) và dọn dẹp các giá trị thô (hardcoded / raw values) trên Figma canvas trước khi Handoff cho bộ phận phát triển.

Mã nguồn Plugin Figma hoàn chỉnh được lưu tại: [`source/`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source)

---

## 1. Mục đích & Giá trị cốt lõi

1. **Kiểm toán chất lượng file thiết kế (Hygiene & Compliance Audit):**
   - Rà soát toàn bộ các giá trị màu sắc, kích thước số và cỡ chữ trên Page hoặc trong Frame/Section được chỉ định.
   - Phát hiện các layer sử dụng giá trị thô (Raw / Unlinked) chưa được liên kết với Design Tokens hoặc Figma Styles.
2. **Đo lường mức độ chuẩn hóa (% Tokenization):**
   - Thống kê tỷ lệ phần trăm các phần tử đã được token hóa trên toàn bộ thiết kế và chi tiết theo 4 nhóm thuộc tính.
3. **Chuẩn hóa & Gán Token hàng loạt (Batch Normalization & Merge):**
   - Lựa chọn 1 Variable hoặc Style chuẩn đang có sẵn trong file/library và áp dụng hàng loạt cho tất cả các node đang sử dụng giá trị thô tương ứng chỉ với một thao tác.
   - Hỗ trợ gỡ liên kết (Unlink) hoặc đồng nhất các biến thể binding về một nguồn duy nhất.

---

## 2. Phạm vi & Thuộc tính quét (Scan Scope & Specifications)

| Nhóm (`category`) | Thuộc tính Figma quét | Tiêu chuẩn Token / Binding hợp lệ |
| :--- | :--- | :--- |
| **`color`** | `fills`, `strokes` (chỉ xét dạng `SOLID`) | Color Variable (`VARIABLE`) hoặc Paint Style (`STYLE`) |
| **`radius`** | `cornerRadius` và 4 góc riêng biệt (`topLeftRadius`, `topRightRadius`, `bottomLeftRadius`, `bottomRightRadius`) | `FLOAT` Variable |
| **`spacing`** | Auto-layout: `itemSpacing`, `counterAxisSpacing`, `paddingLeft`, `paddingRight`, `paddingTop`, `paddingBottom` | `FLOAT` Variable |
| **`textSize`** | `fontSize` của `TextNode` (hỗ trợ cả uniform lẫn mixed font size per-range) | Text Style hoặc `FLOAT` Variable |

> [!NOTE]
> **Các thuộc tính không nằm trong phạm vi quét:** Stroke weight, width/height cố định, Effects/Shadows, Gradient/Image fills, nội dung chuỗi ký tự (Text characters content).

---

## 3. Phân loại Trạng thái Binding (Binding Statuses)

- 🟣 **Variable / Token (Tím):** Đã liên kết trực tiếp với Figma Variable (`type: 'variable'`).
- 🔵 **Style (Xanh lá / Xanh dương):** Đã liên kết với Figma Style (`type: 'style'`).
- 🔴 **No Link / Raw (Đỏ):** Giá trị thô được nhập cứng trực tiếp vào layer, chưa liên kết với bất kỳ token hay style nào (`type: 'none'`).

### Phân loại trạng thái Nhóm giá trị (`ValueGroup Status`):
- `raw`: 100% các lần xuất hiện đều là giá trị thô (`tokenized === 0`).
- `partial`: Còn ít nhất 1 lần xuất hiện chưa được link (`0 < tokenized < count`).
- `tokenized`: 100% các lần xuất hiện đã được gán token/style chuẩn (`tokenized === count`).

---

## 4. Kiến trúc & Mô hình Dữ liệu (Data Model)

Mã nguồn sử dụng cấu trúc bất biến (immutable) và các API `async` chuẩn `dynamic-page` của Figma:

```typescript
// Định nghĩa kiểu liên kết Token/Style
interface Binding {
  type: 'variable' | 'style' | 'none';
  tokenId?: string;
  tokenName?: string;
  remote?: boolean; // true nếu token từ Team Library
}

// Đại diện cho một lần xuất hiện cụ thể trên canvas
interface Occurrence {
  nodeId: string;
  nodeName: string;
  category: 'color' | 'radius' | 'spacing' | 'textSize';
  property: string;
  paintProp?: 'fills' | 'strokes';
  paintIndex?: number;
  fields?: string[]; // vd: ['paddingLeft', 'paddingRight'] hoặc ['cornerRadius']
  range?: { start: number; end: number }; // Dành cho Text mixed range
  binding: Binding;
}

// Gom nhóm theo giá trị thực tế
interface ValueGroup {
  key: string;            // color|#RRGGBBAA, radius|8, spacing|16, textSize|14
  category: string;
  displayValue: string;
  swatch?: string;        // Hex8 color code
  numberValue?: number;
  occurrences: Occurrence[];
  count: number;          // Tổng số lần xuất hiện
  tokenizedCount: number; // Số lần đã gắn token
  status: 'raw' | 'partial' | 'tokenized';
}

// Thống kê % độ phủ
interface Stats {
  overall: { tokenized: number; total: number; pct: number };
  byCategory: Record<'color' | 'radius' | 'spacing' | 'textSize', { tokenized: number; total: number; pct: number }>;
}
```

---

## 5. Quy trình Kiểm toán & Chuẩn hóa (Audit & Merge Workflow)

```
[Bắt đầu Audit]
       │
       ▼
[Xác định Scope] ─── (Có chọn Frame/Section?) ──► Quét vùng chọn (Selection)
       │                                     └──► Quét toàn bộ Page
       ▼
[Thu thập Node] ──► [Trích xuất Color / Radius / Spacing / TextSize]
       │
       ▼
[Phân loại Binding & Gom nhóm ValueGroup]
       │
       ▼
[Tính toán % Token Compliance] ──► [Hiển thị Dashboard 4 cột]
                                           │
                                           ▼
             [Select & Zoom to Canvas] ── AND ── [Thực hiện Batch Merge]
```

### 5.1. Thao tác Chọn & Định vị (Select & Zoom)
- Cho phép chọn toàn bộ các node thuộc một nhóm giá trị hoặc một sub-group token/raw cụ thể.
- Tự động gọi `figma.currentPage.selection = nodes` kèm `figma.viewport.scrollAndZoomIntoView(nodes)`.
- Sử dụng cơ chế ghi nhớ `programmaticSelectionKey` để việc chọn node trên canvas không làm thay đổi hay co hẹp Scope quét ban đầu của plugin.

### 5.2. Thao tác Merge (Hợp nhất & Gán Token hàng loạt)
- Khi một nhóm giá trị (`ValueGroup`) có cả bản ghi đã gán Token lẫn bản ghi còn `No Link`:
  - **Áp dụng Token/Style:** Bấm icon Merge tại dòng Token/Style để gán biến thể đó cho tất cả các node còn lại trong nhóm.
  - **Gỡ bỏ Token (Unlink):** Bấm icon Merge tại dòng `No Link` để gỡ bỏ toàn bộ liên kết của nhóm về giá trị thô.
- Sau khi thực hiện Merge thành công, hệ thống tự động kích hoạt quét lại (`runScan`) để cập nhật số liệu thời gian thực.

---

## 6. Hướng dẫn Phát triển & Tích hợp Plugin trong Figma

### 6.1. Cài đặt và Build mã nguồn:
Mã nguồn nằm trong thư mục [`source/`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source):

```bash
cd .agents/skills/token_scanner/source
npm install
npm run build      # Compile TypeScript (code.ts -> code.js)
npm run watch      # Chế độ tự động build khi thay đổi code
npm run lint       # Kiểm tra quy chuẩn code với Typed-Linting
```

### 6.2. Import vào Figma Desktop:
1. Mở ứng dụng Figma Desktop.
2. Vào **Menu** -> **Plugins** -> **Development** -> **Import plugin from manifest...**.
3. Chọn file [`manifest.json`](file:///Users/tuanvq/Documents/Mew-Design/.agents/skills/token_scanner/source/manifest.json).
4. Khởi chạy plugin trực tiếp từ mục **Development Plugins** bất kỳ lúc nào.

---

## 7. Nguyên tắc Kỹ thuật Figma API (Best Practices & Constraints)

1. **Async Document Access (`dynamic-page`):**
   - Luôn sử dụng các API bất đồng bộ: `getNodeByIdAsync`, `getVariableByIdAsync`, `getStyleByIdAsync`, `getLocalPaintStylesAsync`, `getLocalTextStylesAsync`, `setFillStyleIdAsync`, `setTextStyleIdAsync`.
2. **Xử lý Mảng Thuộc tính Read-only:**
   - Mảng `node.fills` và `node.strokes` trong Figma là bất biến. Khi gán variable vào paint hoặc thay đổi màu sắc, bắt buộc phải sao chép (`clone = [...node.fills]`), sửa đổi trên bản sao, sau đó gán ngược lại `node.fills = clone`.
3. **Self-contained UI:**
   - Plugin chạy với chính sách bảo mật mạng `networkAccess: "none"`. Toàn bộ asset, CSS và JS trong `ui.html` phải là inline hoặc nhúng dưới dạng base64 Data-URI.
