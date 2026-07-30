import glob
import re

files = glob.glob('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/*.html')

translations = {
    r'Use btn-icon-only for an evenly-padded square action button, ensuring an aria-label is provided.': r'Sử dụng btn-icon-only cho nút hành động hình vuông \action button\, đảm bảo luôn cung cấp thuộc tính \aria-label\.',
    r'Add btn-icon-left or btn-icon-right to correctly space an inline SVG.': r'Sử dụng class \btn-icon-left\ hoặc \btn-icon-right\ để tạo khoảng cách phù hợp cho \icon SVG inline\.'
}

def translate_match(match):
    original = match.group(0)
    inner_html = match.group(1)
    normalized = " ".join(inner_html.split())
    
    for eng, vie in translations.items():
        if eng in normalized:
            vie = vie.replace('\\', '')
            return re.sub(eng, vie, original)
    
    return original

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = re.sub(r'<p[^>]*>(.*?)</p>', translate_match, content, flags=re.DOTALL)
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
