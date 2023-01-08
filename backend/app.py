from atexit import register

from core import QA
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

load_dotenv()

qa = QA()
register(qa.close)

app = Flask(__name__)
CORS(app)


@app.post("/")
def get_answer():
    question = request.json.get("question")

    if not question:
        abort(jsonify({"error": "问题不能为空"}), 400)

    return {"answer": qa.answer(question)}


@app.get("/healthz")
def check_health():
    return {"message": "ok"}
