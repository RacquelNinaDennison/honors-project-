import math 

class Distribution:
    def __init__(self, amount_of_ranks, amount_of_statements=None):
        self.amount_of_ranks = amount_of_ranks
        self.amount_of_statements = amount_of_statements

    def calculate_max_d(self):
        # Calculate max_d based on the given ranks and statements
        S = self.amount_of_statements
        R = self.amount_of_ranks
        max_d = (2 * S) / (R * (R - 1))
        return max_d

    def linear_growth(self, d=2):
        rank_n = self.amount_of_ranks
        d_n = d
        statements_n = self.amount_of_statements
        starting_value= (statements_n - (rank_n * (rank_n - 1) * d_n) / 2) / rank_n
        if starting_value != int(starting_value):
            x = math.ceil(starting_value)
            if x < 0:
                required_statements = (rank_n * (rank_n - 1) * d_n) / 2 + (rank_n * d_n)
                return required_statements
            elif x > starting_value:
                self.amount_of_statements = (self.amount_of_ranks/2) * (2*x + (self.amount_of_ranks-1)*d)
                return int(self.amount_of_statements)
        return statements_n
    

