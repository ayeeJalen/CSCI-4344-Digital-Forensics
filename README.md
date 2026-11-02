# Offline Linux forensic analysis utilities

These scripts operate on investigator-provided exports; they do not acquire evidence or change a target system.

- `python3 parse_auth.py /path/to/auth.log`: extract OpenSSH authentication outcomes, accounts, IPs and source ports.
- `bash hash_manifest.sh /path/to/evidence-directory > manifest.sha256`: compute SHA-256 for every regular file under a local directory. Store manifest outside the input directory to avoid self-inclusion.
- `python3 timeline_normalize.py events.csv > sorted.csv`: sort CSV rows whose first field is ISO-8601 UTC (e.g. `2026-10-29T08:41:19Z`).

Requirements: Python 3.9+, Bash, GNU find/coreutils for the Bash utility. Run on authorized offline copies, retain originals read-only, and document timezone and provenance.
