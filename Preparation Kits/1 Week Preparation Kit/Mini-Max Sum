import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    sums = []
    
    for i in range(5):
        copy_arr = arr.copy()
        el = arr[i]
        copy_arr.remove(el)
        sums.append(sum(copy_arr))
        
    print(min(sums), max(sums))    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
