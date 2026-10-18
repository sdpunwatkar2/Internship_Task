## Problem 9: Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d={}
for i in range(n):
    word = input()
    d[word]=d.get(word,0)+1
    
print(len(d))
print(*d.values())
