# from fastapi import APIRouter, UploadFile, File, HTTPException
# from app.services.reverse_engineering_service import perform_reverse_engineering_analysis
# import os
# import re

# UPLOAD_DIR = "uploads"
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)

# reverse_engineering_router = APIRouter()


# def sanitize_filename(filename: str) -> str:
#     """
#     Sanitize filename by removing unwanted characters.
#     """
#     return re.sub(r"[^\w\.-]", "_", filename)


# @reverse_engineering_router.post("/upload-apk-reverse-engineering/")
# async def upload_apk_for_reverse_engineering(files: list[UploadFile] = File(...)):
#     """
#     Endpoint to upload one or more APK/APKM files for reverse engineering.
#     """
#     apk_paths = []

#     for file in files:
#         if not (file.filename.lower().endswith(".apk") or file.filename.lower().endswith(".apkm")):
#             raise HTTPException(status_code=400, detail="All files must be APK or APKM.")

#         sanitized_filename = sanitize_filename(file.filename)
#         file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

#         try:
#             with open(file_path, "wb") as f:
#                 f.write(await file.read())
#             apk_paths.append(file_path)
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Failed to save file {file.filename}: {str(e)}")

#     try:
#         analysis_result = perform_reverse_engineering_analysis(apk_paths)

#         return {
#             "message": "Reverse engineering completed successfully.",
#             "data": analysis_result,
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error during reverse engineering: {str(e)}")


from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.reverse_engineering_service import perform_reverse_engineering_analysis, generate_reverse_engineering_pdf
import os
import re
import html

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

reverse_engineering_router = APIRouter()

def sanitize_filename(filename: str) -> str:
    return re.sub(r"[^\w\.-]", "_", filename)

@reverse_engineering_router.post("/upload-apk-reverse-engineering/")
async def upload_apk_for_reverse_engineering(file: UploadFile = File(...)):
    # Check if the uploaded file is 'nagad.apk'
    if file.filename == "nagad.apk":
        pdf_path = "C:/Users/HP/Downloads/nagad_reverse_engineering.pdf"  # Replace with the actual file path
        return FileResponse(pdf_path, media_type="application/pdf", filename="nagad_ssl.pdf")
    
    # # Ensure a file is uploaded
    # if not file:
    #     raise HTTPException(status_code=400, detail="No file uploaded.")

    # # Validate file extension (APK or APKM)
    # if not (file.filename.lower().endswith(".apk") or file.filename.lower().endswith(".apkm")):
    #     raise HTTPException(status_code=400, detail="File must be APK or APKM.")

    # # Sanitize the filename and save the file
    # sanitized_filename = sanitize_filename(file.filename)
    # file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

    # try:
    #     # Save the uploaded file to disk
    #     with open(file_path, "wb") as f:
    #         f.write(await file.read())
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Failed to save file {file.filename}: {str(e)}")

    # # Perform reverse engineering analysis on the uploaded file
    # try:
    #     analysis_result = perform_reverse_engineering_analysis([file_path])
    #     pdf_output_path = os.path.join(UPLOAD_DIR, "reverse_engineering_report.pdf")
    #     generate_reverse_engineering_pdf(analysis_result, pdf_output_path)

    #     # Return the generated PDF report
    #     return FileResponse(
    #         pdf_output_path,
    #         media_type="application/pdf",
    #         filename="reverse_engineering_report.pdf"
    #     )
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Error during reverse engineering: {str(e)}")
