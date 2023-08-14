from flask import request, jsonify
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.schemas import UserSchema
from app import db
from app.routes import auth_bp

auth_schema = UserSchema()


@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        # User login logic using login_user
        data = request.get_json()
        errors = auth_schema.validate(data)

        if errors:
            return jsonify(errors), 400

        user = User.query.filter_by(username=data["username"]).first()
        if user and user.check_password(data["password"]):
            login_user(user)
            return jsonify(message="Login successful"), 200
        else:
            return jsonify(message="Invalid credentials"), 401
    except Exception as e:
        return jsonify(message="An error occured"), 500


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    # User logout logic using logout_user
    try:
        logout_user()
        return jsonify(message="Logout successful"), 200

    except Exception as e:
        return jsonify(message="An error occurred"), 500
