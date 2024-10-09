import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/test_db.db'  # Đường dẫn đến database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Tắt theo dõi thay đổi để tiết kiệm bộ nhớ
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'  # Secret key cho bảo mật