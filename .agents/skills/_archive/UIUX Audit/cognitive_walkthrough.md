---
name: cognitive-walkthrough
description: Kỹ năng mô phỏng luồng suy nghĩ của người dùng để phát hiện điểm mù nhận thức (Cognitive Load).
---

# Cognitive Walkthrough Skill

Kỹ năng Đóng vai người dùng, tự đặt câu hỏi ở mỗi bước màn hình để tìm ra những điểm thiết kế làm người dùng bối rối hoặc phải suy nghĩ quá nhiều.


## 4 Câu hỏi Cốt lõi cho mỗi bước (Standard Walkthrough)
1. Ý định (Intent): Người dùng có biết mình cần thực hiện hành động này để tiến gần hơn đến mục tiêu không?
2. Khả năng quan sát (Visibility): Nút bấm hoặc điểm tương tác có xuất hiện rõ ràng trong tầm mắt không, hay bị che lấp bởi các yếu tố khác?
3. Liên tưởng ý nghĩa (Mapping & Semantics): Người dùng có hiểu đúng nhãn (label), biểu tượng (icon) hoặc từ ngữ trên nút bấm sẽ dẫn đến kết quả họ muốn không?
4. Phản hồi (Feedback): Sau khi thực hiện thao tác, hệ thống có phản hồi tức thì để xác nhận trạng thái thành công hay thất bại không?


## Bộ câu hỏi Chuyên sâu kiểm tra Tải nhận thức (Cognitive Load)
1. Tải nhận thức Thị giác (Visual & Processing Load)
•	Độ nhiễu giao diện: Có quá nhiều thành phần (banner, hình ảnh, văn bản, nút bấm) cùng lúc cạnh tranh sự chú ý trên một màn hình không?
•	Điểm tập trung (Visual Anchor): Khi vừa mở màn hình, mắt người dùng có nảy ngay đến hành động chính (Primary Call-to-Action) không, hay bị phân tán?
•	Luồng thị giác (Visual Flow): Bố cục thông tin có đi theo luồng đọc tự nhiên (từ trên xuống dưới, từ trái sang phải) không, hay bắt mắt người dùng phải di chuyển liên tục giữa các góc màn hình?

2. Áp lực Bộ nhớ ngắn hạn (Working Memory Load)
•	Yêu cầu ghi nhớ: Người dùng có bắt buộc phải nhớ thông tin từ màn hình trước (ví dụ: giá tiền, mã đơn hàng, thông số đã chọn) để đưa ra quyết định ở màn hình này không?
•	Sự quen thuộc (Mental Model): Thuật ngữ, biểu tượng hoặc luồng thao tác có tuân theo thói quen phổ biến không, hay bắt người dùng phải đoán/học lại từ đầu?
•	Bối cảnh hiện tại: Giao diện có hiển thị rõ người dùng đang ở bước nào trong tổng thể quy trình (Progress Indicator) không?

3. Gánh nặng Ra quyết định (Decision Load & Hick's Law)
•	Số lượng lựa chọn: Màn hình có đưa ra quá nhiều tùy chọn có độ ưu tiên ngang nhau khiến người dùng bị do dự (Choice Paralysis) không?
•	Độ rõ ràng của Microcopy: Nội dung trên nút bấm có ghi rõ hành động cụ thể không (ví dụ: "Thanh toán 250.000đ" thay vì nút "Tiếp tục" chung chung)?
•	Thiết lập mặc định (Smart Defaults): Các trường thông tin có được điền sẵn hoặc gợi ý hợp lý để giảm thiểu số thao tác gõ/chọn của người dùng không?

4. Xử lý Lỗi & Dự phòng (Error & Anxiety Load)
•	Tâm lý lo ngại: Người dùng có sợ bấm nhầm nút này vì không biết điều gì sẽ xảy ra tiếp theo không (có bị mất tiền, mất dữ liệu không)?
•	Rõ ràng về lỗi: Khi nhập sai hoặc gặp lỗi, thông báo lỗi có xuất hiện ngay tại vị trí lỗi kèm hướng dẫn sửa chi tiết không?
•	Khả năng hoàn tác: Giao diện có cho phép người dùng quay lại hoặc hủy bỏ thao tác một cách dễ dàng và an toàn không?
