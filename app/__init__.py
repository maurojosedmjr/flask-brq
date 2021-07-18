from flask import Flask
from flask_restx import Api
from .model import configure_db
from flask_migrate import Migrate
from .routes import ns_residencia, ns_preco_media
import os


def preparar_arquivos():
    csvs_necessarios = ["media_preco.csv", "media_preco_df.csv", "residencias.csv"]
    if not all(
        [filename in os.listdir("./app/bases") for filename in csvs_necessarios]
    ):
        from app.controllers import processar_dataframes

        processar_dataframes()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:////tmp/banco_bases.db")
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
    api.add_namespace(ns_preco_media)

    # gerando os arquivos base
    preparar_arquivos()

    return app


if __name__ == "__main__":
    app = create_app()
