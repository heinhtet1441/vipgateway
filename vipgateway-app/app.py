from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

API_BASE = "https://api.staging.vipgateway.net"

HTML = open("templates/index.html").read()

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/api/channels")
def channels():
    token = request.headers.get("X-Token", "")
    try:
        r = requests.get(
            f"{API_BASE}/v1/channels?limit=50",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/payments", methods=["POST"])
def create_payment():
    token = request.headers.get("X-Token", "")
    try:
        r = requests.post(
            f"{API_BASE}/v1/payments",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            json=request.get_json(),
            timeout=15
        )
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/payments/<payment_id>")
def get_payment(payment_id):
    token = request.headers.get("X-Token", "")
    try:
        r = requests.get(
            f"{API_BASE}/v1/payments/{payment_id}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/payments/<payment_id>/cancel", methods=["POST"])
def cancel_payment(payment_id):
    token = request.headers.get("X-Token", "")
    try:
        r = requests.post(
            f"{API_BASE}/v1/payments/{payment_id}/cancel",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
