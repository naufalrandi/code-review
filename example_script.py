# example_script.py
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def process_data(data):
    return data.upper()

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        return

    data = read_file(input_file)
    processed_data = process_data(data)
    write_file(output_file, processed_data)
    print(f"Data processed and written to {output_file}")

if __name__ == "__main__":
    main()
