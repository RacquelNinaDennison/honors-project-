% ensures the antecedent is apart of the initial ranked statements- the antecedent needs to exist with what was initially had
initial_atom(X) :- rank(m_implication(X,Y),N).

% convert all previous ranked statements to implications 
rank(implication(X,Y),N) :- rank(m_implication(X,Y),N).
% make our query an implication 
implication(X,Y) :- query(X,Y).

% Assigning random ranks to the query we are testing 
{rank(implication(X,Y),0..number_of_statements)} = 1 :- implication(X,Y).

% deriving all possible consequences for our query 
derived(X,X,N) :- rank(implication(X,Y),N).
derived(X,P,N) :- rank(implication(Y,P),N1), derived(X,Y,N), N1 >= N.

%from 0..N, this subset is elimanted and not considered
eliminated(N):- derived(X,Y,N),derived(X,-Y,N).
#minimize{N,X,Y:rank(implication(X,Y),N)}.


% find all the consequences that follow from the rank being true
consequence(X,Y,N) :- query(X,_), rank(implication(X,Y),N), rank(implication(X,Y),N1), N1>=N, not eliminated(N). 
consequence(X,P,N) :- query(X,_), rank(implication(Y,P),N), rank(implication(X,Y),N1), N1>=N, not eliminated(N). 

%* 
Determine if it is entailed or not. 
*%
% Accommodate for entailment checks that are just considering a singular atom, we use none as the consequence
entailed(true) :- consequence(X1,_,N), query(X2,none), X1 = X2, initial_atom(X2). 

% Entailment checks of the form alpha |~ beta 
entailed(true) :- consequence(X1,Y1,N), query(X1,Y1), initial_atom(X1).
entailed(false) :- not entailed(true). 

% Show if the query is entailed by the knowledge base 
#show entailed/1.
#show query/2.


