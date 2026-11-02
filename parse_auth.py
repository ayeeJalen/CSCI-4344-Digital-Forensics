#!/usr/bin/env python3
"""Offline parser of OpenSSH auth logs. Usage: python3 parse_auth.py /path/to/auth.log"""
import re,sys
from pathlib import Path
if len(sys.argv)!=2: raise SystemExit('Usage: parse_auth.py AUTH_LOG')
pattern=re.compile(r'(Failed password|Accepted publickey).*?for (?:invalid user )?(\S+) from ([0-9.]+) port (\d+)')
for line in Path(sys.argv[1]).read_text(errors='replace').splitlines():
 m=pattern.search(line)
 if m: print('\t'.join([line[:15],*m.groups()]))
