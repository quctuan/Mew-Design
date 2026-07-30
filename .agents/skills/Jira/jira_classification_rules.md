# Jira Classification Rules (Từ khoá & Bộ lọc)

Tài liệu này đóng vai trò như bộ quy tắc chính thức để `Jira Logic Analyst` phân loại các Jira Task. **Người dùng có thể thêm/xóa/sửa các loại ID và Từ khoá tại đây.**

Mỗi Task cần được gắn 2 loại nhãn (Tag) tuần tự theo 2 bước sau:

## BƯỚC 1: Phân Loại Theo Issue Type (Nhóm Báo Cáo)
Khi đối chiếu một danh sách task lấy về từ Jira, hãy nhìn vào trường **Issue Type** của từng thẻ và tách chúng làm 2 luồng Báo cáo độc lập:
### 1. Luồng: `PYC`
- **Điều kiện:** Nếu trường Issue Type (hoặc tên thẻ) = `CR_937`
- **Ý nghĩa:** Đây là các Yêu cầu Thay đổi / Phát triển mới (Phiếu Yêu Cầu).

### 2. Luồng: `Support`
- **Điều kiện:** Nếu trường Issue Type (hoặc tên thẻ) = `SR_937`
- **Ý nghĩa:** Đây là các Yêu cầu Hỗ trợ (Service Request).

> ⚠️ Mọi Task sẽ được tách thành 2 luồng danh sách độc lập (`PYC` và `Support`) ngay từ khâu đầu tiên, để sinh ra 2 kịch bản báo cáo tách biệt.

---

## BƯỚC 2: Phân Loại Theo Nghiệp Vụ (Nhóm Số Liệu)
Bên trong mỗi luồng báo cáo ở Bước 1, đọc tiếp nội dung `Description + Attachment` của Task đó để gắn thêm 1 Tag nghiệp vụ duy nhất (Ưu tiên từ trên xuống dưới nếu có nhiều keyword cùng xuất hiện). Khi lập báo cáo, hãy dùng nhóm này để thống kê.

### 1. Nhóm: Di động
- **Mô tả:** Các nghiệp vụ liên quan đến viễn thông di động, mạng não, cước SIM.
- **Keywords nhận diện:** `Di động`, `VinaPhone`, `VNP`, `SIM`, `eSIM`, `Cước di động`, `Gói cước VNP`, `4G`, `5G`, `Mạng di động`.

### 2. Nhóm: Băng rộng cố định
- **Mô tả:** Các nghiệp vụ liên quan đến Internet cáp quang, mạng cố định, băng rộng.
- **Keywords nhận diện:** `Cố định`, `Băng rộng`, `Fiber`, `FTTH`, `Internet`, `Wifi`, `MyTV`, `Cáp quang`, `Đường truyền cố định`.

### 3. Nhóm: Cổng thanh toán / Thanh toán
- **Mô tả:** Liên quan đến các cổng thanh toán, VNPT Pay, Mobile Money nạp thẻ.
- **Keywords nhận diện:** `Thanh toán`, `VNPT Money`, `VNPT Pay`, `Mobile Money`, `VNPAY`, `Nạp thẻ`, `Payment`, `Cổng thanh toán`, `Đối soát`.

### 4. Nhóm: Khác (Others)
- **Mô tả:** Không khớp với nhóm nào ở trên, hoặc là công việc hành chính, thiết kế chung chung, không rõ ràng.
- **Keywords nhận diện:** Không lọt vào các bộ lọc trên.

> ⚠️ **Quy tắc bắt buộc:** Logic Analyst **chỉ sử dụng chính xác tên của các nhóm (Headers) được list trong Bước 2 này** để gắn mác thống kê, tuyệt đối không tự chế ra Tên Nhóm mới.
