#!/bin/bash


output_dir_uniform="results_knowledge_base_uniform_experiment"
output_dir_linear="results_knowledge_base_linear_experiment"
output_dir_random="results_knowledge_base_random_experiment"
# Create output directory if it does not exist

mkdir -p "$output_dir_uniform"
mkdir -p "$output_dir_linear"
mkdir -p "$output_dir_random"

for i in $(seq 50 25 200); do
    for j in $(seq 5 5 40); do
        output_file="${output_dir_linear}/knowledge_base_${i}-${j}_linear_jumpy.txt"
        clingo --outf=2 --quiet=1 --configuration=jumpy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c linear=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_uniform}/knowledge_base_${i}-${j}_uniform_jumpy.txt"
        clingo --outf=2 --quiet=1 --configuration=jumpy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_random}/knowledge_base_${i}-${j}_random_jumpy.txt"
        clingo --outf=2 --quiet=1 --configuration=jumpy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 25 200); do
    for j in $(seq 5 5 40); do
        output_file="${output_dir_linear}/knowledge_base_${i}-${j}_linear_tweety.txt"
        clingo --outf=2 --quiet=1 --configuration=tweety "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c linear=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_uniform}/knowledge_base_${i}-${j}_uniform_tweety.txt"
        clingo --outf=2 --quiet=1 --configuration=tweety "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_random}/knowledge_base_${i}-${j}_random_tweety.txt"
        clingo --outf=2 --quiet=1 --configuration=tweety "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done


for i in $(seq 50 25 200); do
    for j in $(seq 5 5 40); do
        output_file="${output_dir_linear}/knowledge_base_${i}-${j}_linear.txt"
        clingo --outf=2 --quiet=1  "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c linear=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_uniform}/knowledge_base_${i}-${j}_uniform.txt"
        clingo --outf=2 --quiet=1 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_random}/knowledge_base_${i}-${j}_random.txt"
        clingo --outf=2 --quiet=1  "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done


for i in $(seq 50 25 200); do
    for j in $(seq 5 5 40); do
        output_file="${output_dir_linear}/knowledge_base_${i}-${j}_linear-heuristic-usc.txt"
        clingo --outf=2 --quiet=1 --opt-strategy=usc "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c linear=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_uniform}/knowledge_base_${i}-${j}_uniform-heuristic-usc.txt"
        clingo --outf=2 --quiet=1  --opt-strategy=usc "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_random}/knowledge_base_${i}-${j}_random-heuristic-usc.txt"
        clingo --outf=2 --quiet=1 --opt-strategy=usc "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done



for i in $(seq 50 25 200); do
    for j in $(seq 5 5 40); do
        output_file="${output_dir_linear}/knowledge_base_${i}-${j}_linear-bb.txt"
        clingo --outf=2 --quiet=1 --opt-strategy=bb "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c linear=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_uniform}/knowledge_base_${i}-${j}_uniform-heuristic-bb.txt"
        clingo --outf=2 --quiet=1  --opt-strategy=bb "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
        output_file="${output_dir_random}/knowledge_base_${i}-${j}_random-heuristic-bb.txt"
        clingo --outf=2 --quiet=1 --opt-strategy=bb "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done



