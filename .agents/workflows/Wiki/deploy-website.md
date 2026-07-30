---
description: Cách kiểm duyệt và xuất bản tài liệu trên Workspace lên Website (Wiki) Production
---

1. Xem các thay đổi trong thư mục `knowledge base/` hoặc `wiki/docs/` để biết những nội dung nào đang ở dạng nháp (Draft) hoặc được thay đổi.
// turbo-all
2. Thêm các tài liệu đã được Boss/Admin phê duyệt vào Git tracking bằng lệnh:
```bash
git add "knowledge base/" "wiki/docs/"
```
3. Khởi tạo một Commit ghi lại quá trình xuất bản:
```bash
git commit -m "docs: publish approved content to wiki production"
```
4. Đẩy (Push) phiên bản mới nhất lên kho lưu trữ trên GitHub nhánh `main` để kích hoạt máy chủ Vercel:
```bash
git push origin main
```
5. Đợi máy chủ Vercel tự động nhận mã nguồn và tiến hành Build lại MkDocs ra Website. Không cần gõ thêm lệnh local nào.
