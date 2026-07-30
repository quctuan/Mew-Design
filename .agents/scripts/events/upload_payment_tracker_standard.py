import sys
import traceback
import json

try:
    from manage_event_sheets import update_master_sheet
except ImportError:
    print("Error importing manage_event_sheets")
    sys.exit(1)

def run_update():
    events_expanded = []
    
    # 27 Events from the Payment Hub phase 1 standard PDF
    raw_events = [
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn cá nhân", "id": "PAY1", 
            "trigger": "Hiện thị danh sách phương thức thanh toán", "event": "service_block_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "profile"), 
                ("blockName", "=", "payment_methods"), ("itemCount", "=", "số lượng phương thức thanh toán hiển thị"), 
                ("itemList", "nullable", "Danh sách PTTT: mobile_account|vnpt_pay|mobile_money...")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn cá nhân", "id": "PAY2", 
            "trigger": "Click từng phương thức thanh toán", "event": "service_item_selected", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "profile"), 
                ("blockName", "=", "payment_methods"), ("itemName", "=", "Phương thức thanh toán được chọn"), 
                ("itemStatus", "=", "<active|inactive>")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn cá nhân", "id": "PAY3", 
            "trigger": "Click 'Thêm nguồn tiền'", "event": "service_button_clicked", 
            "params": [("partnerName", "=", "myvnpt"), ("screenName", "=", "profile"), ("buttonName", "=", "Additional funds")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn danh sách nguồn tiền", "id": "PAY4", 
            "trigger": "Hiện thị màn danh sách nguồn tiền", "event": "service_screen_displayed", 
            "params": [("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methods"), ("fromFeature", "nullAble", "<screen_name của màn hình trước đó>")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn danh sách nguồn tiền", "id": "PAY5", 
            "trigger": "Expand / Collapse 'Ngân hàng liên kết VNPT Pay'", "event": "service_block_clicked", 
            "params": [("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methods"), ("blockName", "=", "bank_linked"), ("action", "IN SET", "<expand ;collapse>")]
        },
        {
            "luong": "Liên kết nguồn tiền CTT", "screen": "Màn danh sách nguồn tiền", "id": "PAY6", 
            "trigger": "Click 'Thẻ quốc tế'/ Thẻ nội địa/ VNP Money tại block thêm phương thức", "event": "service_block_clicked", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methods / payment_methode_<dịch vụ>"), 
                ("blockName", "=", "add_payment_method"), ("itemName", "IN SET", "<international_card; domestic_card; VNPT Money>")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY7", 
            "trigger": "Mở màn Chi tiết nguồn tiền", "event": "service_screen_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("fromFeature", "nullAble", "<screen_name của màn hình trước đó>"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY8", 
            "trigger": "Click 'Hủy liên kết'", "event": "service_button_clicked", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("buttonName", "=", "unlink_payment_method"), ("itemName", "=", "Phương thức thanh toán đang xem chi tiết")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY9", 
            "trigger": "switch toggle 'Thanh toán nhanh'", "event": "service_button_clicked", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết"), 
                ("componentType", "=", "toggle"), ("componentName", "=", "quick_payment"), 
                ("targetStatus", "IN SET", "<0;1> 0 = OFF, 1 = ON")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY10", 
            "trigger": "BE đổi trạng thái thanh toán nhanh", "event": "ops_receive_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết"), 
                ("componentType", "=", "toggle"), ("componentName", "=", "quick_payment"), 
                ("targetStatus", "IN SET", "<0;1>"), ("apiName", "=", "update_quick_payment"), 
                ("duration", "nullAble", "<ms>"), ("status", "IN SET", "<0;1>"), ("errorCode", "nullAble", "<mã lỗi>")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY11", 
            "trigger": "Hiển thị popup xác nhận hủy liên kết", "event": "service_component_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("componentType", "=", "popup"), ("componentName", "=", "confirm_unlink"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY12", 
            "trigger": "Thao tác trên popup xác nhận hủy liên kết", "event": "service_button_clicked", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("componentType", "=", "popup"), ("componentName", "=", "confirm_unlink"), 
                ("buttonName", "IN SET", "<cancel; confirm>"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY13", 
            "trigger": "Hiển thị BTS xác nhận hủy liên kết VNPT Money", "event": "service_component_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("componentType", "=", "bottom_sheet"), ("componentName", "=", "confirm_unlink"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY14", 
            "trigger": "Thao tác trên BTS xác nhận hủy liên kết VNPT Money", "event": "service_button_clicked", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("componentType", "=", "bottom_sheet"), ("componentName", "=", "confirm_unlink"), 
                ("buttonName", "IN SET", "<cancel; confirm>"), 
                ("itemName", "=", "Phương thức thanh toán đang xem chi tiết"), 
                ("itemCount", "=", "số lượng phương thức thanh toán sẽ hủy"), ("itemList", "=", "Danh sách PTTT")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY15", 
            "trigger": "Backend nhận request hủy liên kết", "event": "ops_request_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("componentName", "=", "confirm_unlink"), ("apiName", "=", "payment_unlink"), 
                ("itemCount", "=", "số lượng phương thức thanh toán hủy"), ("itemList", "=", "Danh sách PTTT")]
        },
        {
            "luong": "Quản lý nguồn tiền", "screen": "Màn chi tiết nguồn tiền", "id": "PAY16", 
            "trigger": "Backend nhận response hủy liên kết", "event": "ops_receive_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_detail"), 
                ("componentName", "=", "confirm_unlink"), ("apiName", "=", "payment_unlink"), 
                ("itemCount", "=", "số lượng phương thức thanh toán hủy"), ("itemList", "=", "Danh sách PTTT"), 
                ("duration", "nullAble", "<ms>"), ("status", "IN SET", "<0;1>"), ("errorCode", "nullAble", "<mã lỗi>")]
        },
        {
            "luong": "Luồng liên kết thẻ quốc tế", "screen": "Màn danh sách thẻ quốc tế", "id": "PAY17", 
            "trigger": "Hiển thị màn danh sách các loại thẻ", "event": "service_screen_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_international"), 
                ("fromFeature", "nullAble", "<screen_name>"), ("itemCount", "=", "<số loại thẻ>"), 
                ("itemList", "=", "visa | mastercard | jcb")]
        },
        {
            "luong": "Luồng liên kết thẻ quốc tế", "screen": "Màn danh sách thẻ quốc tế", "id": "PAY18", 
            "trigger": "Chọn 1 loại thẻ quốc tế", "event": "service_item_selected", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_international"), 
                ("itemName", "IN SET", "<visa;mastercard;jcb>")]
        },
        {
            "luong": "Luồng liên kết thẻ quốc tế", "screen": "Màn danh sách thẻ quốc tế", "id": "PAY19", 
            "trigger": "Hiển thị popup xác nhận", "event": "service_component_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_international"), 
                ("itemName", "IN SET", "<visa;mastercard;jcb>"), ("componentType", "=", "popup"), 
                ("componentName", "=", "confirm_add_payment"), ("paymentType", "=", "international_card")]
        },
        {
            "luong": "Luồng liên kết thẻ nội địa", "screen": "Màn thay đổi phương thức TT", "id": "PAY20", 
            "trigger": "Hiển thị popup xác nhận", "event": "service_component_displayed", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methods / payment_methode_<dịch vụ>"), 
                ("componentType", "=", "popup"), ("componentName", "=", "confirm_add_payment"), 
                ("paymentType", "=", "domestic_card")]
        },
        {
            "luong": "Luồng liên kết thẻ quốc tế", "screen": "Màn danh sách thẻ quốc tế", "id": "PAY21", 
            "trigger": "thao tác trên popup xác nhận liên kết", "event": "service_button_clicked", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_international"), 
                ("itemName", "IN SET", "<visa;mastercard;jcb>"), ("componentType", "=", "popup"), 
                ("componentName", "=", "confirm_add_payment"), ("paymentType", "=", "international_card"), 
                ("buttonName", "IN SET", "<cancel;confirm>")]
        },
        {
            "luong": "Luồng liên kết thẻ nội địa", "screen": "Màn thay đổi phương thức TT", "id": "PAY22", 
            "trigger": "thao tác trên popup xác nhận liên kết", "event": "service_item_selected", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methods / payment_methode_<dịch vụ>"), 
                ("componentType", "=", "popup"), ("componentName", "=", "confirm_add_payment"), 
                ("paymentType", "=", "domestic_card"), ("buttonName", "IN SET", "<cancel;confirm>")]
        },
        {
            "luong": "Luồng liên kết thẻ quốc tế", "screen": "Màn điểm chạm", "id": "PAY23", 
            "trigger": "BE nhận request liên kết thẻ", "event": "ops_request_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_international / etc."), 
                ("itemName", "nullAble", "<visa;mastercard;jcb>"), ("apiName", "=", "link_card"), 
                ("paymentType", "IN SET", "<international_card; domestic_card>")]
        },
        {
            "luong": "Luồng liên kết thẻ quốc tế", "screen": "Màn điểm chạm", "id": "PAY24", 
            "trigger": "BE nhận response liên kết thẻ", "event": "ops_receive_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_method_international / etc."), 
                ("itemName", "nullAble", "<visa;mastercard;jcb>"), ("apiName", "=", "link_card"), 
                ("paymentType", "IN SET", "<international_card; domestic_card>"), 
                ("duration", "nullAble", "<ms>"), ("status", "IN SET", "<0;1>"), ("errorCode", "nullAble", "<mã lỗi>")]
        },
        {
            "luong": "Luồng thanh toán", "screen": "Màn điểm chạm", "id": "PAY25", 
            "trigger": "Chọn nguồn tiền thanh toán", "event": "service_item_selected", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methode_<dịch vụ>"), 
                ("paymentType", "IN SET", "<mobile_account | mobile_money | vnpt_pay | etc>"), 
                ("bank_code", "nullAble", "<bank_code>")]
        },
        {
            "luong": "Luồng thanh toán", "screen": "Màn điểm chạm", "id": "PAY26", 
            "trigger": "BE nhận request thanh toán", "event": "ops_request_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methode_<dịch vụ>"), 
                ("paymentType", "IN SET", "<mobile_account | mobile_money | vnpt_pay | etc>"), 
                ("bank_code", "nullAble", "<bank_code>"), ("apiName", "=", "pay_<dịch vụ>")]
        },
        {
            "luong": "Luồng thanh toán", "screen": "Màn điểm chạm", "id": "PAY27", 
            "trigger": "BE trả kết quả thanh toán", "event": "ops_receive_be", 
            "params": [
                ("partnerName", "=", "myvnpt"), ("screenName", "=", "payment_methode_<dịch vụ>"), 
                ("paymentType", "IN SET", "<mobile_account | mobile_money | vnpt_pay | etc>"), 
                ("bank_code", "nullAble", "<bank_code>"), ("apiName", "=", "pay_<dịch vụ>"), 
                ("duration", "nullAble", "<ms>"), ("status", "IN SET", "<0;1>"), ("errorCode", "nullAble", "<mã lỗi>")]
        }
    ]

    for ev in raw_events:
        params = ev['params']
        if not params:
            events_expanded.append([ev['luong'], ev['screen'], ev['id'], ev['trigger'], ev['event'], "", "", ""])
            continue
            
        first_param = params[0]
        # Format operator with leading quote to prevent excel formula expansion
        operator = first_param[1]
        if operator.startswith("=") or operator.startswith("<"):
            operator = f"'{operator}"
            
        events_expanded.append([
            ev['luong'], ev['screen'], ev['id'], ev['trigger'], ev['event'],
            first_param[0], operator, first_param[2]
        ])
        
        for param in params[1:]:
            op = param[1]
            if op.startswith("=") or op.startswith("<"):
                op = f"'{op}"
            events_expanded.append([
                "", "", "", "", "",
                param[0], op, param[2]
            ])

    print("Adding standardized template to Master File...")
    try:
        sheet_name = 'Payment_Hub_Phase1'
        link = update_master_sheet(events_expanded, sheet_name)
        print(f'\n=== DONE ===\nUPDATE_SUCCESS: {link}')
    except Exception as e:
        print("Failed to update master sheet:")
        traceback.print_exc()

if __name__ == "__main__":
    run_update()
