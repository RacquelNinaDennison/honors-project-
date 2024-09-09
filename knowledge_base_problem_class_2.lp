{defeasible(X,L;X,-L):clash_literal(L)}= 1 :- clashed_atom(X).
:- clash(X,Y), defeasible(X,L1), defeasible(Y,L2), L1=L2. 
defeasible(X,Y) :- clash(X,Y), not classical_included.
classical(X,Y) :- clash(X,Y), classical_included. 
{defeasible(X,Y) : atom(Y), not clashed_atom(Y)} :- clashed_atom(X).
{defeasible(X,Y)} :- atom(X), atom(Y), number_of_ranks -1  == 0. 
m_implication(X,Y) :- defeasible(X,Y).
m_implication(X,Y) :- classical(X,Y).
:-#count{(X,Y):m_implication(X,Y)} < number_of_statements.
:-#count{(X,Y):m_implication(X,Y)} > number_of_statements.

atom_index(a(X), X) :- atom(a(X)).
% set uniform 
statement_count(N, Count) :- clashed_atom(X), atom_index(X,N), Count = #count{Y : m_implication(X,Y)}.

% Only do this if things are uniform 
:- statement_count(N, Count), Count < @uniform(number_of_ranks,number_of_statements), uniform, number_of_ranks -1 != 0, @modulo(number_of_statements,number_of_ranks)=0.
:- statement_count(N, Count), Count > @uniform(number_of_ranks,number_of_statements), uniform, number_of_ranks -1 != 0,@modulo(number_of_statements,number_of_ranks)=0.
:- statement_count(N, Count), Count > @uniform(number_of_ranks,number_of_statements-@modulo(number_of_statements,number_of_ranks)), uniform, number_of_ranks -1 != 0,@modulo(number_of_statements,number_of_ranks)!= 0, N != number_of_ranks-1. 
:- statement_count(N, Count), Count < @uniform(number_of_ranks,number_of_statements-@modulo(number_of_statements,number_of_ranks)), uniform, number_of_ranks -1 != 0,@modulo(number_of_statements,number_of_ranks)!= 0, N != number_of_ranks-1. 
#const remainder = number_of_statements - (number_of_ranks-1). 

%* Linear growth distribution*%
:- statement_count(N, Count), Count < @linear_growth(number_of_statements, number_of_ranks,N), linear, number_of_ranks -1 != 0.
:- statement_count(N, Count), Count < @linear_growth(number_of_statements, number_of_ranks,N), linear, number_of_ranks -1 != 0.
:- statement_count(N, Count), Count < @linear_decline(number_of_statements, number_of_ranks,N), linear_d, number_of_ranks -1 != 0.
:- statement_count(N, Count), Count < @linear_decline(number_of_statements, number_of_ranks,N), linear_d, number_of_ranks -1 != 0.

%* Random growth distribution*%
% Initialize random distribution with desired parameters
:- statement_count(N, Count), Count < @random_index(number_of_statements, number_of_ranks,N), random, number_of_ranks - 1 != 0.
:- statement_count(N, Count), Count > @random_index(number_of_statements, number_of_ranks,N), random, number_of_ranks - 1 != 0.

#show defeasible/2.

