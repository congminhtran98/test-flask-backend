from app.repositories.album_repository import get_all_albums

def get_all_albums_service():
    albums = get_all_albums()
    return [album.__dict__ for album in albums]  # Trả về dạng dictionary
