# System Architecture

The system follows a modular multi-agent workflow.

## Flow

User Proposal  
→ Input Validation  
→ Technology Lead Agent  
→ Product Manager Agent  
→ Risk Agent  
→ Finance Agent  
→ Supervisor Agent  
→ Guardrail Review  
→ Final Recommendation  

## Design Goals

- Separate reasoning by business role
- Improve decision traceability
- Add validation and guardrails
- Support human review for risky decisions
- Keep the workflow modular and extensible
