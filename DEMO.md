# CareContinuum Agent — Live Demo

## Purpose

Demonstrate that the prototype can move from a detected follow-up gap to a **human-approved, executed and verified** workflow.

## Pre-demo

1. Run `START.bat`.
2. Open `http://127.0.0.1:5000`.
3. Confirm the header shows **Prototype · Synthetic data · Human approval ON**.

## 60-second presentation flow

### 1. Establish the problem

Say:

> “A completed consultation does not guarantee that the next care milestones happened. CareContinuum finds the open follow-up gaps and turns them into an executable workflow.”

### 2. Start the agent

Click **Run Care Agent**.

Point to:

- **Lakshmi · P1007**
- the high-risk score
- the longitudinal journey
- pending medicine, lab and follow-up milestones
- the visible risk signals

Then say:

> “The agent is not just answering a question. It is identifying the operational state of the care journey and preparing the next actions.”

### 3. Show the agent trace

Point to:

**Understand → Reason → Plan → Verify**

Explain that the prototype combines patient data, a deterministic operational risk function, a planner, action tools and a verifier.

### 4. Show the plan before execution

The Action Desk displays three proposed actions:

1. Generate a medication reminder in the preferred language
2. Create a prioritized ASHA/CHO follow-up task
3. Schedule laboratory follow-up

Pause on the **Human approval gate**.

Say:

> “The system proposes the work, but outward-facing actions are not executed until a human approves the plan.”

### 5. Execute

Click **Approve & execute**.

Do not skip the transition through **EXECUTING**.

### 6. Finish on the evidence

Show:

- **Agent state: VERIFIED**
- **Open actions: 0**
- **Closed loops: 1**
- **Patient state: Re-engaged**
- **Verification: Verified**

Say:

> “We have closed the loop: the care gap was identified, actions were approved and executed, and the resulting workflow state was verified.”

## If a judge asks “Is this really agentic?”

Use this answer:

> “The prototype has a goal-driven flow, derives operational priority from the care state, constructs a multi-step plan, uses action-specific tools, pauses for human approval, executes the permitted actions and then verifies the resulting state. That is the agentic loop we are demonstrating.”

## If a judge asks “Is the healthcare data real?”

Use this answer:

> “No. The repository uses synthetic demo healthcare data. The prototype demonstrates the workflow and governance model without touching real patient records or external clinical systems.”

## If a judge asks “What happens without approval?”

Use this answer:

> “The proposed plan stays in the Action Desk. The UI exposes a Reject path, and the execution endpoint is only triggered by the explicit approval action in the demo.”

## Demo reset

Click **Reset** in the top-right corner to restore the deterministic synthetic scenario.

## Technical note

No third-party Python packages are required. The server uses Python's standard library, and the frontend is a single HTML/CSS/JavaScript file.
