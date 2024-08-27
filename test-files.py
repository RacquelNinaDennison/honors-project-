import os

class Compare_Base_Rank:
    def __init__(self, base_rank_ASP, base_rank_JAVA):
        self.base_rank_ASP = base_rank_ASP
        self.base_rank_JAVA = base_rank_JAVA

    def extract_implications(self, line):
        rank, implications = line.split(':', 1)
        implications = implications.strip()[1:-1]
        implications_list = [imp.strip() for imp in implications.split(',')]
        return rank.strip(), sorted(implications_list)

    def compare_files(self, file1_path, file2_path):
        try:
            with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
                lines1 = file1.readlines()
                lines2 = file2.readlines()
                if len(lines1) != len(lines2):
                    print("Files have different number of lines.")
                    return
                for line1, line2 in zip(lines1, lines2):
                    rank1, implications1 = self.extract_implications(line1)
                    rank2, implications2 = self.extract_implications(line2)

                    if rank1 == rank2 and implications1 == implications2:
                        print("Pass")
                    else:
                        print(f"Problem: {line1.strip()} != {line2.strip()}")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def read_directory_files(self):
        base_rank_ASP_files = sorted(os.listdir(self.base_rank_ASP))
        base_rank_JAVA_files = sorted(os.listdir(self.base_rank_JAVA))
        
        for filename in base_rank_ASP_files:
            filename_index = filename.split('_', 1)[0]
            for java_file in base_rank_JAVA_files:
                if java_file.startswith(filename_index):
                    asp_file_path = os.path.join(self.base_rank_ASP, filename)
                    java_file_path = os.path.join(self.base_rank_JAVA, java_file)
                    self.compare_files(asp_file_path, java_file_path)
                    break

def main():
    base_rank_ASP = 'formatted_testing_files_ranks'
    base_rank_JAVA = 'formatted-files-MBDR'
    comparer = Compare_Base_Rank(base_rank_ASP, base_rank_JAVA)
    comparer.read_directory_files()

if __name__ == "__main__":
    main()
