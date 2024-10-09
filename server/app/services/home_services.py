from app.queries.home_queries import get_message_from_db

def get_home_message():
    # Xử lý nghiệp vụ, chẳng hạn thêm logic hoặc xử lý dữ liệu khác
    message = get_message_from_db()
    return message
