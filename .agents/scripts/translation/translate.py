import glob
import re

files = glob.glob('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/*.html')

translations = {
    # avatar.html
    r'Avatar supports image, text initials, and icon fallbacks.': r'Avatar hỗ trợ hiển thị hình ảnh, ký tự viết tắt, và biểu tượng dự phòng.',
    r'Avatars can be rendered as full circles or slightly rounded squares.': r'Avatar có thể hiển thị dưới dạng hình tròn khối hoặc hình vuông bo góc nhẹ.',
    
    # badge.html
    r'Use the badge-round modifier to reduce the border radius \(e.g. 8px\).': r'Sử dụng class bổ trợ badge-round để giảm \border-radius\ (ví dụ: 8px).',
    r'Use icon-only variants for compact spaces.': r'Sử dụng các biến thể \icon-only\ cho không gian hẹp.',
    
    # button.html
    r'A low-emphasis variant without border or background, keeping brand-colored text.': r'Biến thể có độ nhấn mạnh thấp, không có đường viền hay hình nền, giữ nguyên màu chữ của thương hiệu.',
    r'An inline text button with an underline, representing the Link hierarchy.': r'Nút bấm dạng chữ \inline\ kèm đường gạch chân, biểu thị cấu trúc của \Link\.',
    r'The standard medium size, used in most cases. Height: 48px.': r'Kích thước vừa tiêu chuẩn, được sử dụng trong hầu hết các trường hợp. Chiều cao: 48px.',
    r'Large size for prominent actions like modal triggers or main form submissions. Height: 56px.': r'Kích thước lớn dành cho các hành động nổi bật như mở \modal\ hoặc gửi biểu mẫu chính. Chiều cao: 56px.',
    r'Small size for localized actions inside cards or dense tables. Height: 40px.': r'Kích thước nhỏ dành cho các hành động cục bộ bên trong \card\ hoặc các bảng dữ liệu dày. Chiều cao: 40px.',
    
    # card.html
    r'Deploy your new project in one-click.': r'Triển khai \project\ mới của bạn chỉ với một lần nhấp.',
    r'Learn how to integrate the design system.': r'Tìm hiểu cách tích hợp \design system\.',
    
    # dropdown.html
    r'Displays a list of actions or options triggered by clicking an element, used for navigation or command menus.': r'Hiển thị danh sách các hành động hoặc tùy chọn khi nhấp vào một thành phần, được sử dụng cho các menu hướng dẫn điều hướng (\navigation\) hoặc lệnh (\command menus\).',
    
    # modal.html
    r'Are you sure you want to deactivate your account\? All of your data will be permanently removed. This action cannot be undone.': r'Bạn có chắc chắn muốn vô hiệu hóa tài khoản không? Tất cả dữ liệu của bạn sẽ bị xóa vĩnh viễn. Hành động này không thể hoàn tác.',
    r'Click the buttons below to open the modal in different sizes.': r'Nhấn vào các nút bên dưới để mở \modal\ với các kích thước khác nhau.',
    r'This is a small modal, ideal for quick confirmations or simple forms.': r'Đây là một \modal\ kích thước nhỏ, lý tưởng cho các thông báo xác nhận nhanh hoặc form đơn giản.',
    r'This is a medium modal \(default size\), suitable for most content like settings, complex forms, or detailed information.': r'Đây là một \modal\ kích thước trung bình (kích thước mặc định), phù hợp với hầu hết nội dung như cài đặt settings, form phức tạp, hoặc thông tin chi tiết.',
    r'This is a large modal, providing ample space for data-heavy views, wizards, or complex multi-step processes.': r'Đây là một \modal\ kích thước lớn, cung cấp không gian rộng rãi cho các view hiển thị nhiều dữ liệu, wizard, hoặc các quy trình nhiều bước phức tạp.',
    r'Scrollable content area ensures the footer remains visible even with extensive information.': r'Khu vực nội dung hỗ trợ \scroll\ đảm bảo \footer\ luôn hiển thị ngay cả khi thông tin dài.',
    r'Placeholder for large content mapping\.\.\.': r'Vị trí \placeholder\  cho khối nội dung lớn...',

    # tab.html
    r'Manage your account settings and preferences here. Notice how the active tab has a solid brand underline.': r'Quản lý cài đặt \settings\ tài khoản và tùy chọn của bạn tại đây. Lưu ý rằng \tab active\ có một đường viền gạch chân liền lạc theo màu thương hiệu.',
    r'Update your password and robust security questions to protect your account from unauthorized access.': r'Cập nhật mật khẩu và các câu hỏi bảo mật mạnh mẽ để bảo vệ tài khoản của bạn khỏi truy cập trái phép.',
    r'Configure how and when you want to be notified about important events related to your services.': r'Cấu hình cách thức và thời điểm bạn muốn nhận thông báo về các sự kiện quan trọng.',
    r'This content should not be visible normally because the tab is disabled.': r'Nội dung này thường không được hiển thị vì \tab\ đang ở trạng thái \disabled\.',
    r'Pill tabs are useful for inner-page navigation where a line-style tab might conflict with a higher-level navigation element.': r'\Pill tabs\ hữu ích cho việc điều hướng \navigation\ bên trong trang nơi mà \line-style tab\ có thể xung đột với thành phần \navigation\ cấp cao hơn.',
    r'Analytics view. The active state resembles a raised card on a slightly darker background.': r'View phân tích dữ liệu. Trạng thái \active\ giống như một \card\ nổi lên trên nền màu tối hơn.',
    r'Reports and exported data view.': r'View của Báo cáo và xuất dữ liệu.',
}

def translate_match(match):
    original = match.group(0)
    inner_html = match.group(1)
    normalized = " ".join(inner_html.split())
    
    for eng, vie in translations.items():
        # Match using re to allow literal string matching while handling escapes
        if re.search(eng, normalized):
            vie = vie.replace('\\', '')
            # replace inner_html and rebuild tag
            # We assume no complex nesting in these <p> tags for simplicity
            return original.replace(inner_html, vie)
    
    return original

total_replaces = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # process only p tags
    content = re.sub(r'<p[^>]*>(.*?)</p>', translate_match, content, flags=re.DOTALL)
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        total_replaces += 1

print(f"Updated {total_replaces} files")
