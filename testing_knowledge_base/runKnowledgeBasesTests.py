import unittest
from knowledgeBaseGenerator import main
import re

class TestKnowledgeGenerator(unittest.TestCase):
    def test_knowledge_gen_no_distribution(self):
        """Testing the number of ranks and statements are generated correctly no distribution specified"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 5
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, '')
        generated_number_of_statements = 0 
        generated_number_of_ranks = len(result)
        for statement in result:
            match = re.search(pattern, statement)
            if match:
                statements_count = int(match.group(1)) 
                generated_number_of_statements += statements_count
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_uniform(self):
        """Testing the number of ranks and statements are generated correctly with uniform dis"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 5
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, 'uniform')
        generated_number_of_statements = 0 
        generated_number_of_ranks = len(result)
        for statement in result:
            match = re.search(pattern, statement)
            if match:
                statements_count = int(match.group(1)) 
                generated_number_of_statements += statements_count
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_linear(self):
        """Testing the number of ranks and statements are generated correctly with linear dis"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 5
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, 'linear')
        generated_number_of_statements = 0 
        generated_number_of_ranks = len(result)
        for statement in result:
            match = re.search(pattern, statement)
            if match:
                statements_count = int(match.group(1)) 
                generated_number_of_statements += statements_count
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_random(self):
        """Testing the number of ranks and statements are generated correctly with linear dis"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 5
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, 'random')
        generated_number_of_statements = 0 
        generated_number_of_ranks = len(result)
        for statement in result:
            match = re.search(pattern, statement)
            if match:
                statements_count = int(match.group(1)) 
                generated_number_of_statements += statements_count
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_less_statements_than_ranks(self):
        """Testing the number of ranks and statements with statements less than ranks"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 5
        number_of_statements = 3
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, '')
        
        generated_number_of_statements = 0 
        generated_number_of_ranks = len(result)
        for statement in result:
            match = re.search(pattern, statement)
            if match:
                statements_count = int(match.group(1)) 
                generated_number_of_statements += statements_count
        self.assertEqual(2*number_of_ranks-1,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_no_distribution_one_rank(self):
        """Testing that specifying number of ranks = 1"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 1
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, '')
        generated_number_of_ranks = len(result)
        generated_number_of_statements = 100 
        generated_number_of_ranks = len(result)+1
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_linear_one_rank(self):
        """Testing that specifying number of ranks = 1"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 1
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, 'linear')
        generated_number_of_ranks = len(result)
        generated_number_of_statements = 100 
        generated_number_of_ranks = len(result)+1
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_random_one_rank(self):
        """Testing that specifying number of ranks = 1"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 1
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, 'random')
        generated_number_of_ranks = len(result)
        generated_number_of_statements = 100 
        generated_number_of_ranks = len(result)+1
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)
    def test_knowledge_gen_uniform_one_rank(self):
        """Testing that specifying number of ranks = 1"""
        pattern = r'statement_count\(\d+,\s*(\d+)\)'
        number_of_ranks = 1
        number_of_statements = 100
        result = main(number_of_statements, number_of_ranks, 0, 0, 0, 'uniform')
        generated_number_of_ranks = len(result)
        generated_number_of_statements = 100 
        generated_number_of_ranks = len(result)+1
        self.assertEqual(number_of_statements,generated_number_of_statements)
        self.assertEqual(number_of_ranks,generated_number_of_ranks)




if __name__ == '__main__':
    unittest.main()
