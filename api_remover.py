def erase_api_prefix(text):
    # Define the prefixes to remove
    prefixes = ['/api/', '/api', 'api/']
    
    # Check and remove the prefix if it exists at the start of the text
    for prefix in prefixes:
        if text.startswith(prefix):
            return text[len(prefix):].lstrip()  # Remove prefix and leading spaces

    return text  # Return the original text if no prefix matches

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    cleaned_lines = [erase_api_prefix(line) for line in lines]

    with open(output_file, 'w') as file:
        file.writelines(cleaned_lines)

if __name__ == "__main__":
    input_file = input("Enter the name of the input text file (e.g., input.txt): ")
    output_file = input("Enter the name of the output text file (e.g., output.txt): ")
    
    process_file(input_file, output_file)
    print(f"Processed text has been saved to {output_file}.")