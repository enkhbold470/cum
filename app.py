from flask import Flask
from config import Config
from extensions import db, migrate, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        # Import and register blueprints
        from routes import auth, main
        app.register_blueprint(auth.bp)
        app.register_blueprint(main.bp)

        @login_manager.user_loader
        def load_user(id):
            from models.user import User
            return User.query.get(int(id))

        return app

app = create_app()

if __name__ == '__main__':
    app.run()