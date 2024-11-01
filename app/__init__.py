from config import Config

from flask import Flask


def create_app(config_class: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        from app import routes  # noqa

    return app
