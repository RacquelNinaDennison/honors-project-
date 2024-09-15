initial_atom(X) :- rank(m_implication(X,Y),N).
rank(implication(X,Y),N) :- rank(m_implication(X,Y),N).
implication(X,Y) :- query(X,Y).

{rank(implication(X,Y),0..number_of_statements)} = 1 :- implication(X,Y).

derive(X,X,N) :- rank(implication(X,Y),N).
derive(X,P,N) :- rank(implication(Y,P),N1), derive(X,Y,N), N1 >= N.

%from 0..N, this subset is elimanted and not considered
eliminated(N):- derive(X,Y,N),derive(X,-Y,N).
#minimize{N,X,Y:rank(implication(X,Y),N)}.
% find all the consequences that follow from the rank being true
consequence(X,Y,N) :- query(X,_), rank(implication(X,Y),N), rank(implication(X,Y),N1), N1>=N, not eliminated(N). 
consequence(X,P,N) :- query(X,_), rank(implication(Y,P),N), rank(implication(X,Y),N1), N1>=N, not eliminated(N). 
% % %* 
% Determine if it is entailed or not. This will need to be extended if 
% we want to determine if the antecedent is simply true
% *%

% Accommodate for entailment checks that are just considering a singular atom
entailed(true) :- consequence(X1,_,N), query(X2,none), X1 = X2, initial_atom(X2). 
entailed(true) :- consequence(X1,Y1,N), query(X1,Y1),initial_atom(X1).
entailed(false) :- not entailed(true). 

% testing for base rank 
#show entailed/1.
