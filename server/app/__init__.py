from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Cấu hình CORS, cho phép các yêu cầu từ 'http://localhost:3000'
    CORS(app)

    # Cấu hình ứng dụng
    app.config.from_object(Config)

    # Khởi tạo database
    db.init_app(app)

    # Đăng ký routes
    from app.routes.user_routes import user_bp
    from app.routes.album_routes import album_bp
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(album_bp, url_prefix='/api')

    return app
