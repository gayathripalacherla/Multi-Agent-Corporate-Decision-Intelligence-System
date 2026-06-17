def analyze_risk(proposal: str) -> dict:
    return {
        "agent": "Risk Analyst",
        "assessment": "Requires guardrails, human review, and monitoring before full deployment.",
        "key_considerations": [
            "data privacy",
            "model hallucination",
            "prompt injection",
            "human-in-the-loop escalation"
        ],
        "risk_level": "Medium",
        "confidence": 0.78
    }
