
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
# The function accepts STRING encoded as parameter.
#
def decode(encoded):
    encoded = encoded[::-1]
    n = 1
    # a = [encoded[i:i+n] for i in range(0, encoded(line), n) n =2 if 32<=i<133 else 3]
    a = []
    i = 0
    while i != len(encoded):
        if int(encoded[i]) ==1:
            n = 3
        else:
            n = 2
        a.append(int(encoded[i:i+n]))
        i+=n
    m = ''.join(chr(i) for i in a)
    return m


# Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    encoded = input()
    
    result = decode(encoded)
    
    fptr.write(result + '\n')
    
    fptr.close()

