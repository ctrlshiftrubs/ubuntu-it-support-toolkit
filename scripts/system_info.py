from datetime import datetime

import platform
import socket

timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %I:%M:%S %p %Z")

print(f"\n--- Check started: {timestamp} ---", flush=True)

hostname = socket.gethostname()
operating_system = platform.system()
os_version = platform.release()
architecture = platform.machine()


print("=== IT SYSTEM INFORMATION ===")
print("Hostname:", hostname)
print("Operating System:", operating_system)
print("OS Version:", os_version)
print("Architecture:", architecture)
