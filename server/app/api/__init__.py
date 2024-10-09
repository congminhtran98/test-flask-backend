from .home.routes import home_bp
from .data.routes import data_bp

def create_blueprints(app):
    app.register_blueprint(home_bp, url_prefix='/api/home')
    app.register_blueprint(data_bp, url_prefix='/api/data')