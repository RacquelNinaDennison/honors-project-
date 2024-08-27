#!/bin/bash


output_dir_uniform_handy="results_knowledge_base_uniform_experiments_final_handy"
output_dir_random_handy="results_knowledge_base_random_experiments_final_handy"
output_dir_uniform_frumpy="results_knowledge_base_uniform_experiments_final_frumpy"
output_dir_random_frumpy="results_knowledge_base_random_experiments_final_frumpy"
output_dir_uniform_trendy="results_knowledge_base_uniform_experiments_final_trendy"
output_dir_random_trendy="results_knowledge_base_random_experiments_final_trendy"
output_dir_uniform_tweety="results_knowledge_base_uniform_experiments_final_tweety"
output_dir_random_crafty="results_knowledge_base_random_experiments_final_crafty"
# Create output directory if it does not exist

mkdir -p "$output_dir_uniform_handy"
mkdir -p "$output_dir_random_handy"
mkdir -p "$output_dir_uniform_frumpy"
mkdir -p "$output_dir_random_frumpy"
mkdir -p "$output_dir_uniform_trendy"
mkdir -p "$output_dir_random_trendy"
mkdir -p "$output_dir_uniform_tweety"
mkdir -p "$output_dir_random_crafty"


for i in $(seq 350 50 350); do
     for j in $(seq 18 1 20); do
        output_file="${output_dir_uniform_tweety}/knowledge_base_${i}-${j}_uniform_tweety.txt"
        clingo --outf=2 --quiet=1 --configuration=tweety "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

