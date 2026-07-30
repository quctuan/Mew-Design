import os
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaInMemoryUpload

# Scopes needed for Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/documents']

def get_creds():
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_full.json'
    if not os.path.exists(token_path):
        token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token.json'
        
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'c:/Users/caida/gds-myvnpt-wiki/wiki/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('c:/Users/caida/gds-myvnpt-wiki/wiki/token_full.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def export_md_to_doc(md_path, doc_name):
    creds = get_creds()
    service = build('drive', 'v3', credentials=creds)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    file_metadata = {
        'name': doc_name,
        'mimeType': 'application/vnd.google-apps.document'
    }
    
    media = MediaInMemoryUpload(content.encode('utf-8'), mimetype='text/markdown')
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    return file.get('webViewLink')

if __name__ == "__main__":
    md_file = 'c:/Users/caida/gds-myvnpt-wiki/wiki/docs/huong-dan-pipeline-event-tracking.md'
    title = 'Huong_dan_Pipeline_Event_Tracking_GDS_Standard_2026'
    try:
        link = export_md_to_doc(md_file, title)
        print(f"EXPORT_SUCCESS: {link}")
    except Exception as e:
        print(f"ERROR: {str(e)}")
