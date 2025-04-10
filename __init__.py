from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.routes import auth, main
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    @login_manager.user_loader
    def load_user(id):
        from app.models.user import User
        return User.query.get(int(id))

    return app 