# Multi-Agent Corporate Decision Intelligence System  
### Kaggle 5-Day AI Agents Intensive — Capstone Project  
### Built with Google ADK (Agents Development Kit) + Gemini 2.5

---

## Overview

This project implements a production-style **Multi-Agent Decision Intelligence System** designed to simulate how real organizations (Product, Engineering, Finance, Ops, Risk) evaluate high-stakes decisions.

Instead of relying on a single LLM answer, this system uses **multiple domain-specialized agents** plus a **Supervisor LLM** to provide a balanced, structured, and explainable recommendation.

This work was developed as the **capstone project** for the Kaggle 5-Day AI Agents Intensive by Google.

---

## Key Features

### Multi-Agent Panel (Google ADK)
The system includes six internal ADK agents:

- Tech Lead  
- Product Manager  
- Risk Analyst  
- Finance  
- Operations  
- Engineering Manager  

Each agent scores organizational decision options using their own logic.

### Supervisor LLM (Gemini 2.5)
The supervisor:

- Synthesizes all agent outputs  
- Resolves disagreements  
- Explains tradeoffs  
- Produces a final decision (JSON + executive summary)  

### Signal Extraction Engine
A custom ADK tool converts natural-language business scenarios into a normalized decision signal vector (0–1).

### Interactive Decision Pipeline
Users can:

1. Enter any real-world corporate scenario  
2. Input signal values (0–10)  
3. Provide agent scores  
4. View radar + heatmap analytics  
5. See the supervisor’s final recommendation  

### Visual Analytics
Includes:

- Radar Chart for scenario signals  
- Heatmap for agent score alignment  

---
# Case Study: Reliability Freeze vs Delivering Feature Horizon  
This document demonstrates how the Multi-Agent Corporate Decision Intelligence System evaluates high-stakes, real-world product and engineering decisions.

---

# Scenario Overview
The organization faces a critical trade-off:

- **Option B:** Deliver Feature Horizon to retain a $6.8M ARR enterprise customer.  
- **Option A:** Enforce a Reliability Freeze to stabilize the core platform, reduce Sev-1 outages, and address SRE overload.

SRE load has reached 2.7x normal levels, the core messaging pipeline is unstable, and engineering capacity is severely constrained. The decision impacts platform reliability, customer retention, and long-term business health.

---

# Option A vs Option B — Side-by-Side Comparison

| **Criteria** | **Option A: Reliability Freeze** | **Option B: Deliver Feature Horizon** |
|--------------|----------------------------------|---------------------------------------|
| **Immediate Outcome** | Likely lose $6.8M ARR customer | Retain $6.8M ARR customer (short-term) |
| **Platform Stability** | Stability restored; Sev-1 outages addressed | High risk of platform-wide outages |
| **Core Messaging Pipeline** | Dedicated focus on root-cause fixes | Fragility worsens under added load |
| **Team Health and Burnout** | Burnout risk reduced; workload normalized | Severe burnout and probable attrition |
| **SRE Load** | Moves from 2.7x to sustainable range | Load increases further; unsafe conditions |
| **Engineering Capacity** | Enables concentrated reliability work | Zero capacity; rushed development |
| **Feature Horizon Success Likelihood** | Higher once platform stabilizes | Low; high probability of defects and instability |
| **Customer Retention Risk** | Lose one major customer | Risk losing many customers due to outages |
| **Brand Impact** | Protects long-term reputation and trust | High risk of irreversible brand damage |
| **Long-Term Business Health** | Preserves future viability | Jeopardizes entire company trajectory |
| **Strategic Trade-Off** | Short-term pain for long-term survival | Short-term win with existential long-term risks |

---

# Final Decision  
Based on system stability, team capacity, and long-term business risk, the recommended choice is:

## **Option A: Prioritize a Reliability Freeze**

This option sacrifices a single major customer to protect the platform, the engineering organization, and thousands of existing customers.

---

# Rationale for Choosing Option A

1. **Platform Integrity**  
   Stabilizing Sev-1 outages and addressing core messaging pipeline failures prevents cascading system issues.

2. **Team Sustainability**  
   Current SRE and engineering load levels are unsafe. Continuing at this pace guarantees burnout and attrition.

3. **Risk Management**  
   Shipping Feature Horizon under current conditions risks widespread outages affecting many more customers.

4. **Long-Term Viability**  
   A stable product and healthy engineering team are essential for future growth, including successful delivery of Feature Horizon later.

---

# Recommended Immediate Actions

## 1. Customer Communication  
- Explain the need to stabilize the platform for all customers.  
- Emphasize long-term partnership and commitment to delivering Feature Horizon.  
- Provide a revised timeline and potential interim workarounds.

## 2. Execute a Reliability Initiative  
- Full-team focus on stabilizing the core messaging pipeline.  
- Conduct root-cause analysis for recent Sev-1 incidents.  
- Reduce SRE on-call burden through automation or temporary support.

## 3. Prevent Future Tipping Points  
- Improve architecture resiliency.  
- Strengthen testing and incident response processes.  
- Create realistic development timelines before resuming high-risk features.

---

# Summary  
Option B risks destabilizing the platform, burning out the team, and damaging long-term customer trust.  
Option A secures the foundation for sustainable growth and long-term product health.

This case study demonstrates how the Multi-Agent Corporate Decision Intelligence System processes complex engineering-product trade-offs to produce grounded, actionable recommendations.
