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
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum=0
    for i in arr:
        sum+=i
    print(sum-arr[-1], sum-arr[0])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

####Problem 3###############################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ind='A'
    a=s[8]
    if a=='P':
        ind='P'
    new_as=s[:8]
    m=new_as[:2]
    if ind == 'A':
        if int(m)==12:
            modified='00'+new_as[2:]
            return modified
        else:
            return new_as
    elif int(m)==12:
        return new_as
    else:
        new_ps=new_as.replace(':', '')
        new_pss=int(new_ps)+120000
        modified= str(new_pss)[:2] + ':' + str(new_pss)[2:4]+':' + str(new_pss)[4:6]
        return modified
OR
    if s[-2] == 'A':
        if s[0:2] == '12':
            return '00' + s[2:-2]
        return s[0:-2]
    if s[0:2] == '12':
        return s[0:-2]
    return str(int(s[0:2]) + 12) + s[2:]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

            
