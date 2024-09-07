from knowledgeGenerator import KnowledgeGenerator


def main(amount_of_statements, amount_of_ranks, classical_statements, encoded, amount_of_encoded, distribution):
    knowledgeGeneratorInstance = KnowledgeGenerator(amount_of_statements, amount_of_ranks, classical_statements, encoded, amount_of_encoded, distribution)
    knowledgeGeneratorInstance.generate_knowledge_base()

if __name__ =="__main__":
    main(5,2,0,0,0,"uniform")
