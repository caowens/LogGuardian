from pydantic import BaseModel
from typing import Dict, Any, List

class Alert(BaseModel):
    detector: str
    severity: str
    confidence: float
    message: str
    log: str
    meta: Dict[str, Any]
    
class AlertReport(BaseModel):
    alerts: List[Alert]
    count: int
