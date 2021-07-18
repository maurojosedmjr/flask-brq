from flask import Blueprint, current_app, request
from flask_restx import Resource, Namespace, fields
from .model import Residencias
from .db_controllers import recuperar_dados_por_vizinhanca
from flask_restx import reqparse


blueprint_residencias = Blueprint("residencias", __name__)

ns_residencia = Namespace("residencias", description="Api de Residencias")


@ns_residencia.route("/")
class Residencias(Resource):
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

    # @ns_residencia.doc("insere departamento")
    # @ns_residencia.expect(departamento)
    # def post(self):
    #     session = current_app.db.session
    #     schema = DepartamentoSchema()
    #     departamento_data: Dict[str, str] = schema.load(data=json.loads(request.data))
    #     resultado: Tuple[Dict[str, str], int] = inserir_linha(
    #         session, Departamento, departamento_data
    #     )
    #     return resultado


blueprint_preco_medio = Blueprint("preco-medio", __name__)

ns_preco_media = Namespace("preco-medio", description="Api de Preço Médio")


@ns_preco_media.route("/")
class PrecoMedio(Resource):
    @ns_preco_media.doc("lista de preço médio")
    def get(self):
        from app.controllers import processar_dataframes

        processar_dataframes()
        parser = reqparse.RequestParser()
        parser.add_argument("neighbourhood_group", type=str, required=True)
        args = parser.parse_args()
        session = current_app.db.session
        lista_de_resultados, status_code = recuperar_dados_por_vizinhanca(
            session, PrecoMedio, args
        )

        return [residencia.to_json() for residencia in lista_de_resultados], status_code
