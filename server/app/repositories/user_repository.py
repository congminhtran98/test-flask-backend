from app.models.user_model import User
from app.database import db

# Create user
def create_user(user_data):
    # SQLAlchemy ORM:
    new_user = User(name=user_data['name'], email=user_data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    # SQL thuần:
    # INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
    return new_user

# Get all users
def get_users():
    # SQLAlchemy ORM:
    return User.query.all()
    
    # SQL thuần:
    # SELECT * FROM users;

# Get user by ID
def get_user_by_id(user_id):
    # SQLAlchemy ORM:
    return User.query.get(user_id)
    
    # SQL thuần:
    # SELECT * FROM users WHERE id = 1;  (trong đó '1' là user_id truyền vào)

# Update user
def update_user(user_id, updated_data):
    # SQLAlchemy ORM:
    user = User.query.get(user_id)
    if user:
        user.name = updated_data.get('name', user.name)
        user.email = updated_data.get('email', user.email)
        db.session.commit()
    
    # SQL thuần:
    # UPDATE users SET name = 'New Name', email = 'newemail@example.com' WHERE id = 1;
    return user

# Delete user
def delete_user(user_id):
    # SQLAlchemy ORM:
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    
    # SQL thuần:
    # DELETE FROM users WHERE id = 1;
    return user
