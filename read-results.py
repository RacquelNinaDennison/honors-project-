import json
import re
import os

uniform = {}
random = {}

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
        return file_content[file_content.find("Total")+ 8:file_content.find("Total")+13]

def compute_time_base_rank(filedir, filename, statements, ranks, filewrite):
    time = time_for_completion(filedir, filename)
    if time is None:
        return
    with open(filewrite, "a+", encoding='utf-8') as file:
        file.writelines(f"{statements}, {ranks}, {time}\n")

def extract_time(input_directory):
    for experiment_dir in input_directory:
        subdirs = os.listdir(experiment_dir)
        subdirs.sort()
        index = experiment_dir[experiment_dir.find("_")+1+experiment_dir[experiment_dir.find("_")+1:].find("_")+1:]
        output_dir = f'experiment_results_{index}'
        os.makedirs(output_dir, exist_ok=True)
        for subdir in subdirs:
            subdir_path = os.path.join(experiment_dir, subdir)
            if not os.path.isdir(subdir_path):
                continue
            files = os.listdir(subdir_path)
            files.sort()
            for filename in files:
                if filename.startswith('.') or filename.startswith('S_'):
                    print(f"Skipping system or hidden file: {filename}")
                    continue
                parts = filename.split('_')
                print(parts)
                config = parts[-1].split('.')[0]
                dis = parts[3]
                numbers_part = parts[2]
                config = "no-config" if config == "config" else config
                statement_count, ranks = numbers_part.split('-')
                filename_out = os.path.join(output_dir, f"knowledge-gen-{config}-time-final-{dis}.csv")
                compute_time_base_rank(subdir_path, filename, statement_count, ranks, filename_out)

def average_time(input_file, config, dis):
    # Select the correct dictionary based on the distribution type
    dictionary = uniform if dis == "uniform" else random

    if config not in dictionary:
        dictionary[config] = {}

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip().split(",")
            statement_count = line[0]
            rank = line[1]
            time = float(line[2])
            
            if statement_count not in dictionary[config]:
                dictionary[config][statement_count] = {}
            
            if rank not in dictionary[config][statement_count]:
                dictionary[config][statement_count][rank] = 0.0
            
            dictionary[config][statement_count][rank] += time

def average_out_dis():
    for key in uniform:
        for key_statement in uniform[key]:
            print(key_statement)
            print(uniform[key][key_statement])
            for rank_key in (uniform[key][key_statement]):
                 uniform[key][key_statement][rank_key] = round(uniform[key][key_statement][rank_key] / 5, 5)

    for key in random:
        for key_statement in random[key]:
            print(key_statement)
            print(random[key][key_statement])
            for rank_key in (random[key][key_statement]):
                 random[key][key_statement][rank_key] = round(random[key][key_statement][rank_key] / 5, 5)

def print_distributions(path, dic, dis):
    for key in dic:
        filename = f'knowledge-gen-{key}-time-final-{dis}-average.csv'
        file_path = os.path.join(path, filename)
        with open(file_path,"a+") as file:
            for key_statement in dic[key]:
                for key_rank in dic[key][key_statement]:
                    line = f'{key_statement}, {key_rank}, {dic[key][key_statement][key_rank]}'
                    file.writelines(line+"\n")
        


def main():
    input_directory = ["experiment_files_1", "experiment_files_2", "experiment_files_3", "experiment_files_4"]
    results_dir = ["experiment_results_0", "experiment_results_1", "experiment_results_2", "experiment_results_3", "experiment_results_4"]
    for results in results_dir:
        files = os.listdir(results)
        files.sort()
        for file in files:
            path = os.path.join(results, file)
            parts = file.split('-')
            dis = parts[-1].split('.')[0]
            config = parts[2]
            config = "no-config" if config == "no" else config
            if dis == "uniform":
                if config not in uniform:
                    uniform[config] = {}
                average_time(path, config, dis)
            else:
                if config not in random:
                    random[config] = {}
                average_time(path, config, dis)
    average_out_dis()
    average_path = "experiment_results_averaged"
    print_distributions(average_path,uniform, "uniform")
    print_distributions(average_path,random, "random")
if __name__ == "__main__":
    main()
