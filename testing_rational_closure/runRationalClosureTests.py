from runRationalClosure import main
import unittest


class TestQueryOne(unittest.TestCase):
    def test_query_one(self):
        """Testing if penguins -> fly is entailed by defeasible(birds,fly), defeasible(penguins,-fly),classical(penguins,birds)
           entailed(false) is expected.  
        """
        result = main(["defeasible(birds,fly)","defeasible(penguins,-fly)"],
                      "query(penguins,fly)", "q1.lp", "rational_queries","ranked1")

        returned_value = result
        expected_result = "entailed(false)"
        print(f"Running test for query: 'penguins -> fly'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        
        self.assertEqual(returned_value, expected_result)
    def test_query_two(self):
        """Testing if penguins -> fly is entailed by defeasible(birds,fly), defeasible(penguins,-fly),classical(penguins,birds)
           entailed(false) is expected.  
        """
        result = main(["defeasible(birds,fly)", "defeasible(penguins,-fly)","classical(penguins,birds)"," defeasible(eagles,fly)", "defeasible(birds,wings)","defeasible(eagles,birds)"],
                      "query(eagles,wings)", "q2.lp", "rational_queries","ranked2")

        returned_value = result
        expected_result = "entailed(true)"
        print(f"Running test for query: 'egales->wings'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        
        self.assertEqual(returned_value, expected_result)


if __name__ =="__main__":
    unittest.main()