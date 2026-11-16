import subprocess
import sys
from pathlib import Path

# Location of your Python scripts
lab_folder = Path(__file__).resolve().parent

scripts = {
    "1": "system_info.py",
    "2": "disk_monitor.py",
    "3": "system_monitor.py",
    "4": "network_check.py",
    "5": "dns_check.py",
    "6": "service_check.py",
    "7": "software_inventory.py",
    "8": "health_report.py",
    "9": "log_collector.py"
}

while True:
    print("\n=== IT SUPPORT AUTOMATION TOOLKIT ===")
    print("1. System Information")
    print("2. Disk Monitoring")
    print("3. CPU and Memory Monitoring")
    print("4. Network Connectivity")
    print("5. DNS Troubleshooting")
    print("6. Linux Service Status")
    print("7. Software Inventory")
    print("8. Complete System Health Report")
    print("9. Troubleshooting Log Collection")
    print("0. Exit")

    choice = input("\nSelect an option: ")

    if choice == "0":
        print("Exiting IT Support Toolkit.")
        break

    elif choice in scripts:
        script_path = lab_folder / scripts[choice]

        if script_path.is_file():
            subprocess.run([sys.executable, str(script_path)])
        else:
            print("ERROR: Script not found:", script_path.name)

    else:
        print("Invalid option. Please try again.")
