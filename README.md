# CareContinuum Agent

## Agentic Follow-up Assurance for Rural Healthcare Workflows

CareContinuum Agent is an agentic healthcare operations prototype designed to reduce missed follow-ups by moving from **risk detection to planned intervention and verified outcome**.

The system identifies a high-risk follow-up case, constructs the patient's care journey, reasons over incomplete milestones, prepares operational actions, requests human approval, executes permitted actions, and verifies whether the patient's care journey has moved forward.

> **From risk signal → intervention plan → verified outcome**

---

## Problem

A healthcare consultation being marked complete does not always mean that the patient's care journey is complete.

Medication collection, laboratory tests, follow-up reviews, and outreach can remain pending or fail to happen. Fragmented records can make it difficult for frontline workers to identify which patient needs attention and what action should happen next.

---

## Solution

CareContinuum Agent provides a closed-loop follow-up workflow:

```text
Understand
    ↓
Reason
    ↓
Plan
    ↓
Use Tools
    ↓
Human Approval
    ↓
Act
    ↓
Verify

The prototype focuses on operational follow-up assurance rather than clinical diagnosis or treatment decisions.

Agent Workflow
1. Understand

Links the patient's care journey and checks pending milestones.

2. Reason

Explains follow-up risk using the patient's available journey information.

3. Plan

Creates the required operational follow-up actions.

4. Human Approval

External or operational actions require human approval before execution.

5. Act

Executes the permitted actions through the prototype action tools.

6. Verify

Checks the resulting care state and records whether the journey moved forward.

Demonstrated Scenario

Example synthetic patient:

Patient: Lakshmi
ID: P1007
Condition: Hypertension
Initial follow-up risk: High
Medicine: Pending
Lab: Pending
Follow-up: Missed

The agent prepares:

Medication reminder
Prioritized ASHA/CHO follow-up task
Laboratory follow-up

After human approval, the actions are executed and the resulting care state is verified.

Demonstrated Result
Open actions: 0
Agent state: Verified
Closed loops: 1
Patient state: Re-engaged
Verification: Passed
Prototype Safety

This prototype uses synthetic healthcare data.

It does not diagnose patients, prescribe medicines, or make clinical treatment decisions.

External or operational actions are gated by human approval.

Technology Stack
Python
HTML
CSS
JavaScript
Local structured healthcare data
Agent orchestration
Risk scoring
Tool-based action execution
Human approval workflow
Verification and action logging
Project Structure
carecontinuum-agent/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── data/
│   ├── patients.json
│   └── action_log.json
│
├── START.bat
├── DEMO.md
├── README.md
└── requirements.txt
Run Locally
Windows

Run:

START.bat

Then open:

http://127.0.0.1:5000
Demo Workflow
Run Care Agent
Review Understand / Reason / Plan
Review the proposed actions
Approve & Execute
Observe action execution
Verify the final care state
Agentic Capabilities

CareContinuum Agent demonstrates:

Goal-driven task execution
Patient journey understanding
Risk-based prioritization
Multi-step planning
Tool-based action execution
Human approval gates
Action verification
Closed-loop workflow completion
Bharat-First Design

The prototype is designed around rural healthcare workflow requirements such as:

Frontline worker prioritization
Follow-up assurance
Operational task coordination
Synthetic patient journey data
Human-controlled external actions
Support for future regional-language workflows
Design considerations for resource-constrained environments
Hackathon

BharatAgentic 2026

Project: CareContinuum Agent

Focus: Agentic healthcare follow-up assurance for rural healthcare workflows

Team
Vamshi Krishna

CMR Engineering College
Team Lead

Raju Jinna

CMR Engineering College
Team Member

Aravind Kumar

CMR Engineering College
Team Member

GitHub Repository

https://github.com/VAMSHIKRISHNAKAMARI/carecontinuum-agent
