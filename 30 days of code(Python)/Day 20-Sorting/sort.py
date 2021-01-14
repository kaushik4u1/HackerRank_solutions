#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total =0
for i in range(n):
    noOfSwap = 0
    for j in range(n-1):
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            noOfSwap += 1
    total += noOfSwap 
    if(noOfSwap == 0):
        break
    
print("Array is sorted in {} swaps.".format(total))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))    
        
            