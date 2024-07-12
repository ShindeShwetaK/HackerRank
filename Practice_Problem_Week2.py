#####################################Week2#############################
#https://www.hackerrank.com/interview/preparation-kits/one-month-preparation-kit/one-month-week-two/challenges
######################################################################
#Q1.Sale by match.
from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    pairs=Counter(ar)
    count_pairs=0
    for i in pairs:
        count_pairs+=pairs.get(i)//2
    return count_pairs
result = sockMerchant(n, ar)
#Python Counter:https://www.youtube.com/watch?v=Lmsz6h25yiA
######################################################################
#Q2.ZigZag
def findZigZagSequence(a, n):
    a.sort()
    mid = n//2
    a[mid], a[n-1] = a[n-1], a[mid]
    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
######################################################################
#Q3.PageFlip
def a(n,p):
    if (p <= n/2):
        return(p//2) 
    return (n//2- p//2)
    or
    l=p//2
    n=n+1 if n%2==0 else n
    r=(n-p)//2
    return min(l,r)
######################################################################
#Q4.
######################################################################
#Q5.Encrypt Message
    o='abcdefghijklmnopqrstuvwxyz'
    #while k>len(o):
       # k-=len(o)
    new_o= o[k%26:]+o[:k%26]
    u_new_o=new_o.upper()
    u_o=o.upper()
    return_str=''
    D={}
    for i in range(len(o)):
        D[o[i]]=new_o[i]
        D[u_o[i]]=u_new_o[i]
    for i in s:
        if i in D:
            return_str+=(D[i])
        else: 
            return_str+=(i)
        
    return return_str
######################################################################
#Q6.Min Max
def maxMin(k, arr):
    # Write your code here
    test_arr=[]
    min_no=[]
    sort_arr=sorted(arr, reverse=True)
    for i in range(len(sort_arr)-(k-1)):
        test_arr=sort_arr[i:i+k]
        min_no.append(test_arr[0]-test_arr[-1])
    return (min(min_no))
     # we can use combination connection to  create different combination of given set or array
     from itertools import combinations
     arr=[1,2,3,4,10,20,30,40,100,200]
     k=4
     min_no=[]
     unique_combinations = set(combinations(arr, k))
     #print(unique_combinations)
     for comb in unique_combinations:
          #print(comb)
          min_no.append(max(comb)-min(comb))
     print(min(min_no))
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.
######################################################################
#Q2.

