import os
import re
from androguard.misc import AnalyzeAPK

def detect_sensitive_data_leakage(apk_path: str) -> dict:
    """
    Detect sensitive data leakage such as financial or personal information
    being exposed through insecure channels or logging.
    """
    try:
        a, d, dx = AnalyzeAPK(apk_path)
        
        leakage_issues = []

        # Search for potentially sensitive data leakage points
        for method in dx.get_methods():
            method_name = method.name.lower()
            class_name = method.class_name
            full_method_name = f"{class_name}->{method_name}"

            instructions = []
            for block in method.get_basic_blocks():
                instructions.extend(block.get_instructions())

            instruction_text = " ".join(instr.get_output() for instr in instructions)

            # Detect potential leakage of sensitive data
            if re.search(r"(getsharedpreferences|getexternalstorage|writeexternalstorage|log|http)", instruction_text):
                leakage_issues.append(full_method_name)

        return {
            "leakage_issues": leakage_issues,
        }
    except Exception as e:
        raise RuntimeError(f"Error during sensitive data leakage detection: {str(e)}")
