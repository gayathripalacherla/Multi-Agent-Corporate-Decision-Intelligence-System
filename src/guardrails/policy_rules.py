REQUIRED_GUARDRAILS = [
    "validate user input",
    "check output structure",
    "log workflow steps",
    "flag high-risk decisions",
    "recommend human review when confidence is low"
]

def get_policy_rules() -> list:
    return REQUIRED_GUARDRAILS
