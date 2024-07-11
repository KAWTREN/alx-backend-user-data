#!/usr/bin/env python3
"""Session authentication views"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
import os
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """POST /auth_session/login
    Handle session authentication login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    cookie_name = os.getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)

    return response
