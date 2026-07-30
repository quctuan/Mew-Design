import os
import re
import urllib.request
import urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

query = "MyTelkomsel UI UX app case study behance"
url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(e)
    exit(1)

matches = re.findall(r'murl&quot;:&quot;(.*?)&quot;', html)
out_dir = "/Users/tuanvq/.gemini/antigravity/brain/ec4aac1b-ff39-41f2-a8f6-fe8f847cfc51"
count = 0

for img_url in matches:
    try:
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img, context=ctx, timeout=5) as img_response:
            data = img_response.read()
            if len(data) > 30000:
                ext = img_url.split('.')[-1].split('?')[0]
                if ext.lower() not in ['png', 'jpg', 'jpeg', 'webp']:
                    ext = 'jpg'
                filename = f"mytelkomsel_screen_{count}.{ext}"
                path = os.path.join(out_dir, filename)
                with open(path, 'wb') as f:
                    f.write(data)
                print(f"Downloaded: {filename}")
                count += 1
                if count >= 6:
                    break
    except Exception as e:
        pass
