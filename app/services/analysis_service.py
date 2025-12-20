import os
from app.utils.androguard_analysis import perform_static_analysis

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import html

def generate_pdf_from_analysis(analysis_results: dict, output_pdf_path: str):
    """
    Generate a PDF with the results of the static analysis with proper styling and multi-page support.
    """
    # Create the PDF document
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    
    # Get the default stylesheet
    styles = getSampleStyleSheet()
    
    # List to store PDF elements
    elements = []

    # Title of the document
    title = Paragraph("<b>APK Static Analysis Report</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Add sections dynamically
    sections = [
        ("SSL/TLS Misconfigurations", analysis_results.get("ssl_tls_issues", []), ["method", "class", "description"]),
        ("Cryptographic Misuse", analysis_results.get("crypto_issues", []), ["method", "class", "description"]),
        ("Access Control Issues", analysis_results.get("access_control_issues", []), ["component", "type", "description"]),
    ]

    for section_title, issues, keys in sections:
        # Skip empty sections
        if not issues:
            continue

        # Add section title
        elements.append(Paragraph(f"<b>{section_title}</b>", styles["Heading2"]))
        elements.append(Spacer(1, 6))

        # Add issues within the section
        for issue in issues:
            for key in keys:
                value = html.escape(issue.get(key, "N/A"))  # Escape HTML special characters
                elements.append(Paragraph(f"<b>{key.capitalize()}:</b> {value}", styles["Normal"]))
            elements.append(Spacer(1, 6))  # Add spacing between issues

        elements.append(Spacer(1, 12))  # Add spacing after the section

    # Add a page break if needed
    elements.append(PageBreak())

    # Build the PDF
    try:
        doc.build(elements)
        print(f"PDF saved to {output_pdf_path}")
    except Exception as e:
        print(f"Error generating PDF: {e}")


def process_static_analysis(file_path: str) -> dict:
    """
    Perform custom static analysis on the given APK file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    print(f"Performing static analysis on {file_path}")
    analysis_results = perform_static_analysis(file_path)
    
    return analysis_results
