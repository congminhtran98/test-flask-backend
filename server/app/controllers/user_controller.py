from flask import jsonify, request
from app.services.user_service import (
    create_user_service, get_users_service, get_user_by_id_service,
    update_user_service, delete_user_service
)

def create_user():
    user_data = request.json
    result = create_user_service(user_data)
    return jsonify(result), 201

def get_users():
    users = get_users_service()
    return jsonify(users), 200

def get_user(user_id):
    user = get_user_by_id_service(user_id)
    return jsonify(user), 200

def update_user(user_id):
    updated_data = request.json
    result = update_user_service(user_id, updated_data)
    return jsonify(result), 200

def delete_user(user_id):
    result = delete_user_service(user_id)
    return jsonify(result), 200
