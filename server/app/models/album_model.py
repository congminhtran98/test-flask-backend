from app.database import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Album {self.title} by {self.artist}>'
