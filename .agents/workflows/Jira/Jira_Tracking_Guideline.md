# 📚 Hướng Dẫn Vận Hành Hệ Thống Jira Tracking (Dành Cho Thành Viên)

Tài liệu này giải thích cách thức hoạt động của "Đội ngũ AI" đang tự động hóa quy trình theo dõi, quản lý, và lập báo cáo công việc trên hệ thống Jira của team.

---

## 1. 👥 Các Thành Viên Khung (AI Agents)
Hệ thống Tracking chia làm "Não" (Logic) và "Tay Chân" (Operations):

**🤖 Jira Operations Bot (Cỗ máy tay chân):** 
- Nhiệm vụ duy nhất là nhận lệnh, kéo dữ liệu thô (Raw Data JSON) bằng API Jira, và đẩy thông tin (Push) lên Telegram bằng API Telegram.
- Nó không có khả năng hiểu hay thay đổi dữ liệu nội dung của báo cáo tự động để đảm bảo tính minh bạch.

**🧠 Jira Logic Analyst (Bộ não phân tích):**
- Đóng vai trò đọc số liệu khô khan do Operations Bot mang về. 
- Nhiệm vụ là phân rã các Task, phát hiện rủi ro (Risk) như quá hạn, dịch thuật, chắt lọc số lượng và tự động soạn thảo lại các bản báo cáo siêu xinh với tiếng Việt chuẩn mực, giàu sự thấu cảm.

---

## 2. 🛠 Bộ Kỹ Năng Và Cấu Hình (`.agents/skills/Jira`)
Để hai con Bot trên làm được việc, nó được trang bị riêng tủ đồ công cụ (Skills) nằm tại folder thư mục `skills/Jira`:

1. **`jira_fetch.md`**: Cấu hình URL endpoint và cách Bot Operations lên server Jira kéo data theo tham số JQL (không chỉnh sửa trừ khi VNPT đổi hệ thống).
2. **`jira_classification_rules.md`**: [CẤU HÌNH QUAN TRỌNG] - Nơi hướng dẫn Logic Analyst **Tách Data thành 2 bản tin** (`CR_937 -> PYC` và `SR_937 -> Support`). Bên trong còn chứa các từ khoá tự định nghĩa (Di động, Băng rộng, Thanh toán) để tính số lượng Task. *Thành viên có thể trực tiếp bổ sung từ khoá vào file này.*
3. **`telegram_report_template.md`**: [CẤU HÌNH QUAN TRỌNG] - Khung hiển thị giao diện báo cáo lên Telegram. *Thành viên có thể đổi Tiêu đề, chèn Emoji hoặc thay đổi bố cục trong file này tuỳ thích.*
4. **`telegram_notify.md`**: Kỹ năng ra lệnh cho Telegram bắn Message. Được trang bị thuật toán **Auto-Split**, tự động bẻ đôi tin nhắn nếu quá dài (Telegram tự từ chối các tin > 4000 ký tự). Có kèm cơ chế chống lỗi ký tự ngoặc nhọn `< >` của Developer.
5. **`risk_assessment.md` & `professional_communication.md`**: Hai kỹ năng thấu cảm và phát hiện trễ nải (Delay), phát hiện bom nổ chậm (Deadline) từ nội dung chữ viết. Giúp Bot viết comment dặn dò Developer không bị quá cộc lốc/bossy.

> 📝 **Bổ sung / `roles/Jira/jira_report_config.md`:** 
> Danh sách những Ai phải làm báo cáo (Assignees), Quy tắc Lọc Trạng Thái, và cấu hình `Group Chat ID + Bot Token` của Telegram.

---

## 3. 🚀 Các Quy Trình Vận Hành (Workflows) 
Hiện tại Hệ thống có 2 Quy trình chính, dựa vào mong muốn và tần suất của sếp/người dùng: 

### 🟢 `workflow_jira_daily_report` (Tần suất Hàng Ngày)
- **Mục đích:** Update siêu nhanh (Snap shot) cho đầu buối sáng Stand-up. 
- **Cách làm:** Chỉ cần gọi Bot Operations kéo thẳng 50 dòng log Task mới nhất của nhân viên trong dự án và vứt (bắn txt đơn) lên Telegram. Không phân tích. Không tô màu. Nhanh - Rẻ - Không tốn Token của AI.
- **Ai dùng:** Chỉ định một bạn mở phiên hàng ngày bấm lệnh này sáng 8h.

### 🟡 `workflow_jira_weekly_recap` (Tần suất Hàng Tuần/Sprint) 
- **Mục đích:** Báo cáo chi tiết, đẹp, sâu sắc và chia cụm riêng biệt để sếp và các PO họp giao ban, Review tổng kết cuối thứ sáu.
- **Cách làm:** 
    1. Kéo data về xưởng nội bộ.
    2. Logic Analyst vào cuộc: Lọc rác (Trừ trạng thái Done/Closed). Nhặt 2 loại Task ném sang 2 cái rổ khác nhau `PYC` và `Support`.
    3. Đọc Description xem task nào lo về viễn thông, về 4G thì quăng Keyword vô đếm là Di Động (theo file Classification).
    4. Đối chiếu mốc thời gian xem `Due Date` có <= 7 ngày không? Có phải là vừa assign lúc tối qua qua (<24h) không? 
    5. Đắp format giao diện bằng file `telegram_report_template.md`. 
    6. Trả kết quả thành 2 bản nháp siêu gọn, chuyển cho Operations Bot để dập lệnh Post liên tiếp lên Telegram cho cả team xem. 
- **Ai dùng:** Lệnh của Lead, điều phối viên. Bấm vào cuối ngày thứ 6 hoặc trước khi chốt một Release mới.

---

### 🎁 Master Workflow (`jira_tracking_master`)
Nếu bạn là người mới vào nhóm, hãy gõ dấu xuỵt chéo `/jira_tracking_master` vào khung chat AI. Bot sẽ giống như một lễ tân, hỏi bạn cần chạy Workflow Daily rỗng tuếch, chạy Recap cuối tuần, hay là muốn nhờ Bot "Giục deadline thay lời khó nói bằng comment tự động"?
