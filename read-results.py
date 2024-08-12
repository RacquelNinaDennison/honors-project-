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
    time = jsonFile.get('Time', {}).get('Total', 'Time field not found')
    print(f"Time: {time}")
    return time

def read_file_json(filedirectory, filename):
    file_path = os.path.join(filedirectory, filename)
    with open(file_path, "r", encoding='utf-8') as f:
        jsonFile = json.load(f)
        return jsonFile



def compute_time_base_rank(filedir, filename):
    statements = filename[filename.find("s")+3:filename.find("-")]
    ranks = filename[filename.find("-")+1:filename.find("u")-1]
    print(statements, ranks)
    time = time_for_completion(filedir, filename)
    with open("knowledge-gen-uniform-time-250.csv", "a+", encoding='utf-8') as file:
         file.writelines(f"{statements}, {ranks}, {time}\n")
def main():
    input_directory = "results_knowledge_base_uniform"
    files = os.listdir(input_directory)
    files.sort()
    for filename in files:
        if filename.startswith('.') or filename.startswith('S_'):
            print(f"Skipping system or hidden file: {filename}")
            continue
        compute_time_base_rank(input_directory, filename)
if __name__ == "__main__":
    main()
