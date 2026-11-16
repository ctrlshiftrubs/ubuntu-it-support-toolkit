import subprocess
from datetime import datetime
from zoneinfo import ZoneInfo

# Get current Eastern Time
check_time = datetime.now(ZoneInfo("America/New_York"))

# Service to monitor
service = "cron"

# Check service status
result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

status = result.stdout.strip()

# Display report
print("=== IT SERVICE STATUS REPORT ===")
print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))
print("Service:", service)
print("Status:", status)

# Determine whether service is running
if status == "active":
    print("SUCCESS: Service is running.")
else:
    print("WARNING: Service is not active.")

print("--------------------------------")
