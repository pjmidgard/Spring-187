# Author Jurijus Pacalovas

# Function to reverse specific bit patterns during compression and extraction
def reverse_bits(data):
    # Bit pattern replacements
    replacements = {
        b'000000000': b'111001101',
        b'111001101': b'000000000',
        b'01011': b'11111',
        b'00000': b'01100',
        b'00001': b'01101',
        b'00010': b'01110',
        b'00011': b'01111',
        b'00100': b'11100',
        b'11111': b'01011',
        b'01100': b'00000',
        b'01101': b'00001',
        b'01110': b'00010',
        b'11100': b'00011',
        b'10': b'11',
        b'00': b'10',
        b'01': b'00',
        b'10': b'00',
    }

    for pattern, replacement in replacements.items():
        data = data.replace(pattern, replacement)

    return data

# Function to perform custom bit replacements based on the specified steps and condition
def perform_custom_bit_replacements(data, bit_length, num_steps, condition):
    for step in range(num_steps):
        for i in range(bit_length):
            if condition(i):
                data = data.replace(bytes(str(i), 'utf-8'), b'0')
    return data

# Function to read and write binary data
def read_write_binary_data(input_filename, output_filename, operation, condition):
    try:
        with open(input_filename, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return

    if operation == "compression":
        # Reverse the first 512 bits
        data = reverse_bits(data[:512]) + data[512:]

        # Perform custom bit replacements for bit lengths ranging from 23 to 100 bits
        for bit_length in range(23, 101):
            num_steps = 100
            check_condition = lambda x: (x < threshold) if less_than else (x >= threshold)
            data = perform_custom_bit_replacements(data, bit_length, num_steps, check_condition)
    elif operation == "extraction":
        # Reverse the first 512 bits
        data = reverse_bits(data[:512]) + data[512:]

        # Perform custom bit replacements for bit lengths ranging from 23 to 100 bits
        for bit_length in range(23, 101):
            num_steps = 100
            check_condition = lambda x: (x < threshold) if less_than else (x >= threshold)
            data = perform_custom_bit_replacements(data, bit_length, num_steps, check_condition)
    else:
        print("Invalid operation. Please use 'compression' or 'extraction'.")
        return

    try:
        with open(output_filename, 'wb') as file:
            file.write(data)
        print(f"Data successfully {operation} and saved to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{output_filename}' not found.")

# Ask the user for options
print("Options:")
print("1. Compression and Save")
print("2. Extraction and Save")
option = input("Select an option (1 or 2): ")

if option == "1":
    # Compression and Save
    input_file_name = input("Enter the name of the input file for compression: ")
    output_file_name = input("Enter the name of the output file for saving compressed data: ")

    # Set the threshold condition for compression
    threshold = (2 ** 23) // 2  # Update this threshold as needed
    less_than = True  # Initialize as less than threshold
    if 23 % 2 == 0:
        less_than = not less_than  # For even bit lengths, alternate between less than and greater than

    condition = lambda x: (x < threshold) if less_than else (x >= threshold)
    
    read_write_binary_data(input_file_name, output_file_name, "compression", condition)

elif option == "2":
    # Extraction and Save
    input_file_name = input("Enter the name of the input compressed file for extraction: ")
    output_file_name = input("Enter the name of the output file for saving extracted data: ")

    # Set the threshold condition for extraction
    threshold = (2 ** 23) // 2  # Update this threshold as needed
    less_than = True  # Initialize as less than threshold
    if 23 % 2 == 0:
        less_than = not less_than  # For even bit lengths, alternate between less than and greater than

    condition = lambda x: (x < threshold) if less_than else (x >= threshold)
    
    read_write_binary_data(input_file_name, output_file_name, "extraction", condition)

else:
    print("Invalid option. Please select 1 for Compression and Save or 2 for Extraction and Save.")