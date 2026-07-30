
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes required: Drive to upload/create, and we'll convert to Google Doc
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    creds = None
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_drive.json'
    creds_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/credentials.json'
    md_file_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/docs/mau-dau-definition.md'

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
            'name': 'Tài liệu Định nghĩa MAU DAU 2026',
            'mimeType': 'application/vnd.google-apps.document' # Convert to Google Doc
        }
        
        # We upload the markdown file as a plain text file, 
        # but tell Drive to convert it to a Google Doc
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
