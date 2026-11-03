Day 03 – Comparing Protein Sequences
About the Project

For this assignment, I decided to create a Python program related to my research.

I study a group of light-sensitive proteins called opsins, and I wanted to compare their amino acid sequences to see how similar or different they are.

I used a FASTA file containing sequences of 8 opsin proteins: Opn6a, Opn6b, Opn7a, Opn7c, Opn7d, Opn8a, Opn8b, and Opn8c.

What Does the Program Do?

The program:

1. Reads the protein sequences from the FASTA file.
2. Compares every possible pair of proteins.
3. Uses Biopython to align the sequences.
4. Calculates the percentage of identical amino acids between each pair.
5. Calculates the percentage of differences.
6. Displays the results in the terminal and saves them in a CSV file.

Since I used 8 proteins, the program makes 28 comparisons.

How Does It Work?

The program uses a method called sequence alignment, which places two protein sequences next to each other to find matching amino acids.

It then calculates the percentage of positions where the amino acids are exactly the same.

Also, the calculation includes gaps in the alignment, which represent positions where one protein has an amino acid and the other does not.

Results

The program creates a table showing the identity and difference percentages for each pair of proteins.

The results are saved in a CSV file, which can also be opened in Excel.

Files
opsin_sequences.fasta – Contains the 8 protein sequences.
sequence_comparison.py – The Python code that compares the sequences.
sequence_comparison_results.csv – Contains the comparison results.

Using AI

I used GitHub Copilot in VS Code to help me write the Python program.

I explained what I wanted the program to do, and Copilot generated the code. I then reviewed the code and asked Copilot to make some changes.

My Prompts

Prompt 1 – Creating the Program

I asked Copilot to create a Python program that reads eight opsin protein sequences from a FASTA file, compares every pair, calculates the identity and difference percentages, and saves the results in a CSV file.

Copilot used Biopython to align the protein sequences. 
(Biopython is a Python library for working with biological data)

Prompt 2 – Adding a Function

I asked Copilot to modify the code by adding a function called calculate_sequence_identity that performs the alignment and calculates the identity and difference percentages.

I also asked it to keep the rest of the program unchanged.