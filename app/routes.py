from flask import Blueprint

bp = Blueprint('example_blueprint', __name__)


@bp.route('/filter/<argument>')
def filter_states(argument: str):

	return argument

@bp.route('/')
def get_all_states():
    return 'Welcome to Mexico State Api. Created by  <a href="https://www.linkedin.com/in/hendrik-martina-54800468/">Hendrik Martina</a>'

