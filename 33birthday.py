# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import random

days = int(sys.argv[1])
people = int(sys.argv[2])
run = 100000
shared = 0

#set number of trails to run
for trails in range(run):
	found = False
	cal = [0 for i in range(days)]  #assign 0 to all the calendar dates

	for personel in range(people):
		birthday = random.randint(0, days - 1) #generate random birthday
		cal[birthday] += 1
		
	for val in cal:
		if val > 1:
			found = True
			break
	if found:
		shared += 1
print(f'{shared/run:.3f}')

"""	
python3 33birthday.py 365 23
0.571
"""

