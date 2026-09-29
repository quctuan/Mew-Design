# Quy chuẩn và Định nghĩa Thực thể lõi (Core Entities) - MyVNPT

Tài liệu này quy chuẩn hóa các khái niệm lõi và mô hình quan hệ giữa các thực thể trong hệ sinh thái MyVNPT, định hướng cho việc thiết kế Kiến trúc thông tin (Information Architecture) và Trải nghiệm người dùng (UX/UI).

## 1. Định nghĩa các Thực thể lõi (Core Entities)

### 1.1. User (Người dùng / Tài khoản MyVNPT)
*   **Bản chất:** Đại diện cho một **"Con người thực tế"**.
*   **Định danh (Identity):** Là duy nhất, được ánh xạ và định danh chéo (KYC) bằng **CCCD/CMND + VNPT Digital ID**.
*   **Nguyên tắc UX:** Người dùng chỉ cần Đăng nhập một lần (Single Sign-On). App nhận diện "Bạn là ai" chứ không phải "Bạn đang dùng số điện thoại nào". Tôn chỉ là cá nhân hóa theo Người dùng.

### 1.2. Subscription (Thuê bao / Dịch vụ)
*   **Bản chất:** Đại diện cho một **"Tài sản số"** hoặc **"Dịch vụ"** mà VNPT cung cấp (VD: Số di động VinaPhone, Đường truyền FiberVNN, Truyền hình MyTV...).
*   **Nguyên tắc UX:** Thuê bao là những "món đồ" nằm trong "chiếc ví" của User. Thuê bao tự nó không có quyền hạn, nó chỉ chịu sự tác động từ User.

### 1.3. Group (Nhóm / Hộ gia đình)
*   **Bản chất:** Là một **"Không gian ảo" (Workspace)** dùng để kết nối nhiều User lại với nhau nhằm mục đích chia sẻ tài nguyên (gói cước gia đình), chia sẻ thông tin, hoặc ủy quyền quản lý.
*   **Cấu trúc:** Gồm 1 Chủ nhóm (Owner) và N Thành viên (Members).

---

## 2. Mô hình Quan hệ giữa các Thực thể (Relationships)

### 2.1. Quan hệ User ↔ Thuê bao: Một - Nhiều (1-N)
*   **Mô tả:** Một User (con người) có thể **sở hữu/đứng tên hợp đồng** rất nhiều Thuê bao khác nhau (VD: 2 số di động, 1 mạng internet ở nhà, 1 mạng internet ở quê).
*   **UX Context:** Khi User đăng nhập vào MyVNPT, hệ thống sẽ tự động quét (dựa trên CCCD) và gom toàn bộ các thuê bao này về chung một màn hình quản lý cá nhân.

### 2.2. Quan hệ User ↔ Group (Nhóm): Nhiều - Nhiều (N-N)
Đây là quan hệ linh hoạt nhất và phản ánh đúng đời thực nhất:
*   Một User có thể là **Chủ nhóm (Owner)** của nhiều Nhóm khác nhau (VD: Nhóm "Gia đình nhỏ của tôi" + Nhóm "Bố mẹ ở quê").
*   Một User cũng có thể đồng thời là **Thành viên (Member)** của nhiều Nhóm khác nhau (VD: Làm thành viên trong nhóm chia sẻ data của hội bạn thân).

---

## 3. Cơ chế Phân quyền & Ủy quyền trong Nhóm (Permissions & Delegation)

Đây là điểm mấu chốt để giải quyết bài toán "Quản lý hộ" mà không vi phạm quyền riêng tư (Privacy) của người dùng. Tách bạch rõ ràng giữa **Quyền sở hữu (Ownership)** và **Quyền quản lý (Management)**:

*   **Chủ nhóm (Owner):** Là người khởi tạo không gian Nhóm. Chủ nhóm có quyền thanh toán, mua sắm định kỳ cho cả nhóm (VD: Mua gói Home Combo chung).
*   **Cơ chế Ủy quyền (Consent/Delegation):**
    *   Thuê bao là tài sản của Thành viên, Chủ nhóm KHÔNG mặc định có quyền can thiệp vào thuê bao của Thành viên.
    *   **Workflow:** Chủ nhóm gửi "Yêu cầu cấp quyền quản lý" -> Thành viên nhận thông báo (Notification/OTP) và bấm "Xác nhận đồng ý".
*   **Quyền hạn sau khi được Ủy quyền:** Khi thành viên đã đồng ý, Chủ nhóm có thể thực hiện các "Hành động hộ" (Proxy Actions) như:
    1.  **Xem (View-only):** Tra cứu lưu lượng data còn lại, kiểm tra cước nóng, xem lịch sử trừ tiền, theo dõi chu kỳ gói cước.
    2.  **Hành động (Action):** Nạp tiền hộ, thanh toán hóa đơn hộ, gia hạn gói cước hoặc mua thêm gói cước data ngắn ngày cho thành viên đó.
    3.  **Hỗ trợ (Support):** Tạo ticket báo hỏng mạng/dịch vụ thay cho thành viên.

---

## 4. Thay đổi cốt lõi về mặt UX/UI (Key Takeaways cho Product Design)

1.  **Chuyển đổi Ngữ cảnh (Context Switcher):** App cần có một thanh điều hướng hoặc khu vực (Workspace selector) ở vị trí dễ thao tác để User chuyển đổi giữa:
    *   *Workspace Cá nhân:* "Tôi đang xem và quản lý đồ của tôi".
    *   *Workspace Gia đình A:* "Tôi đang đứng dưới góc độ Chủ nhóm để xem và thanh toán cước cho gia đình".
2.  **Cá nhân hóa (Personalization):** Lời chào trên App phải là tên thật (Con người): *"Chào buổi sáng, anh Minh"* thay vì *"Chào thuê bao 0912..."*.
3.  **Tách bạch Thông báo (Notification Routing):** Thông báo nào thuộc về cá nhân (sắp hết data của cá nhân) và thông báo nào thuộc về Nhóm (thành viên A vừa yêu cầu mua thêm data) cần được phân loại hoặc gắn tag rõ ràng trong Notification Center.
