---
description: Pipeline Event Tracking GDS (Bản Chuẩn Taxonomy 2026) - Đọc URD, Ép chuẩn Taxonomy và xuất dữ liệu Đa dòng.
---
# 📁 /create_event_tracking [link hoặc file URD]

## 🎯 MỤC ĐÍCH (PURPOSE)
Hệ thống AI sẽ đóng vai trò Data Analyst, tự động đọc luồng từ URD và bóc tách thành một danh sách sự kiện Tracking **tuân thủ nghiêm ngặt 100% Taxonomy** của MyVNPT (Chuẩn 27 Events), sau đó tự động thiết kế định dạng đa dòng (Split-row) để đổ vào Master File.

---

## 🛑 BỘ LUẬT BẮT BUỘC KHI SINH EVENT (CRITICAL RULES)

### 1. Luật Cấm Đặt Tên (Taxonomy Mapping)
AI **tuyệt đối không được** tự sáng tạo tên Event. Bắt buộc phải sử dụng các danh từ quy tắc sau:
- Mở một màn hình mới -> `service_screen_displayed`
- Tương tác với khối / danh sách -> `service_block_displayed` hoặc `service_block_clicked`
- Bấm vào một Nút (Button) -> `service_button_clicked`
- Chọn một mục / Cấu hình (Toggle / Item) -> `service_item_selected`
- Mở một Popup / Bottom Sheet -> `service_component_displayed`
- Nút bấm nằm trên Popup/BottomSheet -> Thêm tham số `componentType` và `componentName` đi kèm `service_button_clicked`.
- Gọi một API Backend -> LUÔN tách thành cặp 2 event: `ops_request_be` (Gửi) và `ops_receive_be` (Nhận/Phản hồi).

### 2. Luật Tham Số Bắt Buộc (Mandatory Parameters)
- Tất cả Event đều phải có: `partnerName = myvnpt`.
- Nhóm Ui/UX phải có: `screenName`, `blockName`, `buttonName`, `itemName` (tùy ngữ cảnh).
- Các luồng danh sách phải kèm: `itemCount` và `itemList`.
- Nhóm Backend (`ops_receive_be`) BẮT BUỘC có: `apiName`, `duration` (ms), `status`, `errorCode` (nullAble).

### 3. Luật Định Dạng Form Xuất Bản (8-Column Presentation)
Khi thiết kế mảng dữ liệu (để đưa vào Google Sheets hoặc vẽ Draft), AI bắt buộc phải phân tách theo luật sau:
- Cột quy định: `Luồng`, `Tên màn hình`, `ID`, `Trigger`, `Event name`, `Param name`, `Param operator`, `Param value`.
- Tách tham số: Một sự kiện có N tham số sẽ chiếm N dòng ngang.
- **Hàng đầu tiên** ghi đầy đủ 5 thông tin đại diện: `Luồng`, `Tên màn hình`, `ID`, `Trigger`, `Event name`.
- **Hàng số 2 trở đi**: 5 cột đầu tiên phải để **RỖNG (BLANK)**, chỉ điền tiếp các Tham số ở 3 cột cuối.
- Dấu hiển thị: Trước các ký tự `=`, `<` phải thêm dấu `'` (Ví dụ: `'=`, `'<nullAble>`) để chống lỗi Function trên Google Sheets.

### 4. Luật Đặt Tên Màn Hình (Screen Naming Convention)
Khi đặt tên màn hình (`screenName`), AI tuân thủ theo nguyên tắc ưu tiên sau:
- **Ưu tiên 1:** Sử dụng chính xác mã màn hình (nếu có) do người dùng (PO) đã ghi sẵn trong URD.
- **Ưu tiên 2:** Tự động khởi tạo theo quy chuẩn tiền tố bắt buộc:
  - `SCR_`: Màn hình full (Các màn hình chính, chiếm toàn bộ thiết bị. VD: Homepage, Profile).
  - `POP_`: Pop-up/ Modal (Các popup nổi lên giữa màn hình yêu cầu thao tác. VD: Alert, Confirm).
  - `BTS_`: Bottom Sheet (Cửa sổ trượt từ dưới lên, thường dùng cho Mobile App).
  - `z_`: Archive / Draft (Bản nháp). AI sẽ **TỰ ĐỘNG BỎ QUA** không track bất cứ event nào nằm trong frame / màn hình có tiền tố này.

---

## 🛠 QUY TRÌNH THỰC THI

### B1. 🔍 Phân tích luồng (Fetch & Analyze)
- Đọc URD và liệt kê đầy đủ các điểm chạm từ UI đến BE. Không được bỏ sót các thao tác nhỏ (Toggle, Expand, xác nhận Popup).

### B2. 📔 Tra cứu & Map Màn hình (Screen Lookup)
- Lấy tên màn hình gốc từ hệ thống. Nếu là màn mới, thông báo đăng ký từ điển (`update_screen_dictionary`).

### B3. 🏗️ Hiển thị Draft Chuẩn (Draft Generation)
- Hiển thị danh sách Event dạng Bảng ra Log/Chat để PO thẩm định. Đảm bảo đúng chuẩn Taxonomy và Format Đa dòng.

### B4. 📁 Tích hợp hệ thống (Master Integration)
// turbo
- AI chờ lệnh "OK" từ PO.
- Viết một kịch bản code (Python) thực hiện nạp mảng dữ liệu (mảng 2 chiều, ép định dạng `'=`) gọi hàm `update_master_sheet(data, sheet_name)` trong thư viện `.agents/scripts/events/manage_event_sheets.py`.
- Tạo một Sheet mới trong Master File và Push dữ liệu.
- Trả về Link Success cho người dùng.

### B5. 🎯 Đóng gói Tiêu chuẩn Sinh Code (Output Standarization)
- Khi phát sinh Code File (Python) để chèn dữ liệu, AI luôn phải đảm bảo:
  - Cập nhật cả `update_screen_dictionary` và `update_master_sheet` trong cùng 1 tập lệnh.
  - Tổ chức code rõ ràng, không lỗi vỡ font tiếng Việt.
  - Mỗi khi thực hiện luồng mới, AI tự động đối chiếu với kết quả hoàn hảo trước đó (Grab Voucher, C06) để không bao giờ "đi lùi" về chất lượng Taxonomy.
