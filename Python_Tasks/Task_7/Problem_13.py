## Problem 13: Sherlock and the Valid String


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    char_freq = Counter(s)
    freq_count = Counter(char_freq.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) > 2:
        return "NO"

    freq1, freq2 = sorted(freq_count.keys())

    # Case 1: One character occurs only once
    if freq1 == 1 and freq_count[freq1] == 1:
        return "YES"

    # Case 2: One character occurs one extra time
    if freq2 == freq1 + 1 and freq_count[freq2] == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
