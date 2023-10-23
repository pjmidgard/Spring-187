import random

# Function to generate a random bit pattern of a specific length in bits
def generate_random_bit_pattern(bit_length):
    return bytes([random.randint(0, 255) for _ in range(bit_length)])

# Create a list of 993 random bit patterns ranging from 8 to 1000 bits
bit_patterns = [generate_random_bit_pattern(bit_length) for bit_length in range(8, 1001)]

# Function to compress data using 993 trees
def compress_data(data, bit_patterns):
    compressed_data = bytearray()
    while data:
        for patterns in bit_patterns:
            if data.startswith(patterns):
                compressed_data += patterns
                data = data[len(patterns):]
                break
    return bytes(compressed_data)

# Function to extract data using 993 trees
def extract_data(compressed_data, bit_patterns):
    extracted_data = bytearray()
    while compressed_data:
        for patterns in bit_patterns:
            if compressed_data.startswith(patterns):
                extracted_data += patterns
                compressed_data = compressed_data[len(patterns):]
                break
    return bytes(extracted_data)

# Function to save data to a binary file
def save_to_binary_file(file_name, data):
    with open(file_name, 'wb') as file:
        file.write(data)

# Function to read data from a binary file
def read_from_binary_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Function to read a specified number of bits from data
def read_bits(data, num_bits):
    bits = data[:num_bits]
    remaining_data = data[num_bits:]
    return bits, remaining_data

# Main program
while True:
    option = input("Options:\n1. Compression\n2. Extraction\n3. Exit\nSelect an option (1, 2, or 3): ")
    if option in ("1", "2", "3"):
        break
    else:
        print("Invalid option. Please select 1 for Compression, 2 for Extraction, or 3 to Exit.")

if option == "1":
    input_file_name = input("Enter the name of the input file: ")
    output_file_name = input("Enter the name of the output file: ")

    original_data = read_from_binary_file(input_file_name)
    if original_data:
        eight_bits, remaining_data = read_bits(original_data, 8)
        compressed_data = compress_data(eight_bits, bit_patterns)
        save_to_binary_file(output_file_name, compressed_data)
        print(f"Data successfully compressed and saved to '{output_file_name}'.")

elif option == "2":
    input_file_name = input("Enter the name of the input file: ")
    output_file_name = input("Enter the name of the output file: ")

    compressed_data = read_from_binary_file(input_file_name)
    if compressed_data:
        extracted_data = extract_data(compressed_data, bit_patterns)
        save_to_binary_file(output_file_name, extracted_data)
        print(f"Data successfully extracted and saved to '{output_file_name}'.")

print("Program terminated.")