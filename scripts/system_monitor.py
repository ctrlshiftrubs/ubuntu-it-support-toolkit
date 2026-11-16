import psutil

from datetime import datetime
from zoneinfo import ZoneInfo

check_time = datetime.now(ZoneInfo("America/New_York"))

print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))

cpu_usage = psutil.cpu_percent(interval=1)

print("=== IT SYSTEM PERFORMANCE REPORT ===")
print(f"CPU Usage: {cpu_usage}%")


memory = psutil.virtual_memory()

print(f"Memory Usage: {memory.percent}%")
print(f"Available RAM: {memory.available / (1024**3):.2f} GB")


if cpu_usage >= 90:
    print("WARNING: High CPU usage detected.")
else:
    print("CPU usage is within the lab threshold.")

if memory.percent >= 90:
    print("WARNING: High memory usage detected.")
else:
    print("Memory usage is within the lab threshold.")
