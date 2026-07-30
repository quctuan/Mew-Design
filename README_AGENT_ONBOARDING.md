# HƯỚNG DẪN CÀI ĐẶT AGENT CHO TEAM MEMBER

Tài liệu này hướng dẫn các thành viên trong team (PO, BA, QC, Dev, Designer) tải và đồng bộ hóa hệ thống Agent (bao gồm Design Ops, URD Mapper, UI/UX Audit) về máy cá nhân từ repository chung.

---

## 🚀 1. Tải Hệ thống Agent về máy (Lần đầu tiên)

Nếu bạn là thành viên mới và chưa có thư mục dự án trên máy, hãy thực hiện Clone toàn bộ dự án về máy:

**Bước 1:** Mở Terminal (Mac/Linux) hoặc Command Prompt / PowerShell (Windows).
**Bước 2:** Di chuyển đến thư mục bạn muốn lưu dự án (VD: thư mục `Documents`):
```bash
cd ~/Documents
```
**Bước 3:** Chạy lệnh Clone để tải mã nguồn:
```bash
git clone https://github.com/minhan720/gds-myvnpt-wiki.git
```
*(Nếu GitHub yêu cầu đăng nhập, hãy sử dụng Personal Access Token thay cho mật khẩu).*

---

## 🔄 2. Cập nhật Hệ thống Agent (Đồng bộ hàng ngày)

Nếu bạn đã có sẵn thư mục `gds-myvnpt-wiki` trên máy nhưng Trưởng nhóm (PO/Lead) vừa thông báo có bản cập nhật mới cho các Agent (Ví dụ thêm luật mới cho URD Mappers), bạn cần Pull dữ liệu mới về:

**Bước 1:** Mở Terminal và trỏ vào đúng thư mục dự án:
```bash
cd ~/Documents/gds-myvnpt-wiki
```
**Bước 2:** Cập nhật phiên bản mới nhất từ nhánh `main`:
```bash
git pull origin main
```

---

## 🤖 3. Cách gọi Agent ra làm việc

Sau khi bạn đã tải hoặc cập nhật xong, toàn bộ tri thức của Agent sẽ nằm gọn trong thư mục ẩn `.agents`.

Để yêu cầu AI làm việc đúng vai trò và tuân thủ chặt chẽ rào cản nghiệp vụ của team, bạn **BẮT BUỘC** phải Mention (gọi tên) file Role của Agent đó trong hộp chat AI (như Cursor, Windsurf, Claude).

**Cú pháp:** Gõ `@` cộng với đường dẫn đến file Role của Agent cần gọi.

**Ví dụ thực tế:**
- **Gọi URD Mapper:** `@.agents/roles/Flow design/URD mapper/figma_urd_mapper.md Hãy map link Figma này vào file URD: [Link Google Doc]`
- **Gọi Design Ops:** `@.agents/roles/Design Ops/design_ops.md Hãy phân tích màu sắc và component Badge trong file Figma này...`
- **Gọi UI/UX Auditor:** `@.agents/roles/UIUX Audit/...`

> **Lưu ý quan trọng:** Không cần cung cấp thêm Instruction dài dòng, các Agent đã được tiêm (inject) sẵn hàng loạt các Prompt, Rule, Anti-patterns và Workflows chuẩn hóa của team GDS MyVNPT vào não bộ rồi. Bạn chỉ cần đưa Dữ liệu Đầu vào (Input Data).
