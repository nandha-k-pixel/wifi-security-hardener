from datetime import datetime
import json
import os

from security_score import calculate_score, score_label
from recommendations import build_recommendations

def generate_report(
    gateway,
    findings,
    devices=None,
    service_results=None,
    firmware_info=None,
    network_info=None,
    output_file="security_report.json"
):
    """Generate one combined security report for all tool modules."""
    score = calculate_score(findings) if findings else None
    report = {
        "timestamp": datetime.now().isoformat(),
        "gateway": gateway,
        "audit_type": "Wireless Router Security Audit",
        "security_score": score,
        "score_label": score_label(score) if score is not None else "Not Evaluated",
        "findings": findings,
        "recommendations": build_recommendations(findings),
        "discovered_devices": devices or [],
        "service_results": service_results or [],
        "firmware_info": firmware_info or {},
        "network_info": network_info or {},
        "scope": "Authorized local-network assessment only",
        "limitations": [
            "Open ports do not prove that a service is vulnerable.",
            "Firmware information is user-provided unless verified separately.",
            "The tool does not change router settings automatically."
        ]
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"\n[+] Combined security report saved: {output_file}")
    if score is not None:
     print(f"[+] Security score: {score}/100 ({score_label(score)})")
    else:
     print("[+] Security score: Not Evaluated (no findings)")
    return report
