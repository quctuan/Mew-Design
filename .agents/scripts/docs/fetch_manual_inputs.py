
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def get_doc_content(service, doc_id):
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

def main():
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
    
    docs = {
        "URD": "1IvzaYYFGyCgNdYli8CERBsAiAwn_ilv3Mprov2oGJaw",
        "SRS_APP": "13eGXSqBbLW-a0lelWUVPX193CUDaLLdU7na_IZIhG8E",
        "SRS_CMS": "1q4-kXtHFngBm0KhDZTvULdlWMFpKDUu4"
    }
    
    results = {}
    for name, doc_id in docs.items():
        print(f"Fetching {name}...")
        results[name] = get_doc_content(service, doc_id)
        
    with open('c:/Users/caida/gds-myvnpt-wiki/manual_inputs_data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("All docs fetched successfully.")

if __name__ == "__main__":
    main()
