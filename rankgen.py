import os 
class RankGenerator():
    def __init__(self,ranks,statements,filename,classical_included, distribution):
        self.ranks= ranks
        self.statements = statements
        self.indexValue = 0
        self.clash_atoms=[]
        self.clashed_atoms = []
        self.atoms =[]
        self.clash_literal = ["l0"]
        self.general_statements = []
        self.filename = filename
        self.classical_included = classical_included
        self.distribution = distribution
        self.output_dir = "knowledge-base-instances"

    # helper functions
    def __increase_index(self):
        self.indexValue += 1
    def __reset_index(self):
        self.indexValue = 0

    def generate_ranks(self):
        # generate the ranking clash variables
        while self.indexValue < self.ranks -1 :
            self.clash_atoms.append(f"a{self.indexValue},a{self.indexValue+1}")
            # adding the atoms into clashed_atoms
            if f"a{self.indexValue}" not in self.clashed_atoms:
                self.clashed_atoms.append(f"a{self.indexValue}")
            if f"a{self.indexValue+1}" not in self.clashed_atoms:
                self.clashed_atoms.append(f"a{self.indexValue+1}")
            
            self.__increase_index()  
        # generate the atoms to add to the atoms generated
        for i in range(0,self.ranks):
            self.atoms.append(f"a{i}")  
        while self.statements > len(self.atoms):
            self.atoms.append(f'a{self.indexValue}')
            self.__increase_index()
        self.__reset_index()

        if self.ranks == 0:
            while self.indexValue < self.statements:
                self.atoms.append(f"a{self.indexValue}")
                self.__increase_index()
            self.__reset_index()
    def write_to_file(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        file_path = os.path.join(self.output_dir, f"{self.filename}.lp")

        with open(file_path,"w") as f:
            for atom in self.clash_atoms:
                f.writelines(f"clash({atom}).")
                f.write('\n')
            for atom in self.clash_literal:
                f.writelines(f"clash_literal({atom}).")
                f.write('\n')
            for atom in self.clashed_atoms:
                f.writelines(f"clashed_atom({atom}).")
                f.write('\n')
            for atom in self.atoms:
                f.writelines(f"atom({atom}).")
                f.write("\n")
            f.writelines(f"#const amount_of_statements= {self.statements}.\n")
            if self.classical_included.lower() == "true":
                f.write("classical_included.\n")
            f.writelines(f"#const amount_of_ranks= {self.ranks}.\n")
            if self.distribution.lower() == "uniform":
                f.writelines(f"distribution_specified.\n")
                f.writelines(f"uniform.\n")
                
