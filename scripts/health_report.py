import psutil
import shutil
import socket
import subprocess

from datetime import datetime
from zoneinfo import ZoneInfo



# Date and time
check_time = datetime.now(ZoneInfo("America/New_York"))

# CPU and memory
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

# Disk space
total, used, free = shutil.disk_usage("/")
disk_percent = (used / total) * 100

# Network connectivity
gateway = "127.0.0.1"

ping = subprocess.run(
    ["ping", "-c", "2", "-W", "2", gateway],
    capture_output=True,
    text=True
)

# DNS resolution
try:
    ip_address = socket.gethostbyname("google.com")
    dns_status = f"SUCCESS: {ip_address}"
except socket.gaierror:
    dns_status = "WARNING: DNS resolution failed"

# Linux service
service = "cron"

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

service_status = result.stdout.strip()


print("\n=== IT SYSTEM HEALTH REPORT ===")
print("Check Time:", check_time.strftime("%m/%d/%Y %I:%M:%S %p %Z"))

print("\n--- SYSTEM PERFORMANCE ---")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory.percent}%")
print(f"Available RAM: {memory.available / (1024**3):.2f} GB")

print("\n--- DISK SPACE ---")
print(f"Disk Usage: {disk_percent:.1f}%")
print(f"Free Space: {free / (1024**3):.2f} GB")

print("\n--- NETWORK ---")
print("Gateway:", gateway)
print("Ping:", "SUCCESS" if ping.returncode == 0 else "WARNING: Ping failed")

print("\n--- DNS ---")
print(dns_status)

print("\n--- LINUX SERVICE ---")
print("Service:", service)
print("Status:", service_status)

print("\n=== REPORT COMPLETED ===")
