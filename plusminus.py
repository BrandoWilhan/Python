#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#



def plusMinus(arr, size):
    # Write your code here
    positives = 0
    negatives = 0
    zeros = 0

    for i in arr:
        if(i > 0):
            positives += 1
        if(i == 0):
            zeros += 1
        if(i < 0):
            negatives += 1
    print(f'{positives/size:.6f}')
    print(f'{negatives/size:.6f}')
    print(f'{zeros/size:.6f}')
    
                    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
