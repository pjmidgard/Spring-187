# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas

1. **Importing Libraries:** The script starts by importing the `random` library, which is used to generate random Huffman trees.

2. **Reading Data (Lines 6-15):** The `read_0_to_255_data` function reads data from a binary file in the 0-255 range. It handles file opening and error-checking, ensuring that the data is read correctly.

3. **Applying Variations (Lines 18-22):** The `apply_variations` function takes data and a variation factor as input and applies variations to the data. The variation factor can be modified to scale the data values. In the code, a variation factor of 256 is applied, effectively shifting the data values left by 8 bits.

4. **Generating Random Huffman Trees (Lines 25-28):** The `generate_random_huffman_trees` function generates a specified number of random Huffman trees. The code creates 99 random Huffman trees with bit lengths ranging from 8 to 106 bits. These trees are used in the compression and extraction processes.

5. **Compression (Lines 31-44):** In the compression section, the code checks if the input data matches any of the random Huffman trees. When a match is found, the corresponding Huffman tree is added to the compressed data. This process continues until the entire input data is compressed.

6. **Extraction (Lines 47-60):** The extraction process reverses the compression. It uses the same set of Huffman trees generated during compression to identify and remove Huffman trees from the compressed data. The result is the extracted data.

7. **Data Translation (Lines 63-66):** The `translate_to_0_255` function is responsible for translating binary data back to the 0-255 range. This ensures that the extracted data remains within the specified range.

8. **Saving Data (Lines 69-76):** The code provides functions to save both the compressed and extracted data to binary files. It also saves the random Huffman trees to a binary file for use during extraction.

9. **Main Program (Lines 79-102):** The main program starts by presenting the user with options: compression, extraction, or program termination. The user selects an option, and the corresponding section of the code is executed. The program loop continues until the user chooses to exit.

10. **User Interaction (Lines 79-88):** The code uses a `while` loop to repeatedly prompt the user for their choice. The loop continues until a valid option (1, 2, or 3) is selected. Invalid choices result in an error message.

11. **Compression Section (Lines 91-102):** If the user selects compression (option 1), the code proceeds to compress the data. It applies variations, generates random Huffman trees, saves these trees to a file, and compresses the data using these trees. The compressed data is then translated and saved to an output file.

12. **Extraction Section (Lines 104-115):** If the user selects extraction (option 2), the code performs the extraction process. It loads the previously saved Huffman trees, extracts the data, translates it back to the 0-255 range, and saves the result in an output file.

13. **Program Termination (Line 117):** After completing the selected operation, the code displays a "Program terminated" message and exits.
