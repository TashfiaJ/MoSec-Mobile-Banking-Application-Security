from androguard.misc import AnalyzeAPK
from xml.dom.minidom import parseString

def analyze_ssl_tls_issues(dx) -> list:
    """
    Detect potential SSL/TLS misconfigurations.
    """
    ssl_issues = []
    patterns = [
        r"Ljavax/net/ssl/.*;",          # Direct SSL API usage
        r"Ljava/security/cert/.*;",     # Certificate handling
        r"Lorg/apache/http/conn/ssl/.*" # Deprecated Apache SSL libraries
    ]

    for pattern in patterns:
        for method in dx.find_methods(classname=pattern):
            ssl_issues.append({
                "method": method.name,
                "class": method.class_name,
                "description": "Potential SSL/TLS misuse detected"
            })
    return ssl_issues


def analyze_crypto_misuse(dx) -> list:
    """
    Detect misuse of cryptographic APIs, such as weak algorithms (DES, MD5, SHA1).
    """
    weak_algos = ["DES", "MD5", "SHA1"]
    crypto_issues = []

    for method in dx.find_methods():
        for algo in weak_algos:
            if algo in method.name or algo in method.class_name:
                crypto_issues.append({
                    "method": method.name,
                    "class": method.class_name,
                    "description": f"Use of weak cryptographic algorithm: {algo}"
                })
    return crypto_issues


def analyze_access_control_issues(a) -> list:
    """
    Analyze exported components for improper access control.
    """
    from lxml import etree

    access_issues = []

    # Get the AndroidManifest.xml as an lxml element
    manifest_xml = a.get_android_manifest_xml()

    if manifest_xml is not None:
        # Use XPath to find all components with "android:exported" set to "true"
        for tag in ["activity", "service", "receiver", "provider"]:
            components = manifest_xml.findall(f".//{tag}", namespaces={'android': 'http://schemas.android.com/apk/res/android'})
            for component in components:
                exported = component.get(f"{{http://schemas.android.com/apk/res/android}}exported")
                name = component.get(f"{{http://schemas.android.com/apk/res/android}}name")
                if exported == "true":
                    access_issues.append({
                        "component": name,
                        "type": tag,
                        "description": f"{tag.capitalize()} exported without proper access control"
                    })

    return access_issues


def perform_static_analysis(apk_path: str) -> dict:
    """
    Perform static analysis using Androguard.
    """
    # Load APK and perform analysis
    a, d, dx = AnalyzeAPK(apk_path)

    return {
        "ssl_tls_issues": analyze_ssl_tls_issues(dx),
        "crypto_issues": analyze_crypto_misuse(dx),
        "access_control_issues": analyze_access_control_issues(a)
    }
