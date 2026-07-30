
import os
import base64
import requests
import json
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
    
    CheckMember -- Chưa có TK --> Register[Loyalty: Đăng ký V+ tự động từ CCBS]
    Register --> SendSMS1[Gửi SMS thông báo đăng ký V+ thành công]
    SendSMS1 --> AddPoints
    
    CheckMember -- Đã có TK --> AddPoints[Loyalty: Cộng +3,000 điểm VinaPhone Plus]
    
    AddPoints --> Response[Loyalty: Trả kết quả thành công cho App]
    
    Response --> Touchpoint3[App MyVNPT: Hiển thị Màn hình Quà tặng Onboarding]
    Touchpoint3 --> ViewVouchers[Khách hàng: Xem +3k điểm & Đổi Voucher]
    
    AddPoints --> TimeCheck{Kiểm tra Giờ}
    TimeCheck -- Sau 22h - 7h sáng --> BatchJob[Lưu hàng đợi - Hẹn giờ 7h sáng]
    BatchJob --> SendNoti[Gửi Noti/SMS nhận điểm]
    
    TimeCheck -- Giờ hành chính --> SendNoti
    
    ViewVouchers --> Finish([Kết thúc trải nghiệm])
"""

def generate_mermaid_image(code, output_file):
    # Simplified encoding for mermaid.ink
    # Sometimes complex characters or quotes in labels cause 400/404 if not handled correctly
    # UTF-8 -> Base64 is usually okay, but let's try a clean version
    
    # Compress the code a bit (removal of extra spaces/newlines)
    clean_code = "\\n".join([line.strip() for line in code.split("\\n") if line.strip()])
    
    # Wrap in Mermaid JSON structure if needed, but mermaid.ink usually takes raw b64
    payload = {
        "code": code,
        "mermaid": {"theme": "default"}
    }
    # Encode the whole JSON object
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
        # Try raw code base64 as fallback
        raw_b64 = base64.urlsafe_b64encode(code.encode('utf-8')).decode('utf-8')
        url_fallback = f"https://mermaid.ink/img/{raw_b64}"
        print(f"Trying fallback URL: {url_fallback}")
        resp_fb = requests.get(url_fallback)
        if resp_fb.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(resp_fb.content)
            print("Fallback success!")
            return True
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
    file_metadata = {'name': 'User_Flow_C06_v2.png'}
    media = MediaFileUpload(file_path, mimetype='image/png')
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    print(f"Uploaded! View link: {file.get('webViewLink')}")

if __name__ == "__main__":
    img_file = 'c:/Users/caida/gds-myvnpt-wiki/user_flow_v2.png'
    if generate_mermaid_image(user_flow_code, img_file):
        upload_to_drive(img_file)
