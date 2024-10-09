from flask import Flask
from flask_cors import CORS
from .api import create_blueprints
from .database import init_db

def create_app():
    app = Flask(__name__)
    
    # Cấu hình CORS
    CORS(app)

    # Khởi tạo database
    init_db()

    # Đăng ký các blueprint
    create_blueprints(app)

    return app
