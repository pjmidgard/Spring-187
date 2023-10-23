# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas

1. **Author Information**: The code starts with an author comment, indicating the author as "Jurijus Pacalovas."

2. **Imports and Libraries**: The script imports the `random` module to generate random numbers.

3. **Function Definitions**:

   - `read_0_to_255_data(file_name)`: This function reads binary data from a file, assumed to be in the 0-255 range, and returns it.

   - `apply_variations(data, variation_factor)`: This function applies variations (in this code, multiplying by a factor) to the data and returns the modified data.

   - `generate_random_huffman_trees(num_trees, min_bits, max_bits)`: This function generates random Huffman trees (bit patterns) specified by the number of trees, minimum and maximum bit lengths, and returns them as a list of bytes.

   - `compress_data(data, huffman_trees)`: Given data and a list of Huffman trees, this function compresses the data using Huffman coding and returns the compressed data.

   - `extract_data(compressed_data, huffman_trees)`: This function extracts data from compressed data using the provided Huffman trees and returns the extracted data.

   - `translate_to_0_255(data)`: This function translates binary data back to the 0-255 range.

   - `save_to_binary_file(file_name, data)`: This function saves data to a binary file.

4. **Main Program**:

   - The main program is a loop where the user is prompted to select an option (1 for Compression, 2 for Extraction, or 3 to Exit).

   - If the user selects "1" for Compression:
     - They are asked to provide an input file with data in the 0-255 range.
     - Variations (multiplying by a factor) are applied to the data.
     - Random Huffman trees are generated.
     - Data is compressed using Huffman coding with these trees.
     - The compressed data is translated back to the 0-255 range.
     - The result is saved to an output file.

   - If the user selects "2" for Extraction:
     - They are asked to provide an input file with data in the 0-255 range with variations.
     - Random Huffman trees are generated.
     - Data is extracted from the input file using Huffman trees.
     - The extracted data is translated back to the 0-255 range.
     - The result is saved to an output file.

   - The program ends with a "Program terminated" message.
