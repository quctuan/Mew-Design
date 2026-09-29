---
name: mermaid-optimization
description: Kỹ năng chuẩn hóa và tối ưu sơ đồ luồng UX Flow bằng ngôn ngữ Mermaid.
---

# Mermaid Optimization Skill

Kỹ năng này dành riêng cho UX Designer & Writer để thống nhất cách trình bày luồng thao tác (UX Flow), đảm bảo sơ đồ sinh ra luôn dễ đọc, mạch lạc và chuẩn format của MyVNPT.

## Quy tắc Quy chuẩn Hình học & Cú pháp:
1. **Hướng luồng (Direction):** Luôn sử dụng `graph TD` (Từ trên xuống) hoặc `graph LR` (Từ trái sang phải) tùy thuộc độ dài luồng. Khuyến nghị dùng `TD`.
2. **Hình khối (Shapes):**
   - **Bắt đầu / Kết thúc:** Trạng thái bắt đầu hoặc kết thúc luồng phải dùng khối Bo góc `([Hành động mồi])`.
   - **Hành động / Quy trình (Process):** Dùng khối chữ nhật tiêu chuẩn `[Tên hành động]`.
   - **Kiểm tra / Điều kiện / Rẽ nhánh (Decision):** **BẮT BUỘC** dùng hình thoi `{Điều kiện?}` cho các điểm rẽ nhánh (Ví dụ: Lỗi mạng?, Tài khoản rỗng?).
3. **Mũi tên & Nhãn (Links & Labels):**
   - Sự di chuyển giữa các bước dùng mũi tên `-->`.
   - Các điểm từ nhánh điều kiện (Hình thoi) tỏa ra **BẮT BUỘC** phải có nhãn mô tả trên mũi tên `-- Nhãn -->` (Ví dụ: `-- Yes -->`, `-- Lỗi Timeout -->`).
4. **Edge Cases (Luồng rủi ro):**
   - Các nhánh dẫn đến luồng lỗi mượt mà (Unhappy path) cần được gộp lại rõ ràng, không vẽ đứt gãy.

## Ví dụ Chuẩn:
```mermaid
graph TD
    A([Bắt đầu: User bấm Thanh toán]) --> B{Kiểm tra Số dư}
    B -- Đủ -> C[Chuyển màn hình OTP]
    B -- Không đủ --> D[Hiển thị Toast: Cần nạp tiền]
    C --> E([Kết thúc: Thanh toán thành công])
    D --> F([Kết thúc: Hủy giao dịch])
```
