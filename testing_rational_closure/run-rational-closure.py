import os
import subprocess
import json

class RunRationalClosureTest():
    def __init__(self) -> None:
        pass

    def generate_rational_closure(self, queryFileName, outputFile):
        clingo_command = [
            "clingo", 
            "--outf=2", 
            "--quiet=1",  
            "base-rank.lp", 
            f"{queryFileName}", 
            "rational-closure.lp", 
        ]
        result = subprocess.run(clingo_command, capture_output=True, text=True)
        with open(outputFile, "w") as file:
            file.write(result.stdout)
    def read_query(self,queryFileName):
        with open(queryFileName,"r+") as file:
            jsonFile = json.load(file)
            print(jsonFile["Call"][0]["Witnesses"][0]["Value"])

def main(knowledge_base_rank, query,queryfilename, subdirectory):
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
    queryFilePath = os.path.join(subdirectory, queryfilename)
    with open(queryFilePath, "w+") as file:
        file.write(f"{query}.\n")
        for knowledge_statement in knowledge_base_rank:
            file.write(f"{knowledge_statement}.\n")
        file.write(f"#const number_of_statements={len(knowledge_base_rank)}.\n")
    runRationalClosure = RunRationalClosureTest()
    outputFilePath = os.path.join(subdirectory, f"{query}.json")
    runRationalClosure.generate_rational_closure(queryFilePath, outputFilePath)
    runRationalClosure.read_query(outputFilePath)

def defining_test_data():
    knowledge_base_rank = ["defeasible(a,b)", "defeasible(b,c)"]
    query = "query(a,none)"
    subdirectory = "rational_queries"
    queryFileName = "query1.lp"
    main(knowledge_base_rank, query,queryFileName, subdirectory)