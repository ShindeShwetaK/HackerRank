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
######################################################################
#Q2.

