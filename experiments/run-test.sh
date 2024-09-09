#!/bin/bash

main_directory="experiment_files"
mkdir -p "$main_directory"

# Define and create the subdirectories under the main directory
output_dir_uniform_handy="${main_directory}/results_knowledge_base_uniform_experiments_handy"
output_dir_uniform_tweety="${main_directory}/results_knowledge_base_uniform_experiments_tweety"
output_dir_uniform_jumpy="${main_directory}/results_knowledge_base_uniform_experiments_jumpy"
output_dir_uniform_trendy="${main_directory}/results_knowledge_base_uniform_experiments_trendy"
output_dir_uniform_no_config="${main_directory}/results_knowledge_base_uniform_experiments_no_config"

output_dir_random_handy="${main_directory}/results_knowledge_base_random_experiments_handy"
output_dir_random_tweety="${main_directory}/results_knowledge_base_random_experiments_tweety"
output_dir_random_jumpy="${main_directory}/results_knowledge_base_random_experiments_jumpy"
output_dir_random_trendy="${main_directory}/results_knowledge_base_random_experiments_trendy"
output_dir_random_no_config="${main_directory}/results_knowledge_base_random_experiments_no_config"

# Create all subdirectories
mkdir -p "$output_dir_uniform_handy"
mkdir -p "$output_dir_uniform_tweety"
mkdir -p "$output_dir_uniform_jumpy"
mkdir -p "$output_dir_uniform_trendy"
mkdir -p "$output_dir_uniform_no_config"

mkdir -p "$output_dir_random_handy"
mkdir -p "$output_dir_random_tweety"
mkdir -p "$output_dir_random_jumpy"
mkdir -p "$output_dir_random_trendy"
mkdir -p "$output_dir_random_no_config"
#uniform

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_uniform_handy}/knowledge_base_${i}-${j}_uniform_handy.txt"
        clingo --outf=2 --quiet=1 --configuration=handy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_uniform_tweety}/knowledge_base_${i}-${j}_uniform_tweety.txt"
        clingo --outf=2 --quiet=1 --configuration=tweety "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_uniform_jumpy}/knowledge_base_${i}-${j}_uniform_jumpy.txt"
        clingo --outf=2 --quiet=1 --configuration=jumpy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_uniform_trendy}/knowledge_base_${i}-${j}_uniform_trendy.txt"
        clingo --outf=2 --quiet=1 --configuration=trendy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_uniform_no_config}/knowledge_base_${i}-${j}_uniform_no_config.txt"
        clingo --outf=2 --quiet=1 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c uniform=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done


#random

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_random_handy}/knowledge_base_${i}-${j}_random_handy.txt"
        clingo --outf=2 --quiet=1 --configuration=handy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_random_tweety}/knowledge_base_${i}-${j}_random_tweety.txt"
        clingo --outf=2 --quiet=1 --configuration=tweety "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_random_jumpy}/knowledge_base_${i}-${j}_random_jumpy.txt"
        clingo --outf=2 --quiet=1 --configuration=jumpy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_random_trendy}/knowledge_base_${i}-${j}_random_trendy.txt"
        clingo --outf=2 --quiet=1 --configuration=trendy "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done

for i in $(seq 50 50 350); do
     for j in $(seq 1 1 20); do
        output_file="${output_dir_random_no_config}/knowledge_base_${i}-${j}_random_no_config.txt"
        clingo --outf=2 --quiet=1 "knowledge-base-instances.lp" -c amount_of_ranks=$j -c amount_of_statements=$i -c random=1 "knowledge_base_problem_class_2.lp" "functions.lp" > "${output_file}"
    done
done