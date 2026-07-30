import requests

url = 'https://script.google.com/macros/s/AKfycbzFKPRwFvBVZGnpSkkz6km0NKaPMiwsg_kXCtcqeEL_QbBE9JyuQOk-gl3SnZQ6-RQj/exec'
payload = {
    "sheetName": "PhatSinh",
    "action": "add",
    "task": {
        "ID": "TEST1234",
        "Danh muc": "PYC",
        "Phan loai": "Di động",
        "Ten dau viec": "Check Python Post",
        "Jira": "https://cntt.vnpt.vn",
        "Ngay tiep nhan": "08/03/2026",
        "Ngay hoan thanh": "08/03/2026",
        "Trang thai": "Pending"
    }
}
r = requests.post(url, json=payload, allow_redirects=True)
print(r.status_code)
print(r.text)
