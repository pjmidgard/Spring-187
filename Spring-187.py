import random

# Function to generate random data of a specified length in bits
def generate_random_data(num_bits):
    return bytes([random.randint(0, 255) for _ in range(num_bits)])

# Define 99 sets of bit patterns (Huffman trees)
bit_patterns = [generate_random_data(bits) for bits in range(8, 107)]

# Function to compress data using 99 trees
def compress_data(data, bit_patterns):
    compressed_data = bytearray()
    while data:
        for patterns in bit_patterns:
            if data.startswith(patterns):
                compressed_data += patterns
                data = data[len(patterns):]
                break
    return bytes(compressed_data)

# Function to extract data using 99 trees
def extract_data(compressed_data, bit_patterns):
    extracted_data = bytearray()
    while compressed_data:
        for patterns in bit_patterns:
            if compressed_data.startswith(patterns):
                extracted_data += patterns
                compressed_data = compressed_data[len(patterns):]
                break
    return bytes(extracted_data)

# Function to translate binary data to 0-255 range
def translate_to_0_255(data):
    return bytes([int(byte) for byte in data])

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
        compressed_data = compress_data(original_data, bit_patterns)
        translated_data = translate_to_0_255(compressed_data)
        save_to_binary_file(output_file_name, translated_data)
        print(f"Data successfully compressed and saved as the range 0-255 to '{output_file_name}'.")

elif option == "2":
    input_file_name = input("Enter the name of the input file: ")
    output_file_name = input("Enter the name of the output file: ")

    compressed_data = read_from_binary_file(input_file_name)
    if compressed_data:
        extracted_data = extract_data(compressed_data, bit_patterns)
        translated_data = translate_to_0_255(extracted_data)
        save_to_binary_file(output_file_name, translated_data)
        print(f"Data successfully extracted and saved as the range 0-255 to '{output_file_name}'.")

print("Program terminated.")