from flask import Blueprint
from app.controllers.album_controller import get_all_albums_controller, create_album_controller, get_album_controller, update_album_controller, delete_album_controller

album_bp = Blueprint('albums', __name__)

album_bp.route('/albums', methods=['GET'])(get_all_albums_controller)
album_bp.route('/albums', methods=['POST'])(create_album_controller)
album_bp.route('/albums/<int:album_id>', methods=['GET'])(get_album_controller)
album_bp.route('/albums/<int:album_id>', methods=['PUT'])(update_album_controller)
album_bp.route('/albums/<int:album_id>', methods=['DELETE'])(delete_album_controller)
