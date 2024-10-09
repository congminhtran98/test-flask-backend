from app.queries.data_queries import fetch_data_from_db

def get_data_service():
    # Xử lý nghiệp vụ và tương tác với query để lấy dữ liệu
    data = fetch_data_from_db()
    return data
