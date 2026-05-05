# SOC Analyst Lab — Alert Triage
**Purpose:** Practice tier-1/tier-2 alert triage using real-world simulated alerts, packet captures, and logs.
## Lab Structure

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
