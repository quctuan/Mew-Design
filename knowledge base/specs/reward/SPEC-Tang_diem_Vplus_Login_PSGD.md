# [SPEC] Chương trình Tặng điểm VinaPhone Plus cho Khách hàng Mới và Quay lại

## Metadata
- **Tên tài liệu**: MyVNPT. CTKM Tặng điểm V+
- **Phiên bản**: 1.0.0
- **Ngày khởi tạo**: 2/2/2026
- **Người thực hiện**: Hồ Phạm Quỳnh Mai
- **Trạng thái**: Khởi tạo tài liệu

---

## LỊCH SỬ THAY ĐỔI

| Ngày | Phiên bản | Người thực hiện | Nội dung thay đổi |
| :--- | :--- | :--- | :--- |
| 2/2/2026 | 1.0.0 | Hồ Phạm Quỳnh Mai | Khởi tạo tài liệu |

---

## 1. Thông tin chung

### 1.1. Mục tiêu tài liệu
Tài liệu này mô tả yêu cầu người dùng cho Chương trình Tặng điểm VinaPhone Plus, làm cơ sở cho phân tích nghiệp vụ, thiết kế, phát triển, kiểm thử và triển khai trên MyVNPT.

### 1.2. Tổng quan chương trình
*   **Tên chương trình:** Chương trình Tặng điểm VinaPhone Plus
*   **Mục tiêu kinh doanh:**
    *   Gia tăng số lượng khách hàng phát triển mới app MYVNPT.
    *   Khuyến khích khách hàng phát sinh giao dịch trên hệ sinh thái MyVNPT.
    *   Tăng tần suất sử dụng dịch vụ và mức độ gắn bó của khách hàng.

### 1.3. Phạm vi áp dụng (Đối tượng khách hàng)

#### 1.3.1. Khách hàng mới
*   Khách hàng (tương ứng 01 số điện thoại đăng nhập My VNPT) đăng nhập lần đầu tiên trên ứng dụng My VNPT.
*   Chỉ áp dụng cho thuê bao VinaPhone, không áp dụng thuê bao ngoài mạng.
*   Chỉ áp dụng cho khách hàng đăng nhập ứng dụng, không áp dụng cho đăng nhập website.

#### 1.3.2. Khách hàng quay lại
*   Khách hàng (tương ứng với 01 số điện thoại đăng nhập My VNPT) phát sinh giao dịch (*) trở lại ứng dụng My VNPT sau 03 tháng đến 01 năm (tính từ tháng giao dịch).
*   Chỉ áp dụng cho thuê bao VinaPhone, không áp dụng thuê bao ngoài mạng.
*   **Phát sinh giao dịch:** Là khách hàng thực hiện thành công một trong các giao dịch trên ứng dụng My VNPT sau (Các giao dịch thực hiện trên website http://my.vnpt.com.vn, SDK hoặc bất kì điểm chạm khác không phải ứng dụng My VNPT sẽ không được áp dụng):
    *   Mua gói cước di động và internet & truyền hình (không bao gồm gia hạn gói cước).
    *   Mua sim (mua sim thanh toán thành công).
    *   Nạp tiền điện thoại VinaPhone bao gồm: nạp điện thoại VinaPhone; mua mã thẻ VinaPhone; không bao gồm gạch thẻ điện thoại và nạp tự động.
    *   Thanh toán hóa đơn viễn thông VNPT (hóa đơn trả sau, thanh toán trước cước, thanh toán đơn hàng) (không bao gồm thanh toán tự động).

### 1.4. Giới hạn ưu đãi
*   Mỗi khách hàng chỉ được nhận 01 ưu đãi tặng điểm VinaPhone Plus đối với một loại tương tác.
*   Mỗi KH được nhận tối đa 02 ưu đãi tặng điểm trong thời gian diễn ra chương trình (Tức là 01 khách hàng có thể 01 lần khi đăng nhập lần đầu và/hoặc khi phát sinh trở lại sau 03 tháng đến 01 năm).

---

## 2. Kịch bản chương trình

### 2.1. Kịch bản tặng điểm (Luồng người dùng)

#### Mô tả quy trình:
*   **Bước 1:** Khách hàng lần đầu đăng nhập vào app MYVNPT / khách hàng PSGD trở lại (thuộc đối tượng của chương trình).
*   **Bước 2:** Hệ thống VinaPhone Plus thực hiện kiểm tra thông tin khách hàng:
    *   **Nếu KH chưa là hội viên:**
        *   Thực hiện đăng ký hội viên VinaPhone Plus (thông tin thuê bao lấy từ hệ thống CCBS).
        *   Nhắn tin thông báo đăng ký hội viên thành công.
        *   Thực hiện cộng điểm cho khách hàng theo quy định.
        *   => Chuyển Bước 3.
    *   **Nếu Khách hàng đang là hội viên:** Hệ thống thực hiện cộng điểm theo quy định => Chuyển Bước 3.
*   **Bước 3:** Gửi thông báo nhận điểm cho khách hàng (SMS và Notification).

#### Nội dung thông báo:

| Hình thức | Đối tượng | Nội dung |
| :--- | :--- | :--- |
| **SMS** | KH lần đầu đăng nhập | (CSKH) Chao mung Quy khach den voi ung dung My VNPT. VinaPhone kinh tang Quy khach <số điểm tặng> diem VinaPhone Plus cho lan dau dang nhap. Diem tang co thoi han den dd/mm/yyyy de trai nghiem cac uu dai hap dan (qua tang, phut goi, Data…) tai website/ung dung My VNPT https://my.vnpt.com.vn/adv/vplus. CSKH 18001091 (0d). Tran trong! |
| **SMS** | KH PSGD trở lại | (CSKH) Cam on Quy khach da phat sinh giao dich tro lai tren ung dung My VNPT. VinaPhone kinh tang Quy khach <số điểm tặng> diem VinaPhone Plus co thoi han den dd/mm/yyyy de trai nghiem cac uu dai hap dan (qua tang, phut goi, Data …) tai website/ung dung My VNPT https://my.vnpt.com.vn/adv/vplus. CSKH 18001091 (0d). Tran trong! |
| **Notification** | KH lần đầu đăng nhập | ♥️ My VNPT xin chào! 🎉 Kính tặng bạn <số điểm tặng> điểm VinaPhone Plus cho lần đầu đăng nhập để trải nghiệm ưu đãi hấp dẫn (quà tặng/gói cước,....) ngay trên ứng dụng My VNPT. 👉 Thời hạn điểm đến ngày dd/mm/yyyy. Đừng bỏ lỡ! |
| **Notification** | KH PSGD trở lại | 🎉 Cảm ơn bạn đã trở lại giao dịch cùng My VNPT. ✨ My VNPT kính tặng bạn <số điểm tặng> điểm VinaPhone Plus để trải nghiệm ưu đãi hấp dẫn (quà tặng/gói cước,....) ngay trên ứng dụng My VNPT. 👉 Thời hạn điểm đến ngày dd/mm/yyyy. Đừng bỏ lỡ! |

---

## 3. Báo cáo

Tái sử dụng form báo cáo từ core VinaPhone Plus cũ, nguồn dữ liệu chuyển sang nền tảng Loyalty mới.

### 3.1. Báo cáo chi tiết
*   **Link tham chiếu:** [Link báo cáo chi tiết](https://my.vnpt.com.vn/MyVNPT_NEW/report/v-plus/detail/list)
*   **Tiêu chí lọc:**
    *   Thời gian
    *   Số điện thoại
    *   Loại khách hàng
    *   Trạng thái tặng điểm

### 3.2. Báo cáo tổng hợp
*   **Link tham chiếu:** [Link báo cáo tổng hợp](https://my.vnpt.com.vn/MyVNPT_NEW/report/v-plus/synthesis/list)
*   **Tiêu chí lọc:**
    *   Thời gian
    *   Loại thuê bao
