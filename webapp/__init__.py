import flask
from flask import json
from sisdiconpra.persistence import db
from sisdiconpra.api.v1 import usuarios as api_usuarios
from sisdiconpra.api.v1 import ocorrencias as api_ocorrencias
from sisdiconpra.api.v1 import aluno as api_alunos

from sisdiconpra.webapp import usuarios as crud_usuarios
from sisdiconpra.webapp import ocorrencias as crud_ocorrencias
from sisdiconpra.webapp import alunos as crud_alunos

def create_app():
    app = flask.Flask(__name__)

    app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'
    app.config['FLASK_ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senha@localhost/pi'


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    @app.before_first_request
    def init_app():
        #inicializa o SQLAlchemy atrelado ao app Flask
        db.init_app(app)

        # cria no banco as tabelas baseando-se no modelo das classes
        import sisdiconpra.models
        db.create_all()

    @app.errorhandler(Exception)
    def unhandled_exception(error):
        app.logger.exception("Uncaught exception")
        response = app.response_class(
            response=json.dumps({'mensagem': 'Ocorreu um erro', 'erro': str(error)}),
            mimetype='application/json',
            status=500,
        )
        return response

    app.register_blueprint(crud_usuarios.api, url_prefix='/webapp')
    app.register_blueprint(crud_ocorrencias.api, url_prefix='/webapp/ocorrencias')
    app.register_blueprint(crud_alunos.api, url_prefix='/webapp/alunos')
    
    app.register_blueprint(api_usuarios.api, url_prefix='/api/v1/usuarios')
    app.register_blueprint(api_ocorrencias.api, url_prefix='/api/v1/ocorrencias')
    app.register_blueprint(api_alunos.api, url_prefix='/api/v1/alunos')

    return app
