import re
from .base import Detector

SQL_PATTERNS = [
    r"union\s+select",
    r"or\s+1=1",
    r"--\s*$",
    r";\s*drop\s+table",
]

class SQLInjectionDetector(Detector):
    name = "sql_injection"
    description = "Detect basic SQL injection patterns"

    def analyze(self, record):
        """
        Detects SQL injection patterns.
        Expects record to contain:
          - record['path'] (string)
          - record['raw'] (string)
        """
        text = " ".join(str(record.get(k,"")) for k in ("path","raw"))
        for pattern in SQL_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                yield {
                    "detector": self.name,
                    "severity": "high",
                    "confidence": 0.8,
                    "message": f"SQL injection pattern: {pattern}",
                    "log": record["raw"],
                    "meta": {"pattern": pattern}
                }
