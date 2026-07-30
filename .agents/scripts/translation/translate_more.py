import glob
import re

files = glob.glob('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/*.html')

translations = {
    r'The default high-emphasis button for principal actions.': r'Nút bấm có độ nhấn mạnh cao mặc định cho các hành động chính.',
    r'For medium-emphasis secondary actions. Has a brand-colored border and text.': r'Dành cho các hành động phụ có độ ưu tiên trung bình. Có đường viền và chữ theo màu thương hiệu.',
    r'Icon: Info circle \(filled\), text color: #34404B.': r'Icon: Info circle (filled), màu chữ: #34404B.',
    r'This is alert content.': r'Đây là nội dung alert.',
    r'Warning Icon: Exclamation-triangle \(filled\), color: #FFBE40.': r'Warning Icon: Exclamation-triangle (filled), màu sắc: #FFBE40.',
    r'Destructive Icon: Xmark-circle \(filled\), color: #FF5040.': r'Destructive Icon: Xmark-circle (filled), màu sắc: #FF5040.',
    r'Positive Icon: Check-circle \(filled\), color: #33CC80.': r'Positive Icon: Check-circle (filled), màu sắc: #33CC80.',
    r'Use the btn base class along with variant and size modifiers.': r'Sử dụng base class btn cùng với các class modifiers cho variant và size.',
    r'Use the badge base class along with variant, size, and shape modifiers.': r'Sử dụng base class badge cùng với các class modifiers cho variant, size, và shape.',
    r'Use the avatar base class with avatar-image or fallback content.': r'Sử dụng base class avatar với avatar-image hoặc nội dung fallback.',
}

def translate_match(match):
    original = match.group(0)
    inner_html = match.group(1)
    normalized = " ".join(inner_html.split())
    
    for eng, vie in translations.items():
        if re.search(eng, normalized):
            vie = vie.replace('\\', '')
            # replace inner_html and rebuild tag
            return re.sub(eng, vie, original)
    
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
