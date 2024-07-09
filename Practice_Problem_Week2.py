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
#Q2.
