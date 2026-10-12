# Token Scanner (Figma plugin)

Quét toàn bộ giá trị **màu**, **số** (corner radius, spacing & padding) và **cỡ chữ** trên
1 page hoặc trong frame/section đang chọn; cho biết giá trị nào đã gắn variable/style, giá
trị nào còn raw; thống kê % đã token-hoá; chọn nhanh trên canvas các phần tử cùng giá trị;
và **merge** — áp 1 variable/style có sẵn cho cả nhóm.

## Chức năng
- **Scan thủ công**: bấm nút **Scan**. Không chọn gì → quét toàn page; đang chọn frame/section → chỉ quét trong vùng đó. Sau khi quét, header hiện scope (Toàn trang / tên vùng chọn) và nút đổi thành **Re-scan**.
- Bảng kết quả 4 cột: **Value** · **Style / Token** · **Usage** · **Action**. Mỗi value gom
  theo binding thành từng dòng — dòng đã link hiện tên dưới dạng tag màu (**xanh = style**,
  **tím = variable/token**), dòng chưa link hiện **No Link** (đỏ). Cột Usage là số layer +
  chevron mở danh sách; cột Action có nút đi đến element & merge.
- **Thống kê %** token-hoá tổng thể + theo từng loại (Color / Radius / Spacing / Text).
- **Select**: chọn tất cả node trong nhóm (hoặc từng node) trên canvas + zoom tới.
- **Merge** (icon): chọn 1 variable/style **có sẵn** (local hoặc đang dùng trong file) và áp
  cho toàn bộ node trong nhóm — kể cả node đã có style khác. Xong sẽ tự re-scan.

## Phạm vi quét
| Loại | Thuộc tính | Token hợp lệ |
|------|-----------|--------------|
| Color | `fills`, `strokes` (chỉ SOLID) | color variable / paint style |
| Radius | `cornerRadius` (+ 4 góc) | FLOAT variable |
| Spacing | auto-layout `itemSpacing`, `counterAxisSpacing`, `padding*` | FLOAT variable |
| Text | `fontSize` | text style / FLOAT variable |

## Kiến trúc
- `code.ts` → compile ra `code.js` (main thread, dùng `figma` API; `documentAccess: dynamic-page` nên mọi lookup là async).
- `ui.html` — UI (HTML/CSS/vanilla JS inline, không dùng mạng vì `networkAccess: none`), giao tiếp với main qua `postMessage`.

## Chạy & phát triển
```bash
npm install       # cài @figma/plugin-typings + tooling
npm run build     # tsc code.ts -> code.js
npm run watch     # build lại mỗi khi lưu
npm run lint      # eslint (đã bật typed-linting cho rule dynamic-page)
```
Trong Figma desktop: **Plugins → Development → Import plugin from manifest…** → chọn `manifest.json`,
rồi **Plugins → Development → Token Scanner** để chạy.
