% identifying encoded statements for base rank testing 
coded_classical(X,Y):- defeasible(X,Y), defeasible(Y,X).
classical(X,Y) :- coded_classical(X,Y). 

% material implication of statements 
m_implication(X,Y) :- defeasible(X,Y).
m_implication(X,Y) :- classical(X,Y).

% ranking all classical statements on the infinite level 
rank(m_implication(X,Y),inf) :- classical(X,Y).

% generating ranked statements - this only applies to defeasible statements 
{rank(m_implication(X,Y),0..number_of_statements-1)} = 1 :- m_implication(X,Y), not classical(X,Y), not coded_classical(X,Y).

% defining all possible transitive properties of elements 
derive(X,X,N) :- rank(m_implication(X,Y),N).
derive(X,P,N) :- rank(m_implication(Y,P),N1), derive(X,Y,N), N1 >= N.

% antecdents that are apart of defeasible statements should be ranked on the same level 
N1 = N2 :- rank(m_implication(X,Y1),N1), rank(m_implication(X,Y2),N2), not classical(X,_), not coded_classical(X,_).

test and elminate contradictions
:- derive(X,Y,N),derive(X,-Y,N).

% derive the smallest possible model 
#minimize{N,X,Y:rank(m_implication(X,Y),N)}.

% #show derive/3.