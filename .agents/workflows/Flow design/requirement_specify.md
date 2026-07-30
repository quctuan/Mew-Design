---
description: Khảo sát và làm rõ yêu cầu UX Benchmark (Phase 1/2)
---
# Workflow UX Benchmark Phase 1: Tiền Nghiên Cứu & Chốt Đề Bài

**Mô tả:** Pipeline tự động hóa bước tiếp nhận yêu cầu và khai thác bối cảnh từ người dùng trước khi thực hiện tìm kiếm UX Benchmark.

## Đầu vào (Input)
Một đoạn paragraph / input từ NGƯỜI DÙNG mô tả về yêu cầu sản phẩm (có thể xuất phát từ 1 painpoint, user storyboard, JTBD, hoặc 1 luồng đã có trước đây).

## Các bước thực hiện
1. **[System]** Kích hoạt Agent **`UX Benchmarker`** (có trang bị Skill **`/web-benchmark`**).
2. **`UX Benchmarker`** tiếp nhận Input từ NGƯỜI DÙNG.
3. **`UX Benchmarker`** đóng vai trò như một chuyên gia Nghiên cứu (Researcher) dạn dày kinh nghiệm. Thay vì ngay lập tức chấp nhận thông tin sơ sài, Agent PHẢI chủ động đặt các câu hỏi đào sâu **lần lượt từng câu một** (không hỏi dồn một lúc nhiều câu) vào các vấn đề cốt lõi sau để làm rõ hoàn toàn bối cảnh:
   - **User Painpoint (Nỗi đau):** Người dùng đang gặp khó khăn cụ thể gì? Cảm xúc của họ lúc đó ra sao (bực tức, bối rối, hay mất kiên nhẫn)?
   - **User Goal (Mục tiêu người dùng):** Cuối cùng, người dùng muốn đạt được điều gì thông qua quy trình/tính năng này?
   - **Business Goal (Mục tiêu kinh doanh):** Phía hệ thống/doanh nghiệp muốn thu lại lợi ích gì (ví dụ: tăng conversion rate, giảm thời gian thao tác, thu thập dữ liệu...)?
   - **User Story & JTBD (Việc cần hoàn thành):** Nếu phải đúc kết, "Khi ở trong tình huống [A], người dùng muốn làm [B], để họ có thể đạt được [C]" là gì?
   - **Ràng buộc (Constraints):** Có hạn chế nào về kỹ thuật, nền tảng (chỉ dùng Web hay cả App), hoặc đối tượng user (người già, người rành công nghệ...) không?
   *(Ghi chú: Đợi NGƯỜI DÙNG trả lời xong một mảng thông tin mới hỏi tiếp mảng khác nếu thấy chưa đủ dữ liệu).*
4. Trách nhiệm của **`UX Benchmarker`** là liên tục mài giũa thông tin trao đổi, cho đến khi cảm thấy đề bài đã đạt độ chín (đủ sâu sắc để làm Input chuẩn cho các mô hình thiết kế khác trong team). Sau khi đã thu thập đủ context, **`UX Benchmarker`** tổng hợp và đóng gói tất cả các thông tin thành một **"Đề bài UX Benchmark cuối cùng"** rõ ràng, súc tích.
5. **[HITL]** **`UX Benchmarker`** dừng lại và hỏi: *"Bạn có đồng ý duyệt Đề bài UX Benchmark này không?"*. 
6. Đợi sự phê duyệt (Approve) từ NGƯỜI DÙNG. 
7. Cung cấp Đề bài này thành dạng Text/Markdown. Sau đó, **DỪNG LẠI VÀ CHỜ LỆNH MỚI TỪ NGƯỜI DÙNG**. 
*(Lưu ý: Output của quy trình này có thể được dùng làm Input cho nhiều quy trình Flow design phía sau, ví dụ như `/ux_benchmark_research`, `/create_event_tracking`, hoặc `/urd_map_screenshot_figma`... tuỳ theo yêu cầu tiếp theo của NGƯỜI DÙNG).*
