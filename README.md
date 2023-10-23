# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas


1. **Random Data Generation (generate_random_data)**:
   - This function generates random binary data of a specified length in bits using the `random` module. It returns a `bytes` object.

2. **Bit Patterns (Huffman Trees)**:
   - The code creates 99 sets of bit patterns, which are essentially arrays of random binary data with varying lengths, ranging from 8 to 106 bits. These bit patterns are stored in the `bit_patterns` list.

3. **Compression (compress_data) Function**:
   - This function is designed to compress data using the 99 Huffman trees. It takes two arguments: the data to be compressed and the list of bit patterns.
   - The function iterates through the input data and checks if any of the Huffman trees' patterns match at the beginning of the data.
   - If a match is found, the matching pattern is appended to the `compressed_data` bytearray, and the data is shortened by the length of the pattern.
   - This process continues until all data is compressed, and the result is returned as a `bytes` object.

4. **Extraction (extract_data) Function**:
   - This function is intended for extracting data that was previously compressed. It takes two arguments: the compressed data and the list of bit patterns.
   - Similar to the compression function, it iterates through the compressed data and looks for matching patterns from the Huffman trees.
   - When a pattern is found, it is appended to the `extracted_data` bytearray, and the compressed data is reduced accordingly.
   - The extracted data is returned as a `bytes` object.

5. **Data Translation (translate_to_0_255)**:
   - This function converts binary data to the 0-255 range. It converts each byte in the input data to an integer value.

6. **File Input and Output Functions (save_to_binary_file and read_from_binary_file)**:
   - These functions handle saving and reading binary data to and from files. They use the `'wb'` mode for writing and `'rb'` mode for reading in binary.

7. **Main Program Loop**:
   - The program presents a menu to the user with three options: Compression, Extraction, or Exit.
   - It ensures that the user selects a valid option (1, 2, or 3).

8. **Option Processing**:
   - If the user chooses compression (Option 1), the program asks for input and output file names, compresses the data, translates it to the 0-255 range, and saves it to an output file.
   - If the user chooses extraction (Option 2), it performs a similar process but for extracting data.
   - The program terminates if the user selects Option 3 (Exit).

This code essentially demonstrates a basic data compression and extraction mechanism using a set of predefined Huffman trees. However, the use of random Huffman trees in practice is not recommended, as real-world data compression typically relies on more efficient and predictable algorithms. This code serves as a simplified educational example.
