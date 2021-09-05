from flask import Blueprint
from utility import load_states_suffix_tree, sanitize_string

bp = Blueprint('example_blueprint', __name__)
# First we import the json file and build the suffix tree based on that
mexico_suffix_tree, metadata = load_states_suffix_tree("app\\data\\mexico_states.json")

@bp.route('/filter/<argument>')
def filter_states(argument: str):

	if not len(argument):
		return {"results": 0, "states" : []}
	#sanatize the argument before searching the string in the tree
	argument = sanitize_string(argument)

	# find all the states that match with the argument and extract
	# the information from the metadata and than it convert the list to set and than to list again
	# the reason I did it that way is because there was a loop when you search chihuahua so it returnsa list of chihuahua state 2 times
	# I was afraid it was a bug but it is part of the algorithm
	result = list(set([ metadata[state_code].capitalize() for state_code, _ in mexico_suffix_tree.find_all(argument) ]))

	return {"results": len(result) ,"states" : result}


@bp.route('/')
def get_all_states():
    return { code : state.capitalize() for code, state in metadata.items() }

