from app.models.album_model import Album

# Lấy tất cả albums
def get_all_albums():
    return list(Album.select())

# Tạo album mới
def create_album(album_data):
    return Album.create(Title=album_data['Title'], ArtistId=album_data['ArtistId'])

# Lấy album theo ID
def get_album_by_id(album_id):
    return Album.get_or_none(Album.id == album_id)

# Cập nhật album
def update_album(album_id, updated_data):
    album = Album.get_by_id(album_id)
    album.Title = updated_data.get('Title', album.Title)
    album.ArtistId = updated_data.get('ArtistId', album.ArtistId)
    album.save()

# Xóa album
def delete_album(album_id):
    album = Album.get_by_id(album_id)
    album.delete_instance()
