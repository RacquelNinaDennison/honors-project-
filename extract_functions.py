import json
import os 
def read_file_json(filedirectory, filename):
    with open(os.path.join(filedirectory, filename)) as f:
        jsonFile = json.load(f)
        return jsonFile

def extract(filedirectory, filename, filewritedirectory, filewrite):
    jsonFile = read_file_json(filedirectory, filename)
    models = jsonFile['Call'][0]['Witnesses'][0]['Value']
    for model in models:
        with open(os.path.join(filewritedirectory, filewrite), "a+") as f:
            f.writelines(f"{model}.\n") 

def main():
    input_directory = "results_knowledge_gen"
    output_directory = "formatted-knowledge-bases"
    os.makedirs(output_directory, exist_ok=True)
    
    files = os.listdir(input_directory)
    files.sort()
    for filename in files:
        output_file_kb = filename[:filename.find(".")] + "-kb.lp"
        extract(input_directory, filename, output_directory, output_file_kb)

if __name__ == "__main__":
    main()
