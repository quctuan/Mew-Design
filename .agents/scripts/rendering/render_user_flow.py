
import os
import base64
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# User Flow Mermaid code
user_flow_code = """
flowchart TD
    Start([Khách hàng: Chuẩn hóa TTTB]) --> Success{Chuẩn hóa Thành công?}
    
    Success -- No --> End([Kết thúc / Thử lại])
    Success -- Yes --> Action1[App MyVNPT: Hiển thị Màn hình Thành công - Loading]
    
    Action1 --> CallAPI[Gửi yêu cầu cộng điểm tới Loyalty]
    
    CallAPI --> CheckMember{Kiểm tra Hội viên V+}
    
    CheckMember -- "Chưa có TK" --> Register[Loyalty: Đăng ký V+ tự động từ CCBS]
    Register --> SendSMS1[Gửi SMS thông báo đăng ký V+ thành công]
    SendSMS1 --> AddPoints
    
    CheckMember -- "Đã có TK" --> AddPoints[Loyalty: Cộng +3,000 điểm VinaPhone Plus]
    
    AddPoints --> Response[Loyalty: Trả kết quả thành công cho App]
    
    Response --> Touchpoint3[App MyVNPT: Hiển thị Màn hình Quà tặng Onboarding]
    Touchpoint3 --> ViewVouchers[Khách hàng: Xem +3k điểm & Đổi Voucher]
    
    AddPoints --> TimeCheck{Kiểm tra Giờ (Night mode?)}
    TimeCheck -- "Sau 22h - 7h sáng" --> BatchJob[Lưu hàng đợi - Hẹn giờ 7h sáng]
    BatchJob --> SendNoti[Gửi Noti/SMS nhận điểm]
    
    TimeCheck -- "Giờ hành chính" --> SendNoti
    
    ViewVouchers --> Finish([Kết thúc trải nghiệm])
"""

def generate_mermaid_image(code, output_file):
    # Encode code to base64 for mermaid.ink
    graph_base64 = base64.b64encode(code.encode('utf-8')).decode('utf-8')
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
    file_metadata = {'name': 'User_Flow_C06.png'}
    media = MediaFileUpload(file_path, mimetype='image/png')
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    print(f"Uploaded! View link: {file.get('webViewLink')}")

if __name__ == "__main__":
    img_file = 'c:/Users/caida/gds-myvnpt-wiki/user_flow.png'
    if generate_mermaid_image(user_flow_code, img_file):
        upload_to_drive(img_file)
