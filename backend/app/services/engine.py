from ..detectors.base import load_detectors

detectors = load_detectors()

def analyze_records(records):
    alerts = []
    for rec in records:
        for det in detectors:
            for alert in det.analyze(rec) or []:
                alerts.append(alert)
    return alerts
