from flask import Flask
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # BluePrint
    from .views import main_views, article_views, keyword_view
    app.register_blueprint(main_views.bp)
    app.register_blueprint(article_views.bp)
    app.register_blueprint(keyword_view.bp)

    # filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app


