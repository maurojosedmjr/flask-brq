import json
from typing import Dict, Tuple


def recuperar_dados(session, model, filtro=None) -> Tuple[Dict[str, str], int]:
    query = session.query(model)
    try:
        if filtro:
            return query.filter(filtro), 200
        return query.all(), 200
    except Exception as err:
        print(str(err))
        return {"error": "Algo deu errado. Contate o suporte."}, 400


def inserir_ou_atualizar_linha(
    session, model, data, filtro
) -> Tuple[Dict[str, str], int]:
    acao: str = "inserido"
    try:
        if filtro:
            registro = recuperar_dados(session, model, filtro)
            if registro:
                acao = "atualizado"
                registro.update(**data)
            else:
                return {
                    "error": f"Nenhum registro foi encontrado no modelo {model.__name__} com o filtro {filtro}."
                }, 400
        else:
            session.add(model(**data))
        session.commit()
    except Exception as err:
        print(str(err))
        return {"error": "Algo deu errado. Contate o suporte."}, 304
    return {
        "success": f"Registro {json.dumps(data)} {acao} com sucesso no modelo {model.__name__}."
    }, 201
