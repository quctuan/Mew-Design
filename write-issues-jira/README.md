# write-issues-jira

Skill dùng chung cho các repo thuộc phạm vi MyVNPT đã xác nhận. Không chứa danh tính, Jira site hoặc tài khoản của tác giả.

## Sử dụng
- `/write-issues-jira <task/danh sách task> [context]` qua prompt alias.
- `/skill:write-issues-jira <task/danh sách task> [context]` qua command chuẩn của Pi.

## Cài và chia sẻ
Chia sẻ nguyên thư mục này; không kèm HUMAN.md hoặc các issues cá nhân.
Cài SKILL.md và templates vào `~/.pi/agent/skills/pm-skills/write-issues-jira/` hoặc `.pi/skills/write-issues-jira/`.
Cài `prompts/write-issues-jira.md` vào `~/.pi/agent/prompts/write-issues-jira.md` hoặc `.pi/prompts/write-issues-jira.md` tương ứng.
Reload Pi sau khi cài để nhận command. Không cần extension hay API Jira.
Với Alfie, source nằm ở `agent/skills/pm-skills/write-issues-jira/`; skill được đồng bộ bởi install-home. Prompt alias cần cài riêng từ file trong skill, vì install-home hiện không đồng bộ agent/prompts.

## Dependency và ranh giới
Cần ego-browser đã hoạt động và skill ego-browser có thể đọc được. Xử lý đăng nhập/MFA qua browser handoff, không lưu credentials. Subagents tùy chọn; không đủ điều kiện tách tab thì tạo tuần tự.

Mỗi repo dùng `docs/jira-issue.md` và HUMAN.md riêng. Sau interview, cấu hình chung đã duyệt được lưu; issue drafts ở `docs/jira-issues/` với metadata phiên/version/publication. Không quản lý trạng thái Jira hoặc giờ công.

## Kiểm chứng
Cần kiểm thử riêng: setup thiếu/đủ, minimal draft, sửa sau duyệt, resume phiên, Create không rõ kết quả và pilot trước batch song song.
Không coi kiểm tra cấu trúc skill là bằng chứng đã tạo Jira thành công.
