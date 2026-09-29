---
name: accounting-quotation
description: Kỹ năng định mức chi phí ngày công (Man-day), xây dựng mô hình báo giá thương mại 3-Tier (MVP, Standard, Enterprise), lập tiến độ giải ngân theo mốc nghiệm thu và tính toán hệ số đệm rủi ro cho Design Studio.
---

# Kỹ năng: Lập Báo giá & Quản lý Chi phí Dự án (Accounting Quotation)

## 📌 Tổng quan

Kỹ năng này cung cấp phương pháp luận chuẩn xác cho Studio Accountant để định lượng khối lượng công việc, tính toán đơn giá ngày công (Man-day), xây dựng mô hình báo giá 3-Tier linh hoạt và bảo vệ biên lợi nhuận cho Mew-Design Studio.

---

## 🧮 1. Công thức Định mức Chi phí (Pricing Formula)

Tổng ngân sách dự án được tính theo công thức:
$$\text{Tổng Báo Giá} = \left( \sum (\text{Số ngày công của từng Role} \times \text{Đơn giá ngày công}) + \text{Chi phí công cụ/Asset ngoài} \right) \times (1 + \text{Hệ số Đệm Rủi ro})$$

### Bảng Đơn giá Ngày công Tham chiếu (Studio Baseline Rates):
| Chuyên môn (Role) | Đơn giá / Ngày công (Tham chiếu) | Trách nhiệm tính phí |
| :--- | :--- | :--- |
| **Product Manager (PM)** | 2.500.000 VNĐ - 3.500.000 VNĐ | Phân tích bài toán, viết PRD, họp kickoff, quản lý tiến độ |
| **Senior UX Designer** | 3.000.000 VNĐ - 4.000.000 VNĐ | Nghiên cứu người dùng, vẽ Mermaid flows, viết UX copy |
| **Senior UI Designer** | 3.000.000 VNĐ - 4.500.000 VNĐ | Thiết kế Visual, Design Tokens, Component specs, Figma |
| **QA / Delivery Lead** | 2.000.000 VNĐ - 2.500.000 VNĐ | Kiểm tra đối soát Figma vs Specs, đóng gói bàn giao |

### Hệ số Đệm Rủi ro (Risk Buffer):
- **Dự án Chuẩn (+15%):** Khách hàng có tài liệu nghiệp vụ rõ ràng, ít bên liên quan.
- **Dự án Phức tạp (+25%):** Nghiệp vụ chuyên sâu (Fintech, Telco, Y tế), nhiều vòng kiểm duyệt hoặc yêu cầu tiến độ gấp (Rush Fee).

---

## 🎯 2. Mô hình Báo giá Thương mại 3-Tier (3-Tier Pricing Model)

Khi gửi báo giá cho khách hàng bên ngoài, Accountant luôn lập 3 phương án để tối ưu hóa tỷ lệ chuyển đổi:

| Tiêu chí | Tier 1: MVP Tinh Gọn | Tier 2: Tiêu Chuẩn (Khuyên dùng) | Tier 3: Enterprise / Flagship |
| :--- | :--- | :--- | :--- |
| **Mục tiêu** | Ra mắt thử nghiệm nhanh (POC) | Sản phẩm thương mại hoàn chỉnh | Hệ sinh thái quy mô lớn, thương hiệu dẫn đầu |
| **Phạm vi Màn hình** | 5 - 8 màn hình cốt lõi | 15 - 25 màn hình + Toàn bộ Edge cases | 30+ màn hình + Nhiều phân hệ phức tạp |
| **UX Specs** | Sơ đồ luồng cơ bản | Full Mermaid Flow + Bảng UX Writing | Full User Journey + IA đa tầng + Usability Audit |
| **UI Design System** | Token màu và font cơ bản | Design System V1 hoàn chỉnh | Design System V2 đa nền tảng (Web/App), Micro-physics |
| **Vòng Feedback** | 01 vòng chỉnh sửa | 02 vòng chỉnh sửa chính thức | 03 vòng chỉnh sửa + Họp Review chuyên sâu |
| **Thời gian thực hiện** | 7 - 10 ngày làm việc | 15 - 20 ngày làm việc | 30 - 45 ngày làm việc |

---

## 💳 3. Lịch trình Thanh toán An toàn (Payment Milestones)

Tuyệt đối không bắt đầu làm việc nếu chưa nhận cọc. Cấu trúc thanh toán mặc định:
- **Đợt 1 (40%):** Tạm ứng ngay sau khi ký Hợp đồng dịch vụ (Kick-off Deposit).
- **Đợt 2 (40%):** Thanh toán sau khi nghiệm thu Giai đoạn UX (Wireframe & Sơ đồ luồng Mermaid được duyệt).
- **Đợt 3 (20%):** Thanh toán nốt trong vòng 05 ngày sau khi bàn giao toàn bộ file Figma gốc và biên bản nghiệm thu cuối cùng.

---

## 📄 Mẫu Bảng Báo Giá Chi Tiết (Quotation Sheet)

```markdown
# BẢNG BÁO GIÁ DỊCH VỤ THIẾT KẾ UI/UX
**Kính gửi:** {TEN_KHACH_HANG}
**Dự án:** {TEN_DU_AN}
**Ngày lập:** {NGAY_LAP} | **Hiệu lực báo giá:** 15 ngày kể từ ngày gửi

---

### Bảng Phân Tích Khối Lượng & Chi Phí (Gói Tiêu Chuẩn)
| STT | Hạng mục Công việc | Số ngày công (Man-days) | Đơn giá / Ngày | Thành tiền (VNĐ) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Phân tích Brief & Lập PRD (PM) | 2 | 3.000.000 | 6.000.000 |
| 2 | Kiến trúc Thông tin & Luồng UX (UX) | 4 | 3.500.000 | 14.000.000 |
| 3 | Chế tác Visual UI & Design System (UI) | 6 | 4.000.000 | 24.000.000 |
| 4 | Kiểm thử QA & Bàn giao Kỹ thuật | 2 | 2.000.000 | 4.000.000 |
| **Tổng chi phí trực tiếp:** | | **14 ngày** | | **48.000.000 VNĐ** |
| **Dự phòng rủi ro & Quản lý (15%):** | | | | **7.200.000 VNĐ** |
| **TỔNG GIÁ TRỊ DỰ ÁN (Chưa VAT):** | | | | **55.200.000 VNĐ** |

### Điều khoản Thanh toán:
- Đợt 1: 40% (22.080.000 VNĐ) khi ký hợp đồng.
- Đợt 2: 40% (22.080.000 VNĐ) sau khi chốt luồng UX.
- Đợt 3: 20% (11.040.000 VNĐ) khi bàn giao file thiết kế hoàn chỉnh.
```
