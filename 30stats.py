# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys

data = []
for val in sys.argv[1:]:
	data.append(float(val))
total = 0
count1 = len(data)
sum1 = 0

for val in data:
	total += float(val)
	mean = f'{total/count1:.3f}'
data.sort()
mid = count1 // 2 
if count1 % 2 == 1: 
	median = data[mid]

else:
	median = (data[mid-1] + data[mid]) / 2

for i in range(1, len(sys.argv)):
	sum1 += (float(sys.argv[i]) - float(mean)) ** 2
print('Count:', count1)
print('Minimum:', float(min(sys.argv)))
print('Maximum:',float(max(sys.argv)))
print('Mean:', f'{total/count1:.3f}')
print('Std. dev:', f'{(sum1 / count1) ** 0.5:.3f}')
print('Median', f'{float(median):.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000 
"""