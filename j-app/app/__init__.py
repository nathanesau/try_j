from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from config import Config


bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    bootstrap.init_app(app)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app
