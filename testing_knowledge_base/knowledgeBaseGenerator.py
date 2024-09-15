from asp_files_KLM_framework.distributionClass import Distribution
import argparse
import subprocess
import json 
class KnowledgeGenerator:
    def __init__(self, number_of_statements, number_of_ranks, classical_included, encoded, number_of_encoded, distribution):
        self.number_of_statements = number_of_statements
        self.number_of_ranks = number_of_ranks
        self.number_of_encoded = number_of_encoded
        self.classical_included = classical_included
        self.encoded_included = encoded
        self.distribution = distribution
        self.knowledge_gen_programs = {
            "knowledge-gen-instances": "knowledge-base-problem-instance.lp",
            "knowledge-gen-class": "knowledge-base-problem-class.lp",
            "functions": "functions.lp"
        }

    def set_parameters(self):
        distribution_values = Distribution(self.number_of_ranks, self.number_of_statements)
        if self.distribution == "linear":
            self.number_of_statements = distribution_values.linear_growth()
        if self.number_of_statements < 2 * self.number_of_ranks - 1:
            self.number_of_statements = 2 * self.number_of_ranks - 1
        uniform_flag = 1 if self.distribution == "uniform" else 0
        linear_flag = 1 if self.distribution == "linear" else 0
        random_flag = 1 if self.distribution == "random" else 0
        encoded_flag = 1 if self.encoded_included == "True" else 0
        classical_flag = 1 if self.classical_included == "True" else 0
        return uniform_flag, random_flag, linear_flag, encoded_flag, classical_flag

    def generate_knowledge_base(self, output_file=None):
        uniform_flag, random_flag, linear_flag, encoded_flag, classical_flag = self.set_parameters()
        clingo_command = [
            "clingo", 
            "--outf=2", 
            "--quiet=1",  
            f'{self.knowledge_gen_programs["knowledge-gen-instances"]}', 
            f"-c number_of_ranks={self.number_of_ranks}", 
            f"-c number_of_statements={self.number_of_statements}", 
            f"-c uniform={uniform_flag}",
            f"-c random={random_flag}",
            f"-c linear={linear_flag}", 
            f"-c classical_included={classical_flag}",
            f'{self.knowledge_gen_programs["knowledge-gen-class"]}', 
            "functions.lp"
        ]
        
        result = subprocess.run(clingo_command, capture_output=True, text=True)
        if(output_file != None):
            with open(output_file, "w") as file:
                file.write(result.stdout)
        else:
            jsonFile = json.loads(result.stdout)
            return jsonFile["Call"][0]["Witnesses"][0]["Value"]



def main(number_of_statements=None, number_of_ranks=None, classical_statements=None, encoded=None, number_of_encoded=None, distribution=None):
    """Main function that accepts both function parameters and command-line arguments."""
    
    if number_of_statements is not None and number_of_ranks is not None and classical_statements is not None and encoded is not None and number_of_encoded is not None and distribution is not None:
        knowledgeGeneratorInstance = KnowledgeGenerator(
            number_of_statements,
            number_of_ranks,
            classical_statements,
            encoded,
            number_of_encoded,
            distribution
        )
    else:
        parser = argparse.ArgumentParser(description='Generate a knowledge base.')
        parser.add_argument('number_of_statements', type=int, nargs='?', default=0, help='Number of statements (default: 0)')
        parser.add_argument('number_of_ranks', type=int, nargs='?', default=0, help='Number of ranks (default: 0)')
        parser.add_argument('classical_statements', type=int, nargs='?', default=0, help='Classical statements included (default: 0)')
        parser.add_argument('encoded', type=int, nargs='?', default=0, help='Encoded statements included (default: 0)')
        parser.add_argument('number_of_encoded', type=int, nargs='?', default=0, help='Number of encoded statements (default: 0)')
        parser.add_argument('distribution', type=str, nargs='?', default='uniform', help='Distribution type (default: "uniform")')
        args = parser.parse_args()

        knowledgeGeneratorInstance = KnowledgeGenerator(
            args.number_of_statements,
            args.number_of_ranks,
            args.classical_statements,
            args.encoded,
            args.number_of_encoded,
            args.distribution
        )
    return knowledgeGeneratorInstance.generate_knowledge_base()

