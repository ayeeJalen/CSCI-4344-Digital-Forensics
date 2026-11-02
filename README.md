[README (1).md](https://github.com/user-attachments/files/34283430/README.1.md)
# Linux CI/CD Worker Compromise — Digital Forensics Case Study

**Investigator:** Jalen Davis  
**Course:** CSCI 4344 — Digital Forensics  
**Case ID:** DF-2026-1102-017  
**System:** `ci-worker-03` (Linux CI/CD worker)  
**Primary account:** `worker`  
**IP under investigation:** `192.168.4.35`

## Case materials disclosure

> **This is a fictional educational case study, not a real incident investigation.** Every investigative artifact, timestamp, log excerpt, hash, terminal-output exhibit, finding, and conclusion in this repository was constructed for demonstration. No actual evidence was acquired, verified, or examined. See [`00_Case_Materials_Disclosure.docx`](00_Case_Materials_Disclosure.docx), which governs the entire package.

## Overview

This case study presents an end-to-end investigation of suspected unauthorized access to a Linux-based continuous integration/continuous deployment (CI/CD) worker. The scenario begins with SSH activity involving the `worker` account and `192.168.4.35`, followed by interactive Python execution, unusual CPU utilization, changes to files, suspected user-level persistence, and efforts to obscure shell activity.

The objective is to demonstrate how an investigator correlates authentication, host, process, network, and filesystem artifacts into a defensible incident timeline while distinguishing direct observations from interpretations and unverified possibilities.

## Investigative questions

- Was the `worker` account accessed through SSH in an unauthorized manner?
- Which commands and processes explain the high CPU utilization?
- Were files staged or modified, and is there evidence of data transfer?
- Do the available artifacts support privilege escalation or persistence?
- What evidence suggests attempted concealment, and what remains uncertain?

## Case synopsis

The case chronology centers on **October 29, 2026 (UTC)**. Illustrative authentication records show a failed SSH password attempt followed by an accepted public-key login for `worker` from `192.168.4.35`. Subsequent exhibits and investigative records examine Python shell activity, CI-related file handling, outbound network behavior, user-level systemd persistence, and shell-history suppression.

The analysis does **not** establish successful exfiltration or root-level compromise. These remain distinct from the better-supported account, process, and persistence observations in the constructed case.

## Repository contents

| Path | Purpose |
| --- | --- |
| `00_Case_Materials_Disclosure.docx` | Central disclosure covering all fictional materials |
| `01_Final_Forensic_Report.pdf` | Full investigation, analysis, hypotheses, conclusions, and recommendations |
| `02_Chain_of_Custody.pdf` | Illustrative evidence handling and transfer records |
| `03_Evidence_Inventory.xlsx` | Artifact inventory, provenance fields, hashes, and significance |
| `04_Forensic_Timeline.xlsx` | Chronological sequence of 26 investigative events |
| `05_IOC_List.xlsx` | Indicators of compromise and investigative context |
| `06_MITRE_ATTACK_Mapping.pdf` | Mapping of supported activity to MITRE ATT&CK techniques |
| `07_Investigation_Notes.pdf` | Examination workflow, commands, outputs, and reasoning |
| `08_Screenshots/` | Four **illustrative terminal-output exhibits**, not acquired screenshots |
| `09_Scripts/` | Offline forensic parsing, hashing, and timeline utilities |
| `10_Updated_Resume.pdf` | Resume-ready description of the educational case-study project |
| `11_Links.txt` | Investigator identification and fields for future publication links |
| `README.md` | Repository guide and entry point |

## Methodology

1. **Scope and preservation:** Define the system and relevant artifacts; document an illustrative acquisition and custody process.
2. **Authentication review:** Correlate SSH successes and failures, source IPs, accounts, and session times.
3. **Host examination:** Review process behavior, shell commands, modified files, and account context.
4. **Persistence and privilege review:** Evaluate systemd user-service artifacts and test claims of elevated privileges against available records.
5. **Network analysis:** Compare observed connections with command execution and file-staging activity.
6. **Timeline reconstruction:** Normalize timestamps and cross-reference sources to identify sequences and gaps.
7. **Hypothesis testing:** Compare competing explanations and distinguish established observations from inference.
8. **Reporting:** Summarize indicators, ATT&CK mappings, confidence limits, and response recommendations.

## Analysis scripts

The utilities under [`09_Scripts/`](09_Scripts/) are intended for **authorized offline exports**. They do not perform live acquisition or alter a target host.

```bash
# Extract OpenSSH authentication events from a provided log
python3 09_Scripts/parse_auth.py /path/to/auth.log

# Create a SHA-256 manifest for a local evidence-copy directory
# Save the manifest outside the scanned directory.
bash 09_Scripts/hash_manifest.sh /path/to/evidence-copy > /tmp/evidence-manifest.sha256

# Sort an event CSV whose first column contains ISO-8601 UTC timestamps
python3 09_Scripts/timeline_normalize.py events.csv > sorted-events.csv
```

**Requirements:** Python 3.9+, Bash, and GNU `find`/coreutils for the hashing utility. See [`09_Scripts/README.md`](09_Scripts/README.md) for details. The example input paths are usage illustrations; no raw acquired evidence files are included.

## How to review this case

Start with the final report for the narrative, then use the timeline to follow event order. Consult the evidence inventory and terminal-output exhibits for supporting case materials, the IOC register for detection leads, and the MITRE ATT&CK mapping for behavior classification. Read the chain-of-custody document as a model of documentation practices, **not** as proof that physical or digital evidence was actually collected.

## Skills demonstrated

Linux log interpretation · SSH authentication analysis · incident timeline development · filesystem and process triage · network artifact correlation · evidence documentation · SHA-256 hashing · MITRE ATT&CK mapping · investigative hypothesis testing · technical reporting · Python and Bash scripting.

## Limitations and responsible use

All addresses, artifacts, and investigative records are part of the constructed scenario. `192.168.4.35` is an RFC 1918 private address, not a publicly attributable attacker endpoint. A SHA-256 value recorded in the case is an illustrative case value, not an independently validated digest of acquired evidence. No finding should be used to accuse a real person or organization, or described as professional investigative work performed on a real compromised system.

## Author

**Jalen Davis**  
Computer Science — Cybersecurity / Digital Forensics  
GitHub and presentation links: see `11_Links.txt` (not yet provided).
