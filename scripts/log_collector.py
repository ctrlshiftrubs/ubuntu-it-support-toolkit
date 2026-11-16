import subprocess
from datetime import datetime
from zoneinfo import ZoneInfo

# Get current Eastern Time
check_time = datetime.now(ZoneInfo("America/New_York"))

# Collect recent warning and error logs
result = subprocess.run(
    ["journalctl", "-p", "warning", "-n", "20", "--no-pager"],
    capture_output=True,
    text=True
)

# Display troubleshooting report
print("=== IT TROUBLESHOOTING LOG REPORT ===")
print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))
print("--------------------------------")

if result.returncode == 0:
    print(result.stdout)

    print("SUCCESS: Log collection completed.")
else:
    print("WARNING: Unable to collect system logs.")
    print(result.stderr)

print("--------------------------------")
