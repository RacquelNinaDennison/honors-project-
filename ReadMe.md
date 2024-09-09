# Defeasible conditionals in Answer Set Programming

This project forms part of a larger honors project which
sorts to model defeasible conditionals in Answer Set
Programming. In this project repo we developed an
implemnetation of Base Rank and Rational Closure(RC)
outlined in paper
[Giovanni Casini, Thomas Meyer, Ivan Varzinczak, 2012](#1).
Furthermore, we developed a knowledge generator used
generate data for RC.

### Installation

1. **Clingo**:  
   To run the ASP files, you need to have Clingo installed.
   You can install Clingo by following the instructions
   [here](https://potassco.org/clingo/).
2. **Python**:  
   The Python application used for the knowledge generator
   requires Python to be installed. You can download and
   install Python from the official site
   [here](https://www.python.org/downloads/).

## Running the programs

### Base Rank and Rational Closure

To run Base Rank, given a knowledge base K, all statements
need to be encoded as defeasible or classical facts. A const
should specify the number of statements within the knowledge
base. Example K = {penguins -> birds, birds |~ fly ,
penguins |~ -fly } is encoded as ASP facts:

```asp
defeasible(penguins,-fly).
defeasible(birds,fly).
classical(penguins,birds).
#const number_of_statements=3.
```

Running Base Rank on given set of facts in a file and output
the generation to a file name:

```bash
     clingo <file-with-knowledge-base-facts> base-rank.lp > <output-file-name>
```

To run Rational Closure, the query to be queried against a
knowledge base should be encoded in a file such as:

```asp
query(penguins,fly).
```

To check for entailment for a given set of statements, run
the following command:

```bash
     clingo <file-with-query> <file-with-knowledge-base-facts> base-rank.lp rational-closure.lp > <output-file-name>
```

### Knowledge base generator

The knowledge base generator generates knowledge bases based
on the following parameters:

- Number of statements.
- Number of ranks.
- Classical statements included or not.
- Encoded statements.
- Number of encoded statements if encoded set to true.
- Distribution of statements.

The paramters above are set by external consts used by the
clingo environment.

To set the external consts: 
- Number of statements 
```bash
    -c number_of_statement = <given-amount>
```
- Number of ranks
```bash
    -c number_of_ranks = <given-amount>
```
- Encoded (The number of encoded statements need to be specified)
```bash
    -c encoded=1 -c number_of_encoded_statements= <given-amount>
```
- Distribution
--Uniform
```bash
    -c uniform=1 
```
--Random
```bash
    -c random=1 
```
--Linear
```bash
    -c linear=1 
```

To run the knowledge base:
```bash
        clingo --outf=2 --quiet=1 knowledge-base-instances.lp -c number_of_ranks=<given-amount> -c number_of_statements=<given-amount> -c uniform=1 knowledge_base_problem_class_2.lp "functions.lp" > <output-file>
```
### References

1. Giovanni Casini, Thomas Meyer, Ivan Varzinczak, "Taking
   Defeasible Entailment Beyond Rational Closure" , Logics
   in Artificial Intelligence (pp.182-197), 2012.
   DOI:10.1007/978-3-030-19570-0_12.
