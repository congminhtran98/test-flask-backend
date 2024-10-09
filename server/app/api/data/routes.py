from flask import Blueprint, jsonify
from app.services.data_services import get_data_service

data_bp = Blueprint('data', __name__)

@data_bp.route('/', methods=['GET'])
def get_data():
    data = get_data_service()
    return jsonify(data)
