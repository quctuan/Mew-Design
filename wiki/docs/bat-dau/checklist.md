---
hide:
  - toc
password: gds@ptsp
---
# ✅ Checklist Tuần Đầu (Getting Started)

Tài liệu hướng dẫn thiết lập môi trường làm việc và tích hợp trợ lý **Antigravity AI**. Thành viên mới vui lòng hoàn thành checklist dưới đây trong tuần đầu tiên.

---

## 🛠️ 1. Yêu cầu chuẩn bị
- [ ] Cài đặt **[Git](https://git-scm.com/)**.
- [ ] Đăng ký tài khoản **GitHub** (Cung cấp Username cho Admin để nhận quyền truy cập nếu repo Private).
- [ ] Cài đặt thiết lập IDE có tích hợp trợ lý **Antigravity AI**.

---

## 📥 2. Tải Workspace (Clone Repository)
Tải cấu trúc dự án về máy tính cá nhân:

- [ ] Mở Terminal (Mac/Linux) hoặc Command Prompt / Git Bash (Windows).
- [ ] Clone mã nguồn từ GitHub:
  ```bash
  git clone https://github.com/minhan720/gds-myvnpt-wiki.git
  ```
- [ ] Truy cập thư mục dự án:
  ```bash
  cd gds-myvnpt-wiki
  ```

---

## 🔄 3. Cập nhật Phiên bản Mới nhất (Pull Update)
Khi có thông báo từ Admin về việc cấu trúc hoặc workflow đã được nâng cấp, bạn cần cập nhật về máy cá nhân:

- [ ] Truy cập vào Terminal hoặc Command Prompt, di chuyển đến thư mục dự án (`cd gds-myvnpt-wiki`).
- [ ] Kiểm tra trạng thái hiện tại (Nên đảm bảo bạn không có thay đổi nào chưa lưu):
  ```bash
  git status
  ```
- [ ] Chạy lệnh Pull để đồng bộ source code mới nhất từ GitHub:
  ```bash
  git pull origin main
  ```

---

## 🤖 4. Kích hoạt AI Workspace
Hệ thống "Role Prompts" (`sample_team/`) và "Kỹ năng" (`.agents/skills/SKILL.md`) đã được cấu hình sẵn.

- [ ] **Mở dự án:** Khởi động IDE -> **Open Folder** -> Mở `gds-myvnpt-wiki`.
- [ ] **Khởi động AI:** Mở tab Chat của Antigravity để hệ thống tự động nạp thư mục `.agents`.
- [ ] 💡 **Kiểm thử hệ thống:** Gửi prompt sau vào Chat:
  > *"Kiểm tra các team hiện có trong thư mục sample_team và liệt kê chi tiết."*

---

## 💻 5. Chạy Web Local (Dành cho bộ phận tài liệu)
Phục vụ việc kiểm thử hiển thị nội dung wiki trước khi xuất bản:

- [ ] **Cài đặt thư viện:** 
  ```bash
  cd wiki
  pip install -r requirements.txt
  ```
- [ ] **Khởi động Local Server:** 
  ```bash
  python3 -m mkdocs serve
  ```
- [ ] **Kiểm tra hiển thị:** Truy cập [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🚀 6. Triển khai Web bằng Vercel (Deploy)
Quy trình xuất bản tài liệu sau khi hoàn thành nhiệm vụ:

- [ ] Lưu tài liệu `.md` tại thư mục `knowledge base/`.
- [ ] Chờ cấp quản lý (PO/Admin) phê duyệt (Approved).
- [ ] Sử dụng lệnh sau trong Antigravity Chat:
  > `/deploy-website`
- [ ] Hệ thống tự động triển khai. Kiểm tra lại URL Vercel Public.

---

## 📚 Phụ Lục

### 📁 Cấu Trúc Thư Mục Cốt Lõi

- `/sample_team`: Chứa System/Role Prompts cấu hình chuyên môn cho AI Teams. **Tuyệt đối không tự ý chỉnh sửa hay xóa file tại đây**.
- `/.agents/skills/SKILL.md`: Tệp cấu hình quản lý hệ sinh thái kỹ năng của Antigravity.
- `/knowledge base`: Kho lưu trữ tri thức tập trung. Chứa thiết kế, báo cáo, quy cách để đồng bộ lên wiki.
