import flask

from sisdiconpra.models.User import User
from sisdiconpra.persistence import db

name = "sisdiconpra.usuarios"
api = flask.Blueprint(name, __name__, static_folder="static", template_folder="templates")


@api.route('/', methods=["GET"])
def index():
    return flask.render_template("index.html")

@api.route('/usuarios', methods=["GET"])
def listar_usuarios():
    usuarios = User.query.all()
    return flask.render_template("usuarios/lista.html", usuarios = [x.json() for x in usuarios])

@api.route('/usuarios/novo', methods=["GET"])
def novo_usuario():
    return flask.render_template("usuarios/novo.html")

@api.route('/usuarios/novo', methods=["POST"])
def processa_novo_usuario():
    result = flask.request.form
    usuario = User()
    usuario.name = result['name']
    usuario.email = result['email']
    db.session.add(usuario)
    db.session.commit()
    
    return flask.redirect(flask.url_for('sisdiconpra.usuarios.listar_usuarios'))
