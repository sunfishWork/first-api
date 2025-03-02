from flask import Flask
from controllers.user_controller import user_bp
from controllers.openai_controller import OpenAIController
from services.openai_service import OpenAIService
from controllers.deepseek_controller import DeepSeekController
from services.deekseek_service import DeepSeekService

app = Flask(__name__, template_folder="views")

# OpenAI 서비스 인스턴스 생성
openai_service = OpenAIService()
openai_controller = OpenAIController(openai_service)

# DeepSeek Service
deepseek_service = DeepSeekService()
deepseek_controller = DeepSeekController(deepseek_service)

# 블루프린트 등록 (라우트)
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(openai_controller.blueprint, url_prefix="/openai")
app.register_blueprint(deepseek_controller.blueprint, url_prefix="/deepseek")

if __name__ == "__main__":
    app.run(debug=True)
