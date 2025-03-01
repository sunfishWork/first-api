from flask import Blueprint, render_template, jsonify
from models.user import User

user_bp = Blueprint("user", __name__)

# 가짜 데이터베이스 (예제용)
users = [
    User(1, "Alice", "alice@example.com"),
    User(2, "Bob", "bob@example.com"),
]

# 사용자 목록 조회 API
@user_bp.route("/")
def get_users():
    return jsonify([user.to_dict() for user in users])

# 사용자 HTML 페이지 렌더링
@user_bp.route("/page")
def user_page():
    return render_template("user.html", users=users)
