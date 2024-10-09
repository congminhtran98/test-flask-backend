from flask import jsonify, request
from app.services.album_service import get_all_albums_service, create_album_service, get_album_by_id_service, update_album_service, delete_album_service

# Lấy tất cả albums
def get_all_albums_controller():
    albums = get_all_albums_service()
    return jsonify([album.__data__ for album in albums]), 200

# Tạo album mới
def create_album_controller():
    album_data = request.json
    new_album = create_album_service(album_data)
    return jsonify(new_album.__data__), 201

# Lấy album theo ID
def get_album_controller(album_id):
    album = get_album_by_id_service(album_id)
    if album:
        return jsonify(album.__data__), 200
    return jsonify({'message': 'Album not found'}), 404

# Cập nhật album
def update_album_controller(album_id):
    updated_data = request.json
    updated_album = update_album_service(album_id, updated_data)
    if updated_album:
        return jsonify(updated_album.__data__), 200
    return jsonify({'message': 'Album not found'}), 404

# Xóa album
def delete_album_controller(album_id):
    delete_album_service(album_id)
    return jsonify({'message': 'Album deleted successfully!'}), 200
