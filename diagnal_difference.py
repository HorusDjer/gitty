#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    first_diag = list()
    index = 0
    for row in arr:
        first_diag.append(row[index])
        index += 1
    
    index = -1
    sec_diag = list()
    for row in arr:
        sec_diag.append(row[index])
        index -= 1
    
    return abs(sum(first_diag) - sum(sec_diag))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
