% generate knowledge base statements 

{defeasible(X,L;X,-L):clash_literal(L)}= 1 :- clashed_atom(X).
:- clash(X,Y), defeasible(X,L1), defeasible(Y,L2), L1=L2. 
defeasible(X,Y) :- clash(X,Y), not classical_included.
% classical statements are generated on if this is set to true 
classical(X,Y) :- clash(X,Y), classical_included.

% generating more statements if they are clashed or not 
{defeasible(X,Y)} :- atom(X), atom(Y), not clash(X,Y), clashed_atom(X), not clashed_atom(Y), amount_of_ranks -1 > 0.
% no clash statements - everything placed on lower level 
{defeasible(X,Y)} :- atom(X), atom(Y), amount_of_ranks -1  == 0. 

% remove those atoms that reference themselves 
:- defeasible(X,Y), X=Y.
:- defeasible(X,Y), defeasible(P,Q), X=Q, P = Y .

% amount of statements wanted 
m_implication(X,Y) :- defeasible(X,Y).
m_implication(X,Y) :- classical(X,Y).

:-#count{(X,Y):m_implication(X,Y)} < amount_of_statements.
:-#count{(X,Y):m_implication(X,Y)} > amount_of_statements.

% ranking classical statements on level inf - this will only be computed is someone specifies that there should be a distribution 
ranks(m_implication(X,Y),inf) :- classical(X,Y),distribution_specified.

% generating ranked statements 
% this is only true based on what is specified in terms of a distribution metric
{ranks(m_implication(X,Y),0..amount_of_ranks-1)} = 1 :- m_implication(X,Y), not classical(X,Y), distribution_specified.
derive(X,X,N) :- ranks(m_implication(X,Y),N).
derive(X,P,N) :- ranks(m_implication(Y,P),N1), derive(X,Y,N), N1 >= N.

N1 = N2 :- ranks(m_implication(X,Y1),N1), ranks(m_implication(X,Y2),N2), not classical(X,_).
% test and elminate contradictions
exceptional(X,N):- derive(X,Y,N),derive(X,-Y,N).
:- exceptional(X,N). 

% derive the smallest model possible
#minimize{N,X,Y:ranks(m_implication(X,Y),N)}.

% experimenting with specifing what distribution of statements should there be per level: achieved only uniform 
% based on no classical statements included 
statement_count(N, Count) :- Count = #count{X,Y : ranks(m_implication(X,Y),N), m_implication(X,Y), not classical(X,Y)}, N =0..amount_of_ranks-1, distribution_specified.

% Only do this if things are uniform 
:- statement_count(N, Count), Count < @uniform(amount_of_ranks,amount_of_statements), uniform, amount_of_ranks -1 != 0, @modulo(amount_of_statements,amount_of_ranks)=0, not classical_included.
:- statement_count(N, Count), Count > @uniform(amount_of_ranks,amount_of_statements), uniform, amount_of_ranks -1 != 0,@modulo(amount_of_statements,amount_of_ranks)=0, not classical_included.

% if it is that the number is uneven, then we need to change the uniform distribution :- statement_count(N, Count), Count < @uniform(amount_of_ranks,amount_of_statements), uniform, amount_of_ranks -1 != 0, @modulo(amount_of_statements,amount_of_ranks)=0.
:- statement_count(N, Count), Count > @uniform(amount_of_ranks,amount_of_statements-@modulo(amount_of_statements,amount_of_ranks)), uniform, amount_of_ranks -1 != 0,@modulo(amount_of_statements,amount_of_ranks)!= 0, N != amount_of_ranks-1,not classical_included. 
:- statement_count(N, Count), Count < @uniform(amount_of_ranks,amount_of_statements-@modulo(amount_of_statements,amount_of_ranks)), uniform, amount_of_ranks -1 != 0,@modulo(amount_of_statements,amount_of_ranks)!= 0, N != amount_of_ranks-1,not classical_included. 
#const remainder = amount_of_statements - (amount_of_ranks-1). 

%*Classical statements included*%

:- statement_count(N, Count), Count < @uniform(remainder,amount_of_statements), uniform, amount_of_ranks -1 != 0, @modulo(remainder,amount_of_ranks)=0, classical_included.
:- statement_count(N, Count), Count > @uniform(remainder,amount_of_statements), uniform, amount_of_ranks -1 != 0,@modulo(remainder,amount_of_ranks)=0, classical_included.

:- statement_count(N, Count), Count > @uniform(amount_of_ranks,remainder-@modulo(remainder,amount_of_ranks)), uniform, amount_of_ranks -1 != 0,@modulo(remainder,amount_of_ranks)!= 0, N != amount_of_ranks-1,classical_included. 
:- statement_count(N, Count), Count < @uniform(amount_of_ranks,remainder-@modulo(remainder,amount_of_ranks)), uniform, amount_of_ranks -1 != 0,@modulo(remainder,amount_of_ranks)!= 0, N != amount_of_ranks-1,classical_included. 




