# Ubuntu Server IT Support & Python Automation Toolkit

## Project Overview

A hands-on IT Support homelab project built using Ubuntu Server, Python, Linux command-line utilities, and cron automation.

This project demonstrates practical troubleshooting, system monitoring, software inventory, and automation skills relevant to Help Desk Level 1, IT Support Specialist, and Desktop Support roles.

## Technologies Used

- Ubuntu Server
- Python 3
- Bash and Linux CLI
- Git and GitHub
- systemd and journalctl
- cron
- psutil
- VirtualBox

## Python IT Support Tools

| Script | Description |
|---|---|
| `system_info.py` | Retrieves operating system and hostname information |
| `disk_monitor.py` | Monitors disk usage and available storage |
| `system_monitor.py` | Checks CPU and memory utilization |
| `network_check.py` | Tests network connectivity using ping |
| `dns_check.py` | Troubleshoots DNS name resolution |
| `service_check.py` | Checks Linux service status |
| `software_inventory.py` | Retrieves installed software and package versions |
| `health_report.py` | Generates a combined system health report |
| `log_collector.py` | Collects system warnings and errors |
| `it_toolkit.py` | Provides a menu for running IT diagnostic scripts |

## Automation

Python scripts are scheduled using Linux cron to generate timestamped reports.

Monitoring schedules used in the homelab include:

- Disk monitoring: every hour
- CPU, memory, network, DNS, service, and software inventory checks: every 4 hours
- System health reports and troubleshooting log collection: every 12 hours

## Skills Demonstrated

- Linux system administration
- IT troubleshooting and diagnostics
- Python scripting and automation
- Network connectivity and DNS troubleshooting
- CPU, memory, and disk monitoring
- Software inventory management
- Linux service troubleshooting
- System log analysis
- Scheduled task management
- Git version control

## Running the Toolkit

Install the required Python package:

```bash
python3 -m pip install psutil
```

From the repository's root directory, run:

```bash
python3 scripts/it_toolkit.py
```

The interactive menu allows the user to select individual diagnostic tools.

**Note:** This toolkit is designed for Ubuntu-based systems. Some checks require Linux utilities such as `systemctl`, `journalctl`, and `dpkg-query`. Network settings may need adjustment for different environments.

## Project Purpose

This project was developed as part of a hands-on IT Support learning path to strengthen troubleshooting, Linux administration, and automation skills through practical homelab exercises.
