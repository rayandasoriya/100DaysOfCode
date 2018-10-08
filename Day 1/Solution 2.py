#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n, m = [int(n) for n in input().split()]
    l = [0]*(n+1)
    for _ in range(m):
        a, b, k = [int(n) for n in input().split()]
        l[a-1] += k
        l[b] -= k;
    max = a = 0
    for i in l:
        a+=i;
            if max<a:
            max=a;
        print(max)
