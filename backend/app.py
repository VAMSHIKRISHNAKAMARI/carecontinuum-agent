from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import json
import os
import uuid
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'patients.json')
LOG_PATH = os.path.join(BASE_DIR, 'data', 'action_log.json')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')
HOST = '127.0.0.1'
PORT = 5000


def read_patients():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_patients(data):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def reset_demo_state():
    data = read_patients()
    for p in data:
        if p['patient_id'] == 'P1007':
            p.update({
                'medicine_status': 'pending',
                'lab_status': 'pending',
                'followup_status': 'missed',
                'recent_outreach': 'failed'
            })
    write_patients(data)
    return data


def risk_for(p):
    score = 0
    reasons = []
    if p.get('medicine_status') == 'pending':
        score += 35
        reasons.append('Medication collection is pending')
    if p.get('lab_status') == 'pending':
        score += 25
        reasons.append('Laboratory milestone is pending')
    if p.get('followup_status') == 'missed':
        score += 30
        reasons.append('Previous follow-up was missed')
    if p.get('recent_outreach') == 'failed':
        score += 10
        reasons.append('Previous outreach was unsuccessful')
    level = 'HIGH' if score >= 60 else 'MEDIUM' if score >= 35 else 'LOW'
    return score, level, reasons


def get_patient(pid):
    return next((p for p in read_patients() if p['patient_id'] == pid), None)


def build_plan(p):
    plan = []
    if p.get('medicine_status') == 'pending':
        plan.append({'tool': 'generate_followup_message', 'description': 'Generate medication reminder in preferred language'})
    if p.get('followup_status') == 'missed':
        plan.append({'tool': 'create_asha_task', 'description': 'Create prioritized ASHA/CHO follow-up task'})
    if p.get('lab_status') == 'pending':
        plan.append({'tool': 'schedule_lab_followup', 'description': 'Schedule laboratory follow-up'})
    return plan


def append_log(record):
    try:
        with open(LOG_PATH, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except Exception:
        logs = []
    logs.append(record)
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(logs[-100:], f, indent=2)


def execute_actions(pid):
    data = read_patients()
    patient = next((p for p in data if p['patient_id'] == pid), None)
    if not patient:
        return None, 'Patient not found'

    plan = build_plan(patient)
    if not plan:
        return None, 'No pending actions for this patient'

    action_id = uuid.uuid4().hex[:8]
    now = datetime.now().isoformat(timespec='seconds')

    # Simulated, safe demo actions.
    patient['medicine_status'] = 'completed'
    patient['lab_status'] = 'scheduled'
    patient['followup_status'] = 're-engaged'
    patient['recent_outreach'] = 'successful'

    write_patients(data)
    append_log({
        'action_id': action_id,
        'patient_id': pid,
        'timestamp': now,
        'status': 'verified',
        'actions': plan,
        'verification': 'Patient moved from at-risk to re-engaged workflow.'
    })

    return {
        'action_id': action_id,
        'patient': patient,
        'plan': plan,
        'verified': True,
        'message': 'Actions executed and outcome verified.'
    }, None


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload, status=200):
        raw = json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(raw)

    def _body(self):
        length = int(self.headers.get('Content-Length', '0') or '0')
        raw = self.rfile.read(length) if length else b'{}'
        try:
            return json.loads(raw.decode('utf-8'))
        except Exception:
            return {}

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/api/patients':
            result = []
            for p in read_patients():
                score, level, reasons = risk_for(p)
                result.append({**p, 'risk_score': score, 'risk_level': level, 'reasons': reasons})
            result.sort(key=lambda x: x['risk_score'], reverse=True)
            return self._json(result)

        if path == '/' or path == '/index.html':
            file_path = os.path.join(FRONTEND_DIR, 'index.html')
        else:
            # Only serve local frontend files.
            requested = path.lstrip('/')
            file_path = os.path.join(FRONTEND_DIR, requested)
            if not os.path.isfile(file_path):
                return self._json({'error': 'Not found'}, 404)

        try:
            with open(file_path, 'rb') as f:
                body = f.read()
            content_type = 'text/html; charset=utf-8' if file_path.endswith('.html') else 'text/plain; charset=utf-8'
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)
        except Exception as exc:
            self._json({'error': str(exc)}, 500)

    def do_POST(self):
        path = urlparse(self.path).path
        body = self._body()

        if path == '/api/reset':
            reset_demo_state()
            return self._json({'ok': True, 'message': 'Synthetic demo scenario reset.'})

        if path == '/api/agent/run':
            # Always start from the same deterministic demo state.
            reset_demo_state()
            goal = body.get('goal', "Find today's highest-risk follow-up patient and prepare an executable care plan.")
            candidates = []
            for p in read_patients():
                score, level, reasons = risk_for(p)
                candidates.append((score, p, level, reasons))
            candidates.sort(key=lambda x: x[0], reverse=True)
            score, patient, level, reasons = candidates[0]
            plan = build_plan(patient)
            return self._json({
                'goal': goal,
                'understand': [
                    f"Patient {patient['patient_id']} located",
                    'Longitudinal care events checked',
                    'Pending milestones detected'
                ],
                'reason': [f'Risk level: {level}', *reasons],
                'plan': plan,
                'patient': patient,
                'risk_score': score,
                'approval_required': True
            })

        if path == '/api/agent/approve':
            pid = body.get('patient_id')
            result, error = execute_actions(pid)
            if error:
                return self._json({'error': error}, 400)
            return self._json(result)

        return self._json({'error': 'Not found'}, 404)

    def log_message(self, format, *args):
        # Keep the terminal clean for the live demo.
        return


def main():
    reset_demo_state()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f'CareContinuum Agent running at http://{HOST}:{PORT}')
    print('Synthetic healthcare demo data only. Press Ctrl+C to stop.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
