# CLAUDE.md — Token Scanner (Figma plugin)

Tài liệu cho agent/dev: nắm nhanh mục đích, kiến trúc, luồng dữ liệu và các quy ước — **đọc file này trước, không cần scan lại toàn bộ code**. Khi sửa code làm đổi hành vi/kiến trúc bên dưới, **cập nhật lại file này**.

## Mục đích
Plugin quét toàn bộ giá trị **màu / số / cỡ chữ** trên page (hoặc trong selection), cho biết giá trị nào đã gắn variable/style, cái nào còn raw ("No Link"), thống kê % đã token-hoá, chọn nhanh element cùng giá trị trên canvas, và **merge** — áp 1 variable/style có sẵn cho cả nhóm.

## Phạm vi quét (đã chốt với user)
| Loại (`category`) | Thuộc tính Figma | Token hợp lệ |
|---|---|---|
| `color` | `fills`, `strokes` (chỉ SOLID) | color variable / paint style |
| `radius` | `cornerRadius` + 4 góc (`topLeftRadius`…) | FLOAT variable |
| `spacing` | auto-layout `itemSpacing`, `counterAxisSpacing`, `paddingLeft/Right/Top/Bottom` | FLOAT variable |
| `textSize` | TextNode `fontSize` (uniform + per-range khi mixed) | text style / FLOAT variable |
KHÔNG quét: stroke weight, width/height, effect/shadow, gradient/image paint, nội dung text.
**Merge = gộp toàn bộ value về binding của 1 row** đã có trong chính value đó (No Link / style / token). Icon merge chỉ hiện khi value có >1 loại binding. Bấm merge ở row **No Link** = unlink tất cả occurrence còn lại; ở row **style/token** = gán style/token đó cho tất cả. KHÔNG có modal chọn token, KHÔNG tạo token mới, KHÔNG merge sang token chưa xuất hiện trong value.

## Cấu trúc file
- **`code.ts`** → compile ra **`code.js`** (main thread, có `figma`). **TẤT CẢ logic main nằm 1 file** — Figma main thread không hỗ trợ ES module nhiều file, KHÔNG dùng bundler. Đừng tách file trừ khi thêm esbuild.
- **`ui.html`** — UI: HTML + CSS + **vanilla JS inline**, icon là inline SVG, ảnh nhúng **data-URI base64**. Bắt buộc self-contained vì `manifest.networkAccess = "none"` (không load được CDN/font/ảnh ngoài). File này đã ~113KB do có ảnh empty-state nhúng sẵn.
- **`manifest.json`** — `documentAccess: "dynamic-page"` (⇒ mọi lookup document phải dùng **API async**), `editorType: ["figma"]`, `networkAccess: none`. Kích thước UI set trong `figma.showUI(__html__, { width: 440, height: 680, themeColors: true })` (KHÔNG trong manifest).
- **`eslint.config.js`** — đã bật typed-linting (`parserOptions.projectService`) để rule `@figma/figma-plugins` chạy được; nếu không bật, `npm run lint` crash.
- **`image/image 1.png`** — ảnh gốc empty-state. **Không được plugin dùng trực tiếp** (đã resize 256px + nhúng base64 vào `ui.html`). Sửa ảnh phải nhúng lại (xem mục Ảnh).

## Lệnh
```bash
npm install      # cần @figma/plugin-typings
npm run build    # tsc code.ts -> code.js  (BẮT BUỘC sau khi sửa code.ts)
npm run watch    # build lại khi lưu
npm run lint     # eslint (typed-linting)
```
Sửa `ui.html` KHÔNG cần build (chỉ cần chạy lại plugin trong Figma). Import: Figma desktop → Plugins → Development → Import plugin from manifest → `manifest.json`.

## Kiến trúc giao tiếp (postMessage)
main ↔ UI qua `figma.ui.postMessage` / `parent.postMessage({pluginMessage})`.

**UI → main:** `scan` · `select-nodes {nodeIds}` · `zoom-node {nodeId}` · `apply-token {occurrences, target}` · `resize {width,height}` · `close`.

**main → UI:** `scan-progress {done,total}` · `scan-result {scope, contextName, groups, stats, nodeCount}` · `apply-done {applied, failed}` · `error {message}`.
(Đã bỏ: message `context`, và luồng `get-apply-targets`/`apply-targets` + modal chọn token — merge giờ trực tiếp.)

`ApplyTarget` = `{ kind: 'variable'|'style'|'none', category, id?, name? }`. `kind:'none'` = **unlink**; `id` là variable/style id (vắng khi unlink).

## Data model (khai báo trong `code.ts`, UI dùng lại y hệt)
- **`Binding`** `{ type: 'variable'|'style'|'none', tokenId?, tokenName?, remote? }` — `remote`=true nếu token từ team library.
- **`Occurrence`** = 1 lần value xuất hiện: `{ nodeId, nodeName, category, property, paintProp?('fills'|'strokes'), paintIndex?, fields?(bound-var fields cho number, vd ['itemSpacing'] hoặc 4 góc radius), range?({start,end} cho text mixed), binding }`.
- **`ValueGroup`** `{ key, category, displayValue, swatch?(hex8 css cho color), numberValue?, occurrences[], count, tokenizedCount, status, tokenName? }`.
- **`Stats`** `{ overall: CatStat, byCategory: Record<Category,CatStat> }`, `CatStat = {tokenized,total,pct}`. % = occurrence tokenized / tổng (KHÔNG dedupe theo layer — khác với "usage" hiển thị ở UI).

## Luồng chính trong `code.ts`
1. **Bootstrap**: `showUI`; KHÔNG auto-scan (user tự bấm). Không có listener `selectionchange` (đã bỏ — scan thủ công).
2. **Scan** (`handleScanRequest` → `runScan` → `scanOnce`):
   - Scope suy ra từ selection tại lúc bấm: có selection → `{kind:'selection', ids, name}`, không → `{kind:'page'}`. Lưu ở biến `scanScope`; `captureScopeFromSelection()` chỉ chạy khi user bấm, **KHÔNG** khi selection do plugin tự set (so khớp `programmaticSelectionKey` — id set từ nút "Select"). ⇒ Bấm "Select" trên 1 nhóm rồi Re-scan/merge vẫn giữ đúng scope, không bị co về nhóm vừa select.
   - `runScan` có guard chống chồng (`scanning`/`scanQueued`) — gọi lại khi đang chạy sẽ gộp thành 1 lần quét đuôi.
   - `collectScopeNodes` dùng `findAllWithCriteria({types: SCAN_TYPES})` (page) hoặc lặp `scanScope.ids` qua `getNodeByIdAsync` + descendants.
   - Trích value: `extractColors` / `extractRadius` / `extractSpacing` / `extractTextSize`. Guard `figma.mixed`, bỏ paint ẩn/không SOLID, bỏ number ≤ 0. Binding qua `paintBinding` / `variableBinding` / `styleBinding`; tên+remote token cache ở `varCache`/`styleCache` (clear đầu mỗi scan).
   - `buildGroups`: gom theo `_key` (xem dưới), tính `status`, `stats`, sort (raw→partial→tokenized, rồi count desc).
3. **Select** (`selectNodes`): `getNodeByIdAsync` từng id → set `figma.currentPage.selection` + `scrollAndZoomIntoView`; set `programmaticSelectionKey` trước khi set selection.
4. **Apply/merge** (`applyToken` → `applyToNode` → `applyColor`/`applyTextSize`), nhận `occurrences` + `ApplyTarget`:
   - `kind:'variable'`: color→`setBoundVariableForPaint(paint,'color',variable)` (clone paints, gán lại `fills`/`strokes`); radius/spacing→`setBoundVariable(field, variable)`; textSize→`setBoundVariable('fontSize',…)`/`setRangeBoundVariable`.
   - `kind:'style'`: color→`setFillStyleIdAsync`/`setStrokeStyleIdAsync`; textSize→`loadFontAsync` rồi `setTextStyleIdAsync`/`setRangeTextStyleIdAsync`.
   - `kind:'none'` (**unlink**): color→`setFillStyleIdAsync('')`/`setStrokeStyleIdAsync('')` + xoá binding variable trong paint (`setBoundVariableForPaint(paint,'color',null)`); radius/spacing→`setBoundVariable(field, null)`; textSize→`setTextStyleIdAsync('')`/`setRangeTextStyleIdAsync('')` + `setBoundVariable('fontSize', null)`. Chỉ đổi binding, giữ nguyên giá trị màu/số/cỡ.
   - Bọc try/catch từng node → `apply-done {applied, failed}`, rồi **auto `runScan()`** để cập nhật.

### Group key & status (quan trọng)
- Key: `color|#RRGGBBAA` (gộp opacity) · `radius|<n>` · `spacing|<n>` (gộp gap+padding) · `textSize|<n>`. `numKey` làm tròn 2 chữ số.
- **status** (đã fix theo yêu cầu): `raw` nếu `tokenized===0`; **`partial` nếu còn ≥1 occurrence chưa link** (`0 < tokenized < count`); `tokenized` nếu link **hết** (`tokenized===count`, kể cả vào **nhiều token khác nhau**). Status chỉ dùng cho filter dropdown; KHÔNG hiển thị badge trên từng row.

## UI (`ui.html`)
### Trạng thái màn hình
- **Chưa scan**: header ẩn (`#appHeader hidden`), `#list` ẩn. Hiện `#empty` (`.empty-state`, `flex:1` canh giữa): ảnh avatar cá nhân hoá (`#emptyImg`, data-URI) → dòng nhắn 1 hàng (`#emptyMsg`, `white-space:nowrap`) → nút **Scan** (`#scanBtnCenter`).
- **Đang scan**: `#progress` hiện.
- **Có kết quả**: hiện header (tag context + nút **Re-scan** `#scanBtn`), `#stats`, `#controls`, `#list`. Ẩn `#empty`.
- **Không kết quả**: `showEmpty('Không tìm thấy…', false)` (ẩn nút Scan giữa vì đã có Re-scan).
- `#scanBtn` và `#scanBtnCenter` cùng gọi `doScan`; cả 2 disable khi đang quét. `updateContext` set tag "Full Page" hoặc **tên selection**.

### Bảng kết quả (4 cột: Value · Style/Token · Usage · Action)
- Mỗi `ValueGroup` render 1 `.vgroup` = cột Value (spanning trái, `valueCell`) + `.vsubs` chứa các **sub-row theo binding** (`buildSubs`: 1 row / token, + 1 row "No Link"; bound trước, none sau).
- **Cột Style/Token** (`tokenCell`): chưa link → `No Link` (đỏ); đã link → tên token là **tag màu**: **style = xanh** (`.tokentag.style`), **variable = tím** (`.tokentag.token`). (Tag "Team"/"Local" đã bỏ.)
- **Cột Usage**: `layerCount(s.occ)` = **số layer/node duy nhất** (dedupe theo nodeId, khớp số element được "đi đến"). Số của No Link tô đỏ. Chevron mở danh sách element (state `expanded`, key = `groupKey::subKey`).
- **Cột Action**: `goto-sub` (chọn cả nhóm + zoom); `merge-sub` **chỉ hiện khi value có >1 binding-row** (`subs.length > 1`); khi không có merge thì render `.actspacer` (24px) giữ chỗ để icon go-to luôn thẳng 1 cột giữa các row (nút go-to trong panel expand cũng canh cùng cột qua `margin-right: 24px`). Bấm merge = `mergeConsolidate(g, subKey)`: lấy binding của row đó làm target (No Link → `{kind:'none'}`, còn lại → `{kind, id, name}`), gửi `apply-token` với **các occurrence còn lại của value** (`bindKey !== subKey`). KHÔNG còn modal/target-picker. Panel mở rộng (`occRows` + `OCC_BUCKETS`): **color** thống kê theo paint (Fill/Stroke), **spacing** theo 5 mục (Gap [gộp cả counterAxisSpacing]/Top/Bottom/Left/Right Padding), **radius** 1 mục Corner radius (gộp uniform + 4 góc lẻ), **textSize** 1 mục Font size (gộp uniform + per-range) — mỗi dòng = label + số occurrence + nút `goto-bucket` (select các node khớp bucket), ẩn bucket count=0. KHÔNG còn category nào liệt kê từng layer/frame (nhánh fallback per-layer + `goto-node` vẫn giữ trong code cho category tương lai). CSS: `.occ` dùng **cùng grid `1fr 54px 56px`** với `.vsub-main`, số count có `padding-right: 26px` (= chevron 24px + gap 2px) để thẳng hàng với số Usage tổng — đổi cột ở `.vsub-main` thì phải đổi `.occ` theo.

### Filter & stats
- Tabs `#tabs` (`data-cat`): **All · Color · Text · Spacing · Radius** (thứ tự hiển thị đã đổi; `data-cat` khớp `category`, tab Text = `textSize`). CSS: cao 32px, active nền `#0d99ff`, default nền xanh scale-100 (`color-mix 12%`).
- `#statusFilter` (all/raw/partial/tokenized), `#search` (khớp displayValue + tên token trong occurrences). `filtered()` lọc theo cả 3.
- `renderStats`: % tổng + 4 chip theo category.

### Ảnh empty-state (cách nhúng lại)
```bash
sips -Z 256 "image/image 1.png" --out /tmp/empty.png
printf 'data:image/png;base64,' > /tmp/u.txt && base64 -i /tmp/empty.png | tr -d '\n' >> /tmp/u.txt
# rồi thay chuỗi trong src="data:image/png;base64,..." của #emptyImg trong ui.html
```
Không link file ngoài (networkAccess none) — phải data-URI. Chỉnh kích thước hiển thị ở `.empty-state .empty-img` (hiện 140×140).

## Quy ước & gotcha
- **Dynamic-page**: mọi truy cập document → async (`getNodeByIdAsync`, `getVariableByIdAsync`, `getStyleByIdAsync`, `getLocal*Async`, `setFill/StrokeStyleIdAsync`, `setTextStyleIdAsync`). Không dùng bản sync (eslint sẽ báo).
- **eslint**: `no-explicit-any` bật → tránh `any`, dùng type-guard `'prop' in node` để narrow union `SceneNode`. `code.js`, `dist`, `eslint.config.js` bị ignore.
- Mảng `fills`/`strokes` read-only → **clone trước khi sửa** (`.slice()`), rồi gán lại cả mảng.
- Theme: dùng biến `--figma-color-*` (đã bật `themeColors`) để hợp light/dark.
- Ngôn ngữ UI: tiếng Việt.
- Verify: build+lint là gate tối thiểu; test thật phải chạy trong Figma desktop (agent không chạy được app Figma). Script UI có thể check cú pháp: trích `<script>` rồi `node --check`.
- Git: theo rule global, push bằng tài khoản **anhnh-design** (set `user.name`/`user.email` trước khi push).
