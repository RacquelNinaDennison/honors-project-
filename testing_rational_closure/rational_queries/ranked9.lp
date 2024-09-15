rank(m_implication(birds,fly),0).
rank(m_implication(birds,wings),0).
rank(m_implication(superpenguins,penguins),2).
rank(m_implication(penguins,birds),1).
rank(m_implication(superpenguins,fly),2).
rank(m_implication(penguins,-fly),1).
query(penguins,-fly).
#const number_of_statements=6.
