# Spring-187
Spring-187
Random Compression Created by Jurijus Pacalovas 


1. **`reverse_bits` Function:**
   - This function takes two parameters, `data` and `step`.
   - It defines a dictionary called `replacements`, which maps specific bit patterns to their replacements.
   - It performs bit pattern replacements in the `data` using the `replacements` dictionary.
   - It also includes additional bit replacements based on the `step` value.
   - The modified `data` is returned as the result.

2. **`find_pythagorean_triples` Function:**
   - This function takes a single parameter, `limit`.
   - It initializes several variables, including `d`, `e`, `f`, and `g`.
   - It iterates through values of `a` and `b` to find Pythagorean triples where `c` is a perfect square.
   - The found Pythagorean triples are appended to the `triples` list.
   - The list of Pythagorean triples is returned.

3. **`triples_to_binary` Function:**
   - This function takes a list of Pythagorean triples, `triples`, as input.
   - It converts the Pythagorean triples into binary data and appends it to the `binary_data`.
   - It performs range checks to ensure that each component of the triple is within the valid byte range (0-255).
   - The binary data is returned as a bytes object.

4. **`binary_to_triples` Function:**
   - This function takes binary data as input.
   - It converts the binary data back into Pythagorean triples and returns them in a list.

5. **`apply_bit_replacements` Function:**
   - This function applies bit replacements to the `data` multiple times based on the `repeat` parameter and `step` value.
   - It repeatedly calls the `reverse_bits` function to modify the data.

6. The script interacts with the user to select one of two options: compression or extraction:
   - **Compression**:
     - It takes the name of an input file and reads its contents.
     - It applies bit replacements iteratively, creating a compressed representation.
     - Pythagorean triples are generated, converted to binary data, and appended to the compressed data.
     - The script saves the compressed data to an output file in binary mode.

   - **Extraction**:
     - It takes the name of an input compressed file.
     - The compressed data undergoes bit replacements in reverse order.
     - The binary data representing Pythagorean triples is extracted and converted back to triples.
     - The extracted triples are not printed but could be used or further processed.

Overall, this script demonstrates a fictional data compression and extraction process involving bit manipulation and the use of Pythagorean triples as a data representation technique. It's essential to note that the actual compression and extraction methods are not explicitly defined in the script and would need to be implemented separately.


