import os
import sys
import json
import base64
import requests
import datetime
import urllib.parse
from getpass import getpass

# Handle Windows terminal encoding for Vietnamese characters
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# JIRA CONFIGURATION
JIRA_BASE_URL = 'https://cntt.vnpt.vn'
JIRA_TOKEN = os.getenv('JIRA_TOKEN', '')

# TELEGRAM CONFIGURATION
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
GROUP_CHAT_ID = '-4580999681'

# GOOGLE SHEETS APP SCRIPT URL (task manager URL)
GS_APP_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzFKPRwFvBVZGnpSkkz6km0NKaPMiwsg_kXCtcqeEL_QbBE9JyuQOk-gl3SnZQ6-RQj/exec'

# RULES & ASSIGNEES
VALID_ASSIGNEES = ['An Vũ Nhật Minh', 'Hồ Phạm Quỳnh Mai', 'Nguyễn Việt Hà']
EXCLUDE_STATUSES = ['Closed', 'Done', 'Resolved']

def fetch_jira_tasks():
    print("Mở kết nối tới Jira API...")
    
    jql = 'assignee in ("An Vũ Nhật Minh", "Hồ Phạm Quỳnh Mai", "Nguyễn Việt Hà") AND status not in (Closed, Done, Resolved) ORDER BY duedate DESC'
    url = f"{JIRA_BASE_URL}/rest/api/2/search?jql={urllib.parse.quote(jql)}&maxResults=100&fields=summary,issuetype,assignee,status,created,description,duedate"
    
    headers = {
        "Authorization": f"Bearer {JIRA_TOKEN}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Đã tải thành công {len(data.get('issues', []))} tasks hợp lệ từ Jira.")
        return data.get('issues', [])
    except Exception as e:
        print(f"❌ Lỗi truy xuất Jira API: {e}")
        if hasattr(e, 'response') and e.response is not None:
             print(e.response.text)
        sys.exit(1)

def classify_task(issue):
    # Rule 1: Issue Type (PYC or Support)
    issue_type_name = issue['fields'].get('issuetype', {}).get('name', '')
    summary = issue['fields'].get('summary', '')
    
    # PYC default if it matches CR_937 or just call it PYC if not SR
    danh_muc = 'Support' if 'SR_937' in issue_type_name or 'SR_937' in summary else 'PYC'
    
    description = issue['fields'].get('description', '') or ''
    full_text = summary + " " + description
    
    # Rule 2: Phân loại Nghiệp vụ
    phan_loai = 'Khác (Others)'
    
    # Check Di động
    if any(k.lower() in full_text.lower() for k in ['Di động', 'VinaPhone', 'VNP', 'SIM', 'eSIM', 'Cước di động', 'Gói cước VNP', '4G', '5G', 'Mạng di động']):
        phan_loai = 'Di động'
    # Check Băng rộng cố định
    elif any(k.lower() in full_text.lower() for k in ['Cố định', 'Băng rộng', 'Fiber', 'FTTH', 'Internet', 'Wifi', 'MyTV', 'Cáp quang', 'Đường truyền cố định']):
        phan_loai = 'Băng rộng cố định'
    # Check Cổng thanh toán
    elif any(k.lower() in full_text.lower() for k in ['Thanh toán', 'VNPT Money', 'VNPT Pay', 'Mobile Money', 'VNPAY', 'Nạp thẻ', 'Payment', 'Cổng thanh toán', 'Đối soát']):
        phan_loai = 'Cổng thanh toán / Thanh toán'
        
    return danh_muc, phan_loai

def generate_reports(tasks):
    pyc_tasks = []
    support_tasks = []
    
    for task in tasks:
        danh_muc, phan_loai = classify_task(task)
        fields = task['fields']
        
        task_info = {
            'id': task['key'],
            'summary': fields.get('summary', ''),
            'assignee': fields.get('assignee', {}).get('displayName', 'Unassigned') if fields.get('assignee') else 'Unassigned',
            'status': fields.get('status', {}).get('name', ''),
            'created': fields.get('created', '')[:10],
            'duedate': fields.get('duedate', '') or 'Chưa set',
            'link': f"{JIRA_BASE_URL}/browse/{task['key']}",
            'phan_loai': phan_loai,
            'danh_muc': danh_muc
        }
        
        if danh_muc == 'PYC':
            pyc_tasks.append(task_info)
        else:
            support_tasks.append(task_info)
            
    # Build Text Report using HTML to avoid Telegram Markdown parsing crashes on special Jira chars
    now = datetime.datetime.now().strftime('%d/%m/%Y')
    
    def render_text(title, list_tasks):
        if not list_tasks:
            return f"🟢 <b>{title} ({now})</b>\n\nKhông có task nào đang mở."
            
        txt = f"🔥 <b>{title} ({now})</b>\nTổng cộng: {len(list_tasks)} tasks\n\n"
        
        # Group by Assignee
        by_assignee = {}
        for t in list_tasks:
            if t['assignee'] not in by_assignee:
                by_assignee[t['assignee']] = []
            by_assignee[t['assignee']].append(t)
            
        for assignee, t_list in by_assignee.items():
            txt += f"👤 <b>{assignee}</b> ({len(t_list)})\n"
            for t in t_list:
                safe_summary = t['summary'].replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;')
                txt += f"  🔹 <b>[{t['id']}]</b> {safe_summary}\n"
                txt += f"      🏷 Loại: <i>{t['phan_loai']}</i> | ⏳ Due: {t['duedate']}\n"
                txt += f"      🔗 <a href='{t['link']}'>Nguồn Jira</a>\n"
            txt += "\n"
            
        return txt

    pyc_msg = render_text("BÁO CÁO CÔNG VIỆC PYC", pyc_tasks)
    support_msg = render_text("BÁO CÁO CÔNG VIỆC SUPPORT", support_tasks)
    
    return pyc_msg, support_msg, pyc_tasks + support_tasks

def send_telegram(message):
    print(f"Pushing message to Telegram ({len(message)} chars)...")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    lines = message.split('\n')
    chunks = []
    current_chunk = ""
    for line in lines:
        if len(current_chunk) + len(line) + 1 > 4000:
            chunks.append(current_chunk)
            current_chunk = line + "\n"
        else:
            current_chunk += line + "\n"
    if current_chunk:
        chunks.append(current_chunk)
        
    for i, str_chunk in enumerate(chunks):
        payload = {
            "chat_id": GROUP_CHAT_ID,
            "text": str_chunk,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        try:
            r = requests.post(url, json=payload)
            r.raise_for_status()
            print(f"✅ Telegram O.K (Part {i+1}/{len(chunks)})")
        except Exception as e:
            print(f"❌ Lỗi gửi Telegram Part {i+1}: {e}")
            if hasattr(e, 'response') and getattr(e, 'response') is not None:
                print(e.response.text)

def sync_to_google_sheets(tasks):
    print("Ghi nhận dữ liệu vào Google Sheets (Tab Phát sinh)...")
    
    print("  Đang kiểm tra các task đã tồn tại...")
    existing_ids = set()
    try:
        r_get = requests.get(f"{GS_APP_SCRIPT_URL}?sheetName=PhatSinh", allow_redirects=True, timeout=15)
        r_get.raise_for_status()
        gs_data = r_get.json()
        for row in gs_data:
            if 'ID' in row:
                existing_ids.add(str(row['ID']).strip())
        print(f"  Đã tìm thấy {len(existing_ids)} tasks hiện có trên Sheet.")
    except Exception as e:
        print(f"❌ Lỗi khi tải dữ liệu cũ từ Sheets: {e}")
        
    for i, t in enumerate(tasks):
        # We simulate writing an "add" or "update" event to Apps Script.
        
        # Parse Dates
        created_dt = t['created']
        try:
           created_dt = datetime.datetime.strptime(t['created'], "%Y-%m-%d").strftime("%d/%m/%Y")
        except:
           pass
           
        due_dt = t['duedate']
        try:
           due_dt = datetime.datetime.strptime(t['duedate'], "%Y-%m-%d").strftime("%d/%m/%Y")
        except:
           pass
        
        # Upsert determination pattern -> Changed to Add-only as requested
        if str(t['id']).strip() in existing_ids:
            print(f"  [{i+1}/{len(tasks)}] Task {t['id']} đã tồn tại. Bỏ qua (chỉ import task mới).")
            continue
            
        action = "add"
        
        payload = {
            "sheetName": "PhatSinh",
            "action": action,
            "task": {
                "ID": t['id'],
                "Danh muc": t['danh_muc'],
                "Phan loai": t['phan_loai'],
                "Ten dau viec": t['summary'],
                "Jira": t['link'],
                "Ngay tiep nhan": created_dt,
                "Ngay hoan thanh": due_dt if due_dt != 'Chưa set' else '',
                "Trang thai": "Pending"
            }
        }
        
        try:
            print(f"  [{i+1}/{len(tasks)}] Đang {action} {t['id']}...")
            r = requests.post(GS_APP_SCRIPT_URL, json=payload, allow_redirects=False, timeout=15)
            r.raise_for_status()
        except Exception as e:
            print(f"❌ Lỗi thao tác Google Sheet cho task {t['id']}: {e}")
            if hasattr(e, 'response') and getattr(e, 'response') is not None:
                print(e.response.text)
            
    print(f"✅ Đã PUSH hoàn tất sang Sheets.")

if __name__ == '__main__':
    # 1. Khởi chạy Workflow Kéo dữ liệu Jira
    tasks = fetch_jira_tasks()
    
    # 2. Phân tích Dữ liệu và Khai thác Báo cáo
    pyc_msg, support_msg, all_parsed = generate_reports(tasks)
    
    # 3. Ghi nhận dữ liệu Google Sheets
    sync_to_google_sheets(all_parsed)
    
    # 4. Gửi Auto-Split Telegram
    send_telegram(pyc_msg)
    send_telegram(support_msg)
    
    print("\n🎉 Hoàn thành Master Workflow!")
