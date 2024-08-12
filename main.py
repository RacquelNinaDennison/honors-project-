from rankgen import RankGenerator
import sys




def main(filename,number_of_statements,number_of_ranks,classical_included, distribution):
    if (number_of_statements < 2*number_of_ranks-1):
        print("The number of statements limits the amound of ranks")
        number_of_ranks = int(input("Enter the amount of ranks"))
        number_of_statements = int(input("Enter the amount of statements"))
    rankGen = RankGenerator(ranks= number_of_ranks,statements = number_of_statements, filename=filename, classical_included=classical_included, distribution=distribution)
    rankGen.generate_ranks()
    rankGen.write_to_file()


if __name__ == "__main__":
    main(filename = sys.argv[1], number_of_statements=int(sys.argv[2]), number_of_ranks=int(sys.argv[3]), classical_included = sys.argv[4], distribution= sys.argv[5])