# Author Jurijus Pacalovas
import random

# Function to read data from a binary file in the 0-255 range
def read_0_to_255_data(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Function to apply variations (e.g., multiply by a factor)
def apply_variations(data, variation_factor):
    return bytes([min(255, max(0, int(byte) * variation_factor)) for byte in data])

# Function to generate random Huffman trees (bit patterns)
def generate_random_huffman_trees(num_trees, min_bits, max_bits):
    return [bytes([random.randint(0, 255) for _ in range(random.randint(min_bits, max_bits))]) for _ in range(num_trees)]

# Function to compress data using Huffman trees
def compress_data(data, huffman_trees):
    compressed_data = bytearray()
    while data:
        for tree in huffman_trees:
            if data.startswith(tree):
                compressed_data += tree
                data = data[len(tree):]
                break
    return bytes(compressed_data)

# Function to extract data using Huffman trees
def extract_data(compressed_data, huffman_trees):
    extracted_data = bytearray()
    while compressed_data:
        for tree in huffman_trees:
            if compressed_data.startswith(tree):
                extracted_data += tree
                compressed_data = compressed_data[len(tree):]
                break
    return bytes(extracted_data)

# Function to translate binary data to the 0-255 range
def translate_to_0_255(data):
    return bytes([int(byte) for byte in data])

# Function to save data to a binary file
def save_to_binary_file(file_name, data):
    with open(file_name, 'wb') as file:
        file.write(data)

# Function to save Huffman trees to a binary file
def save_huffman_trees_to_file(file_name, huffman_trees):
    with open(file_name, 'wb') as file:
        for tree in huffman_trees:
            file.write(tree)

# Main program
while True:
    option = input("Options:\n1. Compression\n2. Extraction\n3. Exit\nSelect an option (1, 2, or 3): ")
    if option in ("1", "2", "3"):
        break
    else:
        print("Invalid option. Please select 1 for Compression, 2 for Extraction, or 3 to Exit.")

if option == "1":
    input_file_name = input("Enter the name of the input file (0-255 range): ")
    output_file_name = input("Enter the name of the output file (0-255 range variations): ")

    original_data = read_0_to_255_data(input_file_name)
    if original_data:
        # Apply variations (e.g., multiply by a factor)
        variation_factor = 256  # Adjust this factor as needed
        varied_data = apply_variations(original_data, variation_factor)

        # Generate random Huffman trees
        huffman_trees = generate_random_huffman_trees(99, 8, 106)

        # Save the Huffman trees to a file
        save_huffman_trees_to_file("huffman_trees.bin", huffman_trees)

        # Compress data into Huffman trees
        compressed_data = compress_data(varied_data, huffman_trees)

        # Translate the compressed data back to the 0-255 range
        translated_data = translate_to_0_255(compressed_data)

        # Save the result
        save_to_binary_file(output_file_name, translated_data)

        print(f"Data successfully transformed and saved in the range 0-255 variations to '{output_file_name}'.")

elif option == "2":
    input_file_name = input("Enter the name of the input file (0-255 range variations): ")
    output_file_name = input("Enter the name of the output file (0-255 range): ")

    varied_data = read_0_to_255_data(input_file_name)
    if varied_data:
        # Load Huffman trees from a file
        huffman_trees = []
        with open("huffman_trees.bin", 'rb') as file:
            while True:
                tree = file.read(1)
                if not tree:
                    break
                huffman_trees.append(tree)

        # Extract data from Huffman trees
        extracted_data = extract_data(varied_data, huffman_trees)

        # Translate the extracted data back to the 0-255 range
        translated_data = translate_to_0_255(extracted_data)

        # Save the result
        save_to_binary_file(output_file_name, translated_data)

        print(f"Data successfully extracted and saved in the range 0-255 to '{output_file_name}'.")

print("Program terminated.")