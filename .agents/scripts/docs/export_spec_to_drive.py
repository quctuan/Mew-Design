
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes needed: Drive file access
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    creds = None
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_drive.json'
    creds_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/credentials.json'
    md_file_path = 'c:/Users/caida/gds-myvnpt-wiki/knowledge base/specs/SPEC-001_Tang_diem_C06.md'

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

    try:
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': 'SPEC-001: Chương trình Tặng điểm VPlus Chuẩn hóa C06',
            'mimeType': 'application/vnd.google-apps.document'
        }
        
        media = MediaFileUpload(md_file_path, mimetype='text/markdown')
        
        file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id, webViewLink').execute()
        
        print(f'Success! File ID: {file.get("id")}')
        print(f'Web View Link: {file.get("webViewLink")}')

    except Exception as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()
