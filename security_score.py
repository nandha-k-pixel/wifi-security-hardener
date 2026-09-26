SEVERITY_POINTS = {
    "HIGH": 25,
    "MEDIUM": 15,
    "REVIEW": 10,
    "LOW": 5,
    "INFO": 0,
    "PASS": 0,
}

def calculate_score(findings):
    """Return a simple 0-100 security score based on findings."""
    penalty = sum(SEVERITY_POINTS.get(f.get("severity", "INFO"), 0) for f in findings)
    return max(0, min(100, 100 - penalty))

def score_label(score):
    if score >= 80:
        return "Good"
    if score >= 60:
        return "Needs Improvement"
    if score >= 40:
        return "Weak"
    return "Critical Review Required"
