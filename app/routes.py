from flask import Blueprint, current_app
from flask_restx import Resource, Namespace
from .model import Residencias, PrecoMedio
from .db_controllers import recuperar_dados_por_vizinhanca, atualiza_like_residencia
from flask_restx import reqparse


blueprint_residencias = Blueprint("residencias", __name__)

ns_residencia = Namespace("residencias", description="Api de Residencias")


@ns_residencia.route("/")
class ApiResidencias(Resource):
    @ns_residencia.doc("lista de residencias")
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("neighbourhood_group", type=str, required=True)
        args = parser.parse_args()
        session = current_app.db.session
        lista_de_resultados, status_code = recuperar_dados_por_vizinhanca(
            session, Residencias, args
        )

        return [residencia.to_json() for residencia in lista_de_resultados], status_code

    @ns_residencia.doc("atualiza residencia")
    def post(self):
        session = current_app.db.session
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=str, required=True)
        parser.add_argument("like", type=str, required=True)
        args = parser.parse_args()
        filtro = args.get("id")
        like = args.get("like", False)
        like = True if like == "true" else False
        resultado = atualiza_like_residencia(session, Residencias, filtro, like)
        return resultado


blueprint_preco_medio = Blueprint("preco-medio", __name__)

ns_preco_media = Namespace("preco-medio", description="Api de Preço Médio")


@ns_preco_media.route("/")
class ApiPrecoMedio(Resource):
    @ns_preco_media.doc("lista de preço médio")
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("neighbourhood_group", type=str, required=True)
        args = parser.parse_args()
        session = current_app.db.session
        lista_de_resultados, status_code = recuperar_dados_por_vizinhanca(
            session, PrecoMedio, args
        )
        if not isinstance(lista_de_resultados, list):
            return lista_de_resultados, status_code

        print("-----------------------", lista_de_resultados[0])
        return [vizinhanca.to_json() for vizinhanca in lista_de_resultados], status_code
