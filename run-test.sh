#!/bin/bash


output_dir_uniform="results_knowledge_base_uniform"
output_dir_linear="results_knowledge_base_linear"
output_dir_random="results_knowledge_base_random"
# Create output directory if it does not exist

mkdir -p "$output_dir_uniform"
mkdir -p "$output_dir_linear"
mkdir -p "$output_dir_random"

for i in $(seq 50 50 200); do
    for j in $(seq 1 1 20); do
        if [ $i -eq 10 ] && [ $j -gt 5 ]; then
            # Skip this particular case
            continue
        fi
        output_file="${output_dir_linear}/knowledge_base_${i}-${j}_linear.txt"
        clingo --outf=2 --quiet=1 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c linear=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_uniform}/knowledge_base_${i}-${j}_uniform.txt"
        clingo --outf=2 --quiet=1 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_random}/knowledge_base_${i}-${j}_random.txt"
        clingo --outf=2 --quiet=1 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done




