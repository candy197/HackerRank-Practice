import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2==1:
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