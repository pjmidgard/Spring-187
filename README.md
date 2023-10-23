# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas

1. **Importing Modules**: The code begins by importing the `random` module. This module is used for generating random values, which is crucial for creating Huffman trees.

2. **Data Reading and Processing Functions**:
   - `read_0_to_255_data(file_name)`: This function reads binary data from a file in the range 0-255.
   - `apply_variations(data, variation_factor)`: This function applies variations to the input data, such as multiplying each byte by a specified factor.
   - `translate_to_0_255(data)`: This function converts binary data to the 0-255 range by casting each byte to an integer.
   - `save_to_binary_file(file_name, data)`: This function saves binary data to a file.

3. **Huffman Tree Generation Functions**:
   - `generate_random_huffman_trees(num_trees, min_bits, max_bits)`: This function generates random Huffman trees (bit patterns) and returns them as a list of bytes.

4. **Data Compression and Extraction Functions**:
   - `compress_data(data, huffman_trees)`: This function compresses data using a list of Huffman trees.
   - `extract_data(compressed_data, huffman_trees)`: This function extracts data from compressed data using Huffman trees.

5. **Main Program**:
   - The program runs in a loop, allowing the user to select between three options: Compression (1), Extraction (2), or Exit (3). Invalid options trigger an error message.
   - If the user selects "Compression" (option 1), they are prompted to input the names of the input and output files.
     - The original data is read from the input file in the 0-255 range.
     - Variations (e.g., multiplication by a factor) are applied to the data.
     - Random Huffman trees are generated and saved to a binary file.
     - The data is compressed using the generated Huffman trees and saved as a binary file in the 0-255 range variations.
   - If the user selects "Extraction" (option 2), they are prompted to input the names of the input and output files.
     - Varied data is read from the input file.
     - Huffman trees are loaded from the binary file.
     - Data is extracted from the varied data using the Huffman trees.
     - The extracted data is saved to an output file in the 0-255 range.
   - The program displays success messages after performing the selected operation.

6. **Saving Huffman Trees**:
   - To save the Huffman trees, a new function `save_huffman_trees_to_file` is introduced. It writes the Huffman trees to a binary file named "huffman_trees.bin" during the compression process and reads them during extraction.
