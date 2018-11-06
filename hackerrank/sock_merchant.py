#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    total_socks = {}
    for num in ar:
        if num in total_socks:
            total_socks[num] += 1
        else:
            total_socks[num] = 1

    total = 0
    for value in total_socks.values():
        value = value // 2
        total = value + total

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()