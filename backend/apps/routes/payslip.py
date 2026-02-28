from fastapi import APIRouter, UploadFile, File
import pdfplumber
from app.services.payslip_parser import parse_payslip

router = APIRouter(prefix="/payslip", tags=["Payslip"])

@router.post("/upload")
def upload_payslip(file: UploadFile = File(...)):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    components = parse_payslip(text)

    return {
        "message": "Payslip processed",
        "components": components
    }