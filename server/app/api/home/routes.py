from flask import Blueprint, jsonify
from app.services.home_services import get_home_message

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    return jsonify({'message': get_home_message()})
