def build_recommendations(findings):
    """Create a de-duplicated recommendation list from audit findings."""
    recommendations = []
    for finding in findings:
        severity = finding.get("severity", "INFO")
        title = finding.get("title", "Finding")
        description = finding.get("description", "")
        if severity in {"HIGH", "MEDIUM", "REVIEW", "LOW"}:
            recommendations.append({
                "priority": severity,
                "finding": title,
                "recommendation": description
            })
    return recommendations
