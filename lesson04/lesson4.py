# Lesson 4
# import statement
from math import ceil

# input
section1 = input("Enter first section: ")
section2 = input("Enter second section: ")
section3 = input("Enter third section: ")

# processing
cans = len(section1) + len(section2) + len(section3)

boxes = ceil(cans / 12)
leftover = boxes*12 - cans

total_cost = boxes * 14.95

# result
print("We would need {cans}.")
print("There would be {leftover} leftover.")
print("It would cost {total_cost} dollars.")
