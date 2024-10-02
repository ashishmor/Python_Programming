#Scripts are from this repo - https://github.com/AbeTavarez/Python_DevOps_Scripts/blob/master/Automations/health_check_demo/disk_report.py

#!/usr/bin/env python3
import psutil


cpu_stats = psutil.cpu_percent(0.5)

print(cpu_stats)