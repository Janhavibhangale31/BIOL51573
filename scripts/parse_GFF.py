#! /usr/bin/env python3

import argparse
import gff_functions

# create argument parser 
def get_args():

    parser = argparse.ArgumentParser (description="Parse a Fasta file and GFF file ")
    
# add command line
    parser.add_argument("fasta_file", help="path to the fasta file")

    parser.add_argument("gff_file", help="path to the gff file")

    return parser.parse_args()   

# Read genome sequence
def main():
    args = get_args()
    
    genome_sequence = gff_functions.read_fasta(args.fasta_file, )

    # Extract sequences from GFF
    sequences = gff_functions.read_gff(args.gff_file, genome_sequence)

    # Write output
    gff_functions.write_output(sequences)


    
if __name__ == '__main__':
    main()

