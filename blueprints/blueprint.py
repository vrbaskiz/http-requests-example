from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/blueprint')
def hello():
    return "Hello from blueprint!"
