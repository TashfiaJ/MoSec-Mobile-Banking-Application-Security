# # import re
# # import requests
# # import time
# # from androguard.misc import AnalyzeAPK

# # def extract_urls_from_apk(dx) -> list:
# #     """
# #     Extract URLs from the APK using Androguard.
# #     """
# #     url_pattern = re.compile(r"https?://[^\s]+")
# #     urls = set()

# #     # Iterate over string references in the APK
# #     for string_analysis in dx.get_strings():
# #         try:
# #             # Extract the actual string
# #             string_value = str(string_analysis)
# #             if url_pattern.match(string_value):
# #                 urls.add(string_value)
# #         except Exception as e:
# #             print(f"Error processing string: {e}")

# #     return list(urls)



# # def test_ssl_tls_endpoint(url: str) -> dict:
# #     """
# #     Test SSL/TLS configuration of a remote endpoint using Qualys SSL Labs API.
# #     """
# #     api_url = "https://api.ssllabs.com/api/v3/analyze"
# #     params = {
# #         "host": url,
# #         "publish": "off",
# #         "startNew": "on",
# #         "all": "done"
# #     }

# #     try:
# #         # Initial request to start the test
# #         response = requests.get(api_url, params=params)
# #         response.raise_for_status()
# #         analysis = response.json()

# #         # Poll the API for results
# #         while analysis.get("status") not in ("READY", "ERROR"):
# #             time.sleep(10)  # Wait for 10 seconds before re-checking
# #             response = requests.get(api_url, params={"host": url})
# #             response.raise_for_status()
# #             analysis = response.json()

# #         return analysis

# #     except Exception as e:
# #         print(f"Error testing endpoint {url}: {e}")
# #         return {"error": str(e)}


# # def perform_ssl_tls_testing(apk_path: str) -> dict:
# #     """
# #     Perform SSL/TLS server testing for URLs extracted from the APK.
# #     """
# #     a, d, dx = AnalyzeAPK(apk_path)
# #     urls = extract_urls_from_apk(dx)
# #     ssl_results = []

# #     for url in urls:
# #         # Extract domain from the URL
# #         domain_match = re.search(r"https?://([^/]+)", url)
# #         if domain_match:
# #             domain = domain_match.group(1)
# #             result = test_ssl_tls_endpoint(domain)
# #             ssl_results.append({
# #                 "url": url,
# #                 "domain": domain,
# #                 "result": result
# #             })

# #     return ssl_results


# # import re
# # import requests
# # import time
# # from androguard.misc import AnalyzeAPK
# # import os
# # import zipfile

# # def extract_urls_from_apk(dx) -> list:
# #     """
# #     Extract URLs from the APK using Androguard.
# #     """
# #     url_pattern = re.compile(r"https?://[^\s]+")
# #     urls = set()

# #     # Iterate over string references in the APK
# #     for string_analysis in dx.get_strings():
# #         try:
# #             # Extract the actual string
# #             string_value = str(string_analysis)
# #             if url_pattern.match(string_value):
# #                 urls.add(string_value)
# #         except Exception as e:
# #             print(f"Error processing string: {e}")

# #     return list(urls)


# # def test_ssl_tls_endpoint(url: str) -> dict:
# #     """
# #     Test SSL/TLS configuration of a remote endpoint using Qualys SSL Labs API.
# #     """
# #     api_url = "https://api.ssllabs.com/api/v3/analyze"
# #     params = {
# #         "host": url,
# #         "publish": "off",
# #         "startNew": "on",
# #         "all": "done"
# #     }

# #     try:
# #         # Initial request to start the test
# #         response = requests.get(api_url, params=params)
# #         response.raise_for_status()
# #         analysis = response.json()

# #         # Poll the API for results
# #         while analysis.get("status") not in ("READY", "ERROR"):
# #             time.sleep(10)  # Wait for 10 seconds before re-checking
# #             response = requests.get(api_url, params={"host": url})
# #             response.raise_for_status()
# #             analysis = response.json()

# #         return analysis

# #     except Exception as e:
# #         print(f"Error testing endpoint {url}: {e}")
# #         return {"error": str(e)}


# # def perform_ssl_tls_testing(apk_path: str) -> list:
# #     """
# #     Perform SSL/TLS server testing for URLs extracted from the APK.
# #     """
# #     a, d, dx = AnalyzeAPK(apk_path)
# #     urls = extract_urls_from_apk(dx)
# #     ssl_results = []

# #     for url in urls:
# #         # Extract domain from the URL
# #         domain_match = re.search(r"https?://([^/]+)", url)
# #         if domain_match:
# #             domain = domain_match.group(1)
# #             result = test_ssl_tls_endpoint(domain)
# #             ssl_results.append({
# #                 "url": url,
# #                 "domain": domain,
# #                 "result": result
# #             })

# #     return ssl_results


# # def extract_apks_from_apkm(apkm_path: str) -> list:
# #     """
# #     Extract APK files from an APKM file.
# #     """
# #     extracted_dir = os.path.join("extracted_apks", os.path.basename(apkm_path).replace(".apkm", ""))
# #     os.makedirs(extracted_dir, exist_ok=True)
# #     extracted_apks = []

# #     try:
# #         with zipfile.ZipFile(apkm_path, 'r') as zip_ref:
# #             zip_ref.extractall(extracted_dir)

# #         # Find all APK files in the extracted directory
# #         for root, _, files in os.walk(extracted_dir):
# #             for file in files:
# #                 if file.endswith(".apk"):
# #                     extracted_apks.append(os.path.join(root, file))

# #     except Exception as e:
# #         print(f"Error extracting APKs from APKM: {e}")

# #     return extracted_apks

# import requests
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import subprocess
# import os
# import re

# async def extract_endpoints_from_apk(file_path: str) -> list:
#     """
#     Extracts endpoints (e.g., URLs) from an APK file by decompiling it and searching for URL patterns.
    
#     Args:
#         file_path (str): Path to the APK file.

#     Returns:
#         list: A list of unique endpoints (URLs) found in the APK file.
#     """
#     # Directory for decompiled APK contents
#     decompiled_dir = f"{file_path}_decompiled"
    
#     try:
#         # Step 1: Decompile the APK using apktool
#         apktool_command = [
#             "java", "-jar", "C:/Users/HP/Documents/apktool/apktool.jar",  # Use the correct path to your apktool
#             "d", file_path, "-o", decompiled_dir, "-f"
#         ]

#         # Running the APKTool command to decompile the APK
#         subprocess.run(apktool_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         # Step 2: Search for endpoints in the decompiled files
#         url_pattern = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")

#         endpoints = set()

#         # Walk through the decompiled directory and search for URLs
#         for root, _, files in os.walk(decompiled_dir):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 try:
#                     with open(file_path, "r", encoding="utf-8") as f:
#                         content = f.read()
#                         matches = url_pattern.findall(content)
#                         endpoints.update(matches)
#                 except (UnicodeDecodeError, FileNotFoundError):
#                     # Skip files that cannot be read
#                     continue

#         # Return unique endpoints
#         return list(endpoints)

#     except subprocess.CalledProcessError as e:
#         raise RuntimeError(f"Failed to decompile APK: {e.stderr.decode('utf-8')}") from e

#     finally:
#         # Clean up the decompiled directory if it exists
#         if os.path.exists(decompiled_dir):
#             subprocess.run(["rm", "-rf", decompiled_dir], check=True)


# async def analyze_ssl_tls_endpoints(endpoints: list) -> list:
#     """
#     Analyze the SSL/TLS configuration of endpoints using an external API.
#     """
#     results = []
#     for endpoint in endpoints:
#         try:
#             response = requests.get(f"https://api.ssllabs.com/api/v4/analyze?host={endpoint}", timeout=30)
#             if response.status_code == 200:
#                 results.append({
#                     "endpoint": endpoint,
#                     "grade": response.json().get("endpoints", [{}])[0].get("grade", "Unknown"),
#                     "details": response.json(),
#                 })
#             else:
#                 results.append({
#                     "endpoint": endpoint,
#                     "grade": "Error",
#                     "details": f"Failed to fetch analysis for {endpoint}. HTTP {response.status_code}."
#                 })
#         except Exception as e:
#             results.append({
#                 "endpoint": endpoint,
#                 "grade": "Error",
#                 "details": str(e),
#             })
#     return results

# async def generate_ssl_report(analysis_results: list, output_path: str):
#     """
#     Generate a PDF report for SSL/TLS analysis results using ReportLab.
#     """
#     doc = SimpleDocTemplate(output_path, pagesize=letter)
#     elements = []
#     styles = getSampleStyleSheet()

#     # Title
#     title = Paragraph("SSL/TLS Server Analysis Report", styles["Title"])
#     elements.append(title)

#     # Subtitle
#     subtitle = Paragraph("This report provides an analysis of SSL/TLS configurations for the given endpoints.", styles["BodyText"])
#     elements.append(subtitle)

#     # Spacer
#     from reportlab.platypus import Spacer
#     elements.append(Spacer(1, 12))

#     # Table Data
#     table_data = [["Endpoint", "Grade", "Details"]]
#     for result in analysis_results:
#         endpoint = Paragraph(result["endpoint"], styles["BodyText"])
#         grade = Paragraph(result["grade"], styles["BodyText"])
#         details = Paragraph(
#             str(result["details"]).replace("\n", "").strip()[:500], 
#             styles["BodyText"]
#         )  # Trim details if too long
#         table_data.append([endpoint, grade, details])

#     # Define Table with Column Widths
#     table = Table(table_data, colWidths=[200, 100, 250])  # Adjust widths as needed
#     table.setStyle(TableStyle([
#         ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
#         ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
#         ("ALIGN", (0, 0), (-1, -1), "LEFT"),
#         ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#         ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
#         ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
#         ("GRID", (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     elements.append(table)

#     # Build PDF
#     doc.build(elements)

import httpx
import asyncio

async def perform_ssl_test(url: str) -> dict:
    """
    Perform SSL/TLS server test using Qualys SSL Labs API.
    Returns the test results as a dictionary.
    """
    api_url = "https://api.ssllabs.com/api/v3/analyze"
    params = {
        "host": url,
        "publish": "off",
        "startNew": "on",
        "all": "done",
    }

    async with httpx.AsyncClient() as client:
        try:
            # Start the test
            response = await client.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            # Check the status of the test
            while data.get("status") not in ["READY", "ERROR"]:
                await asyncio.sleep(10)  # Wait for the test to complete
                response = await client.get(api_url, params={"host": url}, timeout=30)
                response.raise_for_status()
                data = response.json()

            # Return the test result
            if data.get("status") == "ERROR":
                return {"error": "SSL test could not be completed", "details": data}

            return data
        except httpx.RequestError as e:
            raise Exception(f"Failed to connect to SSL Labs API: {e}")
