---
description: Lệnh đồng bộ một file Markdown bất kỳ (đặc biệt là các file Spec) lên Google Docs. Lệnh tự động giữ nguyên định dạng (Bold, H1, H2, Bảng biểu) và tự sinh Link.
---

1. Khởi động công cụ Terminal nội bộ hoặc sử dụng `run_command`.
2. Yêu cầu Người dùng cung cấp đường dẫn tuyệt đối hoặc tương đối tới file `.md` mà họ muốn đồng bộ lên Google Docs. (Nếu họ chỉ gõ `/sync_gdocs` mà chưa đưa đường dẫn, hãy hỏi lại họ file nào).
3. Chạy lệnh: `python .agents/scripts/utils/sync_md_to_gdocs.py "[Đường dẫn file]"`
4. Nếu kết quả Terminal trả ra có link (e.g. `https://docs.google.com/document/d/...`), hãy trình bày đường link đó dẹp đẽ ra chat cho người dùng bấm vào. Đồng thời báo cáo là "Script đã tự động chèn Link vào trong file Markdown của bạn".
5. Nếu là lần đầu tiên chạy, trình duyệt (Safari/Chrome) của người dùng sẽ tự bật lên và yêu cầu đăng nhập tài khoản Google. Hãy dặn người dùng "Bấm đăng nhập, tích vào đồng ý các quyền truy cập (nếu có popup cảnh báo 'Google hasn't verified this app' thì bấm Advanced/Nâng cao -> Continue) để cấp quyền xác thực".
