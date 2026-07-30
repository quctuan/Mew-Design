---
description: Pipeline phân tích và tìm kiếm UX Benchmark từ web (4 Bước + HITL)
---
# Workflow UX Benchmark from Web (Master Pipeline)

**Mô tả:** Master Pipeline điều phối chuỗi quy trình nghiên cứu UI/UX (UX Benchmark) từ Web. Workflow này sẽ điều phối và yêu cầu hệ thống tự động chạy tuần tự 2 Phase con bên dưới.

## Phase 1: Tiền Nghiên Cứu & Chốt Đề Bài
- Kích hoạt quy trình con: **`/requirement_specify`**
- Phân công Agent: **`UX Benchmarker`**
- Mục đích: Đặt câu hỏi khai thác thông tin từ người dùng và chốt **"Đề bài UX Benchmark cuối cùng"**.
- Điểm dừng (HITL): Yêu cầu NGƯỜI DÙNG duyệt (Approve) đề bài trước khi sang Phase 2.

## Phase 2: Tìm kiếm, phân tích và tổng hợp Báo cáo
- Kích hoạt quy trình con: **`/ux_benchmark_research`**
- Phân công Agent: **`UX Benchmarker`** (có sử dụng Skill **`/web-benchmark`**)
- Mục đích: Từ Đề bài đã chốt ở Phase 1, tự động dùng trình duyệt web tìm kiếm báo cáo nghiên cứu, thiết kế flow UX, video demo tính năng... sau đó tổng hợp thành file Báo cáo chuẩn lưu vào thư mục `knowledge base/research/UX_Benchmark`.
