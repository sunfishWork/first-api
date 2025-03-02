from flask import request, jsonify, Blueprint, render_template
from services.openai_service import OpenAIService

class OpenAIController:
    def __init__(self, openai_service: OpenAIService):
        self.openai_service = openai_service
        self.blueprint = Blueprint("openai", __name__)
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule("/query", methods=["POST"], view_func=self.query)
        self.blueprint.add_url_rule("/generate_story", methods=["POST"], view_func=self.generate_story)
        self.blueprint.add_url_rule("/page", methods=["GET"], view_func=self.page)

    def query(self):
        try:
            data = request.get_json()
            if not data or "prompt" not in data:
                return jsonify({"error": "Prompt is required"}), 400

            prompt = data["prompt"]
            response_text = self.openai_service.generate_response(prompt)
            return jsonify({"response": response_text})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def generate_story(self):
        try:
            data = request.get_json()
            if not data or "prompt" not in data:
                return jsonify({"error": "Prompt is required"}), 400

            prompt = data["prompt"]
            story_text = self.openai_service.generate_story(prompt)
            return jsonify({"story": story_text})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def page():
        return render_template("openai_page.html")