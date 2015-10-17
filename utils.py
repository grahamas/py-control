import json

def load_json(json_path):
	with open(json_path,'r') as json_file:
		json_dct = json.load(json_file)
	return json_dct