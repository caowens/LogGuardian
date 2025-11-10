import time, json, random

NORMAL_LOGS = [
    '127.0.0.1 - - [date] "GET /home HTTP/1.1" 200',
    '192.168.1.3 - - [date] "POST /login HTTP/1.1" 401',
]
SUSPICIOUS_LOGS = [
    '10.0.0.5 - - [date] "GET /admin HTTP/1.1" 200',
    '10.0.0.8 - - [date] "GET /index.php?id=1 UNION SELECT password FROM users HTTP/1.1" 200',
]

def demo_stream():
    while True:
        log = random.choice(NORMAL_LOGS + SUSPICIOUS_LOGS)
        level = "high" if "UNION" in log or "/admin" in log else "low"
        data = {
            "type": "metric",
            "timestamp": time.time(),
            "severity": level,
            "log": log,
        }
        yield f"data: {json.dumps(data)}\n\n"
        time.sleep(1)
