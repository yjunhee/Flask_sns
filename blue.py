from flask import Blueprint

bp = Blueprint('blue', __name__, url_prefix='/blue')


@bp.route("/1")
def print_blue():
    return "Hello Blue"

@bp.route("/2")
def print_blue2():
    return "2"