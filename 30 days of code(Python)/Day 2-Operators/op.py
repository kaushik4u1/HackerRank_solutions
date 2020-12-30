i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i1 = int(input())
d1 = float(input())
s1 = input('')
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(i+i1)
# Print the sum of the double variables on a new line.
print(d+d1)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+s1)#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip =meal_cost * (tip_percent/100) 
    tax =meal_cost * (tax_percent/100)
    total_cost =int(round(meal_cost + tip + tax))
    print(total_cost)
    
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
        
    solve(meal_cost, tip_percent, tax_percent)
    

        
