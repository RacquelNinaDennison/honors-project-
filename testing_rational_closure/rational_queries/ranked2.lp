rank(m_implication(penguins,birds),inf).
rank(m_implication(birds,fly),0).
rank(m_implication(eagles,fly),0).
rank(m_implication(birds,wings),0).
rank(m_implication(eagles,birds),0).
rank(m_implication(penguins,-fly),1).
query(eagles,wings).
#const number_of_statements=6.
