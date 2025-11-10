from typing import List, Dict, Iterable

class Detector:
    name: str = "base"
    description: str = ""

    def analyze(self, record: Dict) -> Iterable[Dict]:
        raise NotImplementedError

def load_detectors():
    from ..detectors import brute_force
    return [brute_force.BruteForceDetector()]
