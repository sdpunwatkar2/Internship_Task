## problem 15: Game of thrones


#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    odd_count = 0

    for char in set(s):
        if s.count(char) % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
