##problem 15: word ORder
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    words = []
    d = {}
for i in range(n):
    word = input()
    d[word]=d.get(word,0)+1
    
print(len(d))
print(*d.values())
