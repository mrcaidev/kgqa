from core import QA
from flask import Flask, abort, jsonify, request

qa = QA()
app = Flask(__name__)


@app.post("/")
def get_answer():
    question = request.json.get("question")

    if not question:
        abort(jsonify({"error": "问题不能为空"}), 400)

    return {"answer": qa.answer(question)}
