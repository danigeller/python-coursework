import base64
import io
from itertools import combinations

from Bio import SeqIO
from flask import Flask, render_template, request
from openpyxl import Workbook
from werkzeug.exceptions import RequestEntityTooLarge

from sequence_comparison import aligner, calculate_sequence_identity


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWYBJZXUO")


def read_protein_sequences(fasta_text):
    """Parse and validate uploaded FASTA text."""
    try:
        records = list(SeqIO.parse(io.StringIO(fasta_text), "fasta"))
    except ValueError as error:
        raise ValueError("The uploaded file is not valid FASTA.") from error

    if not records:
        raise ValueError("The uploaded file is not valid FASTA or contains no sequences.")
    if len(records) < 2:
        raise ValueError("Please upload a FASTA file containing at least two sequences.")

    sequences = {}
    for record in records:
        sequence = str(record.seq).upper().rstrip("*")
        if not record.id or not sequence:
            raise ValueError("Every FASTA record must have a name and a sequence.")
        if record.id in sequences:
            raise ValueError("Each protein must have a unique FASTA header.")
        if any(residue not in AMINO_ACIDS for residue in sequence):
            raise ValueError(
                f"Sequence '{record.id}' contains characters that are not valid "
                "protein residues."
            )
        sequences[record.id] = sequence

    return sequences


def compare_sequences(sequences):
    """Compare every unique pair using the existing alignment function."""
    results = []
    for (name_a, sequence_a), (name_b, sequence_b) in combinations(
        sequences.items(), 2
    ):
        identity, difference = calculate_sequence_identity(
            sequence_a, sequence_b, aligner
        )
        results.append(
            {
                "Protein 1": name_a,
                "Protein 2": name_b,
                "Identity (%)": round(identity, 2),
                "Difference (%)": round(difference, 2),
            }
        )
    return results


def create_excel_file(results):
    """Create an Excel workbook containing the comparison results."""
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Sequence Comparison"
    worksheet.append(["Protein 1", "Protein 2", "Identity (%)", "Difference (%)"])

    for row in results:
        worksheet.append(
            [
                row["Protein 1"],
                row["Protein 2"],
                row["Identity (%)"],
                row["Difference (%)"],
            ]
        )

    excel_file = io.BytesIO()
    workbook.save(excel_file)
    return base64.b64encode(excel_file.getvalue()).decode("ascii")


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    excel_data = None
    error = None

    if request.method == "POST":
        uploaded_file = request.files.get("fasta_file")
        if uploaded_file is None or not uploaded_file.filename:
            error = "Choose a FASTA file to upload."
        else:
            try:
                fasta_text = uploaded_file.read().decode("utf-8-sig")
                sequences = read_protein_sequences(fasta_text)
                results = compare_sequences(sequences)
                excel_data = create_excel_file(results)
            except UnicodeDecodeError:
                error = "The uploaded file must be a UTF-8 encoded FASTA file."
            except ValueError as validation_error:
                error = str(validation_error)

    return render_template(
        "index.html", results=results, excel_data=excel_data, error=error
    )


@app.errorhandler(RequestEntityTooLarge)
def handle_large_upload(error):
    """Show a friendly message when an upload exceeds Flask's size limit."""
    return (
        render_template(
            "index.html",
            results=None,
            excel_data=None,
            error="The uploaded file is too large. Please choose a file smaller than 5 MB.",
        ),
        413,
    )


if __name__ == "__main__":
    app.run()
