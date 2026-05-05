# SOC Analyst Lab — Alert Triage

**Purpose:** Practice tier-1/tier-2 alert triage using real-world simulated alerts, packet captures, and logs.

##Lab Structure

| Directory | Contents |
|-----------|----------|
| `detections/` | Sigma & Yara rules (the "detection engineering" side) |
| `data/alerts/` | JSON alerts from a SIEM (Splunk, ELK, Sentinel) |
| `data/pcaps/` | Network traffic related to the alerts |
| `data/logs/` | Windows EVTX, Syslog, Suricata logs |
| `reports/` | Triage report template + your answers |
| `tools/` | Helper scripts to generate or test alerts |

## 🚀 Quick Start

### 1. Clone & setup
```bash
git clone https://github.com/your-username/soc-alert-triage-lab.git
cd soc-alert-triage-lab

2. Install dependencies (for log analysis)
bash
pip install pandas evtx tshark (or wireshark)

3. Run the alert simulation script (optional)
bash
python tools/simulate_alert.py --alert 001

Challenge Workflow
Pick an alert from data/alerts/alert_XXX.json

Read the alert and note the MITRE TTP.

Open related pcap or log file.

Perform triage (Is it true positive? False positive? What's the impact?)

Fill out the triage report template (see reports/template_triage.md)

Save your answer in reports/answered/alert_XXX_analyst_NAME.md

✅ Sample Triage Questions
Alert ID:

Rule name:

Source IP / Hostname:

Is this a true positive? (Y/N/Unknown)

What is the phase of the kill chain?

IOCs extracted (hash, domain, IP):

Recommended next step:

MITRE ATT&CK Mapping
All alerts are mapped to tactics like TA0001 (Initial Access), TA0005 (Defense Evasion), etc. See docs/mitre-mapping.md

🧰 Useful commands
Extract IOCs from pcap:

bash
tshark -r data/pcaps/alert_002_traffic.pcap -Y "dns" -T fields -e dns.qry.name
Scan logs for a SHA256:

bash
zgrep -i "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" data/logs/syslog/*.log
