import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = os.path.join(BASE_DIR, 'instance/test_db.db')
    SECRET_KEY = 'your_secret_key'
