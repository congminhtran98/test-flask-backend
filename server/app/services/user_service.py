from app.repositories.user_repository import (
    create_user, get_users, get_user_by_id, update_user, delete_user
)

def create_user_service(user_data):
    if not user_data.get('name') or not user_data.get('email'):
        return {"error": "Name and email are required"}
    return create_user(user_data)

def get_users_service():
    return get_users()

def get_user_by_id_service(user_id):
    return get_user_by_id(user_id)

def update_user_service(user_id, updated_data):
    return update_user(user_id, updated_data)

def delete_user_service(user_id):
    return delete_user(user_id)
