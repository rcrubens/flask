import flask

from sisdiconpra.models.Aluno import Aluno
from sisdiconpra.persistence import db

name = "sisdiconpra.alunos"
api = flask.Blueprint(name, __name__, static_folder="static", template_folder="templates")


@api.route('/', methods=["GET"])
def index():
    return flask.render_template("index.html")

@api.route('/alunos', methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return flask.render_template("alunos/lista.html", alunos = [x.json() for x in alunos])

@api.route('/alunos/novo', methods=["GET"])
def novo_aluno():
    return flask.render_template("alunos/novo.html")

@api.route('/alunos/novo', methods=["POST"])
def processa_novo_alunos():
    result = flask.request.form
    aluno = Aluno()
    aluno.nome_completo = result['nome_completo']
    dados_da_foto = flask.request.files['foto']
    aluno.foto = dados_da_foto.read() if dados_da_foto else None
    
    db.session.add(aluno)
    db.session.commit()
    
    return flask.redirect(flask.url_for('sisdiconpra.alunos.listar_alunos'))
