#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING encoded
#

def decode(codes, text):
    rows = ( line.split('\t') for line in codes )
    dictionary = { row[1]:row[0] for row in rows }
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                if dictionary[k] == '[newline]':
                    res+= "\n"
                    text = text[len(k):]
                else:
                    res += dictionary[k]
                    text = text[len(k):]
    return res






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    codes_count = int(input().strip())
    
    codes = []
    
    for _ in range(codes_count):
        codes_item = input()
        codes.append(codes_item)

    encoded = input()

result = decode(codes, encoded)

fptr.write(result + '\n')

fptr.close()
