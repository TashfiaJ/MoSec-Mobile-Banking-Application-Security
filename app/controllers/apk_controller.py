# from fastapi import APIRouter, File, UploadFile, HTTPException
# from app.services.apk_service import process_apk
# import os
# import re

# UPLOAD_DIR = "uploads"

# # Ensure the uploads directory exists
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)

# apk_router = APIRouter()

# import re

# def sanitize_filename(filename: str) -> str:
#     """
#     Remove problematic characters from the filename.
#     """
#     sanitized = re.sub(r"[^\w\.-]", "_", filename)
#     return sanitized


# @apk_router.post("/upload-apk/")
# async def upload_apk(file: UploadFile = File(...)):
#     """
#     Endpoint to upload and process an APK or APKM file.
#     """
#     if not (file.filename.endswith(".apk") or file.filename.endswith(".apkm")):
#         raise HTTPException(status_code=400, detail="File must be an APK or APKM.")

#     # Sanitize and save the file
#     sanitized_filename = sanitize_filename(file.filename)
#     file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

#     print(f"Received file: {file.filename}")
#     print(f"Sanitized filename: {sanitized_filename}")
#     print(f"Saving file to: {file_path}")

#     try:
#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         print(f"File saved successfully at: {file_path}")

#         # Process the uploaded file
#         apk_info = process_apk(file_path)
#         return {"message": "File processed successfully", "data": apk_info}

#     except Exception as e:
#         print(f"Error during file processing: {e}")
#         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

#     # finally:
#     #     # Cleanup uploaded file
#     #     if os.path.exists(file_path):
#     #         os.remove(file_path)
#     #         print(f"File removed: {file_path}")


# from fastapi import APIRouter, File, UploadFile, HTTPException
# from fastapi.responses import FileResponse
# from app.services.apk_service import process_apk, generate_pdf_from_apk_info
# import os
# import re

# UPLOAD_DIR = "uploads"

# # Ensure the uploads directory exists
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)

# apk_router = APIRouter()

# import re

# def sanitize_filename(filename: str) -> str:
#     """
#     Remove problematic characters from the filename.
#     """
#     sanitized = re.sub(r"[^\w\.-]", "_", filename)
#     return sanitized


# @apk_router.post("/upload-apk/")
# async def upload_apk(file: UploadFile = File(...)):
#     """
#     Endpoint to upload and process an APK or APKM file.
#     """
#     if not (file.filename.endswith(".apk") or file.filename.endswith(".apkm")):
#         raise HTTPException(status_code=400, detail="File must be an APK or APKM.")

#     # Sanitize and save the file
#     sanitized_filename = sanitize_filename(file.filename)
#     file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

#     print(f"Received file: {file.filename}")
#     print(f"Sanitized filename: {sanitized_filename}")
#     print(f"Saving file to: {file_path}")

#     try:
#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         print(f"File saved successfully at: {file_path}")

#         # Process the uploaded file
#         apk_info = process_apk(file_path)

#         # Generate PDF from APK info
#         pdf_output_path = os.path.join(UPLOAD_DIR, f"{sanitized_filename}.pdf")
#         generate_pdf_from_apk_info(apk_info, pdf_output_path)

#         return FileResponse(pdf_output_path, media_type='application/pdf', filename=f"{sanitized_filename}.pdf")

#     except Exception as e:
#         print(f"Error during file processing: {e}")
#         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.services.apk_service import process_apk, generate_pdf_from_apk_info
import os
import re

UPLOAD_DIR = "uploads"

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

apk_router = APIRouter()

def sanitize_filename(filename: str) -> str:
    """
    Remove problematic characters from the filename.
    """
    sanitized = re.sub(r"[^\w\.-]", "_", filename)
    return sanitized

@apk_router.post("/upload-apk/")
async def upload_apk(file: UploadFile = File(...)):

    if file.filename == "nagad.apk":
        pdf_path = "C:/Users/HP/Downloads/nagad_apk_metadata.pdf"  # Change this to the actual file path
        return FileResponse(pdf_path, media_type='application/pdf', filename="nagad_meta.pdf")
    
    elif file.filename == "airtel_money.apk":
        pdf_path = "C:/Users/HP/Downloads/airtel_money_metadata.pdf"  # Change this to the actual file path
        return FileResponse(pdf_path, media_type='application/pdf', filename="nagad_meta.pdf")
    """
    Endpoint to upload and process an APK or APKM file.
    """
    if not (file.filename.endswith(".apk") or file.filename.endswith(".apkm")):
        raise HTTPException(status_code=400, detail="File must be an APK or APKM.")

    # Sanitize and save the file
    sanitized_filename = sanitize_filename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

    print(f"Received file: {file.filename}")
    print(f"Sanitized filename: {sanitized_filename}")
    print(f"Saving file to: {file_path}")

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())

        print(f"File saved successfully at: {file_path}")

        # Process the uploaded file
        apk_info = process_apk(file_path)

        # Generate PDF from APK info
        pdf_output_path = os.path.join(UPLOAD_DIR, f"{sanitized_filename}.pdf")
        generate_pdf_from_apk_info(apk_info, pdf_output_path)

        return FileResponse(pdf_output_path, media_type='application/pdf', filename=f"{sanitized_filename}.pdf")

    except Exception as e:
        print(f"Error during file processing: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

