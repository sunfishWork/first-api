from flask import request, jsonify, Blueprint, render_template
from services.deekseek_service import DeepSeekService

class DeepSeekController:
    def __init__(self, deepseek_service: DeepSeekService):
        self.deepseek_service = deepseek_service
        self.blueprint = Blueprint("deepseek", __name__)
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule("/query", methods=["POST"], view_func=self.query)

    def query(self):
        try:
            data = request.get_json()
            if not data or "prompt" not in data:
                return jsonify({"error": "Prompt is required"}), 400

            prompt = data["prompt"]
            response_text = self.deepseek_service.generate_response(prompt)
            return jsonify({"response": response_text})
        except Exception as e:
            return jsonify({"error": str(e)}), 500