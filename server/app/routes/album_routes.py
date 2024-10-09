from flask import Blueprint
from app.controllers.album_controller import get_all_albums

album_bp = Blueprint('albums', __name__)

# Định nghĩa route để lấy toàn bộ albums
album_bp.route('/albums', methods=['GET'])(get_all_albums)
