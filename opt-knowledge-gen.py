#const amount_of_ranks = 5.
#const amount_of_statements = 20.
#const classical_included = false.
#const distribution_specified = true.
#const uniform = true.

% Constants
#const remainder = amount_of_statements - (amount_of_ranks-1).
uniform_count(C) :- C = amount_of_statements / amount_of_ranks.

% External directives for easy parameter tuning
#external classical_included.
#external distribution_specified.
#external uniform.

% Generate knowledge base statements
{defeasible(X,L;X,-L)} = 1 :- clashed_atom(X).
:- clash(X,Y), defeasible(X,L), defeasible(Y,L).
defeasible(X,Y) :- clash(X,Y), not classical_included.
classical(X,Y) :- clash(X,Y), classical_included.

% Generate more statements
candidate_defeasible(X,Y) :- atom(X), atom(Y), not clash(X,Y), clashed_atom(X), not clashed_atom(Y).
{defeasible(X,Y)} :- candidate_defeasible(X,Y), amount_of_ranks > 1.
{defeasible(X,Y)} :- atom(X), atom(Y), amount_of_ranks == 1.

% Remove self-referencing atoms
:- defeasible(X,X).
:- defeasible(X,Y), defeasible(Y,X).

% Define implications
m_implication(X,Y) :- defeasible(X,Y).
m_implication(X,Y) :- classical(X,Y).

% Ensure correct number of statements
:- #count{X,Y : m_implication(X,Y)} != amount_of_statements.

% Ranking
ranks(m_implication(X,Y), inf) :- classical(X,Y), distribution_specified.
{ranks(m_implication(X,Y), 0..amount_of_ranks-1)} = 1 :- m_implication(X,Y), not classical(X,Y), distribution_specified.

% Simplified derivation
derive(X,Y,N) :- ranks(m_implication(X,Y),N).
derive(X,Z,N) :- ranks(m_implication(X,Y),N1), derive(Y,Z,N2), N1 >= N2, N = N2.

% Ensure consistent ranking for non-classical implications
:- ranks(m_implication(X,Y1),N1), ranks(m_implication(X,Y2),N2), N1 != N2, not classical(X,_).

% Eliminate contradictions
:- derive(X,Y,N), derive(X,-Y,N).

% Minimize ranks
#minimize{N,X,Y : ranks(m_implication(X,Y),N)}.

% Count statements per rank
statement_count(N, Count) :- 
    Count = #sum{1,X,Y : ranks(m_implication(X,Y),N), not classical(X,Y)}, 
    N = 0..amount_of_ranks-1, 
    distribution_specified.

% Uniform distribution constraints
:- statement_count(N, Count), 
   uniform, 
   amount_of_ranks > 1,
   distribution_specified,
   ((not classical_included, Count != uniform_count) ;
    (classical_included, Count != remainder / amount_of_ranks)).

% Output
#show defeasible/2.
#show classical/2.
#show ranks/2.