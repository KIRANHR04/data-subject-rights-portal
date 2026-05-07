from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from services.security import sanitize_input
from services.groq_client import GroqClient

app = Flask(__name__)

@app.after_request
def add_security_headers(response):

    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"

    return response

# Rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# Home route for ZAP scan
@app.route("/")
def home():
    return "AI Service Running"

# Health check route
@app.route("/health")
def health():
    return {"status": "AI service running"}

# AI generate route
@app.route("/generate", methods=["POST"])
@limiter.limit("30 per minute")
def generate():

    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"error": "Prompt is required"}), 400

    prompt = sanitize_input(data["prompt"])

    if not prompt:
        return jsonify({"error": "Invalid or unsafe input"}), 400

    client = GroqClient()

    response = client.generate(prompt)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)