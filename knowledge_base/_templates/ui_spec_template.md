# Đặc tả Thiết kế Giao diện Thị giác (UI Visual Specification)

> **Dự án:** `{PROJECT_NAME}` | **Module:** `{MODULE_NAME}` | **Mã Spec:** `UI-{MODULE_CODE}`  
> **UI Designer:** `{DESIGNER_NAME}` | **Ngày tạo:** `{YYYY-MM-DD}` | **Phiên bản:** `v1.0`  
> **Link Figma File:** `[Figma Design File](https://figma.com/file/...)`  
> **Tài liệu tham chiếu:** [UX Spec tương ứng](../04_design_assets/UX_{MODULE_CODE}.md)

---

## 1. Định hướng Thị giác & Thẩm mỹ (Visual Direction & Mood)

- **Phong cách chủ đạo:** Premium Modern SaaS / FinTech với không gian thoáng đãng (Airy), cấu trúc Bento Grid 2.0, viền kính quang học (Liquid Glassmorphism) và độ sâu tự nhiên qua Diffusion Shadow.
- **Tiêu chuẩn Anti-AI-Slop:** Không sử dụng dải màu tím/hồng neon AI, không nhồi nhét text vào các hộp vuông xám lặp đi lặp lại. Sử dụng icon vector Phosphor chuẩn nét 1.5px, cấm dùng emoji làm icon hệ thống.

---

## 2. Hệ thống Design Tokens Cốt lõi (Core Tokens)

### 2.1. Bảng màu (Color Palette)
```css
:root {
  /* Neutral Backgrounds */
  --bg-primary: #0A0D14;          /* Nền chính sâu thẳm */
  --bg-surface: #121721;          /* Bề mặt card chính */
  --bg-surface-elevated: #1A2230; /* Bề mặt nổi / Dropdown / Modal */

  /* Borders & Dividers */
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-focus: rgba(255, 255, 255, 0.20);

  /* Typography Colors */
  --text-primary: #F8FAFC;        /* Chữ tiêu đề & nội dung chính */
  --text-secondary: #94A3B8;      /* Chữ phụ, mô tả ngắn */
  --text-muted: #64748B;          /* Placeholder, ngày tháng, caption */

  /* Single Crisp Accent */
  --accent-primary: #2563EB;      /* Xanh đậm thanh lịch */
  --accent-hover: #1D4ED8;
  --accent-glow: rgba(37, 99, 235, 0.25);

  /* Semantic Feedback */
  --status-success: #10B981;
  --status-warning: #F59E0B;
  --status-error: #EF4444;
}
```

### 2.2. Phân cấp Chữ (Typography Hierarchy)
- **Heading Font:** `Geist Sans` hoặc `Outfit` (sans-serif)
- **Body Font:** `Geist Sans` hoặc `Plus Jakarta Sans`
- **Quy tắc Canh Chỉnh Khoảng cách Ký tự (Letter Spacing):**
  - **H1 (Display 32px - 40px):** `letter-spacing: -0.03em; font-weight: 700; line-height: 1.15;`
  - **H2 (Section 24px - 28px):** `letter-spacing: -0.02em; font-weight: 600; line-height: 1.25;`
  - **Body Regular (15px):** `letter-spacing: -0.01em; font-weight: 400; line-height: 1.6;`
  - **Caption (12px - 13px):** `letter-spacing: 0; font-weight: 500; text-transform: uppercase;`

### 2.3. Bán kính Bo góc (Corner Radii)
- `--radius-sm: 8px;` (Cho input, badge, tag nhỏ)
- `--radius-md: 16px;` (Cho nút bấm, popup nhỏ)
- `--radius-lg: 24px;` (Cho Bento Card tiêu chuẩn)
- `--radius-xl: 32px;` (Cho Modal chính, Drawer lớn)

---

## 3. Đặc tả Trạng thái Tương tác Component (Interactive States)

### Component: Primary Button (Nút Hành động Cốt lõi)
| Trạng thái | Thuộc tính CSS / Hiệu ứng | Cảm giác Tương tác |
| :--- | :--- | :--- |
| **Default** | `bg-[--accent-primary] text-white rounded-xl px-5 py-3 font-semibold` | Rõ ràng, nổi bật nhất trên màn hình |
| **Hover** | `bg-[--accent-hover] shadow-lg shadow-[--accent-glow]` | Nổi nhẹ lên đón đầu con trỏ chuột |
| **Active / Pressed** | `transform: scale(0.98); transition: transform 0.1s ease;` | Cảm giác lún phím vật lý thực thụ |
| **Disabled** | `bg-white/10 text-white/30 cursor-not-allowed pointer-events-none` | Trầm xuống, không gây phân tâm |
| **Loading** | `opacity: 0.8; pointer-events-none` kèm spinner xoay mượt ở tâm | Người dùng biết hệ thống đang xử lý |

---

## 4. Bố cục Bento Grid & Responsive Viewport

- **Kích thước An toàn Màn hình (Safe Height):** Sử dụng `min-h-[100dvh]` để tránh lỗi nhảy thanh công cụ trình duyệt Safari/Chrome trên smartphone.
- **Bento 2.0 Spacing:** Padding trong card tối thiểu `24px` đến `32px`. Khoảng cách giữa các card là `16px` đến `24px`.
