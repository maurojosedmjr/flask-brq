from flask import Blueprint, current_app, request
from flask_restx import Resource, Namespace, fields
from .model import Residencias
from .db_controllers import recuperar_dados


blueprint_departamento = Blueprint("residencias", __name__)

ns_residencia = Namespace("residencias", description="Api de Residencias")

departamento = ns_residencia.model(
    "Residencias",
    {
        "nome": fields.String(required=True, description="Nome do departamento"),
    },
)


@ns_residencia.route("/")
class Departamentos(Resource):
    @ns_residencia.doc("lista de residencias")
    def get(self):
        session = current_app.db.session
        lista_de_departamentos, status_code = recuperar_dados(session, Residencias)

        return [
            residencia.to_json() for residencia in lista_de_departamentos
        ], status_code

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
