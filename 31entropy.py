# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import math
import sys
probs = []
sum_probs = sum(probs)


for val in sys.argv[1:]:
	try:
		probs.append(float(val))
	except:
		raise ValueError(f'cannot conver {val} to a number')
	

try:
	assert(math.isclose(sum(probs), 1.0))
except:
	raise ValueError(f'Sum of probability do not add to 1')

h = 0
for val in probs:
	h += -(val * math.log2(val))
print(f'{h:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
