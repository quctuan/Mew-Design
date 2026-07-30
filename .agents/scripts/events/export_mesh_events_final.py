
import os.path
import csv
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes needed
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

def upload_to_drive(csv_path, filename):
    token_path = 'c:/Users/caida/gds-myvnpt-wiki/wiki/token_drive.json'
    creds = get_creds(token_path, WRITE_DRIVE_SCOPES)
    service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {
        'name': f'Event_Tracking_{filename}',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(csv_path, mimetype='text/csv')
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
    return file.get('webViewLink')

def main():
    # Data to be written (following the user's requested format)
    # Each list represents a row: [Luồng, Tên màn hình, ID, Trigger, Event name, Param name, Param operator, Param value]
    data = [
        ['Bán Mesh/Cam', 'VNPT Shop', 'MESH0', 'Click "Thiết bị mạng"', 'service_block_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'vnpt_shop_main'],
        ['', '', '', '', '', 'componentName', "'=", 'category_internet_tab'],
        ['', '', '', '', '', 'service', "'=", 'thiet_bi_mang'],
        ['Bán Mesh/Cam', 'Device List', 'MESH1', 'Chọn thiết bị xem chi tiết', 'service_block_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'mesh_device_list'],
        ['', '', '', '', '', 'componentName', "'=", 'device_item_card'],
        ['', '', '', '', '', 'deviceId', 'IN SET', '<mã_thiết_bị>'],
        ['', '', '', '', '', 'deviceName', 'IN SET', '<tên_thiết_bị>'],
        ['Bán Mesh/Cam', 'Device Detail', 'MESH2', 'Chọn hình thức Thuê/Mua', 'service_button_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'device_detail'],
        ['', '', '', '', '', 'buttonName', "'=", 'select_purchase_type'],
        ['', '', '', '', '', 'type', "'=", 'thue / mua'],
        ['Bán Mesh/Cam', 'Device Detail', 'MESH3', 'Nhấn "Tiếp tục"', 'service_button_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'device_detail'],
        ['', '', '', '', '', 'buttonName', "'=", 'continue_to_order'],
        ['', '', '', '', '', 'quantity', 'IN SET', '<số_lượng_chọn>'],
        ['Bán Mesh/Cam', 'Order Confirm', 'MESH4', 'Thay đổi thuê bao quản lý', 'service_button_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'order_confirm'],
        ['', '', '', '', '', 'buttonName', "'=", 'change_account'],
        ['', '', '', '', '', 'accountType', "'=", 'chinh_chu / khac'],
        ['Bán Mesh/Cam', 'Order Confirm', 'MESH5', 'Chọn gói cước Internet', 'service_block_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'order_confirm'],
        ['', '', '', '', '', 'componentName', "'=", 'internet_package_list'],
        ['', '', '', '', '', 'packageCode', 'IN SET', '<mã_gói_cước>'],
        ['Bán Mesh/Cam', 'Order Confirm', 'MESH6', 'Nhấn "Đăng ký ngay"', 'service_button_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'order_confirm'],
        ['', '', '', '', '', 'buttonName', "'=", 'confirm_register'],
        ['', '', '', '', '', 'totalAmount', 'IN SET', '<tổng_tiền_đơn_hàng>'],
        ['Bán Mesh/Cam', 'Order Success', 'MESH7', 'Màn đăng ký thành công', 'service_screen_viewed', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'order_success_result'],
        ['', '', '', '', '', 'transactionId', 'IN SET', '<mã_đơn_hàng_onebss>'],
        ['Bán Mesh/Cam', 'Order Tracking', 'MESH8', 'Nhấn "Tạo đơn mới" (hủy)', 'service_button_clicked', 'partnerName', "'=", 'myvnpt'],
        ['', '', '', '', '', 'screenName', "'=", 'order_tracking'],
        ['', '', '', '', '', 'buttonName', "'=", 'create_new_order'],
        ['', '', '', '', '', 'oldOrderId', 'IN SET', '<mã_đơn_cũ>']
    ]

    csv_filename = 'final_event_tracking.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Luồng', 'Tên màn hình', 'ID', 'Trigger', 'Event name', 'Param name', 'Param operator', 'Param value'])
        writer.writerows(data)
    
    print(f"Uploading to Drive...")
    link = upload_to_drive(csv_filename, 'Ban_Mesh_Cam_GDS_2026')
    print(f"Success! Your Event Tracking Sheet: {link}")
    
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

if __name__ == "__main__":
    main()
