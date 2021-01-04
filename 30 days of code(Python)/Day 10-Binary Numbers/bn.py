#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
def func(n):
    count = 0
    
    # Count the number of iterations to 
    # reach n = 0. 
    
    while (n!=0): 
      
        # This operation reduces length 
        # of every sequence of 1s by one. 
        n &= n << 1
   
        count += 1 
    return count 
print(func(n))