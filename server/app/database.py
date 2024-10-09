import sqlite3

DATABASE = 'instance/test_db.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # Thực thi các script để tạo bảng nếu chưa có
    conn.close()