#base rank testing and rational closure testing 
#!/bin/bash

for i in $(seq 60 10 100); do
    for j in $(seq 5 5 20); do
        if [ $i -eq 10 ] && [ $j -gt 5 ]; then
            # Skip this particular case
            continue
        fi
        clingo --outf=2 --quiet=1 --time-limit=10000 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" "base-rank.lp" > "rational-closure-files/${i}-${j}-uniform.txt"
    done
done
