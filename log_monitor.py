#!/usr/bin/env python3
import time

LOG_FILE = "/var/log/syslog"
KEYWORDS = ["error", "fail", "critical"]

def monitor_logs():
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # Move to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            for word in KEYWORDS:
                if word.lower() in line.lower():
                    print(f"[ALERT] Found '{word}' in logs: {line.strip()}")

if __name__ == "__main__":
    monitor_logs()
