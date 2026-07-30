import sys
import traceback

try:
    from manage_event_sheets import update_screen_dictionary
except ImportError:
    print("Error importing manage_event_sheets")
    sys.exit(1)

def run_update():
    screens = [
        ("Màn thanh toán thành công", "payment_success")
    ]
    
    print("Registering new screen dictionaries...")
    for display_name, screen_name in screens:
        try:
            update_screen_dictionary(display_name, screen_name)
            print(f"Registered: {display_name} -> {screen_name}")
        except Exception as e:
            print(f"Warning on update dictionary for {screen_name}: {e}")

if __name__ == "__main__":
    run_update()
