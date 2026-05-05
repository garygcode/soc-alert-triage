
## 2. CHALLENGES.md`

```markdown
# 🔍 Alert Triage Challenges

## Challenge 1: Suspicious PowerShell (Alert 001)
- **File:** `data/alerts/alert_001_phish_creds.json`
- **PCAP:** `data/pcaps/alert_001_http_phish.pcap`
- **Goal:** Determine if the host `DESKTOP-JR2` sent creds to a malicious domain.
- **Extra:** Extract the stolen username/password from the POST request.

## Challenge 2: Reverse Shell from HR Laptop (Alert 002)
- **File:** `data/alerts/alert_002_reverse_shell.json`
- **Logs:** `data/logs/windows_sec_evtx/security.evtx` (Event ID 4688)
- **Goal:** Find the parent process that spawned `nc.exe -e cmd.exe`

## Challenge 3: LSASS Memory Access (Alert 003)
- **File:** `data/alerts/alert_003_lsass_dump.json`
- **Syslog:** `data/logs/syslog/alert_003_suricata.json`
- **Goal:** Is this a false positive from a backup agent? Justify.

## Submitting answers
Save your `*.md` report inside `reports/answered/` and open a pull request (if using GitHub) or just review locally.