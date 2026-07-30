---
name: modular-agent-architecture
description: Hướng dẫn cấu trúc Modular của Agent Team (Roles, Skills, Teams, Core). Đọc file này để hiểu cách tham chiếu và lắp ghép các role/skill.
---

# Modular Agent Architecture

Hệ thống quản lý Agent Team đã được quy hoạch lại từ kiến trúc Monolithic sang **Modular**. Thay vì lưu trữ mọi thứ trong một file khổng lồ hoặc hardcode trong từng thư mục team, hệ thống chia nhỏ các thành phần ra để tái sử dụng.

## 1. Cấu trúc thư mục

Tất cả nằm trong `/.agents/`:

- **`core/`**: Chứa logic cốt lõi. Ví dụ: script tạo tmux team (`team-creator.md`), các hook và lệnh hệ thống.
- **`skills/`**: Thư viện chứa các Kỹ năng độc lập (ví dụ: `agile/`, `analysis/`, `design_audit/`). Các file `.md` ở đây chỉ đặc tả 1 kỹ năng cụ thể.
- **`roles/`**: Thư viện chứa các Vai trò (Role). Ví dụ: `product_owner.md`, `qa_engineer.md`. Một role có thể nhúng các đường dẫn tham chiếu đến `skills/` mà nó cần.
- **`teams/`**: Thư viện cấu hình Team. Mỗi team (ví dụ: `scrum-team/`) sẽ chứa file `team_config.yaml` và `workflow.md`. File cấu hình sẽ lắp ghép các `roles` lại để tạo thành team.

## 2. Cách mở rộng / Nâng cấp

- **Khi có yêu cầu cập nhật năng lực cho 1 vai trò (Role):** Sửa file tương ứng trong `roles/`.
- **Khi có logic thao tác mới (Skill):** Tạo file `.md` mới trong `skills/` và bổ sung đường dẫn file đó vào `roles/` tương ứng.
- **Khi có yêu cầu tạo Team mới:** Tạo thư mục con trong `teams/`, định nghĩa file `team_config.yaml` kế thừa từ các `roles`.

## 3. Quản lý Tmux Team

Logic cốt lõi dùng để phân tích và khởi tạo multi-agent tmux session (trước đây nằm ở file này) đã được chuyển về:
👉 **`.agents/core/team-creator.md`**
