# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas 

1. The code begins with a few predefined functions, including:
   - `reverse_bits(data)`: A function to reverse specific bit patterns in binary data.
   - `perform_custom_bit_replacements(data, bit_length, num_steps, condition)`: A function to perform custom bit replacements based on the specified steps and a condition function.

2. The `read_write_binary_data` function takes care of reading and writing binary data. It has parameters for input and output filenames, the operation ("compression" or "extraction"), and a condition function.

3. The main part of the code is user-driven, offering two options:
   - Option 1: Compression and Save
   - Option 2: Extraction and Save

4. For compression, the code:
   - Prompts the user to provide the name of the input file for compression and the output file for saving compressed data.
   - Defines a threshold and a condition based on bit length (23 bits in this example).
   - Reads the input file, reverses the first 512 bits, and performs custom bit replacements based on the condition.
   - Writes the modified data to the output file and informs the user of successful compression.

5. For extraction, the code:
   - Prompts the user to provide the name of the input compressed file and the output file for saving the extracted data.
   - Defines a threshold and a condition similar to the compression part.
   - Reads the input file, reverses the first 512 bits, and performs custom bit replacements based on the condition.
   - Writes the modified data to the output file and informs the user of successful extraction.

6. The code also handles some error checking for file operations, such as checking if the files exist.

7. The threshold condition for bit replacement can be easily customized within the code. The code also provides support for bit lengths ranging from 23 to 100 bits, allowing for versatile use in different scenarios.

This code is useful for those who need to apply specific bit replacements based on conditions for compression and extraction of binary data. It can be adapted and extended for various applications, especially when working with binary data files.


