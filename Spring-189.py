import random
import hashlib
import time
from tqdm import tqdm

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

# Function to compress data using Huffman trees and add a checksum
def compress_data_with_checksum(data, huffman_trees):
    compressed_data = bytearray()

    # Calculate the checksum of the original data
    checksum = hashlib.sha256(data).digest()

    # Append the checksum to the compressed data
    compressed_data += checksum

    for _ in tqdm(huffman_trees, desc="Compressing"):
        tree = huffman_trees.pop(0)
        while data:
            if data.startswith(tree):
                compressed_data += tree
                data = data[len(tree):]
            else:
                break
    return bytes(compressed_data)

# Function to extract data using Huffman trees and verify the checksum
def extract_data_with_checksum(compressed_data, huffman_trees):
    extracted_data = bytearray()
    for _ in tqdm(huffman_trees, desc="Extracting"):
        tree = huffman_trees.pop(0)
        while compressed_data:
            if compressed_data.startswith(tree):
                extracted_data += tree
                compressed_data = compressed_data[len(tree):]
            else:
                break

    # Verify the checksum
    received_checksum = extracted_data[:32]  # SHA-256 checksum length
    data = extracted_data[32:]

    calculated_checksum = hashlib.sha256(data).digest()
    if received_checksum == calculated_checksum:
        return data
    else:
        print("Checksum verification failed. The data may be compromised.")
        return None

# Function to save data to a binary file
def save_to_binary_file(file_name, data):
    with open(file_name, 'wb') as file:
        file.write(data)

# Main program
while True:
    option = input("Options:\n1. Compression\n2. Extraction\n3. Exit\nSelect an option (1, 2, or 3): ")
    if option in ("1", "2", "3"):
        if option == "1":
            input_file_name = input("Enter the name of the input file (0-255 range): ")
            output_file_name = input("Enter the name of the output file (0-255 range variations): ")
            for _ in range(100):  # Repeat the compression 100 times
                input_file_name=input_file_name
                output_file_name=output_file_name

                original_data = read_0_to_255_data(input_file_name)
                if original_data:
                    # Apply variations (e.g., multiply by a factor)
                    variation_factor = 256  # Adjust this factor as needed
                    start_time = time.time()
                    varied_data = apply_variations(original_data, variation_factor)

                    # Generate random Huffman trees
                    huffman_trees = generate_random_huffman_trees(99, 8, 106)

                    # Save the Huffman trees to a file
                    save_to_binary_file("huffman_trees.bin", b''.join(huffman_trees))

                    # Compress data into Huffman trees with a checksum
                    compressed_data = compress_data_with_checksum(varied_data, huffman_trees)

                    # Save the result
                    save_to_binary_file(output_file_name, compressed_data)

                    end_time = time.time()
                    time_taken = end_time - start_time

                    print(f"Data successfully transformed and saved in the range 0-255 variations to '{output_file_name}'.")
                    print(f"Time taken: {time_taken} seconds")

        elif option == "2":
            input_file_name = input("Enter the name of the input file (0-255 range variations): ")
            output_file_name = input("Enter the name of the output file (0-255 range): ")
            for _ in range(100):  # Repeat the extraction 100 times
                input_file_name=input_file_name
                output_file_name=output_file_name
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

                    start_time = time.time()
                    # Extract data from Huffman trees and verify the checksum
                    extracted_data = extract_data_with_checksum(varied_data, huffman_trees)

                    if extracted_data:
                        # Save the result
                        save_to_binary_file(output_file_name, extracted_data)

                        end_time = time.time()
                        time_taken = end_time - start_time

                        print(f"Data successfully extracted and saved in the range 0-255 to '{output_file_name}'.")
                        print(f"Time taken: {time_taken} seconds")

        else:
            break
    else:
        print("Invalid option. Please select 1 for Compression, 2 for Extraction, or 3 to Exit.")

print("Program terminated.")