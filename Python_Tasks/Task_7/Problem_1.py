## Problem 1: Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

print(len(english.symmetric_difference(french)))
