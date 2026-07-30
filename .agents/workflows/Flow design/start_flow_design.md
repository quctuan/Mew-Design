---
description: Start Flow Design (Master Menu) - Kích hoạt tùy chọn một trong 3 luồng Thiết kế UX
---

# Workflow Khởi tạo Quy trình Flow Design (Master Menu)

Quy trình này đóng vai trò như một "Lễ tân" Hệ thống, giúp NGƯỜI DÙNG chọn đúng định dạng luồng làm việc Thiết kế Trải nghiệm (Flow Design) tùy thuộc vào nguồn gốc của Yêu cầu ban đầu.

## Bước 1: Trình bày Menu Lựa Chọn (Trigger)
1. **[System]** Khi Master Workflow được kích hoạt (thông qua lệnh `/start_flow_design`), Hệ thống hiển thị ngay lập tức Menu sau và đợi NGƯỜI DÙNG nhập lựa chọn (từ 1 đến 3):

> Chào bạn, quy trình Thiết kế Flow Design đã sẵn sàng. Vui lòng cho biết nguồn gốc xuất phát của yêu cầu công việc bạn muốn thực thi bằng cách gõ phím tương ứng:
> **[1] Xử lý Yêu cầu từ Jira (PYC)**
> **[2] Xử lý Yêu cầu từ Email / File đính kèm**
> **[3] Yêu cầu khảo sát từ đầu (Nghiệp vụ BAU/SIP)**

2. **[HITL]** Hệ thống **DỪNG LẠI** và chờ NGƯỜI DÙNG gõ số `1`, `2` hoặc `3`.

## Bước 2: Nhận diện & Yêu cầu Input Khởi tạo (Routing & Input)
Dựa trên phản hồi bằng phím số của NGƯỜI DÙNG, Hệ thống thực hiện rẽ nhánh tương ứng:

*   **Nếu NGƯỜI DÙNG gõ `1` (Chọn Jira):**
    1. Hệ thống hỏi: *"Tuyệt vời! Vui lòng cung cấp cho tôi **Link Task Jira** hoặc **Mã Task** để tôi đi kéo dữ liệu nhé."*
    2. Chờ Input chứa URL/Mã từ NGƯỜI DÙNG.
    3. Sau khi nhận được Input, lập tức kích hoạt và đẩy dữ liệu sang chạy quy trình `.agents/workflows/Flow design/PYC_execute_workflow.md`.
    
*   **Nếu NGƯỜI DÙNG gõ `2` (Chọn Email):**
    1. Hệ thống hỏi: *"Đã rõ! Vui lòng dán toàn bộ **nội dung Text của Email** (hoặc nội dung file đính kèm/Link drive) vào đây để tôi phân tích."*
    2. Chờ Input là đoạn văn bản hoặc file từ NGƯỜI DÙNG.
    3. Sau khi nhận được Input, lập tức kích hoạt và đẩy dữ liệu sang chạy quy trình `.agents/workflows/Flow design/email_execute_workflow.md`.

*   **Nếu NGƯỜI DÙNG gõ `3` (Chọn BAU/SIP):**
    1. Hệ thống báo: *"Đã nhận lệnh BAU/SIP! Hệ thống sẽ chuyển ngay sang Khâu Khảo sát & Chốt đề bài."*
    2. Trong trường hợp này, vì yêu cầu của BAU/SIP không có URL hay Text cụ thể ngay từ đầu, Hệ thống **KHÔNG YÊU CẦU INPUT**, mà lập tức kích hoạt luồng `.agents/workflows/Flow design/BAU_SIP_execute_workflow.md` để Agent `UX Benchmarker` bắt đầu tự đặt câu hỏi phỏng vấn NGƯỜI DÙNG.

## Bước 3: Hậu xử lý & Đồng bộ (Post-Processing)
Sau khi Hệ thống hoàn tất chạy 1 trong 3 quy trình con và xuất ra được bản Spec Giao diện cuối cùng (file URD/BAU_SIP... .md), Master Workflow sẽ tự động "thức tỉnh" trở lại để dẫn dắt NGƯỜI DÙNG thực hiện các bước đóng gói thủ tục cuối cùng:

### Step 3.1: Đồng bộ tài liệu lên Google Docs
1. **[System]** Hệ thống gửi lời chào chúc mừng hoàn thành Spec, kèm theo câu hỏi: *"Bạn có muốn tôi đồng bộ file Spec này lên Google Docs để tiện chia sẻ cho Dev/QA không? (Gõ **Có** hoặc **Không**)"*
2. **[HITL]** Nếu NGƯỜI DÙNG chọn **Có**: 
   - Hệ thống tự động kích hoạt lệnh `/sync_gdocs`.
   - Khi chạy xong và có Link Google Docs (chứa file Spec vừa đồng bộ), Hệ thống mời NGƯỜI DÙNG chuyển sang Step 3.2.
3. **[HITL]** Nếu NGƯỜI DÙNG chọn **Không**: 
   - Hệ thống báo cáo: *"Quy trình Master Workflow chính thức khép lại. Chúc bạn một ngày làm việc hiệu quả!"* và **KẾT THÚC** toàn bộ luồng.

### Step 3.2: Khai báo Mã Màn hình (Screen Name)
1. **[System]** Hệ thống nhắc nhở NGƯỜI DÙNG: *"Để tôi có thể tự động lấy ảnh Screenshot từ Figma dán vào Google Docs cho bạn, vui lòng mở file Spec vừa tạo, tìm đến bảng mô tả các bước User Flow và điền tay **Tên/Mã Màn hình** tương ứng vào đó nhé."*
2. **[HITL]** Hệ thống **DỪNG LẠI** chờ đợi cho đến khi NGƯỜI DÙNG gõ xác nhận *"Đã điền xong"* hoặc *"Done"*.

### Step 3.3: Map Ảnh Screenshot từ Figma (Figma to URD)
1. **[System]** Khi đã nhận được xác nhận từ Step 3.2, Hệ thống hỏi xin NGƯỜI DÙNG cung cấp **Link Figma** chứa các thiết kế màn hình của tính năng này.
2. **[Action]** Sau khi nhận Link Figma, Hệ thống tự động kích hoạt quy trình `/urd_map_screenshot_figma`.
3. **[Input]** Cung cấp tự động 2 tham số đầu vào cho quy trình trên:
   - File Google Docs mục tiêu: Là link bài Google Docs vừa tạo được ở Step 3.1.
   - Nguồn Figma: Là Link Figma NGƯỜI DÙNG vừa cung cấp ở trên.
4. **[HITL]** Dừng lại để NGƯỜI DÙNG kiểm tra lại kết quả dán ảnh trên Google Docs. Chờ NGƯỜI DÙNG gõ xác nhận *"Đã map ảnh xong"* để đi tiếp.

### Step 3.4: Tích hợp Event Tracking (Final Step)
1. **[System]** Sau khi hoàn thiện bộ Spec và thiết kế giao diện (đã đính kèm ảnh thành công), Hệ thống nhắc nhở NGƯỜI DÙNG: *"Hồ sơ thiết kế đã hoàn chỉnh. Bạn có muốn kích hoạt quy trình tạo danh sách đo lường **Event Tracking** cho luồng này không? (Gõ **Có** hoặc **Không**)"*
2. **[HITL]** Nếu NGƯỜI DÙNG chọn **Có**:
   - Hệ thống tự động gọi quy trình `/create_event_tracking`.
   - **[Input Input]** Cung cấp tự động tham số đầu vào cho quy trình này chính là **Link File Google Docs (URD Spec)** được trích xuất từ Step 3.3 (Bản Spec này hiện đã có đầy đủ bảng mô tả các bước kèm với hình ảnh Screenshot thực tế rải đều trong luồng).
   - Sau khi quy trình Tracking hoàn tất việc chắt lọc dữ liệu và tự động tạo Event list, hệ thống dừng lại chờ NGƯỜI DÙNG xác nhận (HITL cuối cùng).
3. **[HITL]** Nếu NGƯỜI DÙNG chọn **Không** hoặc sau khi NGƯỜI DÙNG confirm Tracking OK ở mục trên:
   - Hệ thống thông báo: *"Hoàn tất triệt để vòng đời dự án thiết kế Flow. Chúc bạn một ngày làm việc tuyệt vời!"*
   - **ĐÓNG PHIÊN LÀM VIỆC TỔNG (`/start_flow_design`).**
