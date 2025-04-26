from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from .config import Config
blacklist = set()
mongo = PyMongo()
jwt = JWTManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    jwt.init_app(app)
    # Register Blueprints with custom base URL
    from .routes.web import web_bp
    from .routes.api import api_bp

    app.register_blueprint(web_bp, url_prefix='/market/web')
    app.register_blueprint(api_bp, url_prefix='/market/api')

    return app


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist