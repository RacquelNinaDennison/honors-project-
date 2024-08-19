{defeasible(X,L;X,-L):clash_literal(L)}= 1 :- clashed_atom(X).
:- clash(X,Y), defeasible(X,L1), defeasible(Y,L2), L1=L2. 
defeasible(X,Y) :- clash(X,Y), not classical_included.
{defeasible(X,Y) : atom(Y), not clashed_atom(Y)} :- clashed_atom(X).
{defeasible(X,Y)} :- atom(X), atom(Y), amount_of_ranks -1  == 0. 
m_implication(X,Y) :- defeasible(X,Y).
:-#count{(X,Y):m_implication(X,Y)} < amount_of_statements.
:-#count{(X,Y):m_implication(X,Y)} > amount_of_statements.
atom_index(a(X), X) :- atom(a(X)).
% set uniform 

statement_count(N, Count) :- clashed_atom(X), atom_index(X,N), Count = #count{Y : m_implication(X,Y)}.

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
:- statement_count(N,Count), N > amount_of_statements-1. 

%* Linear growth distribution*%
:- statement_count(N, Count), Count < @linear_growth(amount_of_statements, amount_of_ranks,N), linear, amount_of_ranks -1 != 0.
:- statement_count(N, Count), Count < @linear_growth(amount_of_statements, amount_of_ranks,N), linear, amount_of_ranks -1 != 0.


:- statement_count(N, Count), Count < @linear_decline(amount_of_statements, amount_of_ranks,N), linear_d, amount_of_ranks -1 != 0.
:- statement_count(N, Count), Count < @linear_decline(amount_of_statements, amount_of_ranks,N), linear_d, amount_of_ranks -1 != 0.

%* Random growth distribution*%
% Initialize random distribution with desired parameters
:- statement_count(N, Count), Count < @random_index(amount_of_statements, amount_of_ranks,N), random, amount_of_ranks - 1 != 0.
:- statement_count(N, Count), Count > @random_index(amount_of_statements, amount_of_ranks,N), random, amount_of_ranks - 1 != 0.