def remove_leading_slash_from_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove leading slash and write to output file
            modified_line = line.lstrip('/')
            outfile.write(modified_line)

# Get user input for file paths
input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")

# Call the function with user-provided file paths
remove_leading_slash_from_file(input_file_path, output_file_path)

print(f"Processed '{input_file_path}' and saved to '{output_file_path}'.")
