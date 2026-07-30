
import os.path
import csv
import re
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = [
    'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]

MASTER_FILE_ID = '10PDEoMns5mgP4_FWRUDQ2e9nUWaCNmtkKqnix3dA4ZA'

def get_creds():
    # Priority for token_drive.json as it has write access, but full token is better
    token_paths = [
        'c:/Users/caida/gds-myvnpt-wiki/wiki/token_full.json',
        'c:/Users/caida/gds-myvnpt-wiki/wiki/token_drive.json',
        'c:/Users/caida/gds-myvnpt-wiki/wiki/token.json'
    ]
    creds_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/credentials.json'
    creds = None
    
    selected_token = None
    for path in token_paths:
        if os.path.exists(path):
            selected_token = path
            break
            
    if selected_token:
        creds = Credentials.from_authorized_user_file(selected_token, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save back to token_full.json
        with open('c:/Users/caida/gds-myvnpt-wiki/wiki/token_full.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def fetch_urd_info(doc_id):
    creds = get_creds()
    doc_service = build('docs', 'v1', credentials=creds)
    document = doc_service.documents().get(documentId=doc_id).execute()
    title = document.get('title', 'Unknown_URD').replace('/', '_').replace(' ', '_')
    
    content = ""
    for element in document.get('body').get('content'):
        if 'paragraph' in element:
            for run in element.get('paragraph').get('elements'):
                content += run.get('textRun', {}).get('content', '')
        elif 'table' in element:
            for row in element.get('table').get('tableRows'):
                cells = []
                for cell in row.get('tableCells'):
                    cell_text = ""
                    for cell_element in cell.get('content'):
                        if 'paragraph' in cell_element:
                            for run in cell_element.get('paragraph').get('elements'):
                                cell_text += run.get('textRun', {}).get('content', '').strip()
                    cells.append(cell_text)
                content += " | " + " | ".join(cells) + " | \n"
    return title, content

def extract_events(content):
    # Standard 8-column format extraction logic
    # We'll look for lines starting with | or rows containing Event name triggers
    # For now, let's assume we use the AI-generated refined table if URD section is empty
    # If the URD has a table in Section 5, we parse it.
    match = re.search(r"## 5\. Đặc tả Event Tracking.*?(\n\|.*\|(?:\n\|.*\|)+)", content, re.DOTALL | re.IGNORECASE)
    if not match: return []
    
    table_text = match.group(1).strip()
    lines = table_text.split('\n')
    events = []
    for i, line in enumerate(lines):
        if i < 2: continue # skip header/sep
        cols = [c.strip() for c in line.split('|') if c.strip()]
        if len(cols) >= 5: events.append(cols)
    return events

def create_new_file(data, title):
    creds = get_creds()
    drive_service = build('drive', 'v3', credentials=creds)
    
    csv_path = 'temp_export.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Luồng', 'Tên màn hình', 'ID', 'Trigger', 'Event name', 'Param name', 'Param operator', 'Param value'])
        writer.writerows(data)
        
    file_metadata = {
        'name': f'Event_Tracking_{title}',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(csv_path, mimetype='text/csv')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    os.remove(csv_path)
    return file.get('webViewLink')

def update_master_sheet(data, sheet_name):
    creds = get_creds()
    sheets_service = build('sheets', 'v4', credentials=creds)
    
    # 1. Check if sheet exists, if not add it
    spreadsheet = sheets_service.spreadsheets().get(spreadsheetId=MASTER_FILE_ID).execute()
    existing_sheets = [s.get('properties', {}).get('title') for s in spreadsheet.get('sheets', [])]
    
    if sheet_name not in existing_sheets:
        batch_update_request = {
            'requests': [{'addSheet': {'properties': {'title': sheet_name}}}]
        }
        sheets_service.spreadsheets().batchUpdate(spreadsheetId=MASTER_FILE_ID, body=batch_update_request).execute()
    
    # 2. Clear existing content in the sheet
    sheets_service.spreadsheets().values().clear(
        spreadsheetId=MASTER_FILE_ID, range=f"'{sheet_name}'!A1:Z1000").execute()
        
    # 3. Write new standardized data
    header = [['Luồng', 'Tên màn hình', 'ID', 'Trigger', 'Event name', 'Param name', 'Param operator', 'Param value']]
    full_data = header + data
    
    range_name = f"'{sheet_name}'!A1"
    body = {'values': full_data}
    sheets_service.spreadsheets().values().update(
        spreadsheetId=MASTER_FILE_ID, range=range_name,
        valueInputOption='USER_ENTERED', body=body).execute()
        
    return f"https://docs.google.com/spreadsheets/d/{MASTER_FILE_ID}/edit#gid=0"

def update_screen_dictionary(display_name, screen_name):
    creds = get_creds()
    sheets_service = build('sheets', 'v4', credentials=creds)
    sheet_name = 'Tên màn hình'
    
    # 1. Get existing data
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=MASTER_FILE_ID, range=f"'{sheet_name}'!A:B").execute()
    values = result.get('values', [])
    
    # 2. Check if already exists
    exists = False
    for row in values:
        if len(row) >= 2 and row[1] == screen_name:
            exists = True
            break
            
    if not exists:
        # Append new row
        new_row = [[display_name, screen_name]]
        sheets_service.spreadsheets().values().append(
            spreadsheetId=MASTER_FILE_ID, range=f"'{sheet_name}'!A:B",
            valueInputOption='USER_ENTERED', body={'values': new_row}).execute()
        print(f"Added '{screen_name}' to dictionary.")

def append_to_master(data, sheet_name):
    link = update_master_sheet(data, sheet_name)
    
    # Extract unique screens from data and update dictionary
    unique_screens = {}
    for row in data:
        if len(row) >= 2 and row[1]: # Screen Name column
            # We need a display name. For now, we'll try to find it or use a default.
            # In real workflow, Agent will pass this mapping.
            pass 
            
    return link

def main(mode, urd_input, data_file=None):
    print(f"Running in {mode} mode...")
    
    # In 'update' mode, urd_input is actually the sheet_name
    if mode == 'update':
        title = urd_input
    else:
        # Get Title
        if urd_input.startswith("1") and len(urd_input) > 20:
            title, content = fetch_urd_info(urd_input)
        else:
            title = "Manual_URD"
            content = urd_input

    # Use data from file if provided, otherwise try to extract from URD
    if data_file and os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            events = json.load(f)
    else:
        events = extract_events(content)
    
    if not events:
        print("Error: No event data found to export.")
        return

    if mode == 'standalone':
        link = create_new_file(events, title)
    elif mode == 'master':
        link = append_to_master(events, title)
    elif mode == 'update':
        link = update_master_sheet(events, title)
        
    print(f"Success! Link: {link}")

if __name__ == "__main__":
    import sys
    # Usage: python manage_event_sheets.py [standalone|master|update] [URD_ID|SHEET_NAME] [optional_data_json]
    if len(sys.argv) >= 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
