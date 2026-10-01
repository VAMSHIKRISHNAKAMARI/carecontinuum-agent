# CareContinuum Agent

<p align="center">
  <strong>Close the care loop.</strong><br/>
  Agentic follow-up assurance for rural healthcare workflows.
</p>

<p align="center">
  <a href="https://github.com/VAMSHIKRISHNAKAMARI/carecontinuum-agent">
    <img src="https://img.shields.io/badge/status-prototype-0f766e" alt="status"/>
  </a>
  <a href="https://github.com/VAMSHIKRISHNAKAMARI/carecontinuum-agent">
    <img src="https://img.shields.io/badge/hackathon-BharatAgentic%202026-1d4ed8" alt="hackathon"/>
  </a>
  <a href="https://github.com/VAMSHIKRISHNAKAMARI/carecontinuum-agent">
    <img src="https://img.shields.io/badge/data-synthetic-166534" alt="synthetic data"/>
  </a>
</p>

> **From risk signal → intervention plan → verified outcome.**

## What we built

CareContinuum Agent is a working agentic prototype for healthcare follow-up operations.

Instead of stopping at a risk score, the system:

**understands the care journey → explains the risk → creates a multi-step plan → requests human approval → executes permitted actions → verifies the resulting care state.**

The prototype is designed for operational follow-up assurance. It does **not** diagnose patients, prescribe medicines, or alter treatment.

---

## The problem

A consultation being marked complete does not always mean that care is complete.

Medication collection, laboratory tests, follow-up reviews, and outreach can remain pending or fail to happen. Fragmented records can make it difficult for frontline workers to know:

- which patient needs attention first,
- what milestone is incomplete,
- what action should happen next, and
- whether the intervention actually worked.

---

## The agentic solution

### Understand → Reason → Plan → Approve → Act → Verify

| Stage | What the agent does |
|---|---|
| **Understand** | Links the patient's longitudinal care journey and detects incomplete milestones |
| **Reason** | Explains operational follow-up risk using the available context |
| **Plan** | Creates the minimum required intervention sequence |
| **Approve** | Gates outward-facing/operational actions behind human approval |
| **Act** | Executes the permitted prototype actions |
| **Verify** | Checks the resulting care state and closes the workflow when progress is confirmed |

This makes the prototype an **action-oriented agent**, not a chatbot-only interface.

---

## Live prototype flow

The demonstrated synthetic scenario uses:

**Patient:** Lakshmi · P1007  
**Condition:** Hypertension  
**Initial state:** consultation completed, medicine pending, lab pending, follow-up missed  
**Initial operational risk:** High

The agent prepares:

1. Generate a medication reminder in the preferred language
2. Create a prioritized ASHA/CHO follow-up task
3. Schedule laboratory follow-up

After approval, the prototype executes the actions and verifies the resulting care state.

### Demonstrated outcome

```text
Open actions      0
Agent state       VERIFIED
Closed loops      1
Patient state     RE-ENGAGED
Verification      PASSED
```

---

## Why this is agentic

The prototype demonstrates:

- goal-driven task execution
- patient-journey understanding
- risk-based prioritization
- multi-step planning
- tool-based action execution
- human approval gates
- verification after execution
- closed-loop workflow completion

---

## Product interface

The UI is intentionally designed as a **follow-up operations cockpit**, not a generic conversational assistant.

It exposes:

- priority patient queue
- longitudinal care journey
- agent reasoning stages
- proposed action desk
- human approval gate
- execution state
- verification state
- closed-loop outcome

---

## Bharat-first design

The prototype is designed around rural healthcare workflow realities, including:

- frontline-worker prioritization
- follow-up assurance
- operational task coordination
- synthetic longitudinal patient data
- human-controlled external actions
- future regional-language outreach
- resource-constrained/offline-first design considerations

---

## Safety and scope

This is a **prototype using synthetic healthcare data**.

The system does not:

- diagnose disease
- prescribe medication
- change treatment
- make autonomous clinical decisions

Operational/outward-facing actions are gated by human approval.

---

## Technology

- **Backend:** Python standard library
- **Frontend:** HTML, CSS, JavaScript
- **Data:** Local structured synthetic healthcare data
- **Agent:** Planner + policy gate + action tools + verifier
- **Workflow:** Goal → plan → approval → execution → verification
- **Runtime:** Local Windows demo

---

## Repository structure

```text
carecontinuum-agent/
├── backend/
│   └── app.py
├── frontend/
│   └── index.html
├── data/
│   ├── patients.json
│   └── action_log.json
├── START.bat
├── DEMO.md
├── README.md
└── requirements.txt
```

---

## Run locally

### Windows

Run:

```text
START.bat
```

Then open:

```text
http://127.0.0.1:5000
```

### Demo sequence

1. Click **Run Care Agent**
2. Review **Understand → Reason → Plan**
3. Review the proposed actions
4. Click **Approve & execute**
5. Observe execution
6. Confirm **Verified** and **Closed loop = 1**

More details: [DEMO.md](./DEMO.md)

---

## Hackathon

**BharatAgentic 2026**  
**Project:** CareContinuum Agent  
**Focus:** Agentic healthcare follow-up assurance for rural healthcare workflows

### Team

**Vamshi Krishna** — Team Lead  
CMR Engineering College

**Raju Jinna** — Team Member  
CMR Engineering College

**Aravind Kumar** — Team Member  
CMR Engineering College

---

## Repository

[github.com/VAMSHIKRISHNAKAMARI/carecontinuum-agent](https://github.com/VAMSHIKRISHNAKAMARI/carecontinuum-agent)
