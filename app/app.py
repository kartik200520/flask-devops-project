from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "project": "Enterprise Flask DevOps",
        "status": "running",
        "environment": os.getenv("APP_ENV", "development")
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200