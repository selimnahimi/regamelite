import os
import re

def find_and_write_links(root_dir, output_file):
    # Compile the regex pattern to match LINK_ENTITY_TO_CLASS
    pattern = re.compile(r'LINK_ENTITY_TO_CLASS\(\s?(\w+)\s?,\s?(\w+)\s?,\s?(\w+)?\s?\)')
    
    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        # Walk through the directory recursively
        for subdir, _, files in os.walk(root_dir):
            for file in files:
                # Filter for specific file types if necessary
                if file.endswith(('.cpp', '.h')):  # Adjust extensions as needed
                    file_path = os.path.join(subdir, file)
                    print(f'Processing file: {file_path}')  # Debug print
                    try:
                        # Open each file and read its content
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            # Find all matches of the pattern in the content
                            matches = pattern.findall(content)
                            for match in matches:
                                print(f'Found match: {match}')  # Debug print
                                # Write the matched function declarations to the output file
                                outfile.write(f'void {match[0]}( entvars_t *pev );\n')
                    except Exception as e:
                        print(f'Error processing file {file_path}: {e}')  # Debug print

# Usage
root_directory = '.'  # Change this to the directory you want to search
output_txt_file = 'genexports.txt'
find_and_write_links(root_directory, output_txt_file)

def replace_function_declarations(file_path, output_file_path):
    # Compile the regex pattern to match the function declarations
    pattern = re.compile(r'void (\w+)\( entvars_t \*pev \);')
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace the function declarations
    modified_content = pattern.sub(r'{ "\1", (void*)\1 },', content)
    
    # Write the modified content back to the file
    with open(output_file_path, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(modified_content)

# Usage
replace_function_declarations(output_txt_file, 'genexports_modified.txt')