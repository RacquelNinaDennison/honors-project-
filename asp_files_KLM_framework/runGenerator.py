import argparse
from asp_files_KLM_framework.knowledgeGenerator import KnowledgeGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate a knowledge base.')
    parser.add_argument('amount_of_statements', type=int, nargs='?', default=0, help='Number of statements (default: 0)')
    parser.add_argument('amount_of_ranks', type=int, nargs='?', default=0, help='Number of ranks (default: 0)')
    parser.add_argument('classical_statements', type=int, nargs='?', default=0, help='Classical statements included (default: 0)')
    parser.add_argument('encoded', type=int, nargs='?', default=0, help='Encoded statements included (default: 0)')
    parser.add_argument('amount_of_encoded', type=int, nargs='?', default=0, help='Amount of encoded statements (default: 0)')
    parser.add_argument('distribution', type=str, nargs='?', default='uniform', help='Distribution type (default: "none")')
    args = parser.parse_args()
    knowledgeGeneratorInstance = KnowledgeGenerator(
        args.amount_of_statements,
        args.amount_of_ranks,
        args.classical_statements,
        args.encoded,
        args.amount_of_encoded,
        args.distribution
    )
    knowledgeGeneratorInstance.generate_knowledge_base()

if __name__ == "__main__":
    main()
