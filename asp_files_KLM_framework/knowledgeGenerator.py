from asp_files_KLM_framework.distributionClass import Distribution

import subprocess
class KnowledgeGenerator():

    def __init__(self,amount_of_statements, amount_of_ranks, classical_included, encodeded, amount_of_encoded, distribution):
        self.amount_of_statements = amount_of_statements
        self.amount_of_ranks = amount_of_ranks
        self.amount_of_encoded = amount_of_encoded
        self.classical_included = classical_included
        self.encoded_included = encodeded
        self.distribution = distribution
        self.knowledge_gen_programs = {"knowledge-gen-instances":"knowledge-base-problem-instances.lp","knowledge-gen-class":"knowledge-base-problem-class.lp","functions":"functions.lp" }

    def set_parameters(self):
        distribution_values = Distribution(self.amount_of_ranks, self.amount_of_statements)
        if(self.distribution == "linear"):
            self.amount_of_statements = distribution_values.linear_growth()
        if(self.amount_of_statements < 2*self.amount_of_ranks -1):
            self.amount_of_statements = 2*self.amount_of_ranks-1
        uniform_flag = 1 if self.distribution == "uniform" else 0
        linear_flag = 1 if self.distribution == "linear" else 0
        random_flag = 1 if self.distribution == "random" else 0
        encoded_flag = 1 if self.encoded_included == "True" else 0
        classical_flag = 1 if self.classical_included == "True" else 0
        return uniform_flag,random_flag,linear_flag, encoded_flag,classical_flag
    def generate_knowledge_base(self, output_file="output.txt"):
        uniform_flag, random_flag, linear_flag, encoded_flag, classical_flag = self.set_parameters()
        clingo_command = [
            "clingo", 
            "--outf=2", 
            "--quiet=1",  
            f'{self.knowledge_gen_programs["knowledge-gen-instances"]}', 
            f"-c amount_of_ranks={self.amount_of_ranks}", 
            f"-c amount_of_statements={self.amount_of_statements}", 
            f"-c uniform={uniform_flag}",
            f"-c random={random_flag}",
            f"-c linear={linear_flag}", 
            f"-c classical_included={classical_flag}",
            f'{self.knowledge_gen_programs["knowledge-gen-class"]}', 
            "functions.lp"
        ]
        
        result = subprocess.run(clingo_command, capture_output=True, text=True)
        with open(output_file, "w") as file:
            file.write(result.stdout)







