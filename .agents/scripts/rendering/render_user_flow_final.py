
import os
import base64
import requests
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# User Flow based on the table
mermaid_code = """
flowchart TD
    Start([Khách hàng: Chuẩn hóa TTTB thành công]) --> Step2[App MyVNPT: Hiển thị thông báo CTKM & Gửi yêu cầu cộng điểm]
    
    subgraph "Điểm chạm 1: Màn hình Thành công"
    Step2
    end
    
    Step2 --> Step3{Loyalty: Kiểm tra trạng thái Hội viên}
    
    Step3 -- "Chưa là Hội viên" --> Step4[Đăng ký hội viên tự động & Gửi SMS thông báo]
    Step4 --> Step5[Loyalty: Thực hiện cộng +3,000 điểm]
    
    Step3 -- "Đã là Hội viên" --> Step5
    
    Step5 --> Step6[Loyalty: Trả kết quả cộng điểm thành công cho App]
    
    Step5 --> Step8{Kiểm tra khung giờ Giao dịch}
    
    Step8 -- "Hành chính (07h-22h)" --> SendNow[Gửi SMS/Noti thông báo nhận điểm ngay]
    Step8 -- "Nghỉ đêm (22h-07h)" --> BatchJob[Lưu hàng đợi - Hẹn giờ 07h sáng gửi]
    
    SendNow --> End([Kết thúc luồng])
    BatchJob -.-> SendNow
"""

def generate_mermaid_image(code, output_file):
    payload = {
        "code": code,
        "mermaid": {"theme": "default"}
    }
    json_str = json.dumps(payload)
    graph_base64 = base64.urlsafe_b64encode(json_str.encode('utf-8')).decode('utf-8')
    
    url = f"https://mermaid.ink/img/{graph_base64}"
    
    print(f"Downloading image from: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"Image saved to {output_file}")
        return True
    else:
        print(f"Failed to generate image. Status code: {response.status_code}")
        return False

def upload_to_drive(file_path):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = None
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_drive.json'
    creds_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/credentials.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    file_metadata = {'name': 'User_Flow_C06_Final.png'}
    media = MediaFileUpload(file_path, mimetype='image/png')
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    print(f"Uploaded! View link: {file.get('webViewLink')}")

if __name__ == "__main__":
    img_file = 'c:/Users/caida/gds-myvnpt-wiki/user_flow_final.png'
    if generate_mermaid_image(mermaid_code, img_file):
        upload_to_drive(img_file)
