---
name: ui-visual-design
description: Kỹ năng chuyên sâu thiết kế giao diện thị giác cao cấp (High-Aesthetic UI), xây dựng Design Tokens, lưới Bento 2.0, hiệu ứng vi tương tác (Micro-physics) và các quy chuẩn loại bỏ định kiến AI (Anti-AI-Slop).
---

# Kỹ năng: Thiết kế Giao diện Thị giác Cao cấp & Design Tokens (UI Visual Design)

## 📌 Tổng quan

Kỹ năng này định hình các tiêu chuẩn thủ công đỉnh cao (Craftsmanship) trong thiết kế giao diện số của Mew-Design Studio. Mục tiêu là tạo ra các sản phẩm giao diện đạt đẳng cấp phần mềm thương mại hàng đầu (Apple, Linear, Vercel), loại bỏ hoàn toàn các đặc trưng rập khuôn, rẻ tiền của AI thông thường (Anti-AI-Slop).

---

## 🎨 1. Quy tắc Phá vỡ Định kiến AI (Anti-AI-Slop Directives)

1. **Bảng màu Tinh tế (The Color Standard):**
   - **CẤM:** Các dải gradient tím/hồng neon rực rỡ đặc trưng của ChatGPT/AI ("The Lila Ban").
   - **CHUẨN:** Sử dụng nền Neutral sâu lắng (Zinc, Slate, Off-black `#0A0D14` hoặc Off-white `#F9FAFB`). Kết hợp duy nhất **1 màu Accent đắt giá** (Accent saturation < 80%) để thu hút sự chú ý vào nút hành động chính (Primary Action).
2. **Cấu trúc Không gian & Chống lạm dụng Thẻ (Card Overuse):**
   - **CẤM:** Nhốt mọi đoạn text và thông tin vào các ô card vuông trắng viền xám trôi nổi lặp đi lặp lại.
   - **CHUẨN:** Phân tách các khối thông tin bằng khoảng trắng âm (Negative space), đường phân cách mờ nhẹ (`border-t border-black/5` hoặc `border-white/5`), và phân cấp typography rõ ràng.
3. **Typography Hiện đại:**
   - **Font đề xuất:** `Geist Sans`, `Satoshi`, `Outfit`, `Plus Jakarta Sans`.
   - **Optical Tightening:** Các tiêu đề lớn (H1, H2) luôn luôn phải co nhẹ khoảng cách ký tự (`letter-spacing: -0.02em` đến `-0.04em` / `tracking-tight`).
4. **Tuyệt đối Không Dùng Emoji làm Icon:**
   - Sử dụng thư viện vector icons chuyên nghiệp: Phosphor Icons hoặc Lucide Icons với độ dày nét (Stroke width) đồng nhất (1.5px hoặc 2.0px).

---

## 📐 2. Bố cục Bento Grid 2.0 & Kiến trúc Bề mặt

- **Bo góc Sâu & Mềm (Deep Radii):** Bo góc card từ `rounded-2xl` (16px) đến `rounded-[2rem]` (32px).
- **Bóng đổ Khuyếch tán Mịn (Diffusion Shadow):**
  - Không dùng bóng đen đặc gắt.
  - Sử dụng bóng đổ đa tầng:
    `box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05), 0 2px 6px -1px rgba(0, 0, 0, 0.02);`
- **Kính mờ Quang học (Liquid Glassmorphism):**
  - Khi thiết kế hiệu ứng kính, bắt buộc kết hợp:
    `backdrop-blur-md bg-white/70 dark:bg-black/60 border border-white/20 dark:border-white/10 shadow-inset` để giả lập quang học khúc xạ của viền kính thực tế.
- **Viewport Safe Height:**
  - Luôn sử dụng `min-h-[100dvh]` thay cho `h-screen` để tránh bị nhảy layout trên thanh địa chỉ di động Safari/Chrome iOS.

---

## ⚡ 3. Vi Tương tác & Vật lý Chạm (Micro-Physics)

- **Cảm giác Chạm Vật lý (Tactile Feedback):** Mọi nút bấm khi tương tác `:active` đều phải có phản hồi thụt nhẹ tự nhiên (`transform: scale(0.98)`).
- **Spring Physics:** Chuyển động xuất hiện sử dụng gia tốc lò xo (cubic-bezier đàn hồi mượt mà), không dùng chuyển động tuyến tính (`linear`).

---

## 📄 Cấu trúc Mẫu Design Tokens (JSON Schema)

```json
{
  "token_version": "1.0",
  "colors": {
    "background": {
      "primary": "#0A0D14",
      "surface": "#121721",
      "surface_elevated": "#1A202C"
    },
    "border": {
      "subtle": "rgba(255, 255, 255, 0.08)",
      "hover": "rgba(255, 255, 255, 0.16)"
    },
    "text": {
      "primary": "#F8FAFC",
      "secondary": "#94A3B8",
      "muted": "#64748B"
    },
    "accent": {
      "default": "#3B82F6",
      "hover": "#2563EB",
      "active": "#1D4ED8"
    }
  },
  "typography": {
    "font_family_heading": "Geist, system-ui, sans-serif",
    "font_family_body": "Geist, system-ui, sans-serif"
  },
  "radii": {
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "full": "9999px"
  }
}
```
