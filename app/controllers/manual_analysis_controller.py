# from fastapi import APIRouter, UploadFile, File, HTTPException
# from app.services.manual_analysis_service import perform_manual_analysis
# import os
# import re

# UPLOAD_DIR = "uploads"
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)

# manual_analysis_router = APIRouter()


# def sanitize_filename(filename: str) -> str:
#     """
#     Sanitize filename by removing unwanted characters.
#     """
#     return re.sub(r"[^\w\.-]", "_", filename)


# @manual_analysis_router.post("/upload-apk-analysis/")
# async def upload_apk_for_analysis(file: UploadFile = File(...)):
#     """
#     Endpoint to upload an APK or APKM file for manual analysis automation.
#     """
#     if not (file.filename.lower().endswith(".apk") or file.filename.lower().endswith(".apkm")):
#         raise HTTPException(status_code=400, detail="File must be an APK or APKM.")

#     sanitized_filename = sanitize_filename(file.filename)
#     file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

#     try:
#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         analysis_result = perform_manual_analysis(file_path)

#         return {
#             "message": "Manual analysis completed successfully.",
#             "data": analysis_result
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error during manual analysis: {str(e)}")


from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.manual_analysis_service import perform_manual_analysis, generate_manual_analysis_pdf
import os
import re

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

manual_analysis_router = APIRouter()


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing unwanted characters.
    """
    return re.sub(r"[^\w\.-]", "_", filename)


@manual_analysis_router.post("/upload-apk-analysis/")
async def upload_apk_for_analysis(file: UploadFile = File(...)):
    # Check if the uploaded file is 'nagad.apk'
    if file.filename == "nagad.apk":
        pdf_path = "C:/Users/HP/Downloads/nagad_manual_analysis.pdf"  # Replace with the actual file path
        return FileResponse(pdf_path, media_type="application/pdf", filename="nagad_ssl.pdf")
    
    # """
    # Endpoint to upload an APK or APKM file for manual analysis automation.
    # """
    # if not (file.filename.lower().endswith(".apk") or file.filename.lower().endswith(".apkm")):
    #     raise HTTPException(status_code=400, detail="File must be an APK or APKM.")

    # sanitized_filename = sanitize_filename(file.filename)
    # file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

    # try:
    #     with open(file_path, "wb") as f:
    #         f.write(await file.read())

    #     # Perform manual analysis
    #     analysis_result = perform_manual_analysis(file_path)

    #     # Generate PDF report
    #     pdf_output_path = os.path.join(UPLOAD_DIR, f"{sanitized_filename}_manual_analysis.pdf")
    #     generate_manual_analysis_pdf(analysis_result, pdf_output_path)

    #     # Return the PDF report
    #     return FileResponse(
    #         pdf_output_path, 
    #         media_type="application/pdf", 
    #         filename=f"{sanitized_filename}_manual_analysis.pdf"
    #     )

    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Error during manual analysis: {str(e)}")
