from flask import request, jsonify, Blueprint, render_template
from services.openai_service import OpenAIService

openai_bp = Blueprint("openai", __name__)

openai_service = OpenAIService()  # .env에서 API 키를 자동으로 불러옴

@openai_bp.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Prompt is required"}), 400

        prompt = data["prompt"]
        response_text = openai_service.generate_response(prompt)
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@openai_bp.route("/generate_story", methods=["POST"])
def generate_story():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Prompt is required"}), 400

        prompt = data["prompt"]
        story_text = openai_service.generate_story(prompt)
        return jsonify({"story": story_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@openai_bp.route("/page", methods=["GET"])
def page():
    return render_template("openai_page.html")