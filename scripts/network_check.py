from datetime import datetime
from zoneinfo import ZoneInfo

import subprocess


target = "127.0.0.1"


result = subprocess.run(
    ["ping", "-c", "4", target],
    capture_output=True,
    text=True
)

check_time = datetime.now(ZoneInfo("America/New_York"))

print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))

print("=== IT NETWORK CONNECTIVITY REPORT ===")
print("Target:", target)

if result.returncode == 0:
    print("SUCCESS: Ping received a response.")
else:
    print("WARNING: Ping test was unsuccessful.")
