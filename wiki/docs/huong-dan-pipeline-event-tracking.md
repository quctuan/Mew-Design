# 📑 HƯỚNG DẪN VẬN HÀNH PIPELINE EVENT TRACKING TỰ ĐỘNG (GDS STANDARD 2026)

Tài liệu này đặc tả quy trình sử dụng trợ lý AI (Antigravity) để tự động hóa việc thiết kế và quản trị dữ liệu Event Tracking cho dự án GDS VNPT.

---

## Ⅰ. MỤC ĐÍCH CỦA PIPELINE (PURPOSE) 🎯

Hệ thống được thiết kế nhằm tối ưu hóa quy trình làm việc của đội ngũ Product/BA qua các mục tiêu:
*   **Tăng tốc hiệu suất:** Giảm 90% thời gian soạn thảo thủ công bảng Event từ các tài liệu yêu cầu (URD/SRS).
*   **Quản trị tập trung:** Tự động đồng bộ hóa các định danh mới vào "Từ điển hệ thống" và duy trì file Master luôn cập nhật.
*   **Liên thông hành trình:** Đảm bảo mọi sự kiện đều có tính kết nối để phục vụ báo cáo hành trình khách hàng (CJM) chuyên sâu.

---

## Ⅱ. CÁC LỆNH ĐIỀU KHIỂN (COMMANDS) 🚀

Người dùng sử dụng các lệnh điều hướng sau kèm theo link Google Doc hoặc file nội dung URD:

| Câu lệnh (Slash Command) | Chức năng chính | Output mong đợi |
| :--- | :--- | :--- |
| **`/create_event_tracking [link hoặc URD]`** | **Tạo chuẩn Taxonomy:** Tự động đọc URD, phân hạch Event theo đúng chuỗi 27 quy tắc, bóc tách đa dòng 8 cột chuẩn xác và nhúng trực tiếp vào Master File. | Bảng Draft & Cập nhật Master File tập trung. |
| **`/workflow_event_tracking_master`** | **Điều phối Master Pipeline:** Gọi bảng hệ thống tổng hợp tất cả tiến trình Event Tracking (nếu cần xem luồng quy trình tổng). | Trả về thông tin Master Menu. |

---

## Ⅲ. CƠ CHẾ HOẠT ĐỘNG: AI SẼ LÀM GÌ? (PROCESSING FLOW) 🤖

Hạ tầng AI thực hiện quy trình xử lý khép kín qua 6 bước chi tiết:

1.  **🔍 Đọc tài liệu (Fetch & Analyze):** 
    - AI truy cập vào Link Google Doc được cung cấp hoặc đọc trực tiếp nội dung File URD.
    - Phân tích luồng (Funnel) từ UI/UX đến quá trình giao tiếp Backend (BE) để đảm bảo độ phủ 100%.
2.  **📔 Tra cứu Từ điển (Dictionary Lookup):** 
    - AI tự động truy cập vào file Master, tra cứu Sheet **[Tên màn hình]**.
    - Đối soát để tái sử dụng chính xác các `screen_name` đã có, đăng ký mới nếu chưa tồn tại.
3.  **🏗️ Áp dụng Phân hạch Hệ thống (Taxonomy Mapping):** 
    - AI **TỪ CHỐI** các tên Event tự chế. Thay vào đó, map toàn bộ thao tác vào Khung chuẩn cố định của MyVNPT:
        *   `service_screen_displayed` (Mở màn hình)
        *   `service_block_displayed` / `service_block_clicked` (Tương tác vùng/khối)
        *   `service_button_clicked` / `service_item_selected` (Tương tác Nút/Phần tử)
        *   `service_component_displayed` (Hiển thị Popup / Bottom Sheet)
        *   `ops_request_be` & `ops_receive_be` (Cặp bài trùng Gửi/Nhận API Backend)
4.  **📝 Chuẩn hóa Định dạng 8 Cột (8-Column Formatting):** 
    - Áp dụng cấu trúc hiển thị chia cắt (Split-row Presentation): 
        *   Hàng đầu tiên chứa đầy đủ thông tin mô tả Event.
        *   Tách biệt MỖI Tham số (Parameter) ra một hàng rỗng độc lập ở bên dưới.
    - Ép buộc định dạng text cho Google Sheets (Thêm dấu `'` trước dấu `=`, `<`).
5.  **💬 Hội ý & Hiệu chỉnh (Review):** 
    - AI hiển thị bảng dự thảo (Draft) ngay tại giao diện chat để PO/BA duyệt.
6.  **✅ Xuất bản (Publish):** 
    - Ghi dữ liệu trực tiếp vào Google Drive hoặc cập nhật Tab Master File.

---

## Ⅳ. QUY CHUẨN TUÂN THỦ (COMPLIANCE STANDARDS) 📐

Mọi dữ liệu xuất bản bắt buộc phải tuân thủ Tuyệt đối các nguyên tắc quản trị sau:

*   **🛡️ Tham số Gốc (Root Parameters):** Mọi sự kiện luôn luôn bao gồm cặp tham số bắt buộc: `partnerName = myvnpt` và `screenName` / `blockName` / `itemName`.
*   **🔗 Mạch liên thông UI/UX:** Đo lường chuyển đổi chi tiết bằng tham số UI phụ trợ: `fromFeature` (đến từ đâu), `itemCount` (số lượng phần tử) và `itemList` (danh sách phần tử phân tách bởi dấu `|`).
*   **⚙️ Giám sát Hiệu năng (Performance Monitoring):** Mọi sự kiện nhận phản hồi Backend (`ops_receive_be`) bắt buộc phải phải kẹp 3 tham số kỹ thuật: `apiName`, `duration` (ms) và `errorCode`.
*   **📔 Kỷ luật Tên màn (Screen Name):** Tuyệt đối chỉ sử dụng định danh từ **Từ điển màn hình**. Tuyệt đối không tự ý đẻ mã màn hình rác.

---
> 💡 *Sản phẩm được tối ưu bởi Đội ngũ Antigravity AI Implementation Team phục vụ GDS Standard 2026.*
