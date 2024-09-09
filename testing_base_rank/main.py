import os
import json
from testing.convert import ConvertToFormat

def write_to_file(output_directory, filename, ranked_implications):
    output_path = os.path.join(output_directory, filename)
    with open(output_path, "a+") as f:
          sorted_keys = sorted(ranked_implications.keys(), key=lambda x: (x != '∞', -int(x) if x != '∞' else float('inf')))
          for rank in sorted_keys:
                implications = ", ".join(f"({imp})" for imp in ranked_implications[rank])
                f.write(f"{rank} :\t{{ {implications} }}\n") 

def extract_models(input_directory, filename):
    with open(os.path.join(input_directory, filename), 'r') as file:
        json_data = json.load(file)
        return json_data['Call'][0]['Witnesses'][0]['Value']


def write_models(input_dir, output_dir):
    files = os.listdir(input_dir)
    files.sort()
    
    for filename in files:
        if filename.startswith('.') or filename.startswith('S_'):
            print(f"Skipping system or hidden file: {filename}")
            continue
        
        output_file = filename[:filename.find(".")] + "_formatted.txt"  
        models = extract_models(input_dir, filename)
        formatter = ConvertToFormat(models)
        formatted = formatter.ranked_implications()
        
        write_to_file(output_dir, output_file, formatted)

def main():
    input_directory = "output-testing-files"
    output_directory = "formatted_testing_files_ranks"
    os.makedirs(output_directory, exist_ok=True)
    write_models(input_directory, output_directory)

if __name__ == "__main__":
    main()
