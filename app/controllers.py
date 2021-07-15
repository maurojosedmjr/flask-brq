import pandas as pd
import os
from typing import Optional
import json


def tratar_csv_para_dataframe(
    caminho_do_arquivo: str,
    chave: str,
    separador: str = ",",
    dropar_linhas_com_erros: Optional[bool] = None,
) -> pd.DataFrame:
    if not os.path.exists(caminho_do_arquivo):
        raise Exception(
            "ArquinhoNaoEncontrado", "O arquivo informado não foi encontrado"
        )
    elif not chave:
        raise Exception("ChaveNaoInformada", "A chave do arquivo não foi informada")

    # carregando o arquvio no dataframe
    df_origem = pd.read_csv(
        caminho_do_arquivo, sep=separador, error_bad_lines=dropar_linhas_com_erros
    )

    if chave not in list(df_origem.columns):
        raise Exception(
            "ChaveNaoEncontrada",
            f"A chave {chave} não foi encontrada nas colunas do arquivo",
        )

    # removendo duplicadas
    df_origem.drop_duplicates(subset=chave, inplace=True)

    # removendo linhas vazias
    df_origem = df_origem.dropna(inplace=True)

    return df_origem


def processar_dataframes():
    df_airbnb = tratar_csv_para_dataframe("./bases/airbnb_ny_2019.csv", chave="id")
    df_map_vizinhanca = tratar_csv_para_dataframe(
        "./bases/mapeamento_vizinhanca.csv",
        chave="vizinhanca",
        separador=";",
        dropar_linhas_com_erros=False,
    )

    df_airbnb_vizinhanca = df_airbnb.join(
        df_map_vizinhanca.set_index("vizinhanca"), on="neighbourhood"
    )

    if "vizinhanca" in df_airbnb_vizinhanca:
        df_airbnb_vizinhanca = df_airbnb_vizinhanca.drop(columns="vizinhanca")

    df_airbnb_vizinhanca.rename(
        columns={"vizinhanca_grupo": "neighbourhood_group"}, inplace=True
    )

    df_filtrado = df_airbnb_vizinhanca.query(
        "neighbourhood_group in ['Brooklyn', 'Manhattan', 'Queens', 'Staten Island']"
    ).to_csv("./bases/residencias.csv", sep=",", index=False)

    df_filtrado.to_csv("./bases/residencias.csv", sep=",", index=False)

    df_filtrado.groupby(["neighbourhood_group", "room_type"])["price"].mean().to_json(
        "./bases/media_preco.csv", orient="split"
    )

    parsed = (
        df_filtrado.groupby(["neighbourhood_group", "room_type"])["price"]
        .mean()
        .to_json(orient="table")
    )
    parsed = json.loads(parsed)
    data = parsed["data"]

    with open("./bases/media_preco.csv", "w") as f:
        json.dump(data, f)
