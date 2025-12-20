# import os
# import subprocess
# import re
# import zipfile
# from androguard.misc import AnalyzeAPK

# BAKSMALI_PATH = "C:/Users/HP/Documents/SPL3/tools/baksmali-2.5.2.jar"  # Update path if needed


# def disassemble_apk(apk_path: str, output_dir: str) -> str:
#     """
#     Disassemble an APK into Smali code using Baksmali.
#     """
#     try:
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)

#         # Run Baksmali to disassemble the APK
#         cmd = ["java", "-jar", BAKSMALI_PATH, "disassemble", apk_path, "-o", output_dir]
#         subprocess.run(cmd, check=True)
#         return output_dir
#     except Exception as e:
#         raise RuntimeError(f"Failed to disassemble APK: {str(e)}")


# def detect_libraries(smali_dir: str) -> dict:
#     """
#     Detect cryptography and dangerous libraries using regex and pattern matching.
#     """
#     detected_libraries = {"cryptography": [], "networking": [], "dangerous": []}
#     crypto_patterns = [r"javax\.crypto", r"java\.security", r"org\.bouncycastle"]
#     dangerous_patterns = [r"com\.example\.dangerouslib", r"maliciouslib"]

#     try:
#         for root, _, files in os.walk(smali_dir):
#             for file in files:
#                 if file.endswith(".smali"):
#                     file_path = os.path.join(root, file)
#                     with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#                         content = f.read()

#                         # Match cryptography libraries
#                         for pattern in crypto_patterns:
#                             if re.search(pattern, content):
#                                 detected_libraries["cryptography"].append(file_path)

#                         # Match networking libraries
#                         if "http" in content or "socket" in content:
#                             detected_libraries["networking"].append(file_path)

#                         # Match dangerous libraries
#                         for pattern in dangerous_patterns:
#                             if re.search(pattern, content):
#                                 detected_libraries["dangerous"].append(file_path)
#     except Exception as e:
#         raise RuntimeError(f"Error during library detection: {str(e)}")

#     return detected_libraries


# def trace_lifecycle(apk_path: str) -> dict:
#     """
#     Perform control flow analysis for lifecycle methods like onCreate and data handling.
#     """
#     lifecycle_methods = {"onCreate": [], "onStart": [], "registration": [], "login": [], "money_transfer": []}
#     try:
#         a, d, dx = AnalyzeAPK(apk_path)

#         for method in dx.get_methods():
#             method_name = method.name
#             if "onCreate" in method_name:
#                 lifecycle_methods["onCreate"].append(method.full_name)
#             elif "onStart" in method_name:
#                 lifecycle_methods["onStart"].append(method.full_name)
#             elif "register" in method_name.lower():
#                 lifecycle_methods["registration"].append(method.full_name)
#             elif "login" in method_name.lower():
#                 lifecycle_methods["login"].append(method.full_name)
#             elif "transfer" in method_name.lower() or "money" in method_name.lower():
#                 lifecycle_methods["money_transfer"].append(method.full_name)
#     except Exception as e:
#         raise RuntimeError(f"Error during lifecycle tracing: {str(e)}")

#     return lifecycle_methods


# def extract_apks_from_apkm(apkm_path: str) -> list:
#     """
#     Extract APK files from an APKM file.
#     """
#     extracted_dir = os.path.join("extracted_apks", os.path.basename(apkm_path).replace(".apkm", ""))
#     os.makedirs(extracted_dir, exist_ok=True)
#     extracted_apks = []

#     try:
#         with zipfile.ZipFile(apkm_path, "r") as zip_ref:
#             zip_ref.extractall(extracted_dir)

#         # Find all APK files in the extracted directory
#         for root, _, files in os.walk(extracted_dir):
#             for file in files:
#                 if file.endswith(".apk"):
#                     extracted_apks.append(os.path.join(root, file))
#     except Exception as e:
#         raise RuntimeError(f"Failed to extract APKs from APKM: {str(e)}")

#     return extracted_apks


# def perform_manual_analysis(file_path: str) -> dict:
#     """
#     Main function to perform all manual analysis automation tasks.
#     Handles both APK and APKM files.
#     """
#     results = {}
#     apk_files = []

#     try:
#         # Step 1: Handle APKM files
#         if file_path.lower().endswith(".apkm"):
#             apk_files = extract_apks_from_apkm(file_path)
#             if not apk_files:
#                 raise RuntimeError("No APKs found in the APKM file.")
#         else:
#             apk_files = [file_path]

#         # Step 2: Analyze each APK
#         for apk_path in apk_files:
#             apk_name = os.path.basename(apk_path)
#             disassembled_dir = os.path.join("disassembled_code", apk_name)

#             try:
#                 # Disassemble APK
#                 smali_dir = disassemble_apk(apk_path, disassembled_dir)

#                 # Detect Libraries
#                 libraries = detect_libraries(smali_dir)

#                 # Trace Lifecycle
#                 lifecycle = trace_lifecycle(apk_path)

#                 results[apk_name] = {"libraries": libraries, "lifecycle": lifecycle}

#             except Exception as e:
#                 results[apk_name] = {"error": str(e)}

#     except Exception as e:
#         raise RuntimeError(f"Error during manual analysis: {str(e)}")

#     return results

import os
import subprocess
import re
import zipfile
from androguard.misc import AnalyzeAPK
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import html

BAKSMALI_PATH = "C:/Users/HP/Documents/SPL3/tools/baksmali-2.5.2.jar"  # Update path if needed


def disassemble_apk(apk_path: str, output_dir: str) -> str:
    """
    Disassemble an APK into Smali code using Baksmali.
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Run Baksmali to disassemble the APK
        cmd = ["java", "-jar", BAKSMALI_PATH, "disassemble", apk_path, "-o", output_dir]
        subprocess.run(cmd, check=True)
        return output_dir
    except Exception as e:
        raise RuntimeError(f"Failed to disassemble APK: {str(e)}")


def detect_libraries(smali_dir: str) -> dict:
    """
    Detect cryptography and dangerous libraries using regex and pattern matching.
    """
    detected_libraries = {"cryptography": [], "networking": [], "dangerous": []}
    crypto_patterns = [r"javax\\.crypto", r"java\\.security", r"org\\.bouncycastle"]
    dangerous_patterns = [r"com\\.example\\.dangerouslib", r"maliciouslib"]

    try:
        for root, _, files in os.walk(smali_dir):
            for file in files:
                if file.endswith(".smali"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                        # Match cryptography libraries
                        for pattern in crypto_patterns:
                            if re.search(pattern, content):
                                detected_libraries["cryptography"].append(file_path)

                        # Match networking libraries
                        if "http" in content or "socket" in content:
                            detected_libraries["networking"].append(file_path)

                        # Match dangerous libraries
                        for pattern in dangerous_patterns:
                            if re.search(pattern, content):
                                detected_libraries["dangerous"].append(file_path)
    except Exception as e:
        raise RuntimeError(f"Error during library detection: {str(e)}")

    return detected_libraries


def trace_lifecycle(apk_path: str) -> dict:
    """
    Perform control flow analysis for lifecycle methods like onCreate and data handling.
    """
    lifecycle_methods = {"onCreate": [], "onStart": [], "registration": [], "login": [], "money_transfer": []}
    try:
        a, d, dx = AnalyzeAPK(apk_path)

        for method in dx.get_methods():
            method_name = method.name
            if "onCreate" in method_name:
                lifecycle_methods["onCreate"].append(method.full_name)
            elif "onStart" in method_name:
                lifecycle_methods["onStart"].append(method.full_name)
            elif "register" in method_name.lower():
                lifecycle_methods["registration"].append(method.full_name)
            elif "login" in method_name.lower():
                lifecycle_methods["login"].append(method.full_name)
            elif "transfer" in method_name.lower() or "money" in method_name.lower():
                lifecycle_methods["money_transfer"].append(method.full_name)
    except Exception as e:
        raise RuntimeError(f"Error during lifecycle tracing: {str(e)}")

    return lifecycle_methods


def extract_apks_from_apkm(apkm_path: str) -> list:
    """
    Extract APK files from an APKM file.
    """
    extracted_dir = os.path.join("extracted_apks", os.path.basename(apkm_path).replace(".apkm", ""))
    os.makedirs(extracted_dir, exist_ok=True)
    extracted_apks = []

    try:
        with zipfile.ZipFile(apkm_path, "r") as zip_ref:
            zip_ref.extractall(extracted_dir)

        # Find all APK files in the extracted directory
        for root, _, files in os.walk(extracted_dir):
            for file in files:
                if file.endswith(".apk"):
                    extracted_apks.append(os.path.join(root, file))
    except Exception as e:
        raise RuntimeError(f"Failed to extract APKs from APKM: {str(e)}")

    return extracted_apks


def generate_manual_analysis_pdf(analysis_results: dict, output_pdf_path: str):
    """
    Generate a PDF report summarizing the manual analysis results.
    """
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("<b>Manual Analysis Report</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Iterate through APK analysis results
    for apk_name, results in analysis_results.items():
        elements.append(Paragraph(f"<b>APK: {apk_name}</b>", styles["Heading2"]))
        elements.append(Spacer(1, 6))

        if "error" in results:
            # If there was an error during analysis
            elements.append(Paragraph(f"<b>Error:</b> {html.escape(results['error'])}", styles["Normal"]))
        else:
            # Libraries Section
            libraries = results.get("libraries", {})
            elements.append(Paragraph("<b>Libraries Detected:</b>", styles["Heading3"]))
            elements.append(Spacer(1, 6))

            for category, files in libraries.items():
                elements.append(Paragraph(f"<b>{category.capitalize()}:</b> {len(files)} occurrences", styles["Normal"]))
                for file in files:
                    elements.append(Paragraph(f"- {html.escape(file)}", styles["Normal"]))
                elements.append(Spacer(1, 6))

            # Lifecycle Section
            lifecycle = results.get("lifecycle", {})
            elements.append(Paragraph("<b>Lifecycle Methods:</b>", styles["Heading3"]))
            elements.append(Spacer(1, 6))

            for method_type, methods in lifecycle.items():
                elements.append(Paragraph(f"<b>{method_type.capitalize()}:</b> {len(methods)} methods", styles["Normal"]))
                for method in methods:
                    elements.append(Paragraph(f"- {html.escape(method)}", styles["Normal"]))
                elements.append(Spacer(1, 6))

        elements.append(Spacer(1, 12))  # Add spacing after each APK
        elements.append(PageBreak())  # Page break for the next APK

    try:
        doc.build(elements)
    except Exception as e:
        raise RuntimeError(f"Error generating PDF: {str(e)}")


def perform_manual_analysis(file_path: str) -> dict:
    """
    Main function to perform all manual analysis automation tasks.
    Handles both APK and APKM files.
    """
    results = {}
    apk_files = []

    try:
        # Step 1: Handle APKM files
        if file_path.lower().endswith(".apkm"):
            apk_files = extract_apks_from_apkm(file_path)
            if not apk_files:
                raise RuntimeError("No APKs found in the APKM file.")
        else:
            apk_files = [file_path]

        # Step 2: Analyze each APK
        for apk_path in apk_files:
            apk_name = os.path.basename(apk_path)
            disassembled_dir = os.path.join("disassembled_code", apk_name)

            try:
                # Disassemble APK
                smali_dir = disassemble_apk(apk_path, disassembled_dir)

                # Detect Libraries
                libraries = detect_libraries(smali_dir)

                # Trace Lifecycle
                lifecycle = trace_lifecycle(apk_path)

                results[apk_name] = {"libraries": libraries, "lifecycle": lifecycle}

            except Exception as e:
                results[apk_name] = {"error": str(e)}

    except Exception as e:
        raise RuntimeError(f"Error during manual analysis: {str(e)}")

    return results
