from flask import Blueprint

initial_bp = Blueprint('initial', __name__)

@initial_bp.route('/', methods=['GET'])
def initial():
    return 'Server Working.'

