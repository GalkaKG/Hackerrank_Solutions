#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    unique_el = 0
    is_unique = True

    for i in range(len(a)):
        for j in range(0, len(a)):
            if j == i:
                continue
            el1 = a[i]
            el2 = a[j]
            if el1 == el2:
                is_unique = False
        if is_unique:
            unique_el = a[i]
        is_unique = True

    return unique_el

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
