import os
import re
import urllib.request
import urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = [
    "MyTelkomsel app review UI",
    "MyTelkomsel redesign app site:youtube.com",
    "MyTelkomsel super app"
]

out_dir = "/Users/tuanvq/.gemini/antigravity/brain/ec4aac1b-ff39-41f2-a8f6-fe8f847cfc51"
count = 10

images_saved = []

for q in queries:
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        continue
    
    matches = re.findall(r'murl&quot;:&quot;(.*?)&quot;', html)
    
    for img_url in matches:
        if len(images_saved) >= 12: break
        try:
            req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_img, context=ctx, timeout=5) as img_response:
                data = img_response.read()
                if len(data) > 15000:
                    filename = f"mytelkomsel_extra_{count}.jpg"
                    path = os.path.join(out_dir, filename)
                    with open(path, 'wb') as f:
                        f.write(data)
                    print(f"Downloaded: {filename}")
                    images_saved.append(filename)
                    count += 1
        except Exception:
            pass
