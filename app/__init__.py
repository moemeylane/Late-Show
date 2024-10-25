from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here to ensure they are registered before migrations
    with app.app_context():
        from app.models import Episode, Guest, Appearance  # Import your models here

    from app.routes import main
    app.register_blueprint(main)

    print("App initialized successfully.")

    # Register the custom seed command within create_app
    @app.cli.command("seed_db")
    def seed_db_command():
        """Seed the database."""
        from app.seeds import seed_db
        seed_db()
        print("Database seeded successfully!")

    return app
