from .base import Detector

SUSPICIOUS_PATHS = ["/admin", "/wp-login.php", "/phpmyadmin", "/config"]

class SuspiciousEndpointDetector(Detector):
    name = "suspicious_endpoints"
    description = "Flag access to sensitive or known attack paths"

    def analyze(self, record):
        path = record.get("path") or ""
        for target in SUSPICIOUS_PATHS:
            if target in path.lower():
                yield {
                    "detector": self.name,
                    "severity": "medium",
                    "confidence": 0.7,
                    "message": f"Suspicious path access: {path}",
                    "log": record["raw"],
                    "meta": {"path": path},
                }
