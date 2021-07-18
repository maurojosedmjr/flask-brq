from app.model import PrecoMedio, Residencias
from app import preparar_arquivos
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DB_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:////tmp/banco_bases.db")
ENGINE = create_engine(DB_URI)


def rodar_migrate():
    os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")


def popular_database(engine=ENGINE):
    rodar_migrate()
    preparar_arquivos()
    print("aqui")

    if not engine:
        raise Exception(
            "ConexaoComDBNaoInformada",
            "É necessário informar uma conexão antes",
        )

    preco_medio_df = pd.read_csv("./app/bases/media_preco_df.csv", sep=",")

    linhas_para_inserir_preco_medio = []
    for linha in preco_medio_df.iterrows():
        linhas_para_inserir_preco_medio.append(
            {
                "neighbourhood_group": linha[1][0],
                "room type": linha[1][1],
                "price": linha[1][2],
            }
        )

    residencias = pd.read_csv("./app/bases/residencias.csv", sep=",")
    linhas_para_inserir_vizinhanca = []
    for linha in residencias.iterrows():
        dict_linha = {
            "id": linha[1][0],
            "name": linha[1][1],
            "host_id": linha[1][2],
            "host_name": linha[1][3],
            "neighbourhood": linha[1][4],
            "latitude": linha[1][5],
            "longitude": linha[1][6],
            "room_type": linha[1][7],
            "price": linha[1][8],
            "minimum_nights": linha[1][9],
            "number_of_reviews": linha[1][10],
            "last_review": linha[1][11],
            "reviews_per_month": linha[1][12],
            "calculated_host_listings_count": linha[1][13],
            "availability_365": linha[1][14],
            "neighbourhood_group": linha[1][15],
        }
        linhas_para_inserir_vizinhanca.append(dict_linha)

    for base in [
        (PrecoMedio, linhas_para_inserir_preco_medio),
        (Residencias, linhas_para_inserir_vizinhanca),
    ]:
        with Session(ENGINE) as session:
            session.bulk_insert_mappings(base[0], base[1])
            session.commit()


if __name__ == "__main__":
    print(DB_URI)
    popular_database()
