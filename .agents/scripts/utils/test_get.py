import requests

url = 'https://script.google.com/macros/s/AKfycbzFKPRwFvBVZGnpSkkz6km0NKaPMiwsg_kXCtcqeEL_QbBE9JyuQOk-gl3SnZQ6-RQj/exec'
try:
    r = requests.get(f"{url}?sheetName=PhatSinh", allow_redirects=True, timeout=15)
    print(r.status_code)
    data = r.json()
    print(len(data), "rows")
    if len(data) > 0:
        print(data[0])
except Exception as e:
    print(e)
