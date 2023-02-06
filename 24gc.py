# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
GC = 0
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
for i in range(len(dna)-1):
	if dna[i] == 'G' or dna[i] == 'C': GC += 1
print(f'{GC/len(dna):.2}')
"""
python3 24gc.py
0.42
"""
