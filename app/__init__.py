from flask import Flask
from flask_restx import Resource, Api
from .model import configure_db
from flask_migrate import Migrate
from .routes import ns_residencia


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/banco_bases.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # configuração de banco
    configure_db(app)

    # config migrate
    Migrate(app, app.db)

    api = Api(
        app,
        version="1.0",
        title="Docs Api",
        description="Teste BRQ",
    )

    api.add_namespace(ns_residencia)

    return app


if __name__ == "__main__":
    create_app()
