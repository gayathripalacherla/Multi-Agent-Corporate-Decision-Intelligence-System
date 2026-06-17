from agents.tech_lead_agent import analyze_technical_feasibility
from agents.product_manager_agent import analyze_product_value
from agents.risk_agent import analyze_risk
from agents.finance_agent import analyze_financial_impact
from agents.supervisor_agent import synthesize_recommendation
from guardrails.validation import validate_input
from utils.logger import log_step

def run_decision_workflow(proposal: str) -> dict:
    validate_input(proposal)
    log_step("Starting multi-agent decision workflow")

    technical = analyze_technical_feasibility(proposal)
    product = analyze_product_value(proposal)
    risk = analyze_risk(proposal)
    finance = analyze_financial_impact(proposal)

    final_recommendation = synthesize_recommendation(
        proposal=proposal,
        technical=technical,
        product=product,
        risk=risk,
        finance=finance
    )

    return final_recommendation
