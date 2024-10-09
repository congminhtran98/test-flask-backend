from flask import jsonify
from app.services.album_service import get_all_albums_service

def get_all_albums():
    albums = get_all_albums_service()
    return jsonify(albums), 200
