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
run = 10
shared = 0
for i in sys.argv[1:]:
	for bd in range(run):
#I am not done yet....
				
print(shared/run)
"""
python3 33birthday.py 365 23
0.571
"""

