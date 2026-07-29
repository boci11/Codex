#!/usr/bin/env python3
"""
app.py

Prosty serwer Flask, dostarcza stronę www i endpoint /screen do odbioru tekstu (np. z OCR).
Uruchomienie lokalne:
  pip install -r requirements.txt
  gunicorn -b 0.0.0.0:8000 app:app

Dockerfile dostarcza kontener z Tesseract i aplikacją.
"""
from flask import Flask, request, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Proste przechowywanie ostatnich komunikatów w pamięci (dla demonstracji)
LAST_MESSAGES = []
MAX_MESSAGES = 50

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", messages=list(reversed(LAST_MESSAGES)))

@app.route("/screen", methods=["POST"])
def receive_screen():
    """Odbiera JSON: {"type":"screen_vision","timestamp":"...","text":"..."}
    Możesz dostosować aby integrować z lokalnym czatem GPT (wstrzykiwanie do kontekstu).
    """
    payload = request.get_json(force=True)
    text = payload.get("text") if payload else None
    if not text:
        return jsonify({"ok": False, "error": "no text"}), 400

    entry = {
        "timestamp": payload.get("timestamp") or datetime.utcnow().isoformat() + "Z",
        "text": text,
        "source": payload.get("type") or "screen_vision",
    }

    LAST_MESSAGES.append(entry)
    # przycinamy
    if len(LAST_MESSAGES) > MAX_MESSAGES:
        del LAST_MESSAGES[:-MAX_MESSAGES]

    # Dla demonstracji zwracamy prostą analizę: długość i pierwsze 200 znaków
    return jsonify({
        "ok": True,
        "received": len(text),
        "preview": text[:200]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
