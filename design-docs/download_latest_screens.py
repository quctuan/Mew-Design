import os
import urllib.request
import re
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

out_dir = "/Users/tuanvq/.gemini/antigravity/brain/ec4aac1b-ff39-41f2-a8f6-fe8f847cfc51"
url = "https://play.google.com/store/apps/details?id=com.telkomsel.telkomselcm&hl=en"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(e)
    exit(1)

shots = re.findall(r'https://play-lh\.googleusercontent\.com/[A-Za-z0-9_-]+', html)

screenshots = list(set(shots))
print(f"Found {len(screenshots)} screenshot candidates")

count = 1
for ss in screenshots:
    if count > 6: break
    try:
        hi_res_url = ss + "=w1080-h1920-rw"
        req_img = urllib.request.Request(hi_res_url, headers=headers)
        with urllib.request.urlopen(req_img, context=ctx, timeout=10) as img_res:
            content = img_res.read()
            if len(content) > 20000:
                filename = f"mytelkomsel_latest_gs_{count}.jpg"
                path = os.path.join(out_dir, filename)
                with open(path, 'wb') as f:
                    f.write(content)
                print(f"Saved {filename}")
                count += 1
            time.sleep(0.5)
    except Exception as e:
        print(f"Failed {ss}: {e}")
