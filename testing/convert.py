import re
from collections import defaultdict

class ConvertToFormat:
    def __init__(self,input_data):
        self.input_data = input_data
    def ranked_implications(self):
        ranked_implications = defaultdict(list)
        for entry in self.input_data:
            # Match rank with either a number or 'inf'
            match = re.match(r'rank\(m_implication\((.*)\),(\d+|inf)\)', entry)
            if match:
                implication = match.group(1).replace(",", "=>")
                implication = implication.replace("-", "!")
                rank = match.group(2)
                
                # Replace 'inf' with ∞
                if rank == 'inf':
                    rank = '∞'
                else:
                    rank = int(rank)
                
                ranked_implications[rank].append(implication)
        return ranked_implications