def replace_multiple(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for k, v in replacements.items():
        if k in content:
            content = content.replace(k, v)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replacements_checklist = {
    'nhé!': 'công việc:',
    'Thay vì phải tự tạo từng thư mục file, bạn chỉ cần tải toàn bộ "bộ não" của dự án này về máy. Đánh dấu tick khi bạn đã làm xong:': 'Vui lòng tải toàn bộ cấu trúc không gian làm việc về máy tính cá nhân bằng các bước sau:',
    'Chạy lệnh tải mã nguồn từ kho lưu trữ GitHub:': 'Sử dụng lệnh dưới đây để tải mã nguồn từ kho lưu trữ GitHub hiện tại:',
    'Di chuyển vào thư mục dự án vừa tải về:': 'Di chuyển vào thư mục dự án vừa thiết lập thành công:',
    'hấp thụ': 'phân tách dữ liệu',
    'Test AI: Nhắn câu này vào khung Chat để kiểm tra xem nó đã nhận diện hệ thống chưa:': 'Kiểm tra hoạt động hệ thống AI: Nhập nội dung sau vào khung Chat để kiểm tra tính năng giao tiếp:',
    'Mọi thay đổi mà đồng nghiệp tạo ra trong `knowledge base` đều sẽ được hiển thị trên web. Nếu bạn muốn chạy Web nội bộ (Local) trên máy mình:': 'Mọi thay đổi từ bộ phận liên quan tạo ra trong `knowledge base` đều sẽ được tự động đồng bộ hóa trên hệ thống web. Để kiểm tra quy trình hoạt động (Local) trên thiết bị thiết kế của mình:',
    'Cắm máy chủ (Local Server): Tắt chạy lệnh:': 'Khởi chạy môi trường chạy ngầm máy chủ nội bộ (Local Server): Sử dụng lệnh:',
    'Trải nghiệm: Truy cập': 'Kiểm tra hiển thị: Truy cập',
    'Khi làm xong nhiệm vụ (VD: Phân tích UI, viết Specs), đây là cách bạn đẩy bài lên mạng:': 'Sau khi hoàn thành tạo mới hoặc cập nhật tài liệu (Ví dụ: Phân tích UI, viết chức năng Specs), đây là bước tiến hành xuất bản cập nhật hiển thị tài liệu lên trang web nền tảng:',
    'Nhờ AI viết nội dung mới hoặc tự viết `.md` vào đúng thư mục nhóm `knowledge base/`': 'Tạo mới hoặc cập nhật tài liệu dưới định dạng `.md` và đảm bảo chuyển tới đúng thư mục nhóm `knowledge base/` (có thể kết hợp sử dụng AI).',
    'Chờ Admin (Boss) vào tận nơi rà soát File gốc và phản hồi duyệt (Approved).': 'Chờ Quản trị viên (Admin/PO) tiến hành kiểm tra mã nguồn và phê duyệt (Approved) các cập nhật.',
    'Gõ duy nhất một câu lệnh Slash Command vào khung chat AI:': 'Kích hoạt lệnh Slash Command này một cách độc lập trong cửa sổ tương tác cùng AI:',
    'Tựa lưng uống nước 20 giây, F5 tải lại trang Vercel Public của Admin cấp là hoàn tất!': 'Đợi khoảng 20-30 giây cho hệ thống xử lý đóng gói. Hãy tải lại đường dẫn Vercel Public để kiểm tra cập nhật trên trang điện tử!',
    '🍾 **Chúc mừng bạn đã check xong tuần đầu tiên.** Chào mừng bạn gia nhập dự án! Hãy quay lại [Nguyên lý làm việc](../getting-started/) để học cách điều phối các hệ thống Teams đồ sộ.': 'Màn hình thiết lập hoàn tất thủ tục kiểm tra của tuần đầu tiên. Chào mừng bạn đã chính thức tham gia vào dự án! Vui lòng tham khảo [Nguyên lý làm việc](../getting-started/) để nắm rõ phương pháp điều phối các nhóm Agentic AI.'
}

replace_multiple('wiki/docs/bat-dau/checklist.md', replacements_checklist)

replacements_cong_cu = {
    'Dưới đây là danh sách các công cụ lõi được sử dụng trong hệ sinh thái Agentic AI Workspace của dự án. Mỗi công cụ đều được phân bổ chuyên biệt cho từng vai trò để đảm bảo mọi quy trình diễn ra trơn tru, gọn gàng và hạn chế "loãng" thông tin.': 'Dưới đây là danh sách các công cụ nền tảng được sử dụng trong hệ sinh thái Agentic AI Workspace của dự án. Mỗi công cụ đều được định hướng phân bổ sử dụng chuyên biệt cho từng loại vai trò nhằm đảm bảo mọi nghiệp vụ diễn ra suôn sẻ, hệ thống hóa và tập trung hiệu quả thông tin.',
    'Gắn liền với Role:': 'Đối tượng sử dụng chính:',
    'Mục đích sử dụng:': 'Mục đích tham chiếu:',
    'Không gian chỉ huy đầu não. Đây là nơi duy nhất bạn điều phối binh đoàn AI tạo sinh khổng lồ thay vì chỉ lập trình code.': 'Là trung tâm điều phối xử lý dữ liệu tự động. Đây là giao diện quan trọng quản trị quá trình tự nhận diện đánh giá hệ thống Agentic AI song song với công tác lập trình nguyên thủy.',
    'Đối với PO:': 'Với vai trò Product Owner (PO):',
    'PO mở Tool này dùng để "gọi hồn" (kích hoạt) các Agent Teams như đội Nghiên cứu thị trường hay Jira Tracking. PO giao việc (Briefing) qua khung Chat, thực thi quyền sinh sát (Kiểm duyệt `HITL - Human in The Loop`), phê duyệt các Specs/Tài liệu nội dung và đẩy nó thẳng lên hệ thống Website (Wiki) nội bộ bằng lệnh chớp nhoáng `/deploy-website`.': 'Sử dụng hệ thống này để khởi tạo tương tác tổ đội: Cung cấp yêu cầu công việc qua khung chat, kiểm soát quá trình làm việc của công cụ tự động (`HITL - Human in The Loop`), đánh giá lại tài liệu kỹ thuật (Specs) và kết xuất trực tiếp lên quy trình xuất bản trang Web (Wiki) với quá trình đóng gói `/deploy-website`.',
    'Nơi để triệu hồi `ux-design-team` vẽ luồng hành vi dựa trên Phân tích Nỗi đau, và triệu hồi `uiux-audit-team` để "giết rệp" (bắt lỗi Edge Cases) từ Link Figma. Mọi chất xám đều được gọt giũa ở đây trước khi đem ra vẽ tay.': 'Giao diện tương tác giải pháp phác thảo thông qua quy trình `ux-design-team`, xây dựng trải nghiệm hành vi có định lượng và gọi `uiux-audit-team` để phản biện điểm không thỏa đáng logic (Edge Cases) trên luồng cấu trúc thông tin trước khi thực thi cụ thể bằng các công cụ đồ họa UI.',
    'Bàn vẽ thực địa, nơi các luồng suy nghĩ và phân tích từ Antigravity (JTBD Flow) được cụ thể hoá thành Giao diện Tương tác.': 'Là công cụ thiết kế, một nền tảng chuyển giao từ các giải pháp kiến trúc luồng dữ liệu thô chuẩn hóa trên Antigravity (JTBD Flow) tạo thành hình thái các Giao diện Tương tác cuối cùng.',
    'Thiết kế & Prototype:': 'Thiết kế & Tạo nguyên mẫu (Prototype):',
    'Phác thảo Wireframes thấp đến Màn hình UI độ nét cao. Gắn liên kết tương tác thật (Prototype) cho App MyVNPT.': 'Xây dựng biểu đồ mô phỏng màn hình từ kết cấu tính năng căn bản (Wireframes) cho đến hình thễ màn hình UI chuẩn xác. Tạo lập kết nối tương tác thật từ môi trường chức năng nguyên mẫu (Prototype) cho môi trường ứng dụng dự án MyVNPT.',
    'Kiểm định AI:': 'Kiểm điểm bởi AI:',
    'Khi màn hình vẽ xong, Link Figma sẽ được cung cấp làm "Thức ăn ngõ vào" (Input) cho `uiux-audit-team` quét độ sai lệch giao diện (UI) và ngữ cảnh chữ nghĩa (UX Writing).': 'Hệ thống đánh giá trên tập link gốc sẽ đóng vai trò như đầu vào nhận tiếp thông tin phục vụ bộ phận công cụ hệ thống `uiux-audit-team` truy quét các khác biệt không trùng khớp giữa chức năng hiện và nền đồ họa đã thiết lập, qua đó điều chỉnh mức độ đáp ứng cấu trúc văn phong (UX Writing).',
    'Quản lý danh mục Công việc (Backlog) cốt lõi của máy móc và con người.': 'Quản lý toàn bộ Danh sách phân loại dữ liệu định hướng phát triển tổng quát hệ thống Backlog trên tổng quy trình dự án.',
    'Điều khiển tiến độ:': 'Quản trị Tiến độ Dự án:',
    'PO dùng Jira để tạo các Ticket chẻ nhỏ tính năng lớn, ấn định thời gian Sprint.': 'Sử dụng nền tảng tạo và chia quá trình phân bố những nhiệm vụ, thẻ yêu cầu để phân loại cấu trúc tính năng theo thời hạn giới hạn (Quản lý các thời điểm kết thúc Sprint).',
    'Báo cáo không chạm:': 'Tổng hợp số liệu Báo cáo (Automated Tracking):',
    'Hệ thống AI `jira-tracking-team` sẽ luồn lách vào mỏ dữ liệu Jira mỗi đêm, múc ra những Tickets nào đang bị trễ hạn, ai đang ngâm lâu, mảng nào đang "Bùng cháy" để chắt lọc cảnh báo cho sếp.': 'Hệ thống cấu phần được tạo trên thư mục lưu trữ hoạt động định kì lấy thông tin rà soát và thông kê trên API Jira, từ đó lọc loại nhóm đối tượng có hiện tượng bị chững thao tác (Blocked), cảnh báo trễ hạn trên diện nhiệm vụ theo hệ thống để đưa ra phân tích chính xác giúp người quản đốc trực tiếp điều phối thông tin công việc hiệu quả.',
    'Kênh Giao tiếp Siêu tốc (Alerting & Trigger).': 'Khung trao đổi cảnh quan nhanh với hệ thống nhận cảnh báo từ môi trường điều phới tự động (Alerting & Notification).',
    'Báo cáo định kỳ:': 'Bảo đảm Báo cáo thường kì (Reporting):',
    'Khung cửa sổ telegram nhóm là nơi đội ngũ `jira-tracking-team` xả hàng mỗi sáng, bắn bản tin tóm tắt tiến độ cực xịn do tụi nó gọt dũa xong. PO chỉ cần mở điện thoại lướt nhóm Telegram để nắm đại cuộc dự án lúc 8h sáng.': 'Nhờ vào khả năng khai báo chức năng, tổ đội truy vết bằng kỹ thuật Python tự cập nhật truy vấn đến tập lệnh thông qua kênh để mang lại kết quả thông báo rõ ràng về các thành phẩm tiến độ ngay trong Group công việc. Công cụ hỗ trợ để cập nhật nhanh quy mô các yếu điểm trong lịch trình thao tác dự án hằng ngày.',
    'Văn hoá Handoff:': 'Quản lý Lưu lượng Chuyển giao (Handoff Process):',
    'Telegram không dùng để lưu tài liệu. Chỉ dùng để Tag Ping (Gào thét) gọi nhau vào Review tài liệu: *"Anh zai xem tài liệu Specs tại Wiki nhé"*.': 'Nền tảng không cấu thành được làm việc trên chức năng lưu trữ dài hạn như một tủ lưu trữ thông tin dự án. Công năng tối ưu được vận dụng qua hành vi đề xuất kiểm duyệt cập nhật tài liệu đã hoàn thiện: Ví dụ việc sử dụng Tag Ping hỗ trợ nhanh tương đồng như lệnh *"Thông tin về bản Specs hệ thống phiên bản X được kiểm duyệt vào khu vực Wiki".*'
}
replace_multiple('wiki/docs/bat-dau/cong-cu.md', replacements_cong_cu)
