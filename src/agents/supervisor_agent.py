def synthesize_recommendation(proposal: str, technical: dict, product: dict, risk: dict, finance: dict) -> dict:
    return {
        "proposal": proposal,
        "final_recommendation": "Proceed with phased rollout",
        "reasoning": {
            "technical": technical,
            "product": product,
            "risk": risk,
            "finance": finance
        },
        "required_guardrails": [
            "human approval for high-risk outputs",
            "logging and monitoring",
            "prompt injection checks",
            "structured output validation"
        ],
        "decision_confidence": 0.82
    }
