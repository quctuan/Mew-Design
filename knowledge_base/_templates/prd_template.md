# [Tên Dự án] - Product Requirements Document (PRD)

> **Mã dự án:** `{PROJECT_CODE}` | **Phiên bản:** `v1.0-draft` | **Ngày tạo:** `{YYYY-MM-DD}`  
> **Product Manager:** `{PM_NAME}` | **Khách hàng / Stakeholder:** `{CLIENT_NAME}`  
> **Trạng thái:** `[ ] Bản thảo (Draft)  [ ] Đang thẩm định (In-Review)  [ ] Đã phê duyệt (Approved)`

---

## 1. Tổng quan & Bối cảnh Sản phẩm (Overview & Context)

### 1.1. Tuyên bố Vấn đề (Problem Statement)
*Mô tả thực trạng, nỗi đau (pain point) của người dùng hiện tại và lý do tại sao dự án này cần được thực hiện.*

### 1.2. Mục tiêu Kinh doanh & Sản phẩm (Goals & Success Metrics)
- **Mục tiêu chính:** ...
- **Chỉ số đo lường thành công (KPIs / Metrics):**
  - Tỷ lệ hoàn thành tác vụ (Task Completion Rate): `> 85%`
  - Thời gian thao tác trung bình: Giảm `30%`
  - Tỷ lệ lỗi người dùng (User Error Rate): `< 5%`

---

## 2. Đối tượng Người dùng & Kịch bản (User Personas & Scenarios)

### 2.1. Chân dung Người dùng Cốt lõi (Primary Persona)
- **Họ và tên:** `{PERSONA_NAME}` (Ví dụ: Chuyên viên kinh doanh lưu động)
- **Đặc điểm:** Thường xuyên thao tác trên smartphone, mạng chập chờn, cần tốc độ nhanh.
- **Nỗi đau lớn nhất:** Thao tác nhập liệu quá nhiều bước, thông báo lỗi khó hiểu.

### 2.2. Kịch bản Hành trình (Core Scenario)
*Mô tả một tình huống thực tế khi người dùng mở ứng dụng và hoàn thành tác vụ cốt lõi.*

---

## 3. Ranh giới Phạm vi Dự án (Scope Boundary)

| Phân loại | Danh mục Màn hình / Tính năng | Ghi chú |
| :--- | :--- | :--- |
| **Nằm trong phạm vi (In-Scope)** | • Đăng nhập / Xác thực OTP<br>• Màn hình Trang chủ Dashboard<br>• Luồng Đặt hàng / Thanh toán<br>• Lịch sử giao dịch | Hoàn thiện UX flow + UI Design Tokens + 2 vòng chỉnh sửa |
| **Nằm ngoài phạm vi (Out-of-Scope)** | • Tích hợp cổng thanh toán quốc tế Stripe<br>• Hệ thống Chat thời gian thực<br>• Ứng dụng Desktop chuyên biệt | Sẽ xem xét ở Giai đoạn V2 |

---

## 4. Danh mục Yêu cầu Chức năng (Functional Requirements)

| ID | Phân hệ / Module | Tên Chức năng | Mô tả Chi tiết | Mức độ Ưu tiên |
| :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Authentication | Đăng nhập OTP SMS | Gửi mã xác thực 6 số qua SMS, thời gian hiệu lực 60s | **P0 (Must-have)** |
| **FR-002** | Dashboard | Thống kê Tổng quan | Hiển thị số dư ví, 3 giao dịch gần nhất dạng card | **P0 (Must-have)** |
| **FR-003** | Notification | Bộ lọc Thông báo | Cho phép lọc theo thông báo biến động số dư và khuyến mại | **P1 (Should-have)** |

---

## 5. User Stories & Tiêu chuẩn Nghiệm thu (Gherkin Format)

### US-01: Người dùng đăng nhập hệ thống bằng số điện thoại
> **Là một** khách hàng đã có tài khoản,  
> **Tôi muốn** đăng nhập nhanh bằng số điện thoại và mã OTP,  
> **Để** tôi có thể truy cập ví điện tử một cách an toàn mà không cần nhớ mật khẩu phức tạp.

#### Kịch bản 1: Nhập OTP chính xác (Happy Path)
```gherkin
Scenario: Đăng nhập thành công với mã OTP hợp lệ
  Given Người dùng đang ở màn hình "Xác thực OTP" và mã OTP đã được gửi đến số điện thoại
  When Người dùng nhập chính xác 6 chữ số OTP
  Then Hệ thống xác thực thành công và tự động chuyển hướng người dùng vào màn hình "Trang chủ"
```

#### Kịch bản 2: Nhập sai mã OTP (Unhappy Path)
```gherkin
Scenario: Người dùng nhập sai mã OTP
  Given Người dùng nhập sai ít nhất 1 chữ số trong mã OTP
  When Người dùng bấm nút "Xác nhận"
  Then Hệ thống giữ nguyên mã đã nhập, hiển thị thông báo lỗi màu đỏ cam: "Mã OTP chưa chính xác. Bạn còn 2 lần thử lại."
```

---

## 6. Yêu cầu Phi Chức năng (Non-Functional Requirements)

- **Thời gian phản hồi:** Mọi thao tác chuyển màn hình trên prototype < 200ms.
- **Tiêu chuẩn Tiếp cận (Accessibility):** Tương phản màu tối thiểu chuẩn WCAG 2.1 AA (độ tương phản text vs nền tối thiểu 4.5:1).
- **Hỗ trợ Đa kích thước màn hình:** Tương thích chuẩn màn hình iOS (iPhone 13-16) và Android (Full HD+).

---

## 7. Kế hoạch Triển khai & Mốc Milestones (Timeline)

| Mốc (Milestone) | Nội dung Công việc | Người phụ trách | Hạn hoàn thành | Deliverable |
| :--- | :--- | :--- | :--- | :--- |
| **M1: UX Specs** | Khảo sát, vẽ sơ đồ Mermaid, viết UX Copy | UX Designer | Ngày 05 | `UX_Spec.md` |
| **M2: UI Concept** | Thiết lập Design Tokens, 3 màn hình chính | UI Designer | Ngày 10 | Figma Concept |
| **M3: UI Master** | Hoàn thiện toàn bộ màn hình + Prototype | UI Designer | Ngày 18 | Full Figma File |
| **M4: Handover** | Bàn giao tài sản, biên bản nghiệm thu | PM & Legal | Ngày 20 | Bàn giao hoàn tất |
