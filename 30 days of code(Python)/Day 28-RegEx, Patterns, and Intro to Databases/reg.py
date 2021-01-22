#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
   res = []
N = int(input().strip())
for i in range(N):
    firstName,emailId=input().strip().split(' ')
    if '@gmail.com' in emailId:
        res.append(firstName)
print(*sorted(res),sep="\n")        

