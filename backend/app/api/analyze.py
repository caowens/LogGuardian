from fastapi import APIRouter, UploadFile, File, Form
from ..services.parser import parse_logs
from ..services.engine import analyze_records

router = APIRouter()

@router.post("/scan")
async def scan_logs(text: str = Form(None), upload: UploadFile = File(None)):
    if upload:
        text = (await upload.read()).decode("utf-8")
    if not text:
        return {"error": "no logs provided"}
    records = parse_logs(text)
    report = analyze_records(records)
    return {"alerts": report, "count": len(report)}
