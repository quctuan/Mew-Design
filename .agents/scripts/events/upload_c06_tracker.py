import sys
import traceback

try:
    from manage_event_sheets import update_master_sheet, update_screen_dictionary
except ImportError:
    print("Error importing manage_event_sheets")
    sys.exit(1)

def run_update():
    # Register the screen first
    screens = [
        ("Màn cập nhật thành công (Chương trình C06)", "SCR_C06_SUCCESS")
    ]
    
    print("Registering new screen dictionary...")
    for display_name, screen_name in screens:
        try:
            update_screen_dictionary(display_name, screen_name)
            print(f"Registered: {display_name} -> {screen_name}")
        except Exception as e:
            print(f"Warning on update dictionary for {screen_name}: {e}")

    # Prepare event data
    raw_events = [
        ["Chuẩn hóa TTTB", "Màn cập nhật thành công", "RE01", "Hiển thị màn hình cập nhật thông tin thuê bao Thành công", "service_screen_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_C06_SUCCESS"],
        ["", "", "", "", "", "fromFeature", "nullAble", "'<mã màn hình trước đó>"],
        ["Chuẩn hóa TTTB", "Màn cập nhật thành công", "RE02", "Hiển thị Box thông báo tặng điểm", "service_block_displayed", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_C06_SUCCESS"],
        ["", "", "", "", "", "blockName", "'=", "vplus_bonus_box"],
        ["Chuẩn hóa TTTB", "Màn cập nhật thành công", "RE03", "Click vùng dẫn vào VinaPhone Plus", "service_block_clicked", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_C06_SUCCESS"],
        ["", "", "", "", "", "blockName", "'=", "vplus_bonus_box"],
        ["Chuẩn hóa TTTB", "Màn cập nhật thành công", "RE04", "App gửi yêu cầu cộng điểm cho khách hàng", "ops_request_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_C06_SUCCESS"],
        ["", "", "", "", "", "apiName", "'=", "add_vplus_points"],
        ["Chuẩn hóa TTTB", "Màn cập nhật thành công", "RE05", "App nhận kết quả cộng điểm (điểm trả về lập tức)", "ops_receive_be", "partnerName", "'=", "myvnpt"],
        ["", "", "", "", "", "screenName", "'=", "SCR_C06_SUCCESS"],
        ["", "", "", "", "", "apiName", "'=", "add_vplus_points"],
        ["", "", "", "", "", "duration", "nullAble", "'<ms>"],
        ["", "", "", "", "", "status", "IN SET", "'<0;1>"],
        ["", "", "", "", "", "errorCode", "nullAble", "'<mã lỗi>"],
    ]

    print("Pushing data to Master File...")
    try:
        sheet_name = 'URD_Chuan_Hoa_C06'
        link = update_master_sheet(raw_events, sheet_name)
        print(f'\n=== DONE ===\nUPDATE_SUCCESS: {link}')
    except Exception as e:
        print("Failed to update master sheet:")
        traceback.print_exc()

if __name__ == "__main__":
    run_update()
