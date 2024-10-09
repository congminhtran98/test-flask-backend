from app.database import get_db_connection

def fetch_data_from_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM albums')
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
