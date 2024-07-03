####Problem 1###############################################################################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_p=0
    count_n=0
    count_z=0
    for i in arr:
        if i>0:
            count_p+=1
        elif i<0:
            count_n+=1
        else:
            count_z+=1
    print(f"{count_p/n:.6f}")
    print(f"{count_n/n:.6f}")
    print(f"{count_z/n:.6f}")

####Problem 2###############################################################################
            
