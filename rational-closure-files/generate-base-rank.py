import os 
import json


def read_file_json(filename):
    with open(filename, "r+") as f:
        jsonFile = json.load(f)
        return jsonFile
    

def convert_rank_to_right_format(filename, filewrite):
    jsonFile = read_file_json(filename)
    models = jsonFile['Call'][0]['Witnesses'][0]['Value']
    for model in models:
        with open(filewrite, "a+") as f:
            f.write(f"{model}.\n")

convert_rank_to_right_format("90-10-uniform.txt","90-10-br.lp")