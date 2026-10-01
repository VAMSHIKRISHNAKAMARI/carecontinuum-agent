# CareContinuum Agent

Agentic follow-up assurance prototype for BharatAgentic 2026.

## Run

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python backend/app.py
```

Open http://localhost:5000

## Demo flow

1. Click **Run Care Agent**.
2. Review Understand → Reason → Plan.
3. Click **Approve & Execute**.
4. Show the verified state transition.

The prototype uses synthetic data only.

FINAL DEMO BUILD: metrics are synchronized after verification.
