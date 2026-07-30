import sys
import os
import json
import traceback

try:
    from manage_event_sheets import update_master_sheet, update_screen_dictionary
except ImportError:
    print("Error importing manage_event_sheets")
    sys.exit(1)

def run_update():
    # Raw data definition
    raw_events = [
        {
            "luong": "Payment Hub", "screen": "payment_account_management", "id": "PAY_001", 
            "trigger": "Hiển thị màn hình Quản lý tài khoản (Có hoặc Không có nguồn tiền)", 
            "event": "display_payment_account_management", 
            "params": [("partnerName", "=", "myvnpt"), ("has_payment_source", "=", "true/false")]
        },
        {
            "luong": "Payment Hub", "screen": "payment_method_list", "id": "PAY_002", 
            "trigger": "Hiển thị màn hình Tất cả phương thức thanh toán", 
            "event": "display_payment_method_list", 
            "params": [("partnerName", "=", "myvnpt"), ("fromFeature", "=", "payment_account_management")]
        },
        {
            "luong": "Payment Hub", "screen": "payment_method_detail", "id": "PAY_003", 
            "trigger": "Hiển thị màn chi tiết phương thức thanh toán", 
            "event": "display_payment_method_detail", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(MM, Pay, CTT...)")]
        },
        {
            "luong": "Payment Hub", "screen": "payment_account_management", "id": "PAY_004", 
            "trigger": "Click thêm nguồn tiền/phương thức thanh toán", 
            "event": "click_add_payment_method", 
            "params": [("partnerName", "=", "myvnpt")]
        },
        {
            "luong": "Payment Hub", "screen": "payment_method_detail", "id": "PAY_005", 
            "trigger": "Click Hủy liên kết (xóa phương thức)", 
            "event": "click_unlink_payment_method", 
            "params": [("partnerName", "=", "myvnpt")]
        },
        {
            "luong": "Payment Hub", "screen": "payment_method_detail", "id": "PAY_006", 
            "trigger": "Bật/Tắt thiết lập thanh toán nhanh qua Ví/MM", 
            "event": "toggle_fast_payment", 
            "params": [("partnerName", "=", "myvnpt"), ("action", "=", "on/off")]
        },
        {
            "luong": "Payment Hub", "screen": "payment_method_list", "id": "PAY_007", 
            "trigger": "Chọn loại phương thức để bắt đầu liên kết", 
            "event": "click_select_method_to_link", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(The quoc te, The noi dia...)")]
        },
        {
            "luong": "Payment Hub", "screen": "", "id": "PAY_008", 
            "trigger": "Hệ thống ghi nhận bắt đầu gắn token qua CTT (Webview)", 
            "event": "submit_link_payment_method", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(CTT type)")]
        },
        {
            "luong": "Payment Hub", "screen": "", "id": "PAY_009", 
            "trigger": "Liên kết phương thức thành công/nhận token", 
            "event": "link_payment_method_success", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(CTT type)"), ("action_type", "=", "link_success")]
        },
        {
            "luong": "Payment Hub", "screen": "", "id": "PAY_010", 
            "trigger": "Liên kết phương thức thất bại", 
            "event": "link_payment_method_failed", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(CTT type)"), ("error_code", "=", "(mã lỗi)")]
        },
        {
            "luong": "Payment Hub", "screen": "", "id": "PAY_011", 
            "trigger": "Hủy liên kết phương thức thành công", 
            "event": "unlink_payment_method_success", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(CTT type)"), ("action_type", "=", "unlink_success")]
        },
        {
            "luong": "Payment Hub", "screen": "", "id": "PAY_012", 
            "trigger": "Hủy liên kết thẻ thất bại", 
            "event": "unlink_payment_method_failed", 
            "params": [("partnerName", "=", "myvnpt"), ("method_type", "=", "(CTT type)"), ("error_code", "=", "(mã lỗi)")]
        }
    ]

    events_expanded = []
    
    for ev in raw_events:
        params = ev['params']
        if not params:
            # If no params, just add one row
            events_expanded.append([ev['luong'], ev['screen'], ev['id'], ev['trigger'], ev['event'], "", "", ""])
            continue
            
        # First row contains all the event data + first param
        first_param = params[0]
        events_expanded.append([
            ev['luong'], ev['screen'], ev['id'], ev['trigger'], ev['event'],
            first_param[0], f"'{first_param[1]}", first_param[2]
        ])
        
        # Subsequent rows leave the first 5 columns blank
        for param in params[1:]:
            events_expanded.append([
                "", "", "", "", "",
                param[0], f"'{param[1]}", param[2]
            ])

    print("Adding sheet to Master File...")
    try:
        sheet_name = 'Payment_Hub_Phase1'
        link = update_master_sheet(events_expanded, sheet_name)
        print(f'\n=== DONE ===\nUPDATE_SUCCESS: {link}')
    except Exception as e:
        print("Failed to update master sheet:")
        traceback.print_exc()

if __name__ == "__main__":
    run_update()
