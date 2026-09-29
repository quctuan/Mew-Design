# [SPEC-002] Đề xuất Cải tiến Thiết kế (Redesign UI/UX) Gói cước Truyền hình & Thể thao My VNPT

- **Mã Index:** SPEC-002
- **Phiên bản:** v3.1 (Cập nhật chiến lược thiết kế nhóm chặn quảng cáo)
- **Ngày cập nhật:** 2026-06-27
- **Người thực hiện:** Antigravity (UI/UX Agent)

---

## Phần I: Bối cảnh & Vai trò của Trang (Context)

Với việc dự án đã có một trang **Lifestyle (DigiBox)** làm nhiệm vụ khám phá nội dung điện ảnh/thể thao, màn hình **Danh sách Gói cước (Package List)** đóng vai trò là điểm chạm thuần **Thương mại (Commerce / Pricing Page)**. 
Bài toán thiết kế: Làm sao để người dùng so sánh nhanh nhất, thấy được giá trị cao nhất và chốt đơn (Checkout) với số bước ít nhất.

---

## Phần II: Nguyên tắc Thiết kế cho Màn hình Package List

### 1. Kế thừa Vibe Điện ảnh nhưng Tối giản (Premium Commerce Vibe)
* Giữ sự liền mạch (Consistency) bằng **Giao diện tối (Dark Mode)** hoặc **Nền xám đậm cao cấp (Premium Dark Grey)**. 
* Thay thế hình 3D hoạt hình bằng các **Logo bản quyền** (K+, HBO) chìm mờ làm nền cho các thẻ gói cước nội dung.

### 2. Phân cấp Gói cước rõ ràng (Tiering & Decoy Effect)
* Áp dụng mô hình **Good - Better - Best**. Đẩy mạnh 1 gói **"Phổ biến nhất (Best Seller)"** bằng cách làm thẻ to hơn, viền glow sáng nổi bật.

### 3. Tối ưu nhóm Gói "Tắt Quảng Cáo" (Urgency & Ad-blocker Vibe)
Nhóm gói chặn quảng cáo mang tính chất "Utility" (Công cụ/Bảo vệ) nhiều hơn là "Content" (Nội dung). Do đó, thiết kế thẻ này cần tách biệt khỏi các gói phim/thể thao thông thường và mang **tính cấp bách (urgent)**:
* **Visual Metaphor (Thị giác):** Sử dụng biểu tượng **Khiên bảo vệ (Shield)** hoặc **Biển báo Cấm (Stop sign/Slashed eye)** với tone màu cảnh báo (Neon Red / Cảnh báo Đỏ trên nền đen) thay vì màu xanh dương êm dịu.
* **Copywriting đánh thẳng vào Pain-point:** Thay vì ghi "Data ổn định, không quảng cáo", hãy dùng câu hỏi tạo sự khó chịu: *"Đang xem dở thì dính quảng cáo?"*, *"Cắt đứt ngay quảng cáo rác"* hoặc *"Dọn sạch quảng cáo chỉ với 1 click"*.
* **UI Micro-interaction:** Thiết kế nút Mua không phải là chữ `[Đăng ký]` thông thường, mà có thể là dạng **Công tắc (Toggle Switch)** đang ở trạng thái TẮT 🔴. Khi User gạt sang BẬT 🟢 -> Pop-up thanh toán hiện ra.

---

## Phần III: Cấu trúc Giao diện Đề xuất (Information Architecture)

```
┌────────────────────────────────────────────────────────┐
│ [Tab Bar] Internet  |  Thiết bị  |  [TRUYỀN HÌNH] (Active)│
├────────────────────────────────────────────────────────┤
│ 1. FILTER & TABS CHUYÊN MỤC NHANH                      │
│ [ Tất cả ]  [ Thể thao ]  [ Phim ảnh ]  [ Chặn QC ]    │
├────────────────────────────────────────────────────────┤
│ 2. VÙNG "BEST SELLER" (Gói VIP Bao gồm Nội dung)       │
│ ┌────────────────────────────────────────────────────┐ │
│ │ 🌟 ĐƯỢC MUA NHIỀU NHẤT                             │ │
│ │ Gói MyTV VIP (180 ngày)                            │ │
│ │ Giá: 120.000đ (Tiết kiệm 40.000đ)                  │ │
│ │ -------------------------------------------------- │ │
│ │ Bao gồm:                                           │ │
│ │ ✔ Toàn bộ kho phim CINE & HBO                      │ │
│ │ ✔ Độc quyền K+ Thể thao                            │ │
│ │ ✔ Không quảng cáo & 4K UHD                         │ │
│ │                                                    │ │
│ │ [ ĐĂNG KÝ NGAY ]                                   │ │
│ └────────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────┤
│ 3. VÙNG ADD-ON: CHẶN QUẢNG CÁO (Ad-blocker Vibe)       │
│ ┌────────────────────────────────────────────────────┐ │
│ │ 🛑 ĐANG XEM DỞ THÌ DÍNH QUẢNG CÁO?                 │ │
│ │ Gói Không Quảng Cáo (180 ngày)                     │ │
│ │ Xóa sạch quảng cáo rác, trải nghiệm phim liền mạch │ │
│ │                                                    │ │
│ │ [ 🔴 BẬT KHIÊN CHẶN NGAY - 120.000đ ]              │ │
│ └────────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────┤
│ 4. VÙNG SO SÁNH CÁC GÓI CƠ BẢN (Nằm ngang hoặc Lưới)   │
│ ┌──────────────────────┐  ┌──────────────────────┐     │
│ │ Gói Mê Phim (CINE)   │  │ Gói Thể Thao (SPORT) │     │
│ │ 50.000đ / 30 ngày    │  │ 90.000đ / 90 ngày    │     │
│ │ [ Chọn gói này ]     │  │ [ Chọn gói này ]     │     │
│ └──────────────────────┘  └──────────────────────┘     │
└────────────────────────────────────────────────────────┘
```
