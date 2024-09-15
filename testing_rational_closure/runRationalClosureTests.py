from runRationalClosure import main
import unittest
class TestQueryOne(unittest.TestCase):
    '''Testing the rational closure implementation with pre defined knowledge bases'''
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

    def test_query_three(self):
        """Testing if boats -> leaky entailed by defeasible(boat,floats;leaky,boat;leaky,-floats;flyingDutchman,boat;flyingDutchman,leaky).
        """
        result = main(["defeasible(boat,floats)", "defeasible(leaky,boat)","defeasible(leaky,-floats)", "defeasible(flyingDutchman,boat)", "defeasible(flyingDutchman,leaky)"],
                      "query(boats,leaky)", "q3.lp", "rational_queries","ranked3")

        returned_value = result
        expected_result = "entailed(false)"
        print(f"Running test for query: 'boats->leaky'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        
        self.assertEqual(returned_value, expected_result)
    def test_query_three(self):
        """Testing if leaky -> boat entailed by defeasible(boat,floats;leaky,boat;leaky,-floats;flyingDutchman,boat;flyingDutchman,leaky).
        """
        result = main(["defeasible(boat,floats)", "defeasible(leaky,boat)","defeasible(leaky,-floats)", "defeasible(flyingDutchman,boat)", "defeasible(flyingDutchman,leaky)"],
                      "query(leaky,boat)", "q4.lp", "rational_queries","ranked4")

        returned_value = result
        expected_result = "entailed(true)"
        print(f"Running test for query: 'boats->leaky'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        
        self.assertEqual(returned_value, expected_result)

    def test_query_four(self):
        """Testing if flyingDutchman -> floats entailed by defeasible(boat,floats;leaky,boat;leaky,-floats;flyingDutchman,boat;flyingDutchman,leaky).
        """
        result = main(["defeasible(boat,floats)", "defeasible(leaky,boat)","defeasible(leaky,-floats)", "defeasible(flyingDutchman,boat)", "defeasible(flyingDutchman,leaky)"],
                      "query(flyingDutchman,floats)", "q4.lp", "rational_queries","ranked4")

        returned_value = result
        expected_result = "entailed(false)"
        print(f"Running test for query: 'flyingDutchman->floats'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        self.assertEqual(returned_value, expected_result)

    def test_query_five(self):
        """Testing if normalBoat -> floats entailed by defeasible(boat,floats;leaky,boat;leaky,-floats;flyingDutchman,boat;flyingDutchman,leaky).
        """
        result = main(["defeasible(boat,floats)", "defeasible(leaky,boat)","defeasible(leaky,-floats)", "defeasible(flyingDutchman,boat)", "defeasible(flyingDutchman,leaky)", "defeasible(normalBoat,boat)"],
                      "query(normalBoat,floats)", "q5.lp", "rational_queries","ranked5")

        returned_value = result
        expected_result = "entailed(true)"
        print(f"Running test for query: 'flyingDutchman->floats'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        self.assertEqual(returned_value, expected_result)
    def test_query_six(self):
        """Testing if super penguins fly.
        """
        result = main(["defeasible(birds,fly)", "defeasible(birds,wings)","defeasible(penguins,-fly)", "defeasible(superpenguins,penguins)", "defeasible(penguins,birds)", "defeasible(superpenguins,fly)"],
                      "query(superpenguins,fly)", "q6.lp", "rational_queries","ranked6")

        returned_value = result
        expected_result = "entailed(true)"
        print(f"Running test for query: 'superpenguins->fly'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        self.assertEqual(returned_value, expected_result)
    def test_query_seven(self):
        """Testing if super penguins fly.
        """
        result = main(["defeasible(birds,fly)", "defeasible(birds,wings)","defeasible(penguins,-fly)", "defeasible(superpenguins,penguins)", "defeasible(penguins,birds)", "defeasible(superpenguins,fly)"],
                      "query(superpenguins,wings)", "q7.lp", "rational_queries","ranked7")

        returned_value = result
        expected_result = "entailed(false)"
        print(f"Running test for query: 'superpenguins->wings'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        self.assertEqual(returned_value, expected_result)

    def test_query_eight(self):
        """Testing if super penguins fly.
        """
        result = main(["defeasible(birds,fly)", "defeasible(birds,wings)","defeasible(penguins,-fly)", "defeasible(superpenguins,penguins)", "defeasible(penguins,birds)", "defeasible(superpenguins,fly)"],
                      "query(penguins,wings)", "q8.lp", "rational_queries","ranked8")

        returned_value = result
        expected_result = "entailed(false)"
        print(f"Running test for query: 'penguins->wings'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        self.assertEqual(returned_value, expected_result)
    
    def test_query_nine(self):
        """Testing if super penguins fly.
        """
        result = main(["defeasible(birds,fly)", "defeasible(birds,wings)","defeasible(penguins,-fly)", "defeasible(superpenguins,penguins)", "defeasible(penguins,birds)", "defeasible(superpenguins,fly)"],
                      "query(penguins,-fly)", "q9.lp", "rational_queries","ranked9")

        returned_value = result
        expected_result = "entailed(true)"
        print(f"Running test for query: 'penguins->-fly'")
        print(f"Returned value: {returned_value}, Expected: {expected_result}")
        self.assertEqual(returned_value, expected_result)



if __name__ =="__main__":
    unittest.main()