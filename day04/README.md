# Day 04 – Protein Sequence Comparison Web Application

## About the Project

For this assignment, I continued working on my project from Day 03, where I created a Python program to compare protein sequences.

In Day 03, the program worked through the terminal and saved the comparison results in a CSV file.

For Day 04, I wanted to make the program easier to use by creating a web application using Flask.

Instead of running Python code manually, users can now upload their own FASTA files, compare protein sequences, and view the results directly on a webpage.

The application also allows users to download the results as an Excel file.

## What Does the Application Do?

The application:

1. Allows users to upload a FASTA file containing at least two protein sequences.
2. Reads the protein sequences using Biopython.
3. Compares every possible pair of proteins.
4. Uses global sequence alignment with the BLOSUM62 matrix.
5. Calculates the percentage of identical amino acids between each pair.
6. Calculates the percentage of differences.
7. Displays the results in a table on the webpage.
8. Allows users to download the results as an Excel file.
9. Displays error messages if the uploaded file is invalid.

For example, when I uploaded my original FASTA file containing 8 opsin sequences, the application performed 28 comparisons.

## How Does It Work?

The application uses three main Python files and tools:

**1. sequence_comparison.py – Sequence Alignment**

This file contains the original sequence comparison function from Day 03.

The function `calculate_sequence_identity` uses Biopython to align two protein sequences and calculate their identity and difference percentages.

The alignment includes gaps, which represent positions where one protein has an amino acid and the other does not.

The identity percentage is calculated by dividing the number of identical amino acids by the total alignment length, including gaps.

**2. app.py – Flask Web Application**

Flask is a Python library used to create web applications.

The `app.py` file connects the Python program to the webpage.

It receives the uploaded FASTA file, reads the sequences, and uses the original comparison function to calculate the results.

It also creates an Excel file using the openpyxl library.

**3. index.html – Web Interface**

This file defines how the webpage looks.

It includes the FASTA upload option, the Compare Sequences button, the results table, and the Download Excel button.

## Results

I tested the application using the same FASTA file from Day 03, containing 8 opsin proteins:

Opn6a, Opn6b, Opn7a, Opn7c, Opn7d, Opn8a, Opn8b, and Opn8c.

The application successfully performed 28 comparisons.

The results were displayed directly on the webpage and could also be downloaded as an Excel file.

I compared the Excel results with the original CSV results from Day 03 and confirmed that all 28 comparisons gave identical values.

## Testing

I tested both the original program and the new web application.

I also tested how the application handles invalid FASTA files.

**Test 1 – FASTA File With One Sequence**

I uploaded a FASTA file containing only one protein sequence.

The application displayed an error message explaining that at least two sequences are required.

**Test 2 – Invalid Protein Sequence**

I uploaded a FASTA file containing invalid characters in one of the protein sequences.

The application displayed an error message identifying the problematic sequence.

These tests showed that the application can handle these input errors without crashing.

## Project Files

* `opsin_sequences.fasta` – Contains the original 8 opsin sequences used for testing.
* `sequence_comparison.py` – Contains the original sequence alignment logic.
* `app.py` – Runs the Flask web application.
* `templates/index.html` – Defines the web interface.
* `requirements.txt` – Lists the Python libraries required for the project.

## Using AI

I used GitHub Copilot in VS Code to help me develop the web application.

I explained what I wanted the application to do, and Copilot generated the Flask code and HTML interface.

I then reviewed the generated code and asked Copilot to make several improvements.

I also tested the application to make sure it worked correctly and produced the same results as the original program.

## My Prompts

### Prompt 1 – Creating the Web Application

I asked Copilot to turn my Day 03 protein sequence comparison program into a Flask web application.

I requested a simple interface where users could upload FASTA files, compare all possible pairs of proteins, view the results in a table, and download the results.

I also asked Copilot to reuse the original sequence comparison function instead of writing a new alignment method.

### Prompt 2 – Improving the Application

I asked Copilot to display the comparison results directly on the webpage and replace the CSV download option with an Excel download option using openpyxl.

### Prompt 3 – Adding Validation and Requirements

I asked Copilot to check that the FASTA file contains at least two protein sequences and to create a `requirements.txt` file listing the required libraries.