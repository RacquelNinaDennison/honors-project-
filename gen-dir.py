import os 
def make_directories_if_not_exist():
    os.makedirs("results_base_rank", exist_ok=True)
    os.makedirs("results_knowledge_gen", exist_ok=True)
    os.makedirs("knowledge-base-instances", exist_ok=True)
    os.makedirs("formatted-knowledge-bases", exist_ok=True)


make_directories_if_not_exist()