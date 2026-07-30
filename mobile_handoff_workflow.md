# 🚀 QUY TRÌNH HAND-OFF AI: DESIGN TO NATIVE MOBILE

Quy trình Hand-off Design-to-Code tiêu chuẩn đã được tinh chỉnh chuyên biệt cho **Mobile Native (iOS/Android)**. Quy trình này áp dụng chiến lược "Chia để trị" (Divide & Conquer) giúp AI hiểu sâu cấu trúc Auto Layout của Figma và dịch chuẩn xác ra ngôn ngữ khai báo UI hiện đại.

---

### PHẦN 1: ĐỒNG BỘ & CHUẨN BỊ (PRE-HANDOFF)
Trước khi gọi AI, bạn cần đảm bảo đầu vào đã sẵn sàng:
1. **Chốt Tech Stack:** Thống nhất với Dev về nền tảng: **iOS (Swift / SwiftUI)** và **Android (Kotlin / Jetpack Compose / XML)**.
2. **AI-Ready Audit (Chuẩn hóa Figma):**
   - 100% sử dụng **Auto-layout** từ ngoài vào trong. (Vô cùng quan trọng để AI dịch ra `VStack/HStack` của iOS hoặc `Column/Row` của Android).
   - Đặt tên Layer rõ ràng, có ngữ nghĩa (vd: `HeaderView`, `HeroSection`, `BottomBar`).
   - Đã gán toàn bộ **Design Tokens** (Color, Spacing, Typography). Không để giá trị tự do (px/hex).

---

### PHẦN 2: THỰC THI TRÍCH XUẤT (THE EXTRACTION)
*Lưu ý: Tuyệt đối KHÔNG extract toàn bộ luồng/file cùng lúc. Tiến hành theo thứ tự từ Kế hoạch -> Nền tảng -> Màn hình.*

**Bước 0: Lập kế hoạch kiến trúc (Planning)**
- **Mục tiêu:** Áp dụng kỹ năng `writing-plans` từ bộ `.dev full` để định hình cấu trúc Component Tree trước khi code.
- **Hành động:** Phân tách bản vẽ Figma thành danh sách các Component cần làm. Xác định rõ Component nào là Atoms, Component nào chứa logic phức tạp.

**Bước 1: Trích xuất Nền tảng (Foundation & Tokens)**
- **Mục tiêu:** Dạy AI "ngôn ngữ" của Design System trên nền tảng Mobile.
- **Hành động:** Yêu cầu AI dùng MCP quét toàn bộ Tokens (màu sắc, khoảng cách, font chữ, shadow).
- **Kết quả:** Sinh ra các file Theme cốt lõi. Kể từ lúc này, mọi giao diện bắt buộc gọi từ biến, **nghiêm cấm hardcode hex/dp/pt**.

**Bước 2: Trích xuất Component nguyên tử (Atomic Level)**
- **Mục tiêu:** Xây dựng thư viện UI View tái sử dụng chuẩn 100%.
- **Hành động:** Kích hoạt `executing-plans` để code tuần tự theo bản thiết kế ở Bước 0. Truyền `NodeID` của từng component nhỏ cho AI đọc kỹ toàn bộ trạng thái (States: Pressed, Disabled, Focused).
- **Kết quả:** File View độc lập sử dụng Modifiers chuẩn.

**Bước 3: Trích xuất Màn hình cụ thể (Screen Level)**
- **Mục tiêu:** Ráp nối giao diện màn hình lớn.
- **Hành động:** Truyền `NodeID` của **một màn hình duy nhất**. Dịch cấu trúc Auto Layout thành các khối logic. Nếu gặp lỗi vỡ Layout hoặc sai margin/padding, BẮT BUỘC kích hoạt kỹ năng `systematic-debugging` để rà soát có hệ thống thay vì sửa mò.
- **Kết quả:** File code Screen hoàn chỉnh chuẩn xác tỷ lệ màn hình điện thoại.

---

### PHẦN 3: KIỂM ĐỊNH & BÀN GIAO (QA & HANDOFF)
1. **Kiểm thử tự động (Verification & QA):**
   - Kích hoạt kỹ năng `verification-before-completion` để tự đánh giá lại độ chuẩn xác (1:1 Visual Parity).
   - Build và chạy code trên **Simulator (iOS)** hoặc **Emulator (Android)**. Chụp ảnh màn hình app thực tế và đối chiếu với Node gốc trên Figma để căn chỉnh những sai số nhỏ nhất.
2. **Đóng gói (Packaging):**
   - Lưu đoạn code hoàn thiện thành file (ví dụ: `ProductCard.swift` hoặc `ProductCard.kt`).
   - Đính kèm file này cùng Link Figma để bàn giao cho Mobile Dev.

---

### 💡 CÚ PHÁP PROMPT "ĐÓNG GÓI" TIÊU CHUẨN (CHO MOBILE)
Khi cần extract một màn hình, hãy copy/paste nguyên văn Prompt dưới đây:

> *"Hãy đóng vai một Mobile Developer. Đọc kỹ màn hình (NodeID: [Điền ID]) qua MCP Figma. Nhiệm vụ của bạn là xuất ra file code UI cho màn hình này.*
> 
> ***Yêu cầu bắt buộc:***
> *- **Nền tảng:** Dùng [iOS (SwiftUI) / Android (Jetpack Compose)].*
> *- **Chiến lược:** Đọc Design System Tokens trước. Không viết tất cả màn hình vào 1 file view khổng lồ, hãy phân tách thành các View/Composable hợp lý.*
> *- **Độ chính xác:** Bám sát tuyệt đối Design Tokens (padding, gap, colors). Ánh xạ chuẩn xác cấu trúc Auto Layout thành [VStack, HStack / Column, Row].*
> *- **Quy tắc cứng:** TUYỆT ĐỐI KHÔNG hardcode mã màu Hex hay giá trị px/dp/pt gõ tay. Cần tuân thủ Life-cycle và hỗ trợ tốt hiển thị trên các kích thước màn hình Mobile khác nhau (Responsive/Adaptive)."*
