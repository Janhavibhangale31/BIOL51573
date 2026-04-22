#!/usr/bin/env python3

def read_fasta(fasta_file):
    genome_sequence = ""

    with open(fasta_file, "r") as file:
        next(file)
        for line in file:
            genome_sequence += line.strip()
    return genome_sequence


def read_gff(gff_file, genome_sequence):
    sequences = []

    with open(gff_file, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue
            # line = sumeeta\tb\tc ==. cols = ["sumeeta", "b", "c"]
            cols = line.strip().split("\t")

            start = int(cols[3])
            end = int(cols[4])
            attributes = cols[8]

            seq_id = attributes.split("ID=")[1].split(";")[0]

            seq = genome_sequence[start-1:end]

            sequences.append((seq_id, seq))

    return sequences


def write_output(sequences):
    with open("covid_genes.fasta", "w") as out:
        for seq_id, seq in sequences:
            out.write(f">{seq_id}\n")
            out.write(f"{seq}\n")


