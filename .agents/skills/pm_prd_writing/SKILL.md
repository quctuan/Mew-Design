---
name: pm-prd-writing
description: Kỹ năng chuyên sâu dành cho Product Manager biên soạn tài liệu PRD, phân tích User Stories, viết tiêu chuẩn nghiệm thu Gherkin (Given-When-Then) và phân rã Sprint Task WBS cho Design Studio.
---

# Kỹ năng: Biên soạn PRD & Quản lý Sprint (PM PRD Writing)

## 📌 Tổng quan

Kỹ năng này hướng dẫn Product Manager / Design Producer cách chuyển hóa các yêu cầu sơ khai từ khách hàng hoặc stakeholder thành một bộ tài liệu **Product Requirements Document (PRD)** chặt chẽ, khả thi và rõ ràng để làm kim chỉ nam cho toàn bộ đội ngũ thiết kế UX/UI.

---

## 🛠️ Quy trình Triển khai 5 Bước (Step-by-Step Workflow)

### Bước 1: Xác lập Phạm vi Dự án (Scope Boundary)
- **Problem Statement:** Mô tả vấn đề cốt lõi mà người dùng đang gặp phải và tại sao doanh nghiệp cần giải quyết vấn đề này ngay bây giờ.
- **In-Scope:** Liệt kê tường minh tất cả các màn hình, chức năng và tính năng sẽ được thiết kế trong phiên bản này.
- **Out-of-Scope:** Liệt kê rõ ràng những gì **KHÔNG** làm (để ngăn ngừa rủi ro phình phạm vi và tranh cãi sau này).

### Bước 2: Chân dung Người dùng & Kịch bản Sử dụng (User Persona & Scenarios)
- Xác định 1 - 2 Persona chính (Mục tiêu, Nỗi đau - Pain points, Động lực hành động).
- Phác thảo hành trình cốt lõi (Core User Journey) từ điểm bắt đầu đến khi hoàn thành mục tiêu.

### Bước 3: Danh sách Yêu cầu Chức năng (Functional Requirements)
Đánh số ID duy nhất cho từng yêu cầu theo cấu trúc: `[FR-XXX]`.
Mỗi yêu cầu chức năng phải nêu rõ:
- Tên chức năng
- Mô tả hành vi
- Mức độ ưu tiên (P0: Must-have, P1: Should-have, P2: Nice-to-have)

### Bước 4: Viết User Story theo Định dạng Gherkin
Với mỗi tính năng chính, bắt buộc viết theo cấu trúc:
```gherkin
User Story: Là một [Đối tượng người dùng], tôi muốn [Hành động/Mong muốn], để [Mục đích/Giá trị đạt được].

Scenario: [Tên kịch bản kiểm thử]
  Given [Tiền điều kiện / Trạng thái ban đầu của hệ thống]
  When [Hành động người dùng thực hiện]
  Then [Kết quả kỳ vọng mà hệ thống phản hồi]
```

### Bước 5: Phân rã Công việc (Work Breakdown Structure - WBS) & Mốc Milestones
Chia nhỏ dự án thành các giai đoạn cụ thể:
1. **Milestone 1:** Khảo sát & Chốt Luồng UX (UX Wireflow & IA)
2. **Milestone 2:** Chốt Visual Concept & Design Tokens (V1)
3. **Milestone 3:** Hoàn thiện Toàn bộ Màn hình & Prototype Tương tác (V2)
4. **Milestone 4:** Bàn giao Assets & Hỗ trợ Kiểm thử Kỹ thuật (Dev Handoff)

---

## 📄 Cấu trúc Khung Mẫu PRD Chuẩn (Standard PRD Skeleton)

```markdown
# [Tên Dự án] - Product Requirements Document (PRD)

- **Mã dự án:** {PROJECT_CODE}
- **Phiên bản:** {VERSION} (ví dụ: v1.0)
- **Tác giả (PM):** {AUTHOR_NAME}
- **Trạng thái:** [Draft / In-Review / Approved]
- **Đường dẫn lưu trữ:** `knowledge_base/projects/{PROJECT_CODE}/03_product_specs/PRD_{PROJECT_CODE}.md`

---

## 1. Bối cảnh & Mục tiêu Sản phẩm (Context & Goals)
- **Vấn đề cần giải quyết:** ...
- **Chỉ số đo lường thành công (Success Metrics / KPIs):** ...

## 2. Phạm vi Dự án (Scope Definition)
- **Nằm trong phạm vi (In-Scope):** ...
- **Nằm ngoài phạm vi (Out-of-Scope):** ...

## 3. Danh sách Yêu cầu Chức năng (Functional Requirements)
| ID | Module / Màn hình | Tên Tính năng | Mô tả Chi tiết | Mức độ ưu tiên |
| :--- | :--- | :--- | :--- | :--- |
| FR-01 | Onboarding | Đăng nhập bằng OTP | Xác thực OTP 6 số qua SMS trong 60s | P0 |

## 4. User Stories & Tiêu chuẩn Nghiệm thu (Acceptance Criteria)
### Story 1: [Tên Story]
...

## 5. Yêu cầu Phi Chức năng (Non-Functional Requirements)
- Khả năng phản hồi giao diện (< 200ms)
- Tiêu chuẩn khả năng tiếp cận (Accessibility WCAG AA)
- Tương thích thiết bị (iOS 15+, Android 11+, Web Responsive)

## 6. Kế hoạch Triển khai (Timeline & Milestones)
...
```
