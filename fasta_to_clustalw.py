from Bio import SeqIO
from sys import argv

with open(argv[1], "r") as input_handle:
    with open("012951.aln", "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "fasta")
        count = SeqIO.write(sequences, output_handle, "clustal")
