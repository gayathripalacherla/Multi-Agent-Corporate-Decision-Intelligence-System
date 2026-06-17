def validate_input(proposal: str) -> None:
    if not proposal or not proposal.strip():
        raise ValueError("Proposal cannot be empty.")

    if len(proposal) < 20:
        raise ValueError("Proposal must include enough context for analysis.")
