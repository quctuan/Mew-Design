---
name: write-issues-jira
description: Phân rã công việc thành đầu ra, interview tối thiểu, lưu bản nháp và tạo Jira Issues qua ego-browser cho các repo thuộc phạm vi MyVNPT. Dùng khi người dùng muốn ghi nhận công việc để quản lý nhìn thấy, không dùng để nhập giờ công hoặc quản lý trạng thái Jira.
compatibility: Pi với ego-browser; subagents là tùy chọn.
---

<objective>
Giúp người đang dùng ghi nhận công việc thực tế lên Jira bằng issue ngắn, đúng vai trò và có đầu ra rõ. Dùng chung cho các repo thuộc phạm vi MyVNPT, gồm Web MyVNPT/DigiShop và các công cụ được người dùng xác nhận; không coi các workstream là Product độc lập trái với authority của repo.
</objective>

<quick_start>
Nhận task hoặc danh sách task và context tùy chọn từ người dùng.
Command chuẩn: /skill:write-issues-jira; alias: /write-issues-jira.
Không có task thì hỏi người dùng cần ghi nhận công việc nào. Không yêu cầu cú pháp dấu nháy; nếu ranh giới task/context không rõ và ảnh hưởng nội dung thì hỏi.
Đọc cấu hình → interview và lưu local từng round → duyệt nội dung → chọn nơi tạo → tạo 1 issue thử → tạo phần còn lại → trả links.
</quick_start>

<essential_principles>
- Một issue = một đầu ra có thể kiểm chứng. Hoạt động hỗ trợ nằm trong mô tả; chỉ tách khi có đầu ra độc lập. Cuộc họp có thể là issue nếu có kết luận/đầu ra rõ.
- Viết minimal bằng tiếng Việt, trừ khi người dùng yêu cầu khác. Không tự thêm phần audit, checklist, số liệu, bằng chứng hay chi tiết không cần thiết.
- Hỗ trợ việc đã làm, đang làm và dự kiến làm; giữ đúng cách diễn đạt thực tế, không tự nâng thành đã hoàn tất. Không bắt buộc một trường trạng thái công việc.
- Có thể suy luận cách viết/bố cục từ context và issue tương tự; không suy luận sự kiện đã xảy ra, phê duyệt, thời gian làm việc hoặc kết quả.
- Xác nhận của người dùng đủ để ghi nhận việc họ đã làm. Không bắt buộc bằng chứng là file/link; chỉ làm rõ đầu ra nếu chưa hiểu.
- Không Log work/ghi giờ, chuyển trạng thái Jira, sửa issue cũ hay tự thêm sprint, priority, labels. Chỉ điền trường must-have. Nếu Jira tự đặt default thì không cố xóa; nếu trường ngoài dự kiến là bắt buộc thì hỏi giá trị chưa biết.
- Không hardcode tên, tài khoản, vai trò PO, Jira URL/project hay đường dẫn ego-browser theo máy tác giả.
- Tôn trọng AGENTS.md và authority của repo; không đọc secrets, auth storage, cookies hoặc đưa thông tin riêng từ HUMAN.md vào tài liệu chia sẻ. Không tự stage/commit.
- Chỉ tạo issue sau khi người dùng duyệt toàn bộ nội dung local và xác nhận đích tạo. Đọc dữ liệu Jira không cấp quyền sửa nội dung ngoài batch.
</essential_principles>

<process>
1. Xác định repo root và đọc hướng dẫn repo trước. Đọc HUMAN.md (ưu tiên override đúng phạm vi theo hướng dẫn repo), docs/jira-issue.md và context liên quan trực tiếp đến task. Không quét mọi repo/workstream hoặc toàn bộ kiến thức local. Nếu phạm vi không thuộc MyVNPT và các công cụ được xác nhận, dừng làm rõ.
2. Kiểm tra bốn thông tin: job title; đầu ra thuộc vai trò; mục đích và người đọc issue; format. Có đủ thì không hỏi lại. Thiếu hoặc xung đột thì interview, không tự đổi authority. Tên tool trong HUMAN.md không đồng nghĩa với quyền truy cập.
3. Interview theo frontier: hỏi cùng round những quyết định đã đủ điều kiện, đợi trả lời trước khi hỏi nhánh phụ thuộc. Mỗi câu một nghĩa, ngắn, có đề xuất:
   ❓ **Q1 — Tiêu đề:** Câu hỏi.
   ➡️ Đề xuất cụ thể.
   Không bắt người dùng tìm facts agent có thể đọc trong phạm vi được phép. Không load lại toàn bộ grilling framework nếu các chỉ dẫn này đủ.
4. Khi setup được duyệt, lưu cấu hình chung vào docs/jira-issue.md theo mẫu templates/jira-issue-config.md, giữ phần cấu hình hiện hữu hợp lệ. HUMAN.md chỉ cập nhật khi được phép riêng; không sao chép thông tin cá nhân sang cấu hình chung. Không bịa setup chỉ để đi tiếp.
5. Phân rã task và soạn issue theo format repo, hoặc mẫu templates/issue.md. Mỗi round đưa bản nháp ngắn cùng câu hỏi có tác động đến tính đúng. Không hỏi thông tin dễ suy ra hoặc cố điền hết phần optional. Dùng dẫn chứng/issue mẫu chỉ trong quyền đọc đã cho.
6. Sau mỗi round lưu mọi issue đang biết vào docs/jira-issues/ theo quy tắc local_artifacts bên dưới. Nếu chưa có nội dung issue ở round setup thì chỉ lưu cấu hình đã xác nhận, không tạo issue giả. Trả link file local để người dùng review.
7. Khi không còn điểm mơ hồ đáng kể, trình bày danh sách tiêu đề và bản nháp local; xin duyệt toàn batch. Đánh dấu approved đúng phiên bản đã duyệt. Sửa nội dung sau duyệt phải về draft, xóa approved_version và xin duyệt lại issue bị đổi.
8. Hỏi board cần tạo ở mỗi batch; có thể đưa board đã cấu hình làm đề xuất, không tự chọn. Đọc skill ego-browser đang được cài qua discovery/read_skill, hoặc đường dẫn người dùng cung cấp. Không có thì dừng báo dependency thiếu, không đổi browser hay API.
9. Tạo một TaskSpace cho toàn batch bằng lệnh ego-browser thật và lưu spaceId. Xác minh tài khoản hiện tại, board, project, issue type và người được giao (mặc định chính người đang dùng, không mặc định theo account nếu không khớp). Board có thể lọc nhiều project; dùng giao diện để xác định đích, hỏi khi còn mơ hồ. Không tự giả định board membership hoặc chắc chắn issue sẽ hiện trên board khi bộ lọc không khớp.
10. Chỉ hỏi giá trị must-have chưa biết. Nếu thiếu login/MFA/permission prompt thì handOff theo ego-browser, không đọc credentials; resume cùng TaskSpace sau xác nhận. Khi người dùng lấy quyền điều khiển thì dừng toàn batch/subagents, không route around.
11. Lưu đích tạo và approved_version vào metadata trước khi tạo. Đặt creating ngay trước hành động Create cho issue thử. Sau khi tạo, kiểm tra issue key/URL, đúng project/type/assignee và nội dung đã duyệt qua một quan sát đủ rõ. Ghi created cùng key/URL ngay khi có xác nhận. Không coi click receipt/toast chung là đủ nếu chưa xác định được issue.
12. Issue thử đúng thì tiếp tục toàn batch không xin phép lần nữa. Nếu sai nội dung/đích, thiếu giá trị hoặc phải thay bản duyệt: dừng hỏi, không tự sửa issue đã tạo. Chỉ tạo song song theo parallel_execution; không đủ điều kiện thì tuần tự.
13. Trước khi báo hoàn tất, đối chiếu toàn batch với local; kết thúc TaskSpace đúng một lần theo ego-browser khi thành công. Nếu đang lỗi hoặc chờ người dùng thì không finish. Trả links Jira click được, số đã tạo/tổng và phần chưa tạo hoặc cần kiểm tra. Không báo complete nếu còn issue chưa xác minh.
</process>

<local_artifacts>
- Flat files: docs/jira-issues/{session_id}--{local_id}--{slug}.md. Không thêm folder round hay approved. Chọn session_id gồm thời gian có múi giờ quy đổi UTC và suffix ngẫu nhiên để chống trùng; local_id ổn định trong phiên.
- Dùng frontmatter mẫu templates/issue.md. created_at bất biến; updated_at theo clock thực tế dạng ISO 8601 có múi giờ. Không dùng ngày ví dụ hay ngày suy ra từ task.
- version bắt đầu 1; tăng khi nội dung issue đổi, không tăng chỉ vì cập nhật publication metadata. round ghi round interview hiện tại. Cập nhật cùng file sau mỗi round, không tạo bản lồng nhau hay hứa lưu lịch sử immutable.
- publication_status: draft (chưa duyệt), approved (đã duyệt), creating (đã bắt đầu gửi), created (đã xác minh), needs-check (không biết có tạo thành công không).
- Chỉ bắt đầu tạo khi publication_status=approved và approved_version=version; ngay trước submit chuyển sang creating nhưng giữ approved_version. jira chứa site, board URL, project key, issue type, assignee đã xác nhận; key/url có thể null trước khi tạo. Metadata và ghi chú local không được paste vào Jira.
- Khi tiếp tục phiên cũ: dùng session_id/local_id và file đã có, không chỉ so tiêu đề hoặc chọn file mới nhất. Bỏ qua issue có key/URL hoặc created. Issue creating còn dở phải thành needs-check và đối soát trước.
- Nếu một đầu ra đã được ghi trong phiên khác, đưa candidate để người dùng xác nhận, không âm thầm merge hoặc tạo lại.
</local_artifacts>

<failure_handling>
- Trước Create có thể sửa lỗi form rồi kiểm tra lại. Sau Create mà lỗi/timeout hoặc có late effects: ghi needs-check và tìm issue vừa tạo theo project, creator, tiêu đề, nội dung và thời điểm. Không bấm Create lại khi kết quả chưa rõ.
- Tìm thấy đúng một issue phù hợp thì ghi key/URL sau xác minh. Không tìm thấy hoặc có nhiều candidate mà chưa loại trừ tạo thành công thì dừng hỏi; sự vắng mặt trong search có thể do index chậm, không phải bằng chứng đủ để retry.
- Nếu tạo thành công nhưng ghi local thất bại, giữ key/URL trong báo cáo, dừng phần bị ảnh hưởng và khôi phục local; không tạo lại.
- Lỗi riêng một issue không được báo như thành công. Lỗi chung (permission, sai project, browser ownership) phải dừng mọi worker liên quan. Không tự retry bằng agent mới.
</failure_handling>

<parallel_execution>
Chỉ main session tạo/kết thúc TaskSpace, chọn nơi tạo, duyệt và quản lý batch. Sau pilot, main tạo Pages riêng trong cùng TaskSpace; số worker theo Page budget thực tế và khả năng runtime. Nếu không tách được tab/control an toàn hoặc không có subagents, tạo tuần tự.
Launch worker độc lập trong cùng lượt, run_in_background=true; không để nhiều agent chung một Page hay file. Mỗi worker có thể nhận nhiều issue.
Delegation phải có Task / Context / Link References / Expected Outcome, gồm:
- spaceId và Page label được cấp; không new TaskSpace, không operate tab khác, không handOff/finish toàn space;
- đúng file issue, version đã duyệt, project/type/assignee, hướng dẫn form đã kiểm chứng từ pilot;
- chỉ được tạo issue được giao và cập nhật metadata các file đó; không sửa nội dung, shared config, issue khác hay Jira status;
- đọc ego-browser skill, tuân thủ ownership; báo main khi cần người dùng hoặc gặp lỗi chung;
- trả State / Result / Needs, mapping local_id → key/URL hoặc lỗi chưa giải quyết.
Main đối chiếu file và evidence thực tế của từng worker, không chỉ tin summary. Khi pilot đã chứng minh form, mỗi issue còn lại chỉ cần kiểm chứng vừa đủ; không lặp audit dài.
</parallel_execution>

<success_criteria>
Cấu hình chung được duyệt; issues minimal lưu đúng phiên/version; chỉ bản được duyệt được xuất bản. Issue thử được kiểm chứng trước phần còn lại. Không có retry mù hoặc ghi giờ/chuyển status. Mỗi issue đã tạo có key/URL và link chat; mọi phần chưa chắc chắn được báo rõ.
</success_criteria>
