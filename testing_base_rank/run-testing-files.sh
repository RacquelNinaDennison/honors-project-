# Runs base rank againts predefined knowledge bases

input_directory="testing-files/"
output_directory="output-testing-files/"
mkdir -p "$output_directory"
for file in "${input_directory}"*; do
    if [ -f "$file" ]; then
        echo "Processing $file"
        filename=$(basename "$file" .lp)
        output_filename="${filename}_base-rank.json"
        clingo --outf=2 --quiet=1 "$file" "base-rank.lp" > "${output_directory}/${output_filename}"
    fi
done
