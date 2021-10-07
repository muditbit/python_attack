#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumStones(arr):
    # Write your code here
    length = len(arr)
    split = len//2 + 1
    left = arr[:split]
    right = arr[split+1:]
    left = left.sort
    right=right.sort
    b=[]
    if sum(left)==sum(right):
        return sum(left) +sum(right)
    ''' elif sum(left)>sum(right):
             c=sum(right)
             for i in range(len(left)):
            
                if c<left[i]:
                b.append(c)

            else:
                b.append(left[i])
                c = c- left[i]
      '''          

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

    fptr.write(str(result) + '\n')

    #fptr.close()
