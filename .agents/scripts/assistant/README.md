# 🤖 Telegram Task Monitor cho Nội bộ VNPT

Hệ thống chuyên trách giám sát các nhóm Telegram nội bộ VNPT, tự động gom ngữ cảnh cuộc trao đổi (10-15 tin nhắn trước), tóm tắt yêu cầu và gửi nhắc việc tức thời vào Telegram cá nhân của bạn kèm tính năng tạo **SOW & Timeline** theo yêu cầu.

---

## 🚀 1. Kiểm tra Thử nghiệm Nhanh (Mock Mode)

Bạn có thể chạy thử nghiệm ngay quy trình phát hiện tag, gom ngữ cảnh và sinh SOW mà chưa cần nhập thông tin tài khoản Telegram:

```bash
python3 .agents/scripts/intake/telegram_vnpt_monitor.py --test
```

---

## ⚙️ 2. Cấu hình Kết nối Telegram Thực tế

1. **Sao chép file cấu hình:**
   ```bash
   cp .agents/scripts/intake/config.sample.json .agents/scripts/intake/config.json
   ```

2. **Điền thông tin trong `config.json`:**
   * **`telegram_notifier_bot`:**
     * `bot_token`: Lấy từ `@BotFather` trên Telegram (dùng để gửi tin nhắn cảnh báo đến bạn).
     * `my_chat_id`: ID tài khoản Telegram cá nhân của bạn (lấy bằng cách gửi `/start` cho bot `@userinfobot`).
   * **`telegram_userbot` (Tuỳ chọn - Quét tự động toàn bộ nhóm không cần add bot):**
     * `api_id` & `api_hash`: Lấy miễn phí tại [my.telegram.org](https://my.telegram.org) (mục API Development Tools).
     * `phone_number`: Số điện thoại đăng ký Telegram của bạn (vd: `+849xxxxxxxx`).
   * **`settings`:**
     * `my_usernames`: Username Telegram của bạn (vd: `["@tuanvq", "tuanvq"]`).
     * `keywords`: Danh sách từ khóa kích hoạt nhắc nhở (vd: `["Tuấn", "Anh Tuấn", "TuanVQ", "Mew", "URD", "Design", "Figma", "Gấp"]`).
     * `context_history_limit`: Số lượng tin nhắn liền trước cần gom để lấy ngữ cảnh (mặc định: `15`).

---

## 📑 3. Tạo SOW & Timeline theo Yêu cầu (On-Demand)

Khi nhận được thông báo nhắc việc có kèm `Task ID` (ví dụ: `VNPT_20260808_224500`), bạn có thể tạo ngay file SOW & Timeline bằng lệnh:

```bash
python3 .agents/scripts/intake/telegram_vnpt_monitor.py --sow VNPT_20260808_224500
```

File SOW chuẩn sẽ được tự động lưu vào:
`knowledge_base/projects/<Tên_Dự_Án>/01_sow/YYYYMMDD_VNPT_xxxxxx_sow.md`
