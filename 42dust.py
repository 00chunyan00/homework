# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import mcb185
import math
import sys

def entropy(number):
	assert(math.isclose(1.0, sum(number)))
	h = 0
	for val in number:
		if val != 0: h -= val * math.log2(val)
	return h

def entropy_seq(seq):
	A = seq.count('A')/len(seq)
	C = seq.count('C')/len(seq)
	G = seq.count('G')/len(seq)
	T = seq.count('T')/len(seq)
	return entropy([A, C, G, T])
	
reading_frame = int(sys.argv[2])
threshold = float(sys.argv[3])


for protein_name, seq in mcb185.read_fasta(sys.argv[1]):
	seq_list = list(seq)
	for i in range(len(seq) -reading_frame +1):
		if entropy_seq(seq[i: i+reading_frame]) < threshold: seq_list[i] = 'N'
	seq = ''.join(seq_list)

for j in range(0, len(seq), 60):
	print(seq[j: j+60])

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
