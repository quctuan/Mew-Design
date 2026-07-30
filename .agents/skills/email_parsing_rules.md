---
description: Kỹ năng đọc hiểu, bóc tách và tổng hợp dữ liệu từ nội dung Email nguyên bản và Tài liệu đính kèm.
---

# Hướng dẫn Xử lý Dữ liệu Email (Email Parsing Rules)

Kỹ năng này được sử dụng bởi `@Email Requirements Analyst` để phân tích Dữ liệu Text Email và File Đính Kèm, từ đó biến chúng thành **Master Input** - "mồi chuẩn" cho các bước phân tích UX/UI tiếp theo.

## Quy tắc 1: Khử Nhiễu (Noise Reduction)
Khi nhận được khối văn bản (text) từ một email (thường bị dán kèm chuỗi hội thoại dài hoặc chữ ký auto từ Webmail):
1. **Loại bỏ/Bỏ qua:** Chữ ký (Signatures), Thông báo auto-reply hệ thống, Lời chúc/chào hỏi xã giao, Các thông tin liên lạc cá nhân không liên quan quy trình.
2. **Giữ lại:** Bối cảnh (Ai chat với ai?), Sự cố (Bug report), Yêu cầu tính năng mới (Feature Request), Phản hồi của người dùng (Feedback/Complaint), hoặc Thay đổi nghiệp vụ (Business Rule Change).

## Quy tắc 2: Đối chiếu chéo Đính kèm (Cross-referencing Attachments)
- **Nếu Boss có cung cấp file / text đính kèm (Câu hỏi 2):**
  - Đọc và tóm tắt những ý chính của file đính kèm ĐÓNG GÓP vào bối cảnh chung của Email. 
  - Nếu Email nói Vấn đề A nhưng File Đính kèm chỉ ra Hình ảnh/Chi tiết của A, hãy gộp chúng lại.
- **Nếu Boss trả lời "Bỏ qua" ở Câu hỏi 2:**
  - Bỏ qua các khâu đối chiếu chéo. Chỉ xử lý nội dung văn bản từ Câu 1.

## Quy tắc 3: Định dạng Đầu ra Cuối Cùng (Master Input Structure)
Bạn phải tổng hợp tất cả hiểu biết của mình từ Câu 1 (và Câu 2 nếu có) và TRẢ VỀ kết quả CHUẨN XÁC theo cấu trúc sau. 
TUYỆT ĐỐI KHÔNG thêm lời giải thích cá nhân lan man bên ngoài cấu trúc này.

```markdown
# 📨 MASTER INPUT: [Đặt một Tiêu đề ngắn gọn mô tả cốt lõi yêu cầu Email]

**1. Nguồn yêu cầu:**
- *Người gửi / Thực thể liên quan:* (Nếu nhận diện được, ví dụ: Khách hàng KHDN, Dev, PO...)
- *Phân loại Yêu cầu:* [Bug / Feature Request / UX Feedback / Business Change]

**2. Bối cảnh & Vấn đề Cốt lõi (The Core Problem):**
- *Tóm tắt Bối cảnh:* (Mô tả thật ngắn gọn trong 2-3 câu: chuyện gì đang xảy ra, hệ thống web/app gặp vấn đề gì).
- *Trích dẫn nguyên gốc (Quotes):* (Trích nguyên văn 1-2 câu quan trọng nhất từ Email/File liên quan trực tiếp đến tính năng / nỗi đau).

**3. Yêu cầu Cụ thể / Mong đợi (The Expectation):**
- (Liệt kê dưới dạng danh sách gạch đầu dòng những gì email bắt buộc chúng ta làm).

**4. Dữ liệu bổ sung (Từ File Đính kèm - Nếu có):**
- (Liệt kê các chi tiết kỹ thuật/hình ảnh. Nếu Boss nói "Bỏ qua", ghi "Không có").
```

*Lưu ý cho `@Email Requirements Analyst`: Khi bạn in ra mẫu **Master Input** này, bước 1 của quy trình thành công trọn vẹn và đã có dữ kiện chuẩn mực cho Bước 2.*
