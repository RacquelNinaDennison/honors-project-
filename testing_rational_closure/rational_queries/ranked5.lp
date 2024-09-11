rank(m_implication(boat,floats),0).
rank(m_implication(leaky,boat),1).
rank(m_implication(flyingDutchman,boat),1).
rank(m_implication(flyingDutchman,leaky),1).
rank(m_implication(normalBoat,boat),0).
rank(m_implication(leaky,-floats),1).
query(normalBoat,floats).
#const number_of_statements=6.
