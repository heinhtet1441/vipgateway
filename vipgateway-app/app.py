from flask import Flask, request, jsonify, render_template
import requests, os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

API_BASE = "https://api.staging.vipgateway.net"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/channels")
def channels():
    token = request.headers.get("X-Token", "")
    try:
        r = requests.get(
            f"{API_BASE}/v1/channels?limit=50",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )
        # Return raw text for debugging
        try:
            return jsonify(r.json()), r.status_code
        except Exception:
            return jsonify({"error": f"HTTP {r.status_code}", "raw": r.text[:500]}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/payments", methods=["POST"])
def create_payment():
    token = request.headers.get("X-Token", "")
    try:
        r = requests.post(
            f"{API_BASE}/v1/payments",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json=request.get_json(),
            timeout=15
        )
        try:
            return jsonify(r.json()), r.status_code
        except Exception:
            return jsonify({"error": f"HTTP {r.status_code}", "raw": r.text[:500]}), 500
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
        try:
            return jsonify(r.json()), r.status_code
        except Exception:
            return jsonify({"error": f"HTTP {r.status_code}", "raw": r.text[:500]}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
