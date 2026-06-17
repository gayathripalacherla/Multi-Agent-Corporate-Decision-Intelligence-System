# Multi-Agent Corporate Decision Intelligence System

A production-style **agentic AI decision intelligence system** that simulates how cross-functional teams evaluate high-stakes business and engineering decisions.

This project uses **Google ADK (Agents Development Kit)** and **Gemini 2.5** to coordinate multiple specialized agents across Product, Engineering, Finance, Operations, and Risk. Instead of relying on a single LLM response, the system gathers independent agent perspectives, applies structured decision signals, and produces an explainable final recommendation through a Supervisor LLM.

Built as a capstone project for the **Kaggle 5-Day AI Agents Intensive by Google**.

---

## Problem Statement

Organizations often make complex decisions where one perspective is not enough. Product teams may prioritize customer retention, Engineering may prioritize system stability, Finance may focus on revenue impact, and Risk may flag operational or compliance concerns.

A single LLM response can miss trade-offs, hidden risks, or conflicting stakeholder priorities.

This project demonstrates how **multi-agent AI systems** can support decision-making by:

* Separating reasoning across specialized agents
* Comparing trade-offs across business and technical dimensions
* Applying guardrails and validation checks
* Producing structured, explainable recommendations
* Supporting human review for high-risk decisions

---

## Key Features

* **Multi-agent decision workflow** using Google ADK concepts
* **Supervisor LLM** powered by Gemini 2.5 for final synthesis
* **Role-based agents** for Product, Engineering, Finance, Operations, Risk, and Technical Leadership
* **Signal extraction engine** that converts business scenarios into normalized decision signals
* **Guardrail layer** for validation, confidence checks, and human-review triggers
* **Structured JSON-style outputs** for explainability and traceability
* **Visual analytics** including radar charts and heatmaps
* **Docker support** for containerized execution
* Modular Python source structure for future production extension

---

## Tech Stack

* Python
* Google ADK
* Gemini 2.5
* LLM-based agent orchestration
* Prompt engineering
* JSON-based structured outputs
* Guardrails and validation logic
* Docker
* Git/GitHub

---

## System Architecture

```text
User Scenario
    ↓
Signal Extraction Engine
    ↓
Role-Based Agent Panel
    ├── Tech Lead Agent
    ├── Product Manager Agent
    ├── Risk Analyst Agent
    ├── Finance Agent
    ├── Operations Agent
    └── Engineering Manager Agent
    ↓
Supervisor LLM
    ↓
Guardrail + Validation Layer
    ↓
Final Recommendation
    ↓
Executive Summary + JSON Output + Visual Analytics
```

---

## Agent Responsibilities

### Tech Lead Agent

Evaluates technical feasibility, architecture complexity, scalability, implementation risk, and deployment readiness.

### Product Manager Agent

Evaluates customer value, product impact, roadmap alignment, adoption risk, and business priority.

### Risk Analyst Agent

Evaluates operational risk, compliance exposure, reliability concerns, prompt-safety issues, and escalation needs.

### Finance Agent

Evaluates revenue impact, cost trade-offs, ROI, budget constraints, and long-term financial risk.

### Operations Agent

Evaluates process impact, team workload, delivery feasibility, and operational sustainability.

### Engineering Manager Agent

Evaluates engineering capacity, team health, delivery risk, technical debt, and execution confidence.

### Supervisor LLM

Synthesizes all agent outputs, resolves conflicting recommendations, explains trade-offs, and produces the final decision.

---

## Guardrails and Responsible AI Controls

This project includes lightweight AI reliability and governance mechanisms:

* Input validation
* Structured output checks
* Confidence scoring
* Human-in-the-loop review triggers
* Risk-level flagging
* Prompt injection awareness
* Logging for traceability
* Final recommendation review before decision acceptance

These controls are designed to demonstrate how agentic AI systems can be made more reliable and explainable for enterprise decision-making.

---

## Case Study: Reliability Freeze vs Feature Horizon

### Scenario

The organization faces a critical trade-off:

* **Option A:** Enforce a Reliability Freeze to stabilize the core platform
* **Option B:** Deliver Feature Horizon to retain a $6.8M ARR enterprise customer

The core messaging pipeline is unstable, Sev-1 incidents are increasing, SRE load has reached 2.7x normal capacity, and engineering capacity is severely constrained.

---

## Decision Comparison

| Criteria             | Option A: Reliability Freeze    | Option B: Deliver Feature Horizon    |
| -------------------- | ------------------------------- | ------------------------------------ |
| Immediate Outcome    | Likely lose $6.8M ARR customer  | Retain $6.8M ARR customer short-term |
| Platform Stability   | Stabilizes core platform        | Increases outage risk                |
| SRE Load             | Moves toward sustainable levels | Increases beyond safe capacity       |
| Engineering Capacity | Focused reliability work        | Zero slack for safe delivery         |
| Customer Risk        | Lose one major customer         | Risk broader customer impact         |
| Brand Impact         | Protects long-term trust        | High risk of reputational damage     |
| Long-Term Health     | Preserves future viability      | Creates existential platform risk    |

---

## Final Recommendation

**Recommendation: Option A — Prioritize a Reliability Freeze**

The system recommends sacrificing short-term revenue from one major customer to protect platform stability, engineering sustainability, and long-term customer trust.

### Rationale

* Stabilizing Sev-1 outages prevents cascading failures
* Current SRE load is unsustainable
* Shipping a major feature under unstable platform conditions creates high execution risk
* Long-term business health depends on platform reliability and team capacity

---

## Recommended Immediate Actions

1. **Customer Communication**

   * Explain the platform stabilization priority
   * Offer a revised delivery timeline
   * Provide interim workarounds where possible

2. **Reliability Initiative**

   * Focus engineering capacity on core messaging stability
   * Conduct root-cause analysis for Sev-1 incidents
   * Reduce SRE burden through automation or temporary support

3. **Future Prevention**

   * Improve architecture resilience
   * Strengthen testing and incident response
   * Create realistic delivery timelines before high-risk feature launches

---

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── system_architecture.png
├── multi-agent-corporate-decision-intelligence-system-2.ipynb
├── src/
│   ├── main.py
│   ├── agents/
│   ├── workflows/
│   ├── guardrails/
│   └── utils/
└── docs/
    ├── architecture.md
    └── system_design.md
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/gayathripalacherla/Multi-Agent-Corporate-Decision-Intelligence-System.git
cd Multi-Agent-Corporate-Decision-Intelligence-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up environment variables:

```bash
cp .env.example .env
```

Run the project:

```bash
python src/main.py
```

---

## Sample Output

```json
{
  "final_recommendation": "Proceed with Reliability Freeze",
  "risk_level": "Medium-High",
  "decision_confidence": 0.82,
  "required_guardrails": [
    "human review",
    "executive approval",
    "incident monitoring",
    "customer communication plan"
  ]
}
```

---

## Future Enhancements

* Add Streamlit demo interface
* Add FastAPI endpoint for scenario submission
* Add persistent logging database
* Add automated tests
* Add CI/CD workflow using GitHub Actions
* Add real-time agent evaluation metrics
* Add human approval workflow for high-risk decisions

---

## Why This Project Matters

This project demonstrates how **agentic AI systems** can move beyond simple chatbot responses and support structured enterprise decision-making. It combines multi-agent reasoning, LLM orchestration, guardrails, structured outputs, and explainability — key patterns for building trustworthy AI systems in production environments.
