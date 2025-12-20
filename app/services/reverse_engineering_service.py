# import os
# from androguard.misc import AnalyzeAPK
# import re


# def reverse_engineer_apk(apk_path: str) -> dict:
#     """
#     Reverse-engineer the APK and analyze its code for vulnerabilities and lifecycle methods.
#     """
#     try:
#         a, d, dx = AnalyzeAPK(apk_path)

#         vulnerabilities = {
#             "cryptography_issues": [],
#             "certificate_validation_issues": [],
#             "data_leakage": [],
#         }
#         lifecycle_methods = {
#             "registration": [],
#             "authentication": [],
#             "session_management": [],
#             "transaction_processing": [],
#         }

#         # Analyze methods in the app
#         for method in dx.get_methods():
#             method_name = method.name.lower()
#             class_name = method.class_name
#             full_method_name = f"{class_name}->{method_name}"

#             # Get instructions for the method
#             instructions = []
#             for block in method.get_basic_blocks():
#                 instructions.extend(block.get_instructions())

#             # Convert instructions to a searchable string
#             instruction_text = " ".join(instr.get_output() for instr in instructions)

#             # Detect cryptographic vulnerabilities
#             if re.search(r"javax\.crypto|java\.security|org\.bouncycastle", instruction_text):
#                 vulnerabilities["cryptography_issues"].append(full_method_name)

#             # Detect certificate validation vulnerabilities
#             if re.search(r"trustallcerts|allowallhostnames", instruction_text):
#                 vulnerabilities["certificate_validation_issues"].append(full_method_name)

#             # Detect data leakage points
#             if re.search(r"(getsharedpreferences|getexternalstorage|sendbroadcast)", instruction_text):
#                 vulnerabilities["data_leakage"].append(full_method_name)

#             # Trace lifecycle-related methods
#             if "register" in method_name:
#                 lifecycle_methods["registration"].append(full_method_name)
#             elif "login" in method_name or "authenticate" in method_name:
#                 lifecycle_methods["authentication"].append(full_method_name)
#             elif "session" in method_name:
#                 lifecycle_methods["session_management"].append(full_method_name)
#             elif "transfer" in method_name or "payment" in method_name:
#                 lifecycle_methods["transaction_processing"].append(full_method_name)

#         return {
#             "vulnerabilities": vulnerabilities,
#             "lifecycle_methods": lifecycle_methods,
#         }

#     except Exception as e:
#         raise RuntimeError(f"Error during reverse engineering: {str(e)}")


# def perform_reverse_engineering_analysis(apk_paths: list) -> dict:
#     """
#     Perform reverse engineering analysis on multiple APK files and combine results.
#     """
#     combined_results = {}
#     for apk_path in apk_paths:
#         try:
#             combined_results[os.path.basename(apk_path)] = reverse_engineer_apk(apk_path)
#         except Exception as e:
#             combined_results[os.path.basename(apk_path)] = {"error": str(e)}

#     return combined_results

import os
from androguard.misc import AnalyzeAPK
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import re
import html


def reverse_engineer_apk(apk_path: str) -> dict:
    """
    Reverse-engineer the APK and analyze its code for vulnerabilities and lifecycle methods.
    """
    try:
        a, d, dx = AnalyzeAPK(apk_path)

        vulnerabilities = {
            "cryptography_issues": [],
            "certificate_validation_issues": [],
            "data_leakage": [],
        }
        lifecycle_methods = {
            "registration": [],
            "authentication": [],
            "session_management": [],
            "transaction_processing": [],
        }

        # Analyze methods in the app
        for method in dx.get_methods():
            method_name = method.name.lower()
            class_name = method.class_name
            full_method_name = f"{class_name}->{method_name}"

            # Get instructions for the method
            instructions = []
            for block in method.get_basic_blocks():
                instructions.extend(block.get_instructions())

            # Convert instructions to a searchable string
            instruction_text = " ".join(instr.get_output() for instr in instructions)

            # Detect cryptographic vulnerabilities
            if re.search(r"javax\.crypto|java\.security|org\.bouncycastle", instruction_text):
                vulnerabilities["cryptography_issues"].append(full_method_name)

            # Detect certificate validation vulnerabilities
            if re.search(r"trustallcerts|allowallhostnames", instruction_text):
                vulnerabilities["certificate_validation_issues"].append(full_method_name)

            # Detect data leakage points
            if re.search(r"(getsharedpreferences|getexternalstorage|sendbroadcast)", instruction_text):
                vulnerabilities["data_leakage"].append(full_method_name)

            # Trace lifecycle-related methods
            if "register" in method_name:
                lifecycle_methods["registration"].append(full_method_name)
            elif "login" in method_name or "authenticate" in method_name:
                lifecycle_methods["authentication"].append(full_method_name)
            elif "session" in method_name:
                lifecycle_methods["session_management"].append(full_method_name)
            elif "transfer" in method_name or "payment" in method_name:
                lifecycle_methods["transaction_processing"].append(full_method_name)

        return {
            "vulnerabilities": vulnerabilities,
            "lifecycle_methods": lifecycle_methods,
        }

    except Exception as e:
        raise RuntimeError(f"Error during reverse engineering: {str(e)}")


def generate_reverse_engineering_pdf(analysis_results: dict, output_pdf_path: str):
    """
    Generate a PDF report summarizing the reverse engineering analysis results.
    """
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("<b>Reverse Engineering Report</b>", styles["Title"])
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
            # Vulnerabilities Section
            vulnerabilities = results.get("vulnerabilities", {})
            elements.append(Paragraph("<b>Vulnerabilities:</b>", styles["Heading3"]))
            elements.append(Spacer(1, 6))

            for category, methods in vulnerabilities.items():
                elements.append(Paragraph(f"<b>{category.replace('_', ' ').capitalize()}:</b> {len(methods)} issues", styles["Normal"]))
                for method in methods:
                    elements.append(Paragraph(f"- {html.escape(method)}", styles["Normal"]))
                elements.append(Spacer(1, 6))

            # Lifecycle Methods Section
            lifecycle_methods = results.get("lifecycle_methods", {})
            elements.append(Paragraph("<b>Lifecycle Methods:</b>", styles["Heading3"]))
            elements.append(Spacer(1, 6))

            for method_type, methods in lifecycle_methods.items():
                elements.append(Paragraph(f"<b>{method_type.replace('_', ' ').capitalize()}:</b> {len(methods)} methods", styles["Normal"]))
                for method in methods:
                    elements.append(Paragraph(f"- {html.escape(method)}", styles["Normal"]))
                elements.append(Spacer(1, 6))

        elements.append(Spacer(1, 12))  # Add spacing after each APK
        elements.append(PageBreak())  # Page break for the next APK

    try:
        doc.build(elements)
    except Exception as e:
        raise RuntimeError(f"Error generating PDF: {str(e)}")


def perform_reverse_engineering_analysis(apk_paths: list) -> dict:
    """
    Perform reverse engineering analysis on multiple APK files and combine results.
    """
    combined_results = {}
    for apk_path in apk_paths:
        try:
            combined_results[os.path.basename(apk_path)] = reverse_engineer_apk(apk_path)
        except Exception as e:
            combined_results[os.path.basename(apk_path)] = {"error": str(e)}

    return combined_results
