def requires_human_review(confidence: float, risk_level: str = "Low") -> bool:
    if confidence < 0.75:
        return True

    if risk_level.lower() in ["high", "critical"]:
        return True

    return False
