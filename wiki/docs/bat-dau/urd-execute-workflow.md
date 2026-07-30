# Cẩm nang Hướng dẫn Thực thi Quy trình Xử lý Yêu cầu (PYC Execute Workflow)

Bài viết này hướng dẫn chi tiết cách một thành viên (UX Designer, Researcher, hoặc Product Owner) vận hành quy trình tự động hóa giải quyết một Yêu cầu Cải tiến (PYC) từ Jira, thông qua chuỗi AI Agents để trích xuất Research Insight, định hình Chiến lược, và chốt tài liệu Đặc tả (UX Spec) hoàn chỉnh.

Quy trình này áp dụng tư duy Human-In-The-Loop (HITL), tức là AI sẽ thực thi phần nặng nhọc, nhưng Con người (Bạn) mới là người đưa ra quyết định cuối cùng ở các điểm giao cắt.

---

## 🎯 Tổng quan Kết quả Đầu ra
Kết thúc quy trình này, toàn bộ dữ kiện rải rác trên Jira sẽ được thu thập, phân tích và xuất ra:
1. **01 File Research Insight (`RS...md`)**: Chứa điểm đau, kịch bản JTBD và Chiến lược thấu cảm cốt lõi.
2. **01 File UX Specification (`URD...md`)**: Chứa Bản vẽ Luồng thao tác (Mermaid Flow), Copywriting chuẩn tone và Kịch bản lỗi (Edge Cases) chi tiết.
3. **01 Document Google Docs**: Bản copy hoàn hảo của file UX Spec ở trên, phục vụ mục đích chia sẻ ra bên ngoài.

---

## 🚀 Các Bước Vận hành Chi tiết

### Bước 1: Chuẩn bị Input (Jira Link)
Trước khi khởi động hệ thống, bạn cần xác định Task Jira mà mình chuẩn bị lấy dữ liệu.
- Đảm bảo trong Task Jira đó phần **Description** đã được mô tả vấn đề/nhu cầu, và có đính kèm file tài liệu (nếu có).
- Copy đường link chính xác của Task đó. (Ví dụ: `https://jira.myvnpt.vn/browse/IT360-1587543`)

### Bước 2: Kích hoạt Lệnh Thực thi Cốt lõi
Vào khung Chat của hệ thống Antigravity, bạn mở mào bằng lệnh Slash Command sau:

```bash
/pyc_execute [Dán_Đường_Link_Jira_Vào_Đây]
```

Lúc này, toàn bộ cỗ máy AI sẽ tự động kích hoạt.
1. `Jira Logic Analyst` sẽ thọc sâu vào Jira để lấy Description và nội dung File đính kèm mới nhất.
2. Bạn không cần làm gì cả, chỉ việc theo dõi và chờ hệ thống đọc hiểu tài liệu.

### Bước 3: Điểm Dừng 1 - Nếu Dữ liệu Quá Mỏng
- **Tình huống:** Nếu AI nhận thấy Link Jira kia viết quá sơ sài ("Làm tôi tính năng chuyển tiền" chẳng hạn), nó sẽ CHỦ ĐỘNG DỪNG LẠI và bắt đầu vặn vẹo hỏi bạn các thông tin còn thiếu.
- **Hành động của bạn:** Bạn chỉ cần reply lại vào khung chat câu trả lời bổ sung (Ví dụ: "À ý sếp là khách hàng VIP đang bị khó chịu vụ tốn bước nhập mật khẩu nha").
- Hệ thống sẽ tổng hợp lại thông tin và chạy tiếp.

### Bước 4: Điểm Dừng 2 - Phê duyệt Research Insight (HITL 1)
- **Tình huống:** Sau khi thu thập đủ dữ liệu, AI (`PG-UX Researcher`) sẽ sinh ra 1 file Research (`RSxx...md`).
- File này chứa phân tích về Bối cảnh (When/Where), Cách làm thủ công hiện tại và **Điểm đau cốt lõi (Pain point)**.
- **Hành động của bạn:** AI sẽ dừng lại báo cáo và yêu cầu bạn "Duyệt" file này.
  - Bạn mở file `RS...md` ra đọc.
  - Nếu thấy Điểm đau phân tích sai quá, bạn gõ yêu cầu nó sửa: "Ê sửa lại cái pain point kia đi, không phải bị chậm đâu, mà là họ sợ giao diện mờ".
  - Nếu thấy phân tích cực nét rồi, bạn gõ: **"Proceed"** hoặc **"Đồng ý, chạy tiếp đi"**.

### Bước 5: Điểm Dừng 3 - Phê duyệt Chiến lược Thấu cảm (HITL 2)
- **Tình huống:** Sau khi được bạn duyệt chạy tiếp, AI (`Empathy Strategist`) sẽ nhào vào và "Bơm" thêm giải pháp chiến lược trực tiếp vào phần cuối của file `RS...md` kia.
- Nó sẽ đưa ra định hướng Logic + Định hướng Cảm xúc (Ví dụ: "Người dùng đang rất quạu, nên flow này phải hạn chế màu đỏ, dùng copy rành rọt dứt khoát").
- **Hành động của bạn:** Nó lại dừng lại và chờ bạn chốt.
  - Nếu hướng đi ổn, bạn gõ: **"Proceed"** để chốt hạ chiến lược chung.

### Bước 6: Thưởng thức Thành quả (Spec Generation)
- Từ chiến lược được duyệt phía trên, AI (`UX Designer & Writer`) sẽ tuôn trào ra file đặc tả cuối cùng `URD...md` (UX Spec).
- File này tự động chứa sơ đồ luồng Mermaid cực kỳ rõ nét phân chia nhánh lỗi/thành công, kèm bảng Copywriting đã được gọt giũa kĩ lưởng về Tone-of-Voice. 
- Đến bước này, toàn bộ quy trình thiết kế Spec trong nội bộ máy đã hoàn tất. Bạn có thể tự tay tinh chỉnh thêm, hoặc xóa bớt câu chữ nếu bạn muốn ở file Markdown này.


## 🔗 Bước Bổ trợ: Đồng bộ chia sẻ lên Google Docs
Trong đa số trường hợp, sếp hoặc dev bên ngoài sẽ không đọc file Markdown trên IDE. Bạn cần xuất Spec này ra Google Docs:
1. Copy đường dẫn lưu file `URD...md` vừa sinh ra ở Bước 6.
2. Từ khung chat, gõ lệnh:
```bash
/sync_gdocs [Đường dẫn file URD...md]
```
3. Hệ thống sẽ ngay lập tức convert file Markdown của bạn thành 1 văn bản Google Docs "đẹp nức nở" (Giữ nguyên thẻ Table, Heading, Bold).
4. *(Lưu ý: Nếu đây là lần chạy lệnh /sync_gdocs đầu tiên trong ngày, trình duyệt của bạn có thể bật lên bắt bạn ấn Confirm ủy quyền Google Account, bạn cứ bấm "Allow" nhé).*
5. **Đỉnh cao:** Sau khi tạo xong, nó sẽ tự động chèn cái Link Google Docs đó gắn ngược vào bên trong file `URD...md` của bạn. Và từ lần 2 trở đi, nếu bạn có sửa file Markdown và muốn đè lên Docs cho sếp xem bản cập nhật, bạn chỉ cần nã lại lệnh `/sync_gdocs`. Hệ thống sẽ không đẻ ra file Google Docs mới, mà thay vào đó là ghi đè cái mới nguyên xi lên file hiện tại của bạn.

> [!TIP] **Mẹo cho người mới nạp Workspace:**
> Theo mặc định, lệnh `/sync_gdocs` chỉ chạy được trên máy của người cấu hình Google Cloud ban đầu. Để **bạn** (một member vừa clone repo về) cũng có thể chạy lệnh này:
> - Hãy xin Product Owner / người quản trị file `credentials.json`.
> - Copy file đó bỏ vào thư mục `.agents/scripts/` trên máy tính của bạn.
> - Lần đầu chạy lệnh `/sync_gdocs`, trình duyệt sẽ mở lên để bạn tự đăng nhập bằng tài khoản Gmail của bạn. File sẽ tự động được gửi lên Drive của bạn!
