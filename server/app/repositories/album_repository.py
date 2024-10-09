from app.models.album_model import Album

def get_all_albums():
    return Album.query.all()
