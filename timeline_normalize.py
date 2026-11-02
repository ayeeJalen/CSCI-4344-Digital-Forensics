#!/usr/bin/env python3
"""Sort a CSV with ISO-8601 UTC timestamp in first column. Usage: python3 timeline_normalize.py events.csv"""
import csv,sys,datetime
if len(sys.argv)!=2: raise SystemExit('Usage: timeline_normalize.py events.csv')
with open(sys.argv[1],newline='') as f: rows=list(csv.reader(f))
header,data=rows[0],rows[1:]
def parse(row): return datetime.datetime.fromisoformat(row[0].replace('Z','+00:00'))
writer=csv.writer(sys.stdout);writer.writerow(header);writer.writerows(sorted(data,key=parse))
