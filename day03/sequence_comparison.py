from itertools import combinations
from pathlib import Path
import csv

from Bio import Align
from Bio import SeqIO
from Bio.Align import substitution_matrices


# Keep input and output files beside this script.
folder = Path(__file__).parent
input_file = folder / "opsin_sequences.fasta"

# Also accept the misspelled filename currently in the folder.
if not input_file.exists():
    misspelled_input_file = folder / "opsin_sequnces.fasta"
    if misspelled_input_file.exists():
        input_file = misspelled_input_file

output_file = folder / "sequence_comparison_results.csv"

# Read all protein sequences and remove terminal stop characters.
sequences = {
    record.id: str(record.seq).rstrip("*")
    for record in SeqIO.parse(input_file, "fasta")
}

if not sequences:
    raise ValueError(f"No protein sequences were found in {input_file}.")

# Configure a global protein alignment with BLOSUM62 and affine gap penalties.
aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5


# Align two sequences and return their identity and difference percentages.
def calculate_sequence_identity(sequence_a, sequence_b, aligner):
    alignment = aligner.align(sequence_a, sequence_b)[0]
    identical_residues = 0

    for index_a, index_b in zip(alignment.indices[0], alignment.indices[1]):
        if index_a >= 0 and index_b >= 0:
            if sequence_a[index_a] == sequence_b[index_b]:
                identical_residues += 1

    identity = identical_residues / alignment.length * 100
    difference = 100 - identity
    return identity, difference


results = []

# Align every unique pair and calculate identity across all alignment columns.
for (name_a, sequence_a), (name_b, sequence_b) in combinations(sequences.items(), 2):
    identity, difference = calculate_sequence_identity(
        sequence_a, sequence_b, aligner
    )

    results.append(
        {
            "Protein 1": name_a,
            "Protein 2": name_b,
            "Identity (%)": f"{identity:.2f}",
            "Difference (%)": f"{difference:.2f}",
        }
    )

# Display the results as a simple aligned table.
headers = list(results[0])
column_widths = {
    header: max(len(header), *(len(row[header]) for row in results))
    for header in headers
}

print("  ".join(header.ljust(column_widths[header]) for header in headers))
print("  ".join("-" * column_widths[header] for header in headers))
for row in results:
    print("  ".join(row[header].ljust(column_widths[header]) for header in headers))

# Save the same results to a CSV file beside this script.
with output_file.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to {output_file.name}")
