import flask

from sisdiconpra.models.User import User
from sisdiconpra.models.Ocorrencia import Ocorrencia
from sisdiconpra.persistence import db

name = "sisdiconpra.ocorrencias"
api = flask.Blueprint(name, __name__, static_folder="static", template_folder="templates")


@api.route('/', methods=["GET"])
def index():
    return flask.render_template("index.html")

@api.route('/ocorrencias', methods=["GET"])
def listar_ocorrencias():
    ocorrencias = Ocorrencia.query.all()
    return flask.render_template("ocorrencias/lista.html", ocorrencias = [x.json() for x in ocorrencias])

