from datetime import datetime

import shutil

timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %I:%M:%S %p %Z")

print(f"Checked at: {timestamp}")

total, used, free = shutil.disk_usage("/")

usage_percent = (used / total) * 100

print("=== IT DISK SPACE REPORT ===")
print(f"Total Space: {total / (1024**3):.2f} GB")
print(f"Used Space: {used / (1024**3):.2f} GB")
print(f"Free Space: {free / (1024**3):.2f} GB")
print(f"Disk Usage: {usage_percent:.1f}%")

if usage_percent >= 90:
    print("WARNING: Disk space is critically low!")
elif usage_percent >= 75:
    print("NOTICE: Disk usage is getting high.")
else:
    print("STATUS: Disk space is within normal limits.")

