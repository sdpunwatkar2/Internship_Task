## PROBLEM 10: DESIGNER DOOR MAT

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Door Mat Design
# Input: N (rows), M (columns) where M = 3*N

N, M = map(int, input().split())

# Top half
for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

# Middle line
print("WELCOME".center(M, "-"))

# Bottom half
for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))
