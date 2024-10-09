from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user

user_bp = Blueprint('users', __name__)

user_bp.route('/users', methods=['POST'])(create_user)
user_bp.route('/users', methods=['GET'])(get_users)
user_bp.route('/users/<int:user_id>', methods=['GET'])(get_user)
user_bp.route('/users/<int:user_id>', methods=['PUT'])(update_user)
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
