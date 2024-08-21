import json
import re
import os

def convert_rank_to_right_format(filedirectory, filename, filewritedirectory, filewrite):
    jsonFile = read_file_json(filedirectory, filename)
    models = jsonFile['Call'][0]['Witnesses'][0]['Value']
    filewritedirectory = os.path.join(filedirectory, "normalised")
    os.makedirs(filewritedirectory, exist_ok=True)

    for model in models:
        start = model.find("(")
        middle = model.find(",")
        end = len(model)
        antecedent = model[start+1:middle]
        consequence = model[middle+1:end-1]

        if '-' in consequence:
            negation = consequence.find("-")
            consequence = f"!{consequence[negation+1:]}"

        with open(os.path.join(filewritedirectory, filewrite), "a+", encoding='utf-8') as f:
            f.write(f"{antecedent} |~ {consequence}\n")

def print_base_rank_visual(filedirectory, filename, filewrite):
    jsonFile = read_file_json(filedirectory, filename)
    values = jsonFile['Call'][0]['Witnesses'][0]['Value']
    rank_dict = {}

    for value in values:
        match = re.match(r"rank\((m_implication\(.+\)),(\d+|inf)\)", value)
        if match:
            m_implication = match.group(1)
            rank = match.group(2)
            rank = float('inf') if rank == "inf" else int(rank)
            m_implication = m_implication[m_implication.find("(")+1:m_implication.find(")")]
            
            if rank in rank_dict:
                rank_dict[rank].append(m_implication)
            else:
                rank_dict[rank] = [m_implication]
                    
    with open(os.path.join(filedirectory, filewrite), "w+", encoding='utf-8') as f:
        for rank, implications in sorted(rank_dict.items()):
            if rank == float('inf'):
                f.write(f"Rank inf: ")
                for implication in implications:
                    f.write(f"{implication[:implication.find(',')]}->{implication[implication.find(',')+1:]},")
            else:
                f.write(f"Rank {rank}: ")
                for implication in implications:
                    f.write(f"{implication[:implication.find(',')]}|~{implication[implication.find(',')+1:]},")
            f.write("\n")

def time_for_completion(filedirectory, filename):
    jsonFile = read_file_json(filedirectory, filename)
 
    return jsonFile

def read_file_json(filedirectory, filename):
    file_path = os.path.join(filedirectory, filename)
    
    # Check if the file is empty
    if os.stat(file_path).st_size == 0:
        return
    
    with open(file_path, "r") as f:
        file_content = f.read()
        # return file_content[file_content.find("Total")+ 8:file_content.find("Total")+13]
        try:
            jsonFile = json.loads(file_content)
            return jsonFile
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON in file {filename}: {str(e)}")




def compute_time_base_rank(filedir, filename):
    statements = filename[filename.find("s")+3:filename.find("-")]
    slice= filename[filename.find("_"):]
    slice = slice[slice.find("_"):]
    slice = slice[slice.find("-")+1:]
    ranks = slice[:slice.find("_")]
    print(ranks)
    time = time_for_completion(filedir, filename)
    if(time == None):
        return
    time = time['Time']['Total']
    filewrite = ""
    if(filename.find("jumpy") != -1):
        filewrite = "knowledge-gen-random-time-jumpy-2.csv"
    elif (filename.find("tweety") != -1):
        filewrite = "knowledge-gen-random-time-tweety-2.csv"
    else:
        filewrite = "knowledge-gen-random-time-2.csv"
    with open(filewrite, "a+", encoding='utf-8') as file:
         file.writelines(f"{statements}, {ranks}, {time}\n")
def main():
    input_directory = "results_knowledge_base_random_c"
    files = os.listdir(input_directory)
    files.sort()
    for filename in files:
        if filename.startswith('.') or filename.startswith('S_'):
            print(f"Skipping system or hidden file: {filename}")
            continue
        compute_time_base_rank(input_directory, filename)
if __name__ == "__main__":
    main()
