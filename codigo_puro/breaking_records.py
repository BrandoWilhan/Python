#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max = scores[0]
    min = scores[0]
    count = [0, 0]

    for x in scores:
        if(x > max):
            max = x
            count[0] += 1 
        if(x < min):
            min = x
            count[1] += 1
    
    return count
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print (result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()