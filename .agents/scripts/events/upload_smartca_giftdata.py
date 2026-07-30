import sys
import traceback

try:
    from manage_event_sheets import update_master_sheet, update_screen_dictionary
except ImportError:
    print("Error importing manage_event_sheets")
    sys.exit(1)

def run_update():
    # 1. Register new screen names in the dictionary
    screens = [
        ("Màn cập nhật TTTB thành công (Banner SmartCA)", "SCR_TTTB_SUCCESS"),
        ("Màn kích hoạt SmartCA (SDK Fast-Track)", "SCR_SMARTCA_ACTIVATION"),
        ("Màn kích hoạt SmartCA thành công", "SCR_SMARTCA_SUCCESS")
    ]
    
    print("Step 1: Registering new screen dictionary...")
    for display_name, screen_name in screens:
        try:
            update_screen_dictionary(display_name, screen_name)
            print(f"Registered: {display_name} -> {screen_name}")
        except Exception as e:
            print(f"Warning on update dictionary for {screen_name}: {e}")

    # 2. Prepare event data with the multi-row 8-column format
    raw_events = [
        ["SmartCA Gift Data", "Màn cập nhật TTTB thành công", "SGT_01", "Hiển thị Banner khuyến mãi SmartCA (sau khi TTTB xong)", "service_block_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_TTTB_SUCCESS"],
        ["", "", "", "", "", "blockName", "'=", "smartca_promo_banner"],
        ["SmartCA Gift Data", "Màn cập nhật TTTB thành công", "SGT_02", "Click vào Banner để bắt đầu luồng Fast-Track", "service_block_clicked", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_TTTB_SUCCESS"],
        ["", "", "", "", "", "blockName", "'=", "smartca_promo_banner"],
        ["SmartCA Gift Data", "Màn kích hoạt SmartCA (SDK)", "SGT_03", "Hệ thống tự động Skip bước OCR (kế thừa dữ liệu TTTB)", "ops_request_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_SMARTCA_ACTIVATION"],
        ["", "", "", "", "", "actionName", "'=", "skip_ocr_fasttrack"],
        ["SmartCA Gift Data", "Màn kích hoạt SmartCA (SDK)", "SGT_04", "Kích hoạt SmartCA thành công qua luồng Fast-Track", "service_screen_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_SMARTCA_SUCCESS"],
        ["", "", "", "", "", "fromFeature", "'=", "tttb_fasttrack"],
        ["SmartCA Gift Data", "Điểm chạm ngầm (BE)", "SGT_05", "BE nhận lệnh trả thưởng GIFT DATA cho khách hàng", "ops_request_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "apiName", "'=", "fulfill_gift_data"],
        ["SmartCA Gift Data", "Điểm chạm ngầm (BE)", "SGT_06", "BE xác nhận kết quả trả thưởng Data thành công/thất bại", "ops_receive_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "apiName", "'=", "fulfill_gift_data"],
        ["", "", "", "", "", "duration", "nullAble", "'<ms>"],
        ["", "", "", "", "", "status", "IN SET", "'<0;1>"],
        ["", "", "", "", "", "errorCode", "nullAble", "'<mã lỗi>"],
    ]

    print("\nStep 2: Pushing data to Master File...")
    try:
        sheet_name = 'SmartCA_GiftData'
        link = update_master_sheet(raw_events, sheet_name)
        print(f'\n=== DONE ===\nUPDATE_SUCCESS: {link}')
    except Exception as e:
        print("Failed to update master sheet:")
        traceback.print_exc()

if __name__ == "__main__":
    run_update()
