#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=1
    b=2
    sum=0
    while b<n:
        if(b%2==0):
            sum+=b
        a,b = b,a+b
    print(sum)
