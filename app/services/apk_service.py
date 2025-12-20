# import os
# import tempfile
# import zipfile
# import subprocess
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import os

# APKTOOL_PATH = r"C:/Users/HP/Documents/apktool/apktool.bat"  # Path to Apktool



# def process_apk(file_path: str) -> dict:
#     """
#     Process the APK or APKM file using Apktool to extract manifest, permissions, and metadata.
#     """
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"File not found: {file_path}")

#     if file_path.endswith(".apkm"):
#         # Extract APKM file into a temporary directory
#         with tempfile.TemporaryDirectory() as extract_dir:
#             with zipfile.ZipFile(file_path, "r") as zip_ref:
#                 zip_ref.extractall(extract_dir)

#             # Find all APK files in the extracted directory
#             apk_files = [
#                 os.path.join(extract_dir, f)
#                 for f in os.listdir(extract_dir)
#                 if f.endswith(".apk")
#             ]

#             if not apk_files:
#                 raise RuntimeError("No APK files found in the APKM archive.")

#             # Process each APK file
#             results = [process_individual_apk(apk_file) for apk_file in apk_files]

#             # Combine results from all APKs
#             combined_results = {
#             "manifests": [r["manifest"] for r in results],
#             "permissions": list(
#                 set(perm for r in results for perm in r["permissions"])
#             ),
#             "metadata": [r["metadata"] for r in results],  # Store metadata from all APKs
#         }

#             return combined_results

#     elif file_path.endswith(".apk"):
#         # Process a single APK file
#         return process_individual_apk(file_path)

#     else:
#         raise ValueError("Unsupported file format. Only .apk and .apkm files are supported.")



# def process_individual_apk(apk_path: str) -> dict:
#     """
#     Process an APK file using Apktool to extract metadata.
#     """
#     with tempfile.TemporaryDirectory() as output_dir:
#         # Get absolute paths and ensure they are quoted
#         apk_path = os.path.abspath(apk_path)
#         output_dir = os.path.abspath(os.path.join("extracted", os.path.basename(apk_path).replace(".apk", "")))
        
#         # Create the directory if it doesn't exist
#         os.makedirs(output_dir, exist_ok=True)

#         # Build Apktool command with proper quoting
#         apktool_command = [
#             "java",
#             "-jar",
#             "C:/Users/HP/Documents/apktool/apktool.jar",  # Path to the jar file
#             "d",
#             apk_path,
#             "-o",
#             output_dir,
#             "--no-src",
#             "-f",
#         ]


#         try:
#             print(f"Running Apktool command: {subprocess.list2cmdline(apktool_command)}")  # Debugging
#             result = subprocess.run(
#                 apktool_command,
#                 capture_output=True,
#                 text=True,
#                 check=True,
#                 shell=False,  # Disable shell for better argument handling
#             )

#             # Log the Apktool output for debugging
#             print(f"Apktool stdout: {result.stdout}")
#             print(f"Apktool stderr: {result.stderr}")

#         except subprocess.CalledProcessError as e:
#             print(f"Command failed with exit code {e.returncode}")
#             print(f"Error output: {e.stderr}")
#             raise RuntimeError(f"Apktool failed to process APK: {apk_path}")

#         # Validate output
#         manifest_path = os.path.join(output_dir, "AndroidManifest.xml")
#         if not os.path.exists(manifest_path):
#             raise FileNotFoundError("AndroidManifest.xml not found in the decompiled output.")

#         # Read the manifest
#         with open(manifest_path, "r", encoding="utf-8") as manifest_file:
#             manifest_content = manifest_file.read()

#         # Example: Parse permissions and metadata (dummy function, replace as needed)
#         permissions, metadata = parse_manifest(manifest_path)

#         return {
#             "manifest": manifest_content,
#             "permissions": permissions,
#             "metadata": metadata,
#         }


# def parse_manifest(manifest_path: str) -> tuple:
#     """
#     Parse AndroidManifest.xml to extract permissions and metadata.
#     """
#     import xml.etree.ElementTree as ET

#     tree = ET.parse(manifest_path)
#     root = tree.getroot()

#     permissions = [
#         elem.attrib["{http://schemas.android.com/apk/res/android}name"]
#         for elem in root.findall("uses-permission")
#     ]

#     # Extract versionCode, versionName, platformBuildVersionCode, and platformBuildVersionName
#     version_code = root.attrib.get("{http://schemas.android.com/apk/res/android}versionCode", 
#                                    root.attrib.get("platformBuildVersionCode", "unknown"))
#     version_name = root.attrib.get("{http://schemas.android.com/apk/res/android}versionName", 
#                                    root.attrib.get("platformBuildVersionName", "unknown"))
    
#     metadata = {
#         "package_name": root.attrib.get("package", "unknown"),
#         "version_code": version_code,
#         "version_name": version_name,
#     }

#     return permissions, metadata


# import os
# import tempfile
# import zipfile
# import subprocess
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# import xml.etree.ElementTree as ET

# APKTOOL_PATH = r"C:/Users/HP/Documents/apktool/apktool.bat"  # Path to Apktool

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# import html

# def generate_pdf_from_apk_info(apk_info: dict, output_pdf_path: str):
#     """
#     Generate a PDF with the extracted APK information (manifest, permissions, metadata).
#     """
#     # Create the PDF document
#     doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    
#     # Get the default stylesheet
#     styles = getSampleStyleSheet()
    
#     # Create an empty list to store elements (like Paragraphs)
#     elements = []
    
#     # Title of the document
#     title = Paragraph("<b>APK Analysis Report</b>", styles["Title"])
#     elements.append(title)

#     # Metadata section
#     metadata = apk_info.get("metadata", {})
#     elements.append(Paragraph(f"<b>Package Name:</b> {metadata.get('package_name', 'N/A')}", styles["Normal"]))
#     elements.append(Paragraph(f"<b>Version Code:</b> {metadata.get('version_code', 'N/A')}", styles["Normal"]))
#     elements.append(Paragraph(f"<b>Version Name:</b> {metadata.get('version_name', 'N/A')}", styles["Normal"]))
    
#     # Permissions section
#     permissions = apk_info.get("permissions", [])
#     elements.append(Paragraph("<b>Permissions:</b>", styles["Normal"]))
#     for permission in permissions:
#         elements.append(Paragraph(f"- {permission}", styles["Normal"]))
    
#     # Manifest section (use Paragraph to wrap text)
#     manifest_content = apk_info.get("manifest", "")
    
#     # Escape XML characters for proper display in PDF
#     manifest_content = html.escape(manifest_content)  # This will escape characters like <, >, &, etc.
    
#     # Add manifest as preformatted text
#     elements.append(Paragraph("<b>Android Manifest:</b>", styles["Normal"]))
#     elements.append(Paragraph(f"<pre>{manifest_content}</pre>", styles["Normal"]))

#     # Build the PDF
#     doc.build(elements)
#     print(f"PDF saved to {output_pdf_path}")

# def process_individual_apk(apk_path: str) -> dict:
#     """
#     Process an APK file using Apktool to extract metadata.
#     """
#     with tempfile.TemporaryDirectory() as output_dir:
#         # Get absolute paths and ensure they are quoted
#         apk_path = os.path.abspath(apk_path)
#         output_dir = os.path.abspath(os.path.join("extracted", os.path.basename(apk_path).replace(".apk", "")))
        
#         # Create the directory if it doesn't exist
#         os.makedirs(output_dir, exist_ok=True)

#         # Build Apktool command with proper quoting
#         apktool_command = [
#             "java",
#             "-jar",
#             "C:/Users/HP/Documents/apktool/apktool.jar",  # Path to the jar file
#             "d",
#             apk_path,
#             "-o",
#             output_dir,
#             "--no-src",
#             "-f",
#         ]


#         try:
#             print(f"Running Apktool command: {subprocess.list2cmdline(apktool_command)}")  # Debugging
#             result = subprocess.run(
#                 apktool_command,
#                 capture_output=True,
#                 text=True,
#                 check=True,
#                 shell=False,  # Disable shell for better argument handling
#             )

#             # Log the Apktool output for debugging
#             print(f"Apktool stdout: {result.stdout}")
#             print(f"Apktool stderr: {result.stderr}")

#         except subprocess.CalledProcessError as e:
#             print(f"Command failed with exit code {e.returncode}")
#             print(f"Error output: {e.stderr}")
#             raise RuntimeError(f"Apktool failed to process APK: {apk_path}")

#         # Validate output
#         manifest_path = os.path.join(output_dir, "AndroidManifest.xml")
#         if not os.path.exists(manifest_path):
#             raise FileNotFoundError("AndroidManifest.xml not found in the decompiled output.")

#         # Read the manifest
#         with open(manifest_path, "r", encoding="utf-8") as manifest_file:
#             manifest_content = manifest_file.read()

#         # Example: Parse permissions and metadata (dummy function, replace as needed)
#         permissions, metadata = parse_manifest(manifest_path)

#         return {
#             "manifest": manifest_content,
#             "permissions": permissions,
#             "metadata": metadata,
#         }
    
# def parse_manifest(manifest_path: str) -> tuple:
#     """
#     Parse AndroidManifest.xml to extract permissions and metadata.
#     """
#     import xml.etree.ElementTree as ET

#     tree = ET.parse(manifest_path)
#     root = tree.getroot()

#     permissions = [
#         elem.attrib["{http://schemas.android.com/apk/res/android}name"]
#         for elem in root.findall("uses-permission")
#     ]

#     # Extract versionCode, versionName, platformBuildVersionCode, and platformBuildVersionName
#     version_code = root.attrib.get("{http://schemas.android.com/apk/res/android}versionCode", 
#                                    root.attrib.get("platformBuildVersionCode", "unknown"))
#     version_name = root.attrib.get("{http://schemas.android.com/apk/res/android}versionName", 
#                                    root.attrib.get("platformBuildVersionName", "unknown"))
    
#     metadata = {
#         "package_name": root.attrib.get("package", "unknown"),
#         "version_code": version_code,
#         "version_name": version_name,
#     }

#     return permissions, metadata


# def process_apk(file_path: str) -> dict:
#     """
#     Process the APK or APKM file using Apktool to extract manifest, permissions, and metadata.
#     """
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"File not found: {file_path}")

#     if file_path.endswith(".apkm"):
#         # Extract APKM file into a temporary directory
#         with tempfile.TemporaryDirectory() as extract_dir:
#             with zipfile.ZipFile(file_path, "r") as zip_ref:
#                 zip_ref.extractall(extract_dir)

#             # Find all APK files in the extracted directory
#             apk_files = [
#                 os.path.join(extract_dir, f)
#                 for f in os.listdir(extract_dir)
#                 if f.endswith(".apk")
#             ]

#             if not apk_files:
#                 raise RuntimeError("No APK files found in the APKM archive.")

#             # Process each APK file
#             results = [process_individual_apk(apk_file) for apk_file in apk_files]

#             # Combine results from all APKs
#             combined_results = {
#                 "manifests": [r["manifest"] for r in results],
#                 "permissions": list(set(perm for r in results for perm in r["permissions"])),
#                 "metadata": [r["metadata"] for r in results],  # Store metadata from all APKs
#             }

#             return combined_results

#     elif file_path.endswith(".apk"):
#         # Process a single APK file
#         return process_individual_apk(file_path)

#     else:
#         raise ValueError("Unsupported file format. Only .apk and .apkm files are supported.")


import os
import tempfile
import zipfile
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import html

APKTOOL_PATH = r"C:/Users/HP/Documents/apktool/apktool.jar"  # Path to Apktool

def generate_pdf_from_apk_info(apk_info: dict, output_pdf_path: str):
    """
    Generate a PDF with the extracted APK information (manifest, permissions, metadata).
    """
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title of the document
    title = Paragraph("<b>APK Analysis Report</b>", styles["Title"])
    elements.append(title)

    # Metadata section
    metadata_list = apk_info.get("metadata", [])
    if isinstance(metadata_list, list):
        for idx, metadata in enumerate(metadata_list):
            elements.append(Paragraph(f"<b>APK {idx + 1}:</b>", styles["Normal"]))
            elements.append(Paragraph(f"<b>Package Name:</b> {metadata.get('package_name', 'N/A')}", styles["Normal"]))
            elements.append(Paragraph(f"<b>Version Code:</b> {metadata.get('version_code', 'N/A')}", styles["Normal"]))
            elements.append(Paragraph(f"<b>Version Name:</b> {metadata.get('version_name', 'N/A')}", styles["Normal"]))
    else:
        elements.append(Paragraph(f"<b>Package Name:</b> {metadata_list.get('package_name', 'N/A')}", styles["Normal"]))
        elements.append(Paragraph(f"<b>Version Code:</b> {metadata_list.get('version_code', 'N/A')}", styles["Normal"]))
        elements.append(Paragraph(f"<b>Version Name:</b> {metadata_list.get('version_name', 'N/A')}", styles["Normal"]))

    # Permissions section
    permissions = apk_info.get("permissions", [])
    elements.append(Paragraph("<b>Permissions:</b>", styles["Normal"]))
    for permission in permissions:
        elements.append(Paragraph(f"- {permission}", styles["Normal"]))

    # Manifest section (use Paragraph to wrap text)
    manifest_content = apk_info.get("manifest", "")
    manifest_content = html.escape(manifest_content)
    elements.append(Paragraph("<b>Android Manifest:</b>", styles["Normal"]))
    elements.append(Paragraph(f"<pre>{manifest_content}</pre>", styles["Normal"]))

    doc.build(elements)
    print(f"PDF saved to {output_pdf_path}")

def process_individual_apk(apk_path: str) -> dict:
    with tempfile.TemporaryDirectory() as output_dir:
        apk_path = os.path.abspath(apk_path)
        output_dir = os.path.abspath(os.path.join("extracted", os.path.basename(apk_path).replace(".apk", "")))
        os.makedirs(output_dir, exist_ok=True)

        apktool_command = [
            "java", "-jar", "C:/Users/HP/Documents/apktool/apktool.jar",
            "d", apk_path, "-o", output_dir, "--no-src", "-f",
        ]

        try:
            print(f"Running Apktool command: {subprocess.list2cmdline(apktool_command)}")
            result = subprocess.run(
                apktool_command,
                capture_output=True,
                text=True,
                check=True,
                shell=False,
            )
            print(f"Apktool stdout: {result.stdout}")
            print(f"Apktool stderr: {result.stderr}")
        except subprocess.CalledProcessError as e:
            print(f"Apktool error: {e.stderr}")
            raise RuntimeError(f"Apktool failed: {e}")

        manifest_path = os.path.join(output_dir, "AndroidManifest.xml")
        if not os.path.exists(manifest_path):
            print("Manifest file not found in decompiled output.")
            return {"manifest": "", "permissions": [], "metadata": {}}

        with open(manifest_path, "r", encoding="utf-8") as manifest_file:
            manifest_content = manifest_file.read()
            print(f"Manifest content extracted: {manifest_content[:500]}")  # Log first 500 chars

        permissions, metadata = parse_manifest(manifest_path)
        return {"manifest": manifest_content, "permissions": permissions, "metadata": metadata}


def parse_manifest(manifest_path: str) -> tuple:
    import xml.etree.ElementTree as ET

    tree = ET.parse(manifest_path)
    root = tree.getroot()

    # Define the Android namespace
    android_ns = "http://schemas.android.com/apk/res/android"
    ET.register_namespace('android', android_ns)

    # Extract permissions
    permissions = [
        elem.attrib[f"{{{android_ns}}}name"]
        for elem in root.findall("uses-permission")
    ]

    # Extract metadata with namespace handling
    version_code = root.attrib.get(f"{{{android_ns}}}versionCode", "unknown")
    version_name = root.attrib.get(f"{{{android_ns}}}versionName", "unknown")

    metadata = {
        "package_name": root.attrib.get("package", "unknown"),
        "version_code": version_code,
        "version_name": version_name,
    }

    return permissions, metadata

def process_apk(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.endswith(".apkm"):
        # Extract APKM file into a temporary directory
        with tempfile.TemporaryDirectory() as extract_dir:
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(extract_dir)

            # Find all APK files in the extracted directory
            apk_files = [
                os.path.join(extract_dir, f)
                for f in os.listdir(extract_dir)
                if f.endswith(".apk")
            ]

            if not apk_files:
                raise RuntimeError("No APK files found in the APKM archive.")

            # Process each APK file
            results = [process_individual_apk(apk_file) for apk_file in apk_files]

            # Combine results from all APKs
            combined_results = {
                "manifests": [r["manifest"] for r in results],
                "permissions": list(set(perm for r in results for perm in r["permissions"])),
                "metadata": results[0]["metadata"] if results else {},  # Take metadata from the first APK
            }

            return combined_results

    elif file_path.endswith(".apk"):
        # Process a single APK file
        return process_individual_apk(file_path)

    else:
        raise ValueError("Unsupported file format. Only .apk and .apkm files are supported.")
