# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas

1. **Random Data Generation**:
   - The code begins by importing the `random` module and defines a function `generate_random_data(num_bits)` to generate random binary data of a specified length in bits.

2. **Bit Patterns (Huffman Trees)**:
   - It generates 99 sets of bit patterns, ranging from 8 to 106 bits in length, and stores them in the `bit_patterns` list.

3. **Compression and Extraction Functions**:
   - Two primary functions, `compress_data` and `extract_data`, are defined to compress and extract data using the 99 Huffman trees. These functions identify and match the bit patterns to perform their respective operations.

4. **Data Translation**:
   - Another function, `translate_to_0_255(data)`, converts binary data to the 0-255 range, presumably for easier storage or transmission.

5. **File I/O Functions**:
   - The code includes two functions, `save_to_binary_file` and `read_from_binary_file`, for saving data to binary files and reading data from binary files, respectively. It handles exceptions for file not found scenarios.

6. **Main Program**:
   - The main program runs in a loop, providing options to the user:
     - Option 1: Compression
     - Option 2: Extraction
     - Option 3: Exit

7. **Option Processing**:
   - Depending on the user's choice, the program proceeds as follows:
     - **Compression (Option 1)**: It takes an input file, compresses the data using Huffman trees, translates the data, and saves it to an output file in the 0-255 range.
     - **Extraction (Option 2)**: It reads compressed data from an input file, extracts it using Huffman trees, translates the data, and saves it to an output file in the 0-255 range.

8. **Exit**:
   - The program terminates when the user selects Option 3.

This code seems to be a simplified example of data compression and extraction, but it has some limitations and potential improvements. For instance, the use of random Huffman trees may not be efficient or effective for real-world data compression.
