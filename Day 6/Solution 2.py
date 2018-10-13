#!/bin/python3

import sys

def icecreamParlor(n,m, a):
    # Complete this function
    d=dict()
    for i in range(n):
        if( a[i] in d and d[a[i]]!=0):
            print(d[a[i]],i+1)
            break
        if(a[i]<m):
            d[m-a[i]]=i+1



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        icecreamParlor(n,m, arr)
