#!/bin/python3
# problem no 1: Python If-Else


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2==0):
        if n>20:
            print("Not Weird")
        if n in range(6,21):
            print("Weird")
        if n in range(2,6):
            print("Not Weird")
    else:
        print("Weird")
