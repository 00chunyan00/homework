# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
rev = ''
for i in range(len(dna)):
	if   dna[i] == 'A': rev = 'T' + rev
	elif dna[i] == 'C': rev = 'G' + rev
	elif dna[i] == 'G': rev = 'C' + rev
	else:               rev = 'A' + rev
print(rev)
	

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
