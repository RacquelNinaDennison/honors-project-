%*Using the atoms instead of the clash literal*%
{clashed_init(X,L) : atom(L), not clashed_atom(L) } = 1 :- clash(X,Y).
clashed_init(Y,-L) :- clash(X,Y), clashed_init(X,L).
defeasible(X,Y) :- clash(X,Y).
defeasible(X,Y) :- clashed_init(X,Y).
{defeasible(X,Y)} :- atom(X), atom(Y), not clash(X,Y), clashed_atom(X), not clashed_atom(Y), amount_of_ranks -1 > 0.

m_implication(X,Y) :- defeasible(X,Y), not encoded(X,Y).
m_implication(X,Y) :- classical(X,Y), not encoded(X,Y). 
:-#count{(X,Y):m_implication(X,Y)} < amount_of_statements.
:-#count{(X,Y):m_implication(X,Y)} > amount_of_statements.

atom_index(a(X), X) :- atom(a(X)).
statement_count(N, Count) :- clashed_atom(X), atom_index(X,N), Count = #count{Y : m_implication(X,Y)}.


:- statement_count(N, Count), Count != @uniform(amount_of_ranks,amount_of_statements), uniform, amount_of_ranks -1 != 0, @modulo(amount_of_statements,amount_of_ranks)=0, not classical_included.
:- statement_count(N, Count), Count != @uniform(amount_of_ranks,amount_of_statements-@modulo(amount_of_statements,amount_of_ranks)), uniform, amount_of_ranks -1 != 0,@modulo(amount_of_statements,amount_of_ranks)!= 0, N != amount_of_ranks-1,not classical_included. 
#const remainder = amount_of_statements - (amount_of_ranks-1). 

%*Classical statements included for uniform distributions*%
:- statement_count(N, Count), Count != @uniform(remainder,amount_of_statements), uniform, amount_of_ranks -1 != 0, @modulo(remainder,amount_of_ranks)=0, classical_included.
:- statement_count(N, Count), Count != @uniform(amount_of_ranks,remainder-@modulo(remainder,amount_of_ranks)), uniform, amount_of_ranks -1 != 0,@modulo(remainder,amount_of_ranks)!= 0, N != amount_of_ranks-1,classical_included. 
:- statement_count(N,Count), N > amount_of_statements-1. 

%*Linear growth distribution*%
:- statement_count(N, Count), Count != @linear_growth(amount_of_statements, amount_of_ranks,N), linear, amount_of_ranks -1 != 0.
%*Linear decline distribution*%
:- statement_count(N, Count), Count != @linear_decline(amount_of_statements, amount_of_ranks,N), linear_d, amount_of_ranks -1 != 0.
%* Random growth distribution*%
:- statement_count(N, Count), Count != @random_index(amount_of_statements, amount_of_ranks,N), random, amount_of_ranks - 1 != 0.

















