
import imaplib
import socket

def test_imap(server):
    print(f"Testing {server}...")
    try:
        mail = imaplib.IMAP4_SSL(server, timeout=10)
        print(f"Success: Connected to {server}")
        mail.logout()
        return True
    except Exception as e:
        print(f"Failed to connect to {server}: {e}")
        return False

# Common IMAP servers for VNPT
servers = ["email.vnpt.vn", "imap.vnpt.vn", "mail.vnpt.vn"]
for s in servers:
    test_imap(s)
