# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas

1. **Importing Libraries:**
   The code starts by importing the necessary Python libraries, including the `random` library for generating random numbers. This is important for both creating Huffman trees and introducing variations.

2. **Function Definitions:**
   The code defines several functions, each with specific purposes:

   - `read_0_to_255_data`: Reads data from a binary file in the 0-255 range.
   - `apply_variations`: Applies variations to the data (e.g., multiplication by a factor).
   - `generate_random_huffman_trees`: Generates a specified number of random Huffman trees with lengths in a given range.
   - `compress_data`: Compresses data using Huffman trees.
   - `extract_data`: Extracts data using Huffman trees.
   - `translate_to_0_255`: Translates binary data back to the 0-255 range.
   - `save_to_binary_file`: Saves data to a binary file.
   - `read_from_binary_file`: Reads data from a binary file.

3. **Main Program:**
   The main program is structured around a menu system, allowing the user to select one of the following options:

   - Option 1: Compression
   - Option 2: Extraction
   - Option 3: Exit

   The program loops until a valid option is selected, and it handles invalid selections gracefully.

4. **Option 1: Compression:**
   - The user is prompted to enter the name of an input file containing data in the 0-255 range.
   - They are also prompted to provide the name of an output file where the compressed data (in variations) will be saved.
   - The code reads the data from the input file, applies a specified variation factor (in this case, multiplying by 2), generates random Huffman trees, compresses the data into these trees, and translates the compressed data back to the 0-255 range with variations.
   - Finally, it saves the result to the output file.

5. **Option 2: Extraction:**
   - Similar to Option 1, the user is prompted to enter the names of the input and output files.
   - The code reads the data from the input file (which should be in the 0-255 range with variations), generates random Huffman trees, extracts the data from these trees, and translates it back to the 0-255 range.
   - It then saves the extracted data to the output file.

6. **Program Termination:**
   The program terminates and prints a message when the user selects Option 3 (Exit).
