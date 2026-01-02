# Introduction
Mobile money applications, also known as branchless banking, have revolutionized financial
services in developing countries but often suffer from serious security vulnerabilities, as
highlighted in the paper “Mo(bile) Money, Mo(bile) Problems: Analysis of Branchless Banking
Applications in the Developing World.” Many apps lack proper SSL/TLS encryption, exposing
users to threats like MITM attacks, data leaks, and insecure cryptography. This project aims to
create a tool that combines static and manual analysis to detect these vulnerabilities. The tool
will analyze APK files, automate the methodology from the paper, and present results via a web
dashboard with report generation features.

# Problem Statement and Objectives
As mobile money apps continue to be widely used, the risks associated with their vulnerabilities
increase. Automated tools alone often miss critical issues or generate false positives, especially
regarding SSL/TLS encryption and cryptographic implementations. Manual analysis, while more
accurate, is time-consuming and does not scale easily across numerous applications.
The objectives of this project are:
1. To automate the analysis process for mobile money applications, detecting critical
vulnerabilities such as SSL/TLS misconfigurations, improper certificate validation, and
insecure cryptographic implementations.
2. To integrate both static and manual analysis techniques into a unified pipeline, including
the full lifecycle analysis of registration, login, and transactions to identify weak
authentication or session management issues.
3. To identify and report sensitive data leakage during app execution and data flows,
ensuring that private information is handled securely.
4. To provide a mechanism to verify and reduce false positives from automated tools
through manual validation of findings.
5. To create a web-based interface that allows for the easy upload of APKs, viewing of
analysis results, and generation of reports.
6. To ensure the tool is scalable and accurate, minimizing false positives and false
negatives, and classifying vulnerabilities using CWE (Common Weakness Enumeration)
codes.

# Proposed Solution and Methodology
The proposed solution is a web-based tool that automates the comprehensive security analysis
of mobile money applications. The tool will integrate the complete methodology from the
referenced paper and extend it by building a custom analysis framework using Androguard to
detect cryptographic vulnerabilities. The pipeline will handle APK files as input and provide
outputs in the form of visual dashboards and exportable reports.

# Methodology Details:
1. APK File Input and Extraction:
○ The user will upload APK files via the web interface.
○ The backend will use apktool to extract the application manifest, permissions,
and metadata to provide a high-level overview of the app’s structure and
functionality.

2. Custom Static Analysis Tool (Based on Androguard):
○ Build a custom static analysis tool using the Androguard API to detect SSL/TLS
misconfigurations and cryptographic API misuse
○ Analyze the SSL/TLS certificate validation, improper cryptography, and access
control issues.
○ Provide a baseline of common SSL/TLS weaknesses, such as weak encryption,
unvalidated certificates, or insecure key exchanges.

3. SSL/TLS Server Testing:
○ Use Qualys SSL Server Test to assess the security of remote SSL/TLS endpoints
referenced in the APK.
○ The test will examine the server-side configuration for protocol strength, cipher
choices, and certificate validity.
4. Manual Analysis Automation:
○ Dalvik Bytecode Disassembly: Use Baksmali to disassemble the APK’s bytecode
and identify critical libraries such as cryptographic and networking modules.
○ Library Detection: Automate the detection of cryptography libraries and
dangerous third-party libraries using regex and pattern matching scripts.
○ Lifecycle Tracing: Perform control flow analysis of the app, from the
onCreate() method to registration, login, and money transfer functionalities,
focusing on sensitive data handling.

5. Reverse Engineering:
○ Use the JEB Decompiler to reverse-engineer the app and inspect its code. This
phase will focus on verifying vulnerabilities related to cryptography, certificate
validation, and data leakage.
○ Trace the entire application lifecycle, starting with registration and continuing
through user authentication, session management, and transaction processes.
○ Verify the presence of vulnerabilities in sensitive functionalities, including
authentication, cryptographic procedures, and data handling.

6. Sensitive Data Leakage Detection:
○ Analyze whether sensitive data, such as financial records or personal
information, is leaked through insecure communication channels or logging.

7. Result Compilation:
○ The results of both the static and manual analysis will be displayed on a
dashboard. This includes identified vulnerabilities such as SSL/TLS protocol
errors, cryptographic weaknesses, data leakage, and authentication flaws.
○ Each finding will be automatically verified using additional checks to reduce false
positives and false negatives. This includes dynamic testing, control
flow analysis, and cross-checking with external tools to ensure only real
vulnerabilities are reported.
○ Generate a comprehensive report for users to download, summarizing the
analysis with details on each detected vulnerability, categorized using CWE
(Common Weakness Enumeration) classifications.

This comprehensive tool will automate the entire security analysis process, combining both
static and manual methods. It will provide accurate and actionable insights into the security
posture of mobile money applications, making it easier to detect vulnerabilities, address them,
and enhance user trust in mobile financial services.

