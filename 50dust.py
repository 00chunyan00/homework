# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import argparse
import mcb185
import math

#setup 
parser = argparse.ArgumentParser(description='A better version of Dust program')

#positional arguments
parser.add_argument('file',type=str, metavar='<path>', help='dust program')


#optional argument with default parameters
parser.add_argument('-w','--window_size', required=False, type=int, default=11,
	metavar='<int>', help='optional integer argument [%(default)i]')
parser.add_argument('-t', required=False, type=float, default=1.4,
	metavar='<float>',help='optional floating point argument [%(default).1f]')
parser.add_argument('-s',action='store_true',
	help='mask with N')
arg = parser.parse_args()
#I need to make a new list, and change the sequence within the list

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
	


for protein_name, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	seq_list = list(seq)
	for i in range(len(seq) -arg.window_size +1):
		window = seq[i:i+arg.window_size]
		if entropy_seq(window) < arg.t:
			for j in range(i, i+arg.window_size):
				if arg.s:
					seq_list[j] = 'N'
				else:
					seq_list[j] = seq_list[j].lower()
					
	print_seq = ''.join(seq_list)
	print(f'>{protein_name}')

	for k in range(0, len(print_seq), 60):
		print(print_seq[k: k+60])
#print(arg.file)


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
