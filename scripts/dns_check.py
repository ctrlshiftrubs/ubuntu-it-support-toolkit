from datetime import datetime
from zoneinfo import ZoneInfo

import socket

check_time = datetime.now(ZoneInfo("America/New_York"))

print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))

website = "google.com"

try:
    ip_address = socket.gethostbyname(website)
    print("=== IT DNS TROUBLESHOOTING REPORT ===")
    print("Website:", website)
    print("Resolved IP Address:", ip_address)
    print("STATUS: DNS resolution successful.")

except socket.gaierror:
    print("WARNING: DNS resolution failed.")
