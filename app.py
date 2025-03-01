from flask import Flask
from controllers.user_controller import user_bp
from controllers.openai_controller import openai_bp

app = Flask(__name__, template_folder="views")
app.config.from_object("config.Config")  # 설정 파일 로드

# 블루프린트 등록 (라우트)
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(openai_bp, url_prefix="/openai")

if __name__ == "__main__":
    app.run(debug=True)
