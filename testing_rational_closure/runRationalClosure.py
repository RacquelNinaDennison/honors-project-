import os
import subprocess
import json

class RunRationalClosureTest():
    def generate_base_rank(self, queryFileName, outputFile):
        clingo_command = [
            "clingo", 
            "--outf=2", 
            "--quiet=1",  
            "base-rank.lp", 
            f"{queryFileName}", 
        ]
        result = subprocess.run(clingo_command, capture_output=True, text=True)
        with open(outputFile, "w") as file:
            file.write(result.stdout)

    def generate_entailment(self,queryFilePath,outputFilePath,query):
         ranked = []
         with open(queryFilePath) as file:
            jsonFile = json.load(file)
            ranked =  jsonFile["Call"][0]["Witnesses"][0]["Value"]
         with open(outputFilePath, "w+") as file:
             for ranked_statement in ranked:
                 file.write(f"{ranked_statement}.\n")
             file.write(f"{query}.\n")
             file.write(f"#const number_of_statements={len(ranked)}.\n")
        
         clingo_command = [
            "clingo", 
            "--outf=2", 
            "--quiet=1",   
            f"{outputFilePath}", 
            "rational-closure.lp"
        ]
         result = subprocess.run(clingo_command, capture_output=True, text=True)
         try:
            jsonFile = json.loads(result.stdout)
            return jsonFile["Call"][0]["Witnesses"][0]["Value"]
         except json.JSONDecodeError:
            print("Error decoding JSON from Clingo output")
            return None
def main(knowledge_base_rank, query, queryfilename, subdirectory,entailmentPath):
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
    queryFilePath = os.path.join(subdirectory, queryfilename)
    with open(queryFilePath, "w+") as file:
        for knowledge_statement in knowledge_base_rank:
            file.write(f"{knowledge_statement}.\n")
        file.write(f"#const number_of_statements={len(knowledge_base_rank)}.\n")
    runRationalClosure = RunRationalClosureTest()
    outputFilePath = os.path.join(subdirectory, f"{query}.json")
    entailmentFilePath = os.path.join(subdirectory, f"{entailmentPath}.lp")
    runRationalClosure.generate_base_rank(queryFilePath, outputFilePath)
    return runRationalClosure.generate_entailment(outputFilePath,entailmentFilePath,query)[0]

