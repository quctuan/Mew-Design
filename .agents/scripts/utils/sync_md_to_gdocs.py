import os
import sys
import re
import markdown
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io

# Cấu hình ID thư mục đích trên Google Drive (Để trống '' nếu muốn lưu ở My Drive/Thư mục gốc)
# Cách lấy ID: Mở thư mục đó trên Drive, copy đoạn mã phía sau /folders/ trên thanh địa chỉ.
# Ví dụ: URL là https://drive.google.com/drive/folders/1xV_abc123xyz -> ID là '1xV_abc123xyz'
TARGET_FOLDER_ID = '1RQpG-ydUPOrP19qCcvs4glOTXqiAQ3vc'

# Cấp quyền đọc ghi file trên Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service(creds_path, token_path):
    creds = None
    # Load token đã lưu nếu có (để các lần sau không cần login lại)
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # Nếu chưa có token hoặc token hết hạn thì yêu cầu người dùng login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            # Mở trình duyệt để người dùng đăng nhập và ủy quyền
            creds = flow.run_local_server(port=0)
        # Lưu token lại cho những lần chạy sau
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            
    return build('drive', 'v3', credentials=creds)

def sync_document(filepath):
    # Lấy đường dẫn chính xác của file credentials
    script_dir = os.path.dirname(os.path.abspath(__file__))
    creds_path = os.path.join(script_dir, 'credentials.json')
    token_path = os.path.join(script_dir, 'token.json')
    
    if not os.path.exists(creds_path):
        print(f"Lỗi: Không tìm thấy file {creds_path}.")
        print("Vui lòng tải file credentials.json từ Google Cloud và đặt vào thư mục .agents/scripts/")
        sys.exit(1)

    print(f"Đọc file Markdown: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tìm xem file này đã có gdoc_id (được đồng bộ trước đó) chưa
    match = re.search(r'<!--\s*gdoc_id:\s*([a-zA-Z0-9_-]+)\s*-->', content)
    gdoc_id = match.group(1) if match else None

    # Chuyển đổi Markdown sang HTML để Google Docs giữ được định dạng (In đậm, Table, H1, H2...)
    html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    html_content = f"<html><body>{html_content}</body></html>"
    
    # Bọc nội dung HTML vào Media chuẩn bị đẩy lên Drive
    media = MediaIoBaseUpload(io.BytesIO(html_content.encode('utf-8')), mimetype='text/html', resumable=True)

    # Khởi tạo kết nối tới Drive
    try:
        service = get_drive_service(creds_path, token_path)
    except Exception as e:
        print(f"Lỗi xác thực với Google Drive: {e}")
        sys.exit(1)

    filename = os.path.basename(filepath)
    doc_title = filename.replace('.md', '')

    if gdoc_id:
        print(f"Đang cập nhật nội dung cho Google Doc hiện tại (ID: {gdoc_id})...")
        try:
            # Ghi đè file cũ trên Drive
            service.files().update(
                fileId=gdoc_id,
                media_body=media
            ).execute()
            
            # Cập nhật lại tên file (trong trường hợp user có đổi tên file md)
            service.files().update(
                fileId=gdoc_id,
                body={'name': doc_title}
            ).execute()
            
            print("✅ Cập nhật thành công!")
            print(f"🔗 Link Google Docs: https://docs.google.com/document/d/{gdoc_id}/edit")
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật file: {e}")
            print("Nếu file trên Drive đã bị xóa, hãy xóa dòng <!-- gdoc_id: ... --> ở cuối file markdown và chạy lại.")
    else:
        print("Đang tạo một file Google Doc hoàn toàn mới...")
        file_metadata = {
            'name': doc_title,
            'mimeType': 'application/vnd.google-apps.document'
        }
        
        # Nếu có cấu hình thư mục đích, thêm nó vào metadata
        if TARGET_FOLDER_ID:
            file_metadata['parents'] = [TARGET_FOLDER_ID]
            
        try:
            # Tạo file mới và yêu cầu Drive tự động convert HTML sang định dạng Google Docs
            file = service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            
            new_id = file.get('id')
            doc_link = f"https://docs.google.com/document/d/{new_id}/edit"
            print("✅ Tạo mới Google Docs thành công!")
            print(f"🔗 Link Google Docs: {doc_link}")
            
            # Tự động chèn link vào trong file .md
            # Tìm dòng "- **Link Google Docs:**..." để thay thế, nếu không có thì chèn ngay dưới thẻ Heading 1 đầu tiên.
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            replaced = False
            for i in range(len(lines)):
                if lines[i].startswith("- **Link Google Docs:**"):
                    lines[i] = f"- **Link Google Docs:** [{doc_title}]({doc_link})\n"
                    replaced = True
                    break
            
            if not replaced:
                # Nếu không tìm thấy dòng placeholder, chèn ngay trên dòng đầu tiên hoặc dưới Heading 1
                for i in range(len(lines)):
                    if lines[i].startswith("# "):
                        lines.insert(i + 1, f"- **Link Google Docs:** [{doc_title}]({doc_link})\n")
                        replaced = True
                        break
            
            if not replaced:
                # Nếu không có Heading 1, cứ chèn lên đầu
                lines.insert(0, f"- **Link Google Docs:** [{doc_title}]({doc_link})\n")
                
            # Cập nhật cả gdoc_id vào cuối file
            lines.append(f"\n\n<!-- gdoc_id: {new_id} -->\n")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
                
            print("Đã tự động chèn Link Google Docs trang MD và lưu dấu gdoc_id!")
        except Exception as e:
            print(f"❌ Lỗi khi tải file lên Google Drive: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python3 .agents/scripts/sync_md_to_gdocs.py <duong_dan_file_md>")
        sys.exit(1)
    
    md_file = sys.argv[1]
    if not os.path.exists(md_file):
        print(f"Lỗi: Không tìm thấy file {md_file} trên máy của bạn.")
        sys.exit(1)
        
    sync_document(md_file)
