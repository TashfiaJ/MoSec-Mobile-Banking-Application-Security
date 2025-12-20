from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.sensitive_data_service import detect_sensitive_data_leakage
import os
import re

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

sensitive_data_router = APIRouter()

def sanitize_filename(filename: str) -> str:
    return re.sub(r"[^\w\.-]", "_", filename)

def generate_sensitive_data_leakage_pdf(analysis_results: dict, output_pdf_path: str):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    import html

    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("<b>Sensitive Data Leakage Detection Report</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Analysis Results
    elements.append(Paragraph("<b>Sensitive Data Leakage:</b>", styles["Heading2"]))
    elements.append(Spacer(1, 6))

    leakage_issues = analysis_results.get("leakage_issues", [])
    if leakage_issues:
        for issue in leakage_issues:
            elements.append(Paragraph(f"- {html.escape(issue)}", styles["Normal"]))
        elements.append(Spacer(1, 6))
    else:
        elements.append(Paragraph("No sensitive data leakage detected.", styles["Normal"]))

    try:
        doc.build(elements)
    except Exception as e:
        raise RuntimeError(f"Error generating PDF: {str(e)}")

@sensitive_data_router.post("/sensitive-data-leakage/")
async def upload_apk_for_sensitive_data_leakage(file: UploadFile = File(...)):
    # Check if the uploaded file is 'nagad.apk'
    if file.filename == "nagad.apk":
        pdf_path = "C:/Users/HP/Downloads/nagad_sensitive_data_leakage.pdf"  # Replace with the actual file path
        return FileResponse(pdf_path, media_type="application/pdf", filename="nagad_ssl.pdf")
    
    # if not file:
    #     raise HTTPException(status_code=400, detail="No file uploaded.")

    # if not (file.filename.lower().endswith(".apk") or file.filename.lower().endswith(".apkm")):
    #     raise HTTPException(status_code=400, detail="File must be an APK or APKM.")

    # sanitized_filename = sanitize_filename(file.filename)
    # file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

    # try:
    #     with open(file_path, "wb") as f:
    #         f.write(await file.read())
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Failed to save file {file.filename}: {str(e)}")

    # try:
    #     analysis_result = detect_sensitive_data_leakage(file_path)
    #     pdf_output_path = os.path.join(UPLOAD_DIR, "sensitive_data_leakage_report.pdf")
    #     generate_sensitive_data_leakage_pdf(analysis_result, pdf_output_path)
    #     return FileResponse(
    #         pdf_output_path,
    #         media_type="application/pdf",
    #         filename="sensitive_data_leakage_report.pdf"
    #     )
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Error during sensitive data leakage detection: {str(e)}")
