
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def get_doc_content(doc_id):
    creds = None
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token.json'
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

    service = build('docs', 'v1', credentials=creds)
    document = service.documents().get(documentId=doc_id).execute()
    
    text = ""
    for element in document.get('body').get('content'):
        if 'paragraph' in element:
            for run in element.get('paragraph').get('elements'):
                text += run.get('textRun', {}).get('content', '')
        elif 'table' in element:
            for row in element.get('table').get('tableRows'):
                for cell in row.get('tableCells'):
                    for cell_element in cell.get('content'):
                        if 'paragraph' in cell_element:
                            for run in cell_element.get('paragraph').get('elements'):
                                text += run.get('textRun', {}).get('content', '')
                    text += " | "
                text += "\n"
    return text

if __name__ == "__main__":
    doc_id = "1PDFAUTvjCd_WtcerBYRt-zmLtKhYoEnhsNYddoWxtGY"
    content = get_doc_content(doc_id)
    with open('c:/Users/caida/gds-myvnpt-wiki/urd_assessment_content.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Content fetched successfully.")
