import glob
import re

files = glob.glob('/Users/tuanvq/Documents/gds-myvnpt-wiki/design-docs/pages/components/*.html')

english_texts = set()

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all <p>...</p> tags
    p_tags = re.findall(r'<p[^>]*>(.*?)</p>', content, flags=re.DOTALL)
    for p in p_tags:
        text = p.strip()
        # Remove tags inside
        text = re.sub(r'<[^>]+>', '', text)
        text = " ".join(text.split())
        
        # Check if it has any Vietnamese characters (heuristic)
        if not re.search(r'[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', text.lower()):
            if len(text) > 5:
                english_texts.add(text)

with open('en_texts.txt', 'w', encoding='utf-8') as f:
    for t in english_texts:
        f.write(t + "\n")

print(f"Found {len(english_texts)} English sentences")
