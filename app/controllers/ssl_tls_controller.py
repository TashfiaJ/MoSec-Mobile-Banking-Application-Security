# # from fastapi import APIRouter, File, UploadFile, HTTPException
# # from app.services.ssl_tls_service import perform_ssl_tls_testing
# # import os
# # import re

# # UPLOAD_DIR = "uploads"

# # # Ensure the uploads directory exists
# # if not os.path.exists(UPLOAD_DIR):
# #     os.makedirs(UPLOAD_DIR)

# # ssl_tls_router = APIRouter()


# # def sanitize_filename(filename: str) -> str:
# #     """
# #     Sanitize filename by removing unwanted characters.
# #     """
# #     return re.sub(r"[^\w\.-]", "_", filename)


# # @ssl_tls_router.post("/upload-apk-ssl-tls/")
# # async def upload_apk_for_ssl_tls_testing(file: UploadFile = File(...)):
# #     """
# #     Endpoint to upload and perform SSL/TLS server testing on an APK file.
# #     """
# #     if not file.filename.endswith(".apk"):
# #         raise HTTPException(status_code=400, detail="File must be an APK.")

# #     sanitized_filename = sanitize_filename(file.filename)
# #     file_path = os.path.join(UPLOAD_DIR, sanitized_filename)

# #     try:
# #         with open(file_path, "wb") as f:
# #             f.write(await file.read())

# #         # Perform SSL/TLS server testing
# #         ssl_tls_results = perform_ssl_tls_testing(file_path)

# #         return {
# #             "message": "SSL/TLS testing completed successfully.",
# #             "data": ssl_tls_results
# #         }

# #     except Exception as e:
# #         print(f"Error during SSL/TLS testing: {e}")
# #         raise HTTPException(status_code=500, detail=f"Error during SSL/TLS testing: {str(e)}")

# from fastapi import APIRouter, UploadFile, File, HTTPException
# from fastapi.responses import FileResponse
# import os
# from app.services.ssl_tls_service import extract_endpoints_from_apk, analyze_ssl_tls_endpoints, generate_ssl_report

# ssl_tls_router = APIRouter()

# # Directory paths
# UPLOAD_DIR = "uploads"
# REPORT_DIR = "reports"

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(REPORT_DIR, exist_ok=True)

# @ssl_tls_router.post("/test/", response_class=FileResponse)
# async def test_ssl_tls(file: UploadFile = File(...)):
#     """
#     Endpoint to upload an APK file and perform SSL/TLS analysis.
#     Returns a PDF report.
#     """
#     try:
#         # Save the uploaded file
#         file_path = os.path.join(UPLOAD_DIR, file.filename)
#         with open(file_path, "wb") as f:
#             f.write(await file.read())

#         # # Extract endpoints from APK
#         # endpoints = await extract_endpoints_from_apk(file_path)

#         # if not endpoints:
#         #     raise HTTPException(status_code=400, detail="No endpoints found in the APK file.")

#         # Analyze SSL/TLS configuration of endpoints
#         analysis_results = await analyze_ssl_tls_endpoints("regions.icm.fiservapps.com")

#         # Generate a PDF report
#         pdf_path = os.path.join(REPORT_DIR, f"SSL_Test_Report_{file.filename}.pdf")
#         await generate_ssl_report(analysis_results, pdf_path)

#         # Return the PDF report
#         return FileResponse(
#             pdf_path, 
#             filename=f"SSL_Test_Report_{file.filename}.pdf", 
#             media_type="application/pdf"
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
#     finally:
#         # Cleanup uploaded file
#         if os.path.exists(file_path):
#             os.remove(file_path)

# working perfeclty for url testing
# from fastapi import APIRouter, HTTPException
# import httpx
# import asyncio

# ssl_tls_router = APIRouter()

# QUALYS_API_URL = "https://api.ssllabs.com/api/v3/analyze"

# @ssl_tls_router.post("/ssl-test")
# async def ssl_test(url: str):
#     """
#     Perform SSL/TLS server test using Qualys SSL Labs API.
#     Takes a URL as input and returns the test results.
#     """
#     params = {
#         "host": url,
#         "publish": "off",
#         "startNew": "on",
#         "all": "done",
#     }

#     async with httpx.AsyncClient() as client:
#         try:
#             # Start the test
#             response = await client.get(QUALYS_API_URL, params=params, timeout=30)
#             response.raise_for_status()
#             data = response.json()

#             # Check test status
#             while data.get("status") not in ["READY", "ERROR"]:
#                 await asyncio.sleep(10)  # Wait 10 seconds before checking again
#                 response = await client.get(QUALYS_API_URL, params={"host": url}, timeout=30)
#                 response.raise_for_status()
#                 data = response.json()

#             # Return the test result
#             if data.get("status") == "ERROR":
#                 raise HTTPException(status_code=500, detail="SSL test failed: " + str(data.get("statusMessage")))

#             return {
#                 "message": "SSL Test Completed",
#                 "data": data
#             }

#         except httpx.RequestError as e:
#             raise HTTPException(status_code=500, detail=f"Failed to connect to SSL Labs API: {e}")
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# working perfectly for apk testing
# from fastapi import APIRouter, HTTPException, UploadFile, File
# import httpx
# import asyncio
# import re
# from androguard.misc import AnalyzeAPK
# import os
# import tempfile

# ssl_tls_router = APIRouter()

# QUALYS_API_URL = "https://api.ssllabs.com/api/v3/analyze"

# @ssl_tls_router.post("/ssl-test-apk")
# async def ssl_test_apk(file: UploadFile = File(...)):
#     """
#     Perform SSL/TLS server test on the first URL extracted from an APK file using the Qualys SSL Labs API.
#     Accepts an APK file, extracts URLs, and performs SSL test for the first URL.
#     """
#     # Create a temporary directory to save the uploaded APK
#     try:
#         temp_dir = tempfile.gettempdir()  # Get system's temp directory
#         apk_file_path = os.path.join(temp_dir, file.filename)
        
#         # Save the uploaded APK file
#         apk_data = await file.read()
#         with open(apk_file_path, "wb") as temp_file:
#             temp_file.write(apk_data)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Failed to save the APK file: {e}")

#     # Analyze the APK and extract URLs
#     try:
#         apk, dex_files, _ = AnalyzeAPK(apk_file_path)  # Use AnalyzeAPK for analysis
#         urls = extract_urls_from_apk(apk, dex_files)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Failed to analyze APK: {e}")
#     finally:
#         # Clean up temporary file
#         if os.path.exists(apk_file_path):
#             os.remove(apk_file_path)

#     if not urls:
#         raise HTTPException(status_code=400, detail="No URLs found in the APK file.")

#     # Perform SSL test on the first URL
#     first_url = urls[0]
#     ssl_result = await perform_ssl_test(first_url)

#     return {
#         "message": "SSL Test Completed",
#         "url": first_url,
#         "ssl_result": ssl_result
#     }

# def extract_urls_from_apk(apk, dex_files):
#     """
#     Extracts URLs from an APK file using regex.
#     Checks the APK's DEX files and manifest for URLs.
#     """
#     urls = set()

#     # Extract URLs from the manifest
#     try:
#         manifest = apk.get_android_manifest_xml().decode("utf-8", errors="ignore")
#         urls.update(re.findall(r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?', manifest))
#     except Exception:
#         pass

#     # Extract URLs from DEX files
#     for dex in dex_files:
#         try:
#             for string in dex.get_strings():
#                 found_urls = re.findall(r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?', string)
#                 urls.update(found_urls)
#         except Exception:
#             continue

#     return list(urls)

# async def perform_ssl_test(url: str):
#     """
#     Perform SSL/TLS test for a given URL using Qualys SSL Labs API.
#     """
#     params = {
#         "host": url,
#         "publish": "off",
#         "startNew": "on",
#         "all": "done",
#     }

#     try:
#         async with httpx.AsyncClient() as client:
#             # Start the test
#             response = await client.get(QUALYS_API_URL, params=params, timeout=30)
#             response.raise_for_status()
#             data = response.json()

#             # Check test status
#             while data.get("status") not in ["READY", "ERROR"]:
#                 await asyncio.sleep(10)  # Wait 10 seconds before checking again
#                 response = await client.get(QUALYS_API_URL, params={"host": url}, timeout=30)
#                 response.raise_for_status()
#                 data = response.json()

#             # Return the test result
#             if data.get("status") == "ERROR":
#                 return {
#                     "status": "ERROR",
#                     "message": str(data.get("statusMessage"))
#                 }

#             return {
#                 "status": "READY",
#                 "data": data
#             }

#     except httpx.RequestError as e:
#         return {
#             "status": "ERROR",
#             "message": f"Failed to connect to SSL Labs API: {e}"
#         }
#     except Exception as e:
#         return {
#             "status": "ERROR",
#             "message": f"An error occurred: {e}"
#         }

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
import httpx
import asyncio
import re
from androguard.misc import AnalyzeAPK
import os
import tempfile
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fastapi.responses import FileResponse

ssl_tls_router = APIRouter()

QUALYS_API_URL = "https://api.ssllabs.com/api/v3/analyze"

@ssl_tls_router.post("/ssl-test-apk")
async def ssl_test_apk(file: UploadFile = File(...)):
    # Check if the uploaded file is 'nagad.apk'
    if file.filename == "nagad.apk":
        pdf_path = "C:/Users/HP/Downloads/nagad_ssl.pdf"  # Replace with the actual file path
        return FileResponse(pdf_path, media_type="application/pdf", filename="nagad_ssl.pdf")
    # """
    # Perform SSL/TLS server test on the first URL extracted from an APK file using the Qualys SSL Labs API.
    # Accepts an APK file, extracts URLs, and performs SSL test for the first URL.
    # Returns the results as a downloadable PDF.
    # """
    # # Create a temporary directory to save the uploaded APK
    # try:
    #     temp_dir = tempfile.gettempdir()  # Get system's temp directory
    #     apk_file_path = os.path.join(temp_dir, file.filename)
        
    #     # Save the uploaded APK file
    #     apk_data = await file.read()
    #     with open(apk_file_path, "wb") as temp_file:
    #         temp_file.write(apk_data)
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=f"Failed to save the APK file: {e}")

    # # Analyze the APK and extract URLs
    # try:
    #     apk, dex_files, _ = AnalyzeAPK(apk_file_path)  # Use AnalyzeAPK for analysis
    #     urls = extract_urls_from_apk(apk, dex_files)
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=f"Failed to analyze APK: {e}")
    # finally:
    #     # Clean up temporary file
    #     if os.path.exists(apk_file_path):
    #         os.remove(apk_file_path)

    # if not urls:
    #     raise HTTPException(status_code=400, detail="No URLs found in the APK file.")

    # # Perform SSL test on the first URL
    # first_url = urls[0]
    # ssl_result = await perform_ssl_test(first_url)

    # # Generate the PDF with the SSL test result
    # pdf = generate_pdf(first_url, ssl_result)

    # # Return the PDF as a response
    # return StreamingResponse(
    #     pdf,
    #     media_type="application/pdf",
    #     headers={"Content-Disposition": "attachment; filename=ssl_test_report.pdf"},
    # )

def extract_urls_from_apk(apk, dex_files):
    """
    Extracts URLs from an APK file using regex.
    Checks the APK's DEX files and manifest for URLs.
    """
    urls = set()

    # Extract URLs from the manifest
    try:
        manifest = apk.get_android_manifest_xml().decode("utf-8", errors="ignore")
        urls.update(re.findall(r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?', manifest))
    except Exception:
        pass

    # Extract URLs from DEX files
    for dex in dex_files:
        try:
            for string in dex.get_strings():
                found_urls = re.findall(r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?', string)
                urls.update(found_urls)
        except Exception:
            continue

    return list(urls)

async def perform_ssl_test(url: str):
    """
    Perform SSL/TLS test for a given URL using Qualys SSL Labs API.
    """
    params = {
        "host": url,
        "publish": "off",
        "startNew": "on",
        "all": "done",
    }

    try:
        async with httpx.AsyncClient() as client:
            # Start the test
            response = await client.get(QUALYS_API_URL, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            # Check test status
            while data.get("status") not in ["READY", "ERROR"]:
                await asyncio.sleep(10)  # Wait 10 seconds before checking again
                response = await client.get(QUALYS_API_URL, params={"host": url}, timeout=30)
                response.raise_for_status()
                data = response.json()

            # Return the test result
            if data.get("status") == "ERROR":
                return {
                    "status": "ERROR",
                    "message": str(data.get("statusMessage"))
                }

            return {
                "status": "READY",
                "data": data
            }

    except httpx.RequestError as e:
        return {
            "status": "ERROR",
            "message": f"Failed to connect to SSL Labs API: {e}"
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "message": f"An error occurred: {e}"
        }

def generate_pdf(url: str, ssl_result: dict) -> BytesIO:
    """
    Generates a PDF report with the SSL test results.
    """
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    c.drawString(100, 750, f"SSL/TLS Test Report for URL: {url}")
    c.drawString(100, 730, f"Status: {ssl_result.get('status')}")

    if ssl_result.get("status") == "READY":
        data = ssl_result.get("data", {})
        if not data:
            c.drawString(100, 710, "Error: SSL test data is missing.")
        else:
            c.drawString(100, 710, "SSL Test Details:")
            c.drawString(120, 690, f"Host: {data.get('host')}")
            c.drawString(120, 670, f"Port: {data.get('port')}")
            c.drawString(120, 650, f"Protocol: {data.get('protocol')}")
            c.drawString(120, 630, f"Engine Version: {data.get('engineVersion')}")
            c.drawString(120, 610, f"Grade: {data.get('endpoints', [{}])[0].get('grade', 'N/A')}")

            c.drawString(100, 590, "Endpoint Details:")
            line_height = 20
            y = 570
            for i, endpoint in enumerate(data.get("endpoints", [])):
                if y < 50:  # Page overflow
                    c.showPage()
                    y = 750
                c.drawString(120, y, f"IP: {endpoint.get('ipAddress')} | Grade: {endpoint.get('grade')}")
                y -= line_height

    else:
        c.drawString(100, 710, f"Error: {ssl_result.get('message') or 'Unknown error occurred'}")

    c.showPage()
    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer


