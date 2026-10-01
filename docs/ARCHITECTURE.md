# CareContinuum Agent — Architecture

## Runtime

CareContinuum is intentionally lightweight for the hackathon demo:

- **Frontend:** single-page HTML/CSS/JavaScript cockpit
- **Backend:** Python `ThreadingHTTPServer` using the standard library
- **State:** local JSON files under `data/`
- **Dependencies:** none beyond Python

## End-to-end flow

```text
User goal
   ↓
GET patient context
   ↓
Risk calculation
   ↓
Highest-risk patient
   ↓
Plan generation
   ↓
Human approval gate
   ↓
Approved action execution
   ↓
State update
   ↓
Verification + audit log
```

## Risk model used by the prototype

The current deterministic demo risk function adds operational points:

| Signal | Points |
|---|---:|
| Medicine pending | +35 |
| Lab pending | +25 |
| Follow-up missed | +30 |
| Recent outreach failed | +10 |

Risk bands in the current implementation are:

- **HIGH:** 60 or more
- **MEDIUM:** 35–59
- **LOW:** below 35

This is an operational demo score, not a clinical risk model.

## Agent plan

The planner creates actions only for currently pending milestones:

- `generate_followup_message`
- `create_asha_task`
- `schedule_lab_followup`

The exact action list depends on the selected patient's current state.

## Human governance

The browser must explicitly trigger **Approve & execute** before the prototype calls the approval endpoint. The interface also exposes a Reject path, which demonstrates that a proposed plan can be reviewed without executing it.

## Verification

After approval, the demo:

1. Updates the synthetic patient workflow state.
2. Appends an audit record to `data/action_log.json`.
3. Returns a verified result to the cockpit.
4. Updates the interface to **VERIFIED** and **Closed loop**.

The actions are simulated demo actions. No real patient, message, laboratory booking or external clinical system is contacted.

## Files

```text
backend/app.py          API, risk logic, planner, execution, verification
frontend/index.html     Hackathon cockpit UI and interaction flow
data/patients.json      Synthetic patient state
data/action_log.json    Demo audit trail
DEMO.md                 Live demonstration script
START.bat               Windows launcher
```

## Scope

The prototype is designed to demonstrate **agentic workflow orchestration with human control**. It does not diagnose patients, prescribe treatment, or alter clinical decisions.
