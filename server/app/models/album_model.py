from peewee import Model, CharField, IntegerField, AutoField
from app.database import db

# Định nghĩa model cho bảng "albums"
class BaseModel(Model):
    class Meta:
        database = db

class Album(BaseModel):
    AlbumId = AutoField()  # Khóa chính tự động tăng
    Title = CharField(max_length=160)
    ArtistId = IntegerField()
    
    class Meta: 
        table_name = 'albums'

    def __repr__(self):
        return f'<Album {self.Title} (ArtistId: {self.ArtistId})>'
