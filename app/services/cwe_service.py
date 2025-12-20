import os
import tempfile
from app.utils.cwe_checker import check_apk

async def analyze_apk_for_cwe(file):
    """
    Analyze an uploaded APK file for CWE vulnerabilities.
    """
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".apk") as tmp_file:
            tmp_file.write(await file.read())
            tmp_file_path = tmp_file.name  # Save the temporary file path

        # Perform CWE checks
        results = check_apk(tmp_file_path)

        return results
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        # Ensure the file is deleted after processing
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
