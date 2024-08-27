% material implication of statements 
m_implication(X,Y) :- defeasible(X,Y).
m_implication(X,Y) :- classical(X,Y).

%ranking classical statements on level inf
rank(m_implication(X,Y),inf) :- classical(X,Y).

% generating ranked statements 
{rank(m_implication(X,Y),0..amount_of_ranks-1)} = 1 :- m_implication(X,Y), not classical(X,Y).
derive(X,X,N) :- rank(m_implication(X,Y),N).
derive(X,P,N) :- rank(m_implication(Y,P),N1), derive(X,Y,N), N1 >= N.

N1 = N2 :- rank(m_implication(X,Y1),N1), rank(m_implication(X,Y2),N2), not classical(X,_).
% % test and elminate contradictions
exceptional(X,N):- derive(X,Y,N),derive(X,-Y,N).
:- exceptional(X,N). 
% % derive the smallest model possible
#minimize{N,X,Y:rank(m_implication(X,Y),N)}.


#show rank/2.



