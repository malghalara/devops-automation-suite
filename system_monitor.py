#!/usr/bin/env python3
import psutil
import logging
import time

# Configure logging
logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thresholds
CPU_THRESHOLD = 75   # in %
MEM_THRESHOLD = 80   # in %
DISK_THRESHOLD = 85  # in %

def check_system():
    """Check system resource usage and log warnings if thresholds are exceeded."""
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    logging.info(f"CPU: {cpu_usage}%, Memory: {mem_usage}%, Disk: {disk_usage}%")
    print(f"CPU: {cpu_usage}%, Memory: {mem_usage}%, Disk: {disk_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        warning = f"⚠️ High CPU usage detected: {cpu_usage}%"
        logging.warning(warning)
        print(warning)

    if mem_usage > MEM_THRESHOLD:
        warning = f"⚠️ High Memory usage detected: {mem_usage}%"
        logging.warning(warning)
        print(warning)

    if disk_usage > DISK_THRESHOLD:
        warning = f"⚠️ High Disk usage detected: {disk_usage}%"
        logging.warning(warning)
        print(warning)

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(5)  # check every 5 seconds
