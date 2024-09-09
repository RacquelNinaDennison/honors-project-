import os
import subprocess
import unittest

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


def main(knowledge_base_rank, query, queryFileName, subdirectory):
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
    queryFilePath = os.path.join(subdirectory, queryFileName)
    with open(queryFilePath, "w+") as file:
        file.write(f"{query}.\n")
        for knowledge_statement in knowledge_base_rank:
            file.write(f"{knowledge_statement}.\n")
        file.write(f"#const number_of_statements={len(knowledge_base_rank)}.\n")
    runRationalClosure = RunRationalClosureTest()
    outputFilePath = os.path.join(subdirectory, f"{query}.json")
    runRationalClosure.generate_rational_closure(queryFilePath, outputFilePath)

