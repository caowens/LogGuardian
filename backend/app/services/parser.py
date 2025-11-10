import re
from datetime import datetime

COMBINED_RE = re.compile(r'(\S+) - - \[(.*?)\] "(\S+) (\S+) .*" (\d+)')

def parse_logs(text):
    records = []
    for line in text.splitlines():
        m = COMBINED_RE.match(line)
        if not m:
            # fallback: store raw string
            records.append({"raw": line})
            continue
        ip, date_str, method, path, status = m.groups()
        # parse date like: 09/Nov/2025:18:00:00
        try:
            ts = datetime.strptime(date_str.split()[0], "%d/%b/%Y:%H:%M:%S").timestamp()
        except Exception:
            ts = datetime.utcnow().timestamp()
        records.append({
            "raw": line,
            "ip": ip,
            "method": method,
            "path": path,
            "status": int(status),
            "timestamp": ts
        })
    return records
