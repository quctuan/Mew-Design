---
name: edge-case-analysis
description: Kỹ năng quét và phát hiện các luồng rẽ nhánh, lỗi (Unhappy Paths) mà Designer thường quên.
---

# Edge Case Analysis Skill

Kỹ năng tư duy phản biện để tìm ra các trạng thái "hiếm gặp nhưng làm vỡ luồng" của sản phẩm.

## Bộ lọc kiểm tra Edge Cases:
- **Empty States (Trạng thái Rỗng):** Chuyện gì xảy ra nếu Giỏ hàng trống? Danh sách lịch sử trống? Người dùng mới chưa có dữ liệu?
- **Error States (Trạng thái Lỗi):** Mất kết nối Mạng? API lỗi? Server sập? Lỗi nhập form sai định dạng?
- **Limit/Boundary States (Giới hạn):** Nhập quá số ký tự cho phép? Mật khẩu quá yếu? Tên người dùng quá dài làm vỡ layout? Số dư ví bằng 0 nhưng vẫn bấm thanh toán?
- **Interruption States (Gián đoạn):** Đang tải thì có cuộc gọi đến? Đang tải thì người dùng bấm Back? Thoát app đột ngột?
