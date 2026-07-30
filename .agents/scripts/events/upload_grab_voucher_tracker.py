import sys
import traceback

try:
    from manage_event_sheets import update_master_sheet
except ImportError:
    print("Error importing manage_event_sheets")
    sys.exit(1)

def run_update():
    events_expanded = []
    
    raw_events = [
        ["Grab Voucher", "Màn thanh toán thành công", "GRB_01", "Hiển thị Banner tặng Voucher (chưa nhận hoặc đã nhận)", "service_block_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "blockName", "'=", "grab_voucher_banner"],
        ["", "", "", "", "", "status", "IN SET", "'<chưa nhận; đã nhận>"],
        ["Grab Voucher", "Màn thanh toán thành công", "GRB_02", "Click vào Banner (ngoài không gian nút 'Nhận ngay')", "service_block_clicked", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "blockName", "'=", "grab_voucher_banner"],
        ["Grab Voucher", "Màn thanh toán thành công", "GRB_03", "Click nút 'Nhận ngay' trên Banner", "service_button_clicked", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "buttonName", "'=", "get_voucher_now"],
        ["Grab Voucher", "Điểm chạm ngầm (BE)", "GRB_04", "BE nhận request cấp / gửi SMS Voucher", "ops_request_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "apiName", "'=", "assign_grab_voucher"],
        ["Grab Voucher", "Điểm chạm ngầm (BE)", "GRB_05", "BE trả phản hồi cấp Voucher (Thành công / Hết / Lỗi)", "ops_receive_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "apiName", "'=", "assign_grab_voucher"],
        ["", "", "", "", "", "duration", "nullAble", "'<ms>"],
        ["", "", "", "", "", "status", "IN SET", "'<0;1>"],
        ["", "", "", "", "", "errorCode", "nullAble", "'<mã lỗi>"],
        ["Grab Voucher", "Màn thanh toán thành công", "GRB_06", "Hiển thị Popup Nhận quà thành công", "service_component_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "componentType", "'=", "popup"],
        ["", "", "", "", "", "componentName", "'=", "grab_voucher_success"],
        ["Grab Voucher", "Màn thanh toán thành công", "GRB_07", "Hiển thị Toast thông báo hết quà", "service_component_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "componentType", "'=", "toast"],
        ["", "", "", "", "", "componentName", "'=", "grab_voucher_out_of_stock"],
        ["Grab Voucher", "Màn thanh toán thành công", "GRB_08", "Hiển thị Toast thông báo lỗi hệ thống", "service_component_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "payment_success"],
        ["", "", "", "", "", "componentType", "'=", "toast"],
        ["", "", "", "", "", "componentName", "'=", "grab_voucher_error"]
    ]

    print("Pushing data to Master File...")
    try:
        sheet_name = 'URD_Grab_Voucher_02'
        link = update_master_sheet(raw_events, sheet_name)
        print(f'\n=== DONE ===\nUPDATE_SUCCESS: {link}')
    except Exception as e:
        print("Failed to update master sheet:")
        traceback.print_exc()

if __name__ == "__main__":
    run_update()
