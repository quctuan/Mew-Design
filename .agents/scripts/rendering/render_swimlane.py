
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

SWIMLANE_CODE = """
flowchart TD
    subgraph KH [KHÁCH HÀNG]
        direction TB
        S1([1. Thực hiện chuẩn hóa TTTB thành công])
        S4_KH[Nhận SMS thông báo Đăng ký V+]
        S8_KH[Nhận Push Noti cộng điểm]
        S9_KH[Nhận SMS cộng điểm]
    end

    subgraph APP [APP MY VNPT]
        direction TB
        S2[2. Hiển thị thông báo CTKM & Gửi yêu cầu cộng điểm]
        S8[8. Thông báo Noti cộng điểm thành công]
    end

    subgraph LTY [LOYALTY V+]
        direction TB
        S3{3. Kiểm tra trạng thái Hội viên}
        S4[4. Đăng ký hội viên tự động & Gửi SMS]
        S5[5. Thực hiện cộng +3,000 điểm]
        S6[6. Trả kết quả cộng điểm thành công]
        S9{9. Kiểm tra khung giờ gửi SMS}
    end

    subgraph SYS [HỆ THỐNG]
        direction TB
        S3_DB[(Hồ sơ Hội viên)]
        S5_DB[(Ví điểm Loyalty)]
    end

    %% Luồng tương tác
    S1 --> S2
    S2 --> S3
    S3 -- "Chưa có TK" --> S4
    S4 -.-> S4_KH
    S3 -- "Đã có TK" --> S5
    S4 --> S5
    S5 --> S6
    S6 --> S8
    S8 --> S8_KH
    S5 --> S9
    S9 -- "07h-22h (Gửi ngay)" --> S9_KH
    S9 -- "22h-07h (Hẹn sáng sau)" --> S9_KH

    %% Styles
    style KH fill:#f9f9f9,stroke:#333
    style APP fill:#e1f5fe,stroke:#01579b
    style LTY fill:#fff3e0,stroke:#e65100
    style SYS fill:#f1f8e9,stroke:#33691e
"""

def generate_kroki_image(code, output_file):
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
    path = 'c:/Users/caida/gds-myvnpt-wiki/Swimlane_User_Flow.png'
    if generate_kroki_image(SWIMLANE_CODE, path):
        link = upload_to_drive(path, 'Swimlane_User_Flow_C06.png')
        print(f"SUCCESS: {link}")
    else:
        print("FAILED")
