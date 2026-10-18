## PROBLEM 20: Validating the Phone Number

import re

# Compile regex pattern
pattern = re.compile(r'^[789]\d{9}$')

# Read number of inputs
n = int(input())

for _ in range(n):
    s = input().strip()
    if pattern.match(s):
        print("YES")
    else:
        print("NO")