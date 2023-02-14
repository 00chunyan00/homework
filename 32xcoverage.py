# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys
import random
genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])
genome = []
end = genome_size - read_length
for size in range(genome_size):
	genome.append(0)
	
for start in range(0, read_number):
	start_pos = random.randint(0, end)
	for i in range(start_pos, start_pos + read_length):
		genome[i] += 1
#print(genome)	
mini = min(genome[read_length: - read_length])
maxi = max(genome[read_length: - read_length])
ave = sum(genome[read_length: -read_length])/len(genome)
print(mini, maxi,f'{ave:.5f}')

		
		

	
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
