from flask import Flask, jsonify
from flask_cors import CORS
from app.database import db
from config import Config

from app.models.album_model import Album  # Thêm dòng này

def create_app():
    app = Flask(__name__)

    # Cấu hình ứng dụng
    app.config.from_object(Config)

    # Khởi tạo CORS (cho phép tất cả các domain)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Khởi tạo các route
    from app.routes.album_routes import album_bp
    app.register_blueprint(album_bp, url_prefix='/api')

    # # Tạo bảng nếu chưa có
    # with app.app_context():
    #     from app.models.album_model import Album
    #     db.connect()
    #     db.create_tables([Album])
    #     db.close()
     # Thêm route để kiểm tra dữ liệu albums
    @app.route('/check_albums')
    def check_albums():
        db.connect()  # Mở kết nối tới cơ sở dữ liệu
        albums = Album.select()  # Truy vấn dữ liệu từ bảng albums
        print(albums)
        db.close()  # Đóng kết nối
        print(jsonify([album.__data__ for album in albums]))
        return jsonify([album.__data__ for album in albums])  # Chuyển đối tượng thành dictionary và trả về JSON

    
    return app
