from app.repositories.album_repository import get_all_albums, create_album, get_album_by_id, update_album, delete_album

def get_all_albums_service():
    return get_all_albums()

def create_album_service(album_data):
    return create_album(album_data)

def get_album_by_id_service(album_id):
    return get_album_by_id(album_id)

def update_album_service(album_id, updated_data):
    return update_album(album_id, updated_data)

def delete_album_service(album_id):
    return delete_album(album_id)
