# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas 

1. Import the `random` module to generate random data and other necessary modules.

2. Define a function `generate_random_data(num_bits)` to create random data of a specified length in bits.

3. Generate 99 sets of random bit patterns (Huffman trees) ranging from 8 to 106 bits in length.

4. Define a function `compress_data(data, bit_patterns)` to compress input data using the generated Huffman trees. It iterates through the data and looks for the longest matching bit patterns to compress the data.

5. Define a function `extract_data(compressed_data, bit_patterns)` to extract compressed data using the Huffman trees. It reverses the compression process by finding and removing the Huffman tree patterns.

6. Define functions to save data to a binary file and read data from a binary file, making it possible to save and retrieve data.

7. In the main program, the user is presented with options to perform compression, extraction, or exit.

8. If the user selects compression, they are prompted to enter the names of the input and output files. The program reads the data from the input file, compresses it using the Huffman trees, and saves the compressed data to the output file.

9. If the user selects extraction, they are also prompted to enter input and output file names. The program reads the compressed data from the input file, extracts it using the Huffman trees, and saves the extracted data to the output file.

10. The program allows users to continue selecting options until they choose to exit.

11. If the user selects the exit option or if there's an invalid input, the program terminates.

Keep in mind that this code is a simplified example and does not include some essential features like error handling, actual Huffman tree generation, or meaningful data compression. It's more of a demonstration of the structure and basic functionality needed for a Huffman coding-based compression and extraction program.
