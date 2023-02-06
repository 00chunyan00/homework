# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random
length = 30 
dna = ''
count = 0
for i in range(length):
	r = random.random()
	if r <= 0.6:
		dna += random.choice('TA')
		count += 1
	else: 
		dna += random.choice('CG')

print(length,count/length,dna)
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
