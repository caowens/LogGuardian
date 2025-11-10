# backend/app/detectors/brute_force.py
import time
from collections import defaultdict, deque
from .base import Detector
from typing import Dict, Iterable

# window in seconds and attempt threshold
WINDOW = 60
THRESHOLD = 5
# cooldown before raising another alert for same IP (seconds)
COOLDOWN = 300  # 5 minutes

# per-ip sliding window of attempt timestamps (ints/float epoch seconds)
_failed_attempts: Dict[str, deque] = defaultdict(lambda: deque())
_last_alert_time: Dict[str, float] = {}

def _now_from_record(record):
    ts = record.get("timestamp")
    if isinstance(ts, (int, float)):
        return float(ts)
    if isinstance(ts, str):
        try:
            from datetime import datetime
            return datetime.fromisoformat(ts).timestamp()
        except Exception:
            pass
    # fallback to current time
    return time.time()

class BruteForceDetector(Detector):
    name = "brute_force"
    description = "Detect repeated failed login attempts from a single IP"

    def analyze(self, record: Dict) -> Iterable[Dict]:
        """
        Detects repeated failed login attempts.
        Expects record to contain:
          - record['ip'] (string)
          - record['path'] (string) optional
          - record['status'] (int) optional
          - record['timestamp'] epoch or ISO string (optional)
        """

        ip = record.get("ip")
        if not ip:
            return  # can't attribute to an IP

        # Determine whether this log line is a failed auth attempt.
        # Use heuristics: non-2xx status on common auth endpoints, or explicit "401"/"403"/"429"
        status = record.get("status")
        path = (record.get("path") or "").lower()
        raw = (record.get("raw") or "").lower()

        is_login_path = any(p in path for p in ("/login", "/signin", "/auth"))
        is_failed_status = False
        try:
            if status is not None:
                s = int(status)
                if s == 401 or s == 403 or s == 429 or (400 <= s < 500):
                    is_failed_status = True
        except Exception:
            is_failed_status = False

        # detect explicit words often used in logs
        explicit_failed = any(kw in raw for kw in ("authentication failed", "invalid credentials", "login failed"))

        # decide if this should count as a failed login attempt
        counts_as_failed_login = (is_login_path and is_failed_status) or is_failed_status or explicit_failed

        if not counts_as_failed_login:
            return

        now = _now_from_record(record)

        dq = _failed_attempts[ip]
        # prune old timestamps from left
        while dq and (now - dq[0] > WINDOW):
            dq.popleft()

        dq.append(now)

        if len(dq) >= THRESHOLD:
            last = _last_alert_time.get(ip, 0)
            if now - last < COOLDOWN:
                # already alerted recently, suppress duplicate alert
                return
            _last_alert_time[ip] = now
            yield {
                "detector": self.name,
                "severity": "high",
                "confidence": min(1.0, len(dq) / (THRESHOLD * 1.0)),
                "message": f"Brute force suspected for IP {ip} ({len(dq)} failed attempts in last {WINDOW}s)",
                "log": record.get("raw"),
                "meta": {"ip": ip, "attempts": len(dq), "window": WINDOW}
            }
