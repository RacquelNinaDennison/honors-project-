import re
from collections import defaultdict

class ConvertToFormat:
    '''Converts the data from the base rank of ASP to the format tested from the MBDR implementation'''
    def __init__(self,input_data):
        self.input_data = input_data
    def ranked_implications(self):
        '''Returns the ranked implications in the format needed to test against'''
        ranked_implications = defaultdict(list)
        for entry in self.input_data:
            match = re.match(r'rank\(m_implication\((.*)\),(\d+|inf)\)', entry)
            if match:
                implication = match.group(1).replace(",", "=>")
                implication = implication.replace("-", "!")
                rank = match.group(2)
                if rank == 'inf':
                    rank = '∞'
                else:
                    rank = int(rank)
                
                ranked_implications[rank].append(implication)
        return ranked_implications