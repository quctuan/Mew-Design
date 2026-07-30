# 📄 [TEMPLATE] TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (URD)
## [TÊN_YÊU_CẦU_DỰ_ÁN]

## LỊCH SỬ THAY ĐỔI
| Ngày | Phiên bản | Người thực hiện | Nội dung thay đổi |
| :--- | :--- | :--- | :--- |
| [DD/MM/YYYY] | 1.0.0 | Antigravity (AI BA) | Khởi tạo tài liệu |

---

## 1. Bối cảnh & Mục tiêu (Business)
### 1.1. Bối cảnh
[Mô tả tại sao cần tính năng này, vấn đề hiện tại là gì?]

### 1.2. Mục tiêu
- [Mục tiêu 1]
- [Mục tiêu 2]
- **Value:** [Giá trị mang lại cho KH hoặc Công ty]

---

## 2. Trải nghiệm người dùng & UX/UI
### 2.1. Trải nghiệm tổng quát
- **Phạm vi áp dụng:** [App/Web/Tất cả]
- **Đối tượng:** [Loại khách hàng mục tiêu]
- **Điểm chạm:** [Màn hình nào, vị trí nào trên App]

### 2.2. Đặc tả chi tiết các thành phần giao diện
| Thành phần UI | Khi nào hiển thị? (Condition) | Quy tắc nội dung & Dữ liệu (Rules) | Hành động khi Click (Action) |
| :--- | :--- | :--- | :--- |
| [Tên Component] | [Điều kiện logic để hiện] | [Text, màu sắc, ưu tiên hiển thị] | [Deep-link, mở popup, hay chuyển màn] |

---

## 3. Quy trình Step-by-step & Rule Hệ thống
### 3.1. Bảng trình tự tương tác hệ thống (Logic Table)
| STT | Đối tượng gửi | Đối tượng nhận | Hành động / Dữ liệu trao đổi | Ghi chú nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [User/App/SYS] | [User/App/SYS] | [Lệnh/Dữ liệu] | [Mô tả màn hình/Logic ngầm] |

### 3.2. Business Rules (Quan trọng)
- [Rule 1: Giới hạn, tần suất]
- [Rule 2: Logic thời gian, múi giờ]
- [Rule 3: Các case ngoại lệ]

---

## 4. Đặc tả Truyền thông (Communication)
### 4.1. Nội dung Push Notification
- **Tiêu đề:** [Text]
- **Nội dung:** [Text bao gồm cả biến số dynamic nếu có]

### 4.2. Nội dung SMS
- **Nội dung:** [Sms không dấu chuẩn GDS]

---

## 5. Đặc tả Event Tracking (CJM Standard)
| Luồng | Tên màn hình | ID | Trigger | Event Name | Param Name | Operator | Param Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| [Flow Name] | [Screen_Name] | [ID] | [Hành động trigger] | [service_...] | [Tham số] | [=] | [Giá trị] |

---

## 6. Vận hành & Testing
- [ ] Kiểm tra logic cộng điểm / Đăng ký.
- [ ] Kiểm tra chặn lặp / Giới hạn.
- [ ] Kiểm tra CJM Log thực tế.
