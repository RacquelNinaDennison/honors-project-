# Defeasible conditionals in Answer Set Programming

This project forms part of a larger honors project which
sorts to model defeasible conditionals in Answer Set
Programming. In this project repo we developed an
implemnetation of Base Rank and Rational Closure(RC)
outlined in paper
[Giovanni Casini, Thomas Meyer, Ivan Varzinczak, 2012](#1).
Furthermore, we developed a knowledge generator used
generate data for RC.

## Running the programs

### Base Rank and Rational Closure

To run Base Rank, given a knowledge base K, all statements
need to be encoded as defeasible or classical facts. Example
K = {penguins -> birds, birds |~ fly , penguins |~ -fly } is
encoded as ASP facts:

```asp
defeasible(penguins,-fly).
defeasible(birds,fly).
classical(penguins,birds).
```

Running Base Rank on given set of facts in a file and output the generation to a file name:

```bash
     clingo <file-with-facts> base-rank.lp > "<output-file-name>"
```


###

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

### References

1. Giovanni Casini, Thomas Meyer, Ivan Varzinczak, "Taking
   Defeasible Entailment Beyond Rational Closure" , Logics
   in Artificial Intelligence (pp.182-197), 2012.
   DOI:10.1007/978-3-030-19570-0_12.
