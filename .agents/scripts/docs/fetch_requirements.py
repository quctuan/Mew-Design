
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json

# Scopes to read Docs, Sheets and Drive metadata
SCOPES = [
    'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]

def get_credentials():
    creds = None
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_full.json'
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
    return creds

def read_doc(service, doc_id):
    document = service.documents().get(documentId=doc_id).execute()
    content = document.get('body').get('content')
    text = ""
    for element in content:
        if 'paragraph' in element:
            parts = element.get('paragraph').get('elements')
            for part in parts:
                if 'textRun' in part:
                    text += part.get('textRun').get('content')
    return text

def read_sheet(service, sheet_id):
    spreadsheet = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    sheets = spreadsheet.get('sheets', [])
    data = {}
    for sheet in sheets:
        title = sheet.get('properties').get('title')
        result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=title).execute()
        data[title] = result.get('values', [])
    return data

def main():
    creds = get_credentials()
    
    docs_service = build('docs', 'v1', credentials=creds)
    sheets_service = build('sheets', 'v4', credentials=creds)

    doc_id = '1S-8cs9yPrLaA7YZRiWfoUegICJ5oBmiCSuQIos3ZN-c'
    sheet_ref_id = '1ShqIbKu4IFnFj2SdzWg7gOSC2chVNrbSXQ73LAXMg0U'
    sheet_target_id = '1_-XPLrxyRolVOg8WWELWDRynncIxq7-21BC1VPsMWOk'

    print("--- CONTENT OF REFERENCE DOC ---")
    print(read_doc(docs_service, doc_id))
    
    print("\n--- CONTENT OF REFERENCE SHEET ---")
    ref_data = read_sheet(sheets_service, sheet_ref_id)
    for title, rows in ref_data.items():
        print(f"Sheet: {title}")
        for row in rows:
            print(row)

    print("\n--- CONTENT OF TARGET SHEET ---")
    target_data = read_sheet(sheets_service, sheet_target_id)
    for title, rows in target_data.items():
        print(f"Sheet: {title}")
        for row in rows:
            print(row)

if __name__ == '__main__':
    main()
