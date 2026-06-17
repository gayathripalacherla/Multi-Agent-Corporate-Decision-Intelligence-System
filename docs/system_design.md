# System Design

This project simulates a production-oriented agentic AI decision system.

## Components

## Agents
Each agent is responsible for one decision perspective:
- Technology feasibility
- Product value
- Risk and governance
- Financial impact
- Final supervisory recommendation

## Guardrails
The guardrail layer validates inputs, checks confidence, and recommends human review when needed.

## Reliability
The system includes basic logging, structured outputs, validation checks, and modular components to support future production deployment.

## Future Enhancements

- Add LangGraph state machine
- Add real LLM API calls
- Add Streamlit user interface
- Add persistent logs
- Add automated tests
- Add CI/CD workflow
