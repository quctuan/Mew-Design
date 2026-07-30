
import os
import base64
import requests
import json
import zlib
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

USER_FLOW_CODE = """
flowchart TD
    Start([Khách hàng: Chuẩn hóa TTTB thành công]) --> Step2[App MyVNPT: Thông báo CTKM & Gửi lệnh cộng điểm]
    
    subgraph "Màn hình Thành công"
    Step2
    end
    
    Step2 --> Step3{Loyalty: Kiểm tra Hội viên?}
    
    Step3 -- "Chưa có TK" --> Step4[Đăng ký V+ tự động & Gửi SMS]
    Step4 --> Step5[Loyalty: Thực hiện cộng +3,000 điểm]
    
    Step3 -- "Đã có TK" --> Step5
    
    Step5 --> Step6[Loyalty: Trả kết quả thành công cho App]
    
    Step5 --> Step8{Kiểm tra khung giờ?}
    
    Step8 -- "07h-22h" --> SendNow[Gửi SMS/Noti ngay]
    Step8 -- "22h-07h" --> BatchJob[Lưu hàng đợi - Hẹn 07h sáng]
    
    SendNow --> End([Kết thúc])
    BatchJob -.-> SendNow
"""

def generate_kroki_image(code, output_file):
    # Kroki uses zlib compression followed by base64 encoding
    compressed = zlib.compress(code.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
    url = f"https://kroki.io/mermaid/png/{encoded}"
    
    print(f"Downloading from Kroki: {url}")
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"Kroki failed with {response.status_code}")
    except Exception as e:
        print(f"Kroki error: {e}")
    return False

def upload_to_drive(file_path, drive_name):
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
    file_metadata = {'name': drive_name}
    media = MediaFileUpload(file_path, mimetype='image/png')
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    return file.get('webViewLink')

if __name__ == "__main__":
    path = 'c:/Users/caida/gds-myvnpt-wiki/User_Flow_Kroki.png'
    if generate_kroki_image(USER_FLOW_CODE, path):
        link = upload_to_drive(path, 'User_Flow_Final_PNG.png')
        print(f"SUCCESS: {link}")
    else:
        print("Kroki also failed")
