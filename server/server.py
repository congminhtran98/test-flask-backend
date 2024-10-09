from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('test_db.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/home', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API!'})


@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM albums')
    rows = cursor.fetchall()
    conn.close()
    
    data = [dict(row) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)