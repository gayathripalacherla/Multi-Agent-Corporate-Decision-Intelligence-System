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

## Architecture Diagram
┌───────────────────────────────────────────────────────────────────────────────┐
│ USER / INPUT LAYER │
├───────────────────────────────────────────────────────────────────────────────┤
│ Scenario Description (Natural Language) │
│ Numeric Signals (0–10) │
└───────────────────────────────────────────────────────────────────────────────┘
│
▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ SIGNAL UNDERSTANDING MODULE │
├───────────────────────────────────────────────────────────────────────────────┤
│ NLP Context Interpreter │
│ Signal Vector Generator (0–1) │
└───────────────────────────────────────────────────────────────────────────────┘
│
▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ MULTI-AGENT DECISION PANEL (ADK AGENTS) │
├───────────────────────────────────────────────────────────────────────────────┤
│ Tech Lead, Product Manager, Risk, Finance, Ops, Engineering Manager │
└───────────────────────────────────────────────────────────────────────────────┘
│
▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ SCORING & TRADEOFF ANALYSIS ENGINE │
├───────────────────────────────────────────────────────────────────────────────┤
│ Option Scoring Matrix │
│ Conflict Detection │
│ Consensus Modeling │
└───────────────────────────────────────────────────────────────────────────────┘
│
▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ SUPERVISOR LLM — GEMINI 2.5 │
├───────────────────────────────────────────────────────────────────────────────┤
│ Synthesizes reports, weighs signals, generates final strategy │
└───────────────────────────────────────────────────────────────────────────────┘
│
▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ VISUAL ANALYTICS LAYER │
├───────────────────────────────────────────────────────────────────────────────┤
│ Radar Chart, heatmap │
└───────────────────────────────────────────────────────────────────────────────┘
