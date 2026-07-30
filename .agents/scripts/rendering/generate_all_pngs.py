
import os
import base64
import requests
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Latest Diagrams
SEQUENCE_CODE = """
sequenceDiagram
    autonumber
    actor KH as Khách hàng
    participant APP as MyVNPT
    participant LTY as Loyalty (V+)
    participant SYS as Hệ thống
    participant SMS as SMS/Noti

    KH->>APP: 1. Thực hiện Chuẩn hóa TTTB thành công
    
    Note over APP, LTY: Điểm chạm 1: Màn hình cập nhật TTTB Thành công
    APP->>LTY: 2. Gửi yêu cầu cộng điểm & Hiển thị thông báo CTKM
    
    LTY->>SYS: 3. Kiểm tra trạng thái Hội viên
    
    opt Nếu chưa có TK
        LTY->>KH: 4. Đăng ký hội viên tự động & Gửi SMS thông báo
    end
    
    LTY->>SYS: 5. Thực hiện cộng +3,000 điểm vào TK
    
    LTY->>APP: 6. Trả kết quả cộng điểm thành công
    
    rect rgb(240, 240, 240)
    Note over LTY, SMS: Batch Job: Đảm bảo không làm phiền KH ban đêm
    LTY->>SMS: 8. Kiểm tra khung giờ (Gửi ngay hoặc Hẹn sáng sau)
    end
"""

USER_FLOW_CODE = """
flowchart TD
    Start([Khách hàng: Chuẩn hóa TTTB thành công]) --> Step2[App MyVNPT: Thông báo CTKM & Gửi lệnh cộng điểm]
    
    subgraph "Điểm chạm 1: Màn hình Thành công"
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

def generate_mermaid_image(code, output_file):
    # Using the raw code base64 encoding which is more reliable for simple needs
    graph_base64 = base64.b64encode(code.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/img/{graph_base64}"
    
    print(f"Downloading image from: {url}")
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"Image saved to {output_file}")
            return True
    except Exception as e:
        print(f"Request failed: {e}")
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
    results = {}
    
    # Sequence Diagram
    seq_path = 'c:/Users/caida/gds-myvnpt-wiki/Final_Sequence_Diagram.png'
    if generate_mermaid_image(SEQUENCE_CODE, seq_path):
        results['Sequence Diagram'] = upload_to_drive(seq_path, 'Final_Sequence_Diagram.png')
    
    # User Flow
    flow_path = 'c:/Users/caida/gds-myvnpt-wiki/Final_User_Flow.png'
    if generate_mermaid_image(USER_FLOW_CODE, flow_path):
        results['User Flow'] = upload_to_drive(flow_path, 'Final_User_Flow.png')
    
    print(json.dumps(results, indent=2))
