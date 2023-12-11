import math
import os
import random
import re
import sys

"""
1 codition Odd number should be print in weird
2 even number inclusive(in range) range of 2 to 5 not weird
3 even number inclusive 6 to 20 print weird
4 even and greater than 20 print not weird
""""

if __name__ == '__main__':
    n = int(input().strip())


if n in range(2,5):
    if n%2==0:
        print("Not Weird")
            
    else:
        print("Weird")
elif (n in range(6,20)):
    if n%2==0:
        print("Weird")
            
    else:
        print("Not Weird")
elif (n > 20):
    if n%2==0:
        print("Not Weird")
    else :
        print("Weird")
       