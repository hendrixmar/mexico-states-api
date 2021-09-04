import re
import logging
import json
from suffix_tree import Tree
import os
import platform

logging.basicConfig(filename='mexico_states_api.log', level=logging.INFO,
					format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

flask_logger = logging.getLogger(__name__)


def sanitize_string(input_string: str) -> str:
	return re.sub(r'[\\\!"\#\$%\&\'()\*,-./\:;<=>\?\@\[\]^^_`\{\|\}~+¡]+', " ", input_string).upper()

def load_states_suffix_tree(json_file : str):
	"""
	      Build the suffix tree using Ukkonen’s algorithm
	          :param json_file:
	          :return: suffix tree, states metadata
	"""
	cwd = os.getcwd()
	if platform.system() == "Windows":
		path = f"{cwd}\\{json_file}"
	else:
		json_file = json_file.replace("\\", "/")
		path = f"{cwd}/{json_file}"

	with open(path) as f:
		metadata = json.load(f)

	return Tree(metadata), metadata




