#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley1=0
    land = 0
    for i in s:
        if i=='U':
            land+=1
        if i=='D':
            land+=-1
        if land==0 and i=='U':
            valley1 +=1
    return valley1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    
    s = input()
    
    result = countingValleys(n, s)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
