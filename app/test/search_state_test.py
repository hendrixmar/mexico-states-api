import os
import string
import random
import re
import platform
from suffix_tree import Tree
import pytest
import json

def load_states_suffix_tree(json_file : str):
	"""
	      Build the suffix tree using Ukkonen’s algorithm
	          :param json_file:
	          :return: suffix tree, states metadata
	"""
	cwd = os.getcwd()
	if platform.system() == "Windows":
		path = f"{cwd}\\app\\test\\{json_file}"
	else:

		path = f"{cwd}/app/test/{json_file}"

	with open(path) as f:
		metadata = json.load(f)

	return Tree(metadata), metadata

def brute_force(metadata : {}, search_string : str):

	output = set()
	for i in metadata.values():

		if search_string.upper() in i:

			output.add(i.capitalize() )


	return output


def test_answer():
	state_suffix_tree, metadata = load_states_suffix_tree("mexico_states.json")

	for _ in range(200):

		state = random.choice(list(metadata.values()))
		a = random.randint(0,len(state) // 2)
		b =  random.randint(a + 1, len(state))

		search_test = state[a:b]

		result = set([metadata[state_code].capitalize() for state_code, _ in state_suffix_tree.find_all(search_test)])

		answer = brute_force(metadata, search_test)

		if answer != result:
			pytest.fail(f"Test case {_}: {result} -->> correct {answer}")








