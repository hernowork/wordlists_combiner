import argparse
import os
import re
from collections import Counter

def remove_duplicate_lines(lines):
    """Remove duplicate lines and blank lines from the list."""
    unique_lines = set(line.strip() for line in lines if line.strip())
    return sorted(unique_lines)

def remove_foreign_characters(lines):
    """Remove lines containing non-Latin characters."""
    latin_only = re.compile(r'^[\x00-\x7F]+$')
    return sorted(line.strip() for line in lines if latin_only.match(line))

def remove_file_extensions(lines):
    """Remove lines containing file extensions."""
    return sorted(line.strip() for line in lines if not re.search(r'\.\w{2,5}$', line))

def retain_file_extensions(lines):
    """Retain only lines containing file extensions."""
    return sorted(line.strip() for line in lines if re.search(r'\.\w{2,5}$', line))

def show_unique_lines(lines):
    """Print unique lines to the terminal."""
    unique_lines = remove_duplicate_lines(lines)
    for line in unique_lines:
        print(line)

def show_duplicate_lines(lines):
    """Print duplicate lines with their counts to the terminal."""
    count = Counter(line.strip() for line in lines if line.strip())
    duplicates = {line: cnt for line, cnt in count.items() if cnt > 1}
    for line, cnt in sorted(duplicates.items()):
        print(f"{line} (Count: {cnt})")

def read_input_files(input_files):
    """Read lines from multiple input files."""
    all_lines = []
    for file in input_files:
        if not os.path.isfile(file):
            print(f"Error: The file '{file}' does not exist.")
            continue
        with open(file, 'r', encoding='utf-8') as f:
            all_lines.extend(f.readlines())
    return all_lines

def write_output_file(lines, output_file):
    """Write lines to the specified output file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    parser = argparse.ArgumentParser(description="Process text files.")
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input files')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-rd', '--remove-duplicates', action='store_true', help='Remove duplicate lines')
    parser.add_argument('-rf', '--remove-foreign', action='store_true', help='Remove lines containing foreign characters')
    parser.add_argument('-re', '--remove-extensions', action='store_true', help='Remove lines containing file extensions')
    parser.add_argument('-rt', '--retain-extensions', action='store_true', help='Retain only lines containing file extensions')
    parser.add_argument('-su', '--show-unique', action='store_true', help='Show unique lines')
    parser.add_argument('-sd', '--show-duplicates', action='store_true', help='Show duplicate lines')

    args = parser.parse_args()

    # Read input files
    lines = read_input_files(args.input)

    # Process flags
    if args.remove_duplicates:
        lines = remove_duplicate_lines(lines)
        if args.output:
            write_output_file(lines, args.output)
        else:
            print("Output file not specified. Please use -o to specify an output file.")

    if args.remove_foreign:
        lines = remove_foreign_characters(lines)
        if args.output:
            write_output_file(lines, args.output)
        else:
            print("Output file not specified. Please use -o to specify an output file.")

    if args.remove_extensions:
        lines = remove_file_extensions(lines)
        if args.output:
            write_output_file(lines, args.output)
        else:
            print("Output file not specified. Please use -o to specify an output file.")

    if args.retain_extensions:
        lines = retain_file_extensions(lines)
        if args.output:
            write_output_file(lines, args.output)
        else:
            print("Output file not specified. Please use -o to specify an output file.")

    if args.show_unique:
        show_unique_lines(lines)

    if args.show_duplicates:
        show_duplicate_lines(lines)

if __name__ == "__main__":
    main()