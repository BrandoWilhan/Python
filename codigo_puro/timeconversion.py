#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    slist = list(s)
    print(slist)
    if(slist[8] == 'A' and slist[0] == '1'):
        slist[:2] = ['0','0']
        del slist[8:]
        s = ''.join(slist)
    
    elif(slist[8] == 'P' and slist[0] == '1' and slist[1] == '2'):
        del slist[8:]
        s = ''.join(slist)
    
    elif(slist[8] == 'A' and slist[0] != '1'):
        del slist[8:]
        s = ''.join(slist)
    
    else:
        del slist[8:]
        hour = slist[0] + slist[1]
        hour = int(hour)
        hour += 12
        hour = str(hour)
        del slist[:1]
        slist[0] = hour
        s = ''.join(slist)
            
    return s

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
   # fptr.write(result + '\n')

   # fptr.close()
