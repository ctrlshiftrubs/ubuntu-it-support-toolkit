from datetime import datetime
from zoneinfo import ZoneInfo

import subprocess

# Get current Eastern Time
check_time = datetime.now(ZoneInfo("America/New_York"))

# Retrieve installed software
result = subprocess.run(
    ["dpkg-query", "-W", "-f=${binary:Package}\t${Version}\n"],
    capture_output=True,
    text=True
)

print("=== IT SOFTWARE INVENTORY REPORT ===")
print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))
print("--------------------------------")

if result.returncode == 0:
    print(result.stdout)
    print("SUCCESS: Software inventory completed.")
else:
    print("WARNING: Unable to retrieve software inventory.")
    print(result.stderr)

print("--------------------------------")
