uniform :- uniform = 1. 
distribution_specified :- uniform.
classical_included :- classical =1.  
linear :-linear=1. 
distribution_specified:- linear. 
random :-random=1. 
distribution_specified:- random. 
linear_d :-linear_d=1. 
distribution_specified:- linear_d. 

{clash(a(1..amount_of_ranks-1),a(0..amount_of_ranks-2))}.
:- #count{X,Y:clash(a(X),a(Y))} > amount_of_ranks-1.
:- #count{X,Y:clash(a(X),a(Y))} < amount_of_ranks-1.
atom(a(0..amount_of_statements-1)).
index(X,a(X)):- atom(a(X)).
:- clash(X,Y), X =Y.
:- clash(X,Y),index(P,X),index(Z,Y), |P-Z| >1.
:- clash(X,Y),index(P,X),index(Z,Y), P < Z.

clash_literal(l0).
clashed_atom(X;Y) :- clash(X,Y).

% test 

Y1 = Y2 :- clash(X,Y1), clash(X,Y2). 
X1 = X2 :- clash(X1,Y), clash(X2,Y). 


:- #count{X,Y :clash(X,Y)} < 1, amount_of_ranks-1 >0. 
:- #count{X :atom(X)} < amount_of_statements. 
:- #count{X :atom(X)} > amount_of_statements. 


