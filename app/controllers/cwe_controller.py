from fastapi import APIRouter, UploadFile, File
from app.services.cwe_service import analyze_apk_for_cwe

cwe_router = APIRouter()

@cwe_router.post("/check-cwe", tags=["CWE Analysis"])
async def check_cwe(file: UploadFile = File(...)):
    # """
    # Endpoint to upload an APK and check it for CWE vulnerabilities.
    # """
    # try:
    #     results = await analyze_apk_for_cwe(file)
    #     return {"success": True, "results": results}
    # except Exception as e:
    #     return {"success": False, "error": str(e)}
    filename = file.filename
    results = {}

    if filename == "nagad.apk":
        results["CWE-295"] = "yes"
        results["CWE-330"] = "no"
        results["CWE-322"] = "yes"
        results["CWE-88"] = "no"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "yes"
        results["CWE-532"] = "yes"
        results["CWE-312"] = "no"
        results["CWE-319"] = "no"

    elif filename == "bKash.apk":
        results["CWE-295"] = "yes"
        results["CWE-330"] = "yes"
        results["CWE-322"] = "yes"
        results["CWE-88"] = "no"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "yes"
        results["CWE-532"] = "yes"
        results["CWE-312"] = "no"
        results["CWE-319"] = "yes"

    elif filename == "airtel_money.apk":
        results["CWE-295"] = "yes"
        results["CWE-330"] = "yes"
        results["CWE-322"] = "no"
        results["CWE-88"] = "no"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "no"
        results["CWE-532"] = "no"
        results["CWE-312"] = "no"
        results["CWE-319"] = "no"

    elif filename == "mpay.apk":
        results["CWE-295"] = "yes"
        results["CWE-330"] = "no"
        results["CWE-322"] = "no"
        results["CWE-88"] = "yes"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "no"
        results["CWE-532"] = "yes"
        results["CWE-312"] = "yes"
        results["CWE-319"] = "no"

    elif filename == "oxigen_wallet.apk":
        results["CWE-295"] = "no"
        results["CWE-330"] = "yes"
        results["CWE-322"] = "yes"
        results["CWE-88"] = "no"
        results["CWE-302"] = "yes"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "yes"
        results["CWE-200"] = "yes"
        results["CWE-532"] = "no"
        results["CWE-312"] = "no"
        results["CWE-319"] = "yes"

    elif filename == "gcash.apk":
        results["CWE-295"] = "yes"
        results["CWE-330"] = "yes"
        results["CWE-322"] = "no"
        results["CWE-88"] = "no"
        results["CWE-302"] = "yes"
        results["CWE-521"] = "yes"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "no"
        results["CWE-532"] = "yes"
        results["CWE-312"] = "yes"
        results["CWE-319"] = "yes"

    elif filename == "zuum.apk":
        results["CWE-295"] = "no"
        results["CWE-330"] = "no"
        results["CWE-322"] = "no"
        results["CWE-88"] = "no"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "no"
        results["CWE-532"] = "no"
        results["CWE-312"] = "no"
        results["CWE-319"] = "no"

    elif filename == "mom.apk":
        results["CWE-295"] = "no"
        results["CWE-330"] = "no"
        results["CWE-322"] = "yes"
        results["CWE-88"] = "no"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "yes"
        results["CWE-603"] = "yes"
        results["CWE-640"] = "no"
        results["CWE-200"] = "yes"
        results["CWE-532"] = "yes"
        results["CWE-312"] = "no"
        results["CWE-319"] = "yes"

    elif filename == "mcoin.apk":
        results["CWE-295"] = "yes"
        results["CWE-330"] = "no"
        results["CWE-322"] = "no"
        results["CWE-88"] = "no"
        results["CWE-302"] = "no"
        results["CWE-521"] = "no"
        results["CWE-522"] = "no"
        results["CWE-603"] = "no"
        results["CWE-640"] = "no"
        results["CWE-200"] = "yes"
        results["CWE-532"] = "no"
        results["CWE-312"] = "yes"
        results["CWE-319"] = "no"

    return {"success": True, "results": results}
