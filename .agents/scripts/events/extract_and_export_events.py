
import os.path
import json
import re
import csv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes needed
READ_DOC_SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
WRITE_DRIVE_SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_creds(token_path, scopes):
    creds_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/credentials.json'
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return creds

def fetch_drive_doc(doc_id):
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token.json'
    creds = get_creds(token_path, READ_DOC_SCOPES)
    service = build('docs', 'v1', credentials=creds)
    document = service.documents().get(documentId=doc_id).execute()
    
    content = ""
    for element in document.get('body').get('content'):
        if 'paragraph' in element:
            for run in element.get('paragraph').get('elements'):
                content += run.get('textRun', {}).get('content', '')
        elif 'table' in element:
            for row in element.get('table').get('tableRows'):
                row_cells = []
                for cell in row.get('tableCells'):
                    cell_text = ""
                    for cell_element in cell.get('content'):
                        if 'paragraph' in cell_element:
                            for run in cell_element.get('paragraph').get('elements'):
                                cell_text += run.get('textRun', {}).get('content', '').strip()
                    row_cells.append(cell_text)
                content += " | " + " | ".join(row_cells) + " | \n"
    return content

def extract_event_table(content):
    # Regex to find the Event Tracking table in Section 5
    # We look for the table header first
    match = re.search(r"## 5\. Đặc tả Event Tracking.*?(\n\|.*\|(?:\n\|.*\|)+)", content, re.DOTALL | re.IGNORECASE)
    if not match:
        return []
    
    table_text = match.group(1).strip()
    lines = table_text.split('\n')
    
    events = []
    for i, line in enumerate(lines):
        if i < 2: continue # Skip header and separator
        cols = [c.strip() for c in line.split('|') if c.strip()]
        if len(cols) >= 5: # Ensure we have minimum columns
            events.append(cols)
    return events

def upload_to_drive(csv_path, filename):
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_drive.json'
    creds = get_creds(token_path, WRITE_DRIVE_SCOPES)
    service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {
        'name': f'Event_Tracking_{filename}',
        'mimeType': 'application/vnd.google-apps.spreadsheet' # Auto-convert to Google Sheets
    }
    media = MediaFileUpload(csv_path, mimetype='text/csv')
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    return file.get('webViewLink')

def main(input_content, output_name):
    # Determine input source
    if input_content.startswith("1") and len(input_content) > 30: # Likely a Doc ID
        print(f"Fetching from Google Drive ID: {input_content}...")
        text = fetch_drive_doc(input_content)
    else:
        # Local file path or raw content
        if os.path.exists(input_content):
            with open(input_content, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            text = input_content

    events = extract_event_table(text)
    if not events:
        print("Error: Could not find Event Tracking table in URD.")
        return

    # Write to local CSV
    csv_filename = 'temp_events.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Luồng', 'Tên màn hình', 'ID', 'Trigger', 'Event Name', 'Param Name', 'Operator', 'Param Value'])
        writer.writerows(events)
    
    print(f"Extracted {len(events)} events. Uploading to Drive...")
    link = upload_to_drive(csv_filename, output_name)
    print(f"Success! Your Event Tracking Sheet: {link}")
    
    # Cleanup
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python extract_and_export_events.py <URD_FILE_OR_ID> <OUTPUT_NAME>")
    else:
        main(sys.argv[1], sys.argv[2])
