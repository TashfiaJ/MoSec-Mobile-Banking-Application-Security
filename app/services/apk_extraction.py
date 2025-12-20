import subprocess

def extract_apk(apk_path):
    try:
        # Use apktool to extract the APK
        subprocess.run(["apktool", "d", apk_path, "-o", "/tmp/apk_output"], check=True)
        return {"status": "success", "message": "APK extracted successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
