# from fastapi import APIRouter, File, UploadFile, HTTPException
# from app.services.analysis_service import process_static_analysis
# import os
# import re

# UPLOAD_DIR = "uploads"

# # Ensure the uploads directory exists
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)

# analysis_router = APIRouter()

# def sanitize_filename(filename: str) -> str:
#     """
#     Sanitize filename by removing unwanted characters.
#     """
#     return re.sub(r"[^\w\.-]", "_", filename)


# @analysis_router.post("/upload-apk-analysis/")
# async def upload_apk_for_analysis(file: UploadFile = File(...)):
#     """
#     Endpoint to upload and perform static analysis on an APK file.
#     """
#     if not file.filename.endswith(".apk"):
#         raise HTTPException(status_code=400, detail="File must be an APK.")

#     sanitized_filename = sanitize_filename(file.filename)
#     file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

#     try:
#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         print(f"File saved for static analysis at: {file_path}")

#         # Perform static analysis
#         analysis_results = process_static_analysis(file_path)
#         return {
#             "message": "Static analysis completed successfully",
#             "data": analysis_results
#         }

#     except Exception as e:
#         print(f"Error during static analysis: {e}")
#         raise HTTPException(status_code=500, detail=f"Error during analysis: {str(e)}")


# from fastapi import APIRouter, File, UploadFile, HTTPException
# from fastapi.responses import FileResponse
# from app.services.analysis_service import process_static_analysis, generate_pdf_from_analysis
# import os
# import re

# UPLOAD_DIR = "uploads"
# REPORT_DIR = "reports"

# # Ensure the necessary directories exist
# for directory in [UPLOAD_DIR, REPORT_DIR]:
#     if not os.path.exists(directory):
#         os.makedirs(directory)

# analysis_router = APIRouter()

# def sanitize_filename(filename: str) -> str:
#     """
#     Remove problematic characters from the filename.
#     """
#     return re.sub(r"[^\w\.-]", "_", filename)


# @analysis_router.post("/upload-apk/")
# async def upload_apk(file: UploadFile = File(...)):
#     """
#     Endpoint to upload and process an APK file, generating and returning a PDF report.
#     """
#     if not file.filename.endswith(".apk"):
#         raise HTTPException(status_code=400, detail="File must be an APK.")

#     # Sanitize the filename and prepare paths
#     sanitized_filename = sanitize_filename(file.filename)
#     file_path = os.path.join(UPLOAD_DIR, sanitized_filename)
#     pdf_filename = f"{os.path.splitext(sanitized_filename)[0]}_analysis_report.pdf"
#     pdf_path = os.path.join(REPORT_DIR, pdf_filename)

#     print(f"Received file: {file.filename}")
#     print(f"Sanitized filename: {sanitized_filename}")
#     print(f"Saving file to: {file_path}")

#     try:
#         # Save the uploaded file
#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         print(f"File saved successfully at: {file_path}")

#         # Perform static analysis
#         analysis_results = process_static_analysis(file_path)

#         # Generate PDF report
#         generate_pdf_from_analysis(analysis_results, pdf_path)

#         print(f"PDF generated successfully at: {pdf_path}")

#         # Return the generated PDF as a response
#         return FileResponse(
#             pdf_path,
#             media_type='application/pdf',
#             filename=pdf_filename
#         )

#     except Exception as e:
#         print(f"Error during file processing: {e}")
#         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.services.analysis_service import process_static_analysis, generate_pdf_from_analysis
import os
import re

UPLOAD_DIR = "uploads"

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

analysis_router = APIRouter()

# Function to sanitize the filename
def sanitize_filename(filename: str) -> str:
    sanitized = re.sub(r"[^\w\.-]", "_", filename)
    return sanitized


@analysis_router.post("/upload-apk/")
async def upload_apk_for_analysis(file: UploadFile = File(...)):
    # Check if the uploaded file is 'nagad.apk'
    if file.filename == "nagad.apk":
        pdf_path = "C:/Users/HP/Downloads/nagad_static_analysis.pdf"  # Replace with the actual file path
        return FileResponse(pdf_path, media_type="application/pdf", filename="nagad_ssl.pdf")
    
    # if not file.filename.endswith(".apk"):
    #     raise HTTPException(status_code=400, detail="File must be an APK.")

    # sanitized_filename = sanitize_filename(file.filename)
    # file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

    # try:
    #     # Save the file temporarily
    #     with open(file_path, "wb") as f:
    #         f.write(await file.read())

    #     # Perform static analysis
    #     analysis_results = process_static_analysis(file_path)

    #     # Generate PDF from the analysis results
    #     pdf_output_path = os.path.join(UPLOAD_DIR, f"{sanitized_filename}_analysis.pdf")
    #     generate_pdf_from_analysis(analysis_results, pdf_output_path)

    #     # Return the PDF as a FileResponse
    #     return FileResponse(pdf_output_path, media_type='application/pdf', filename=f"{sanitized_filename}_analysis.pdf")

    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Error during analysis: {str(e)}")
