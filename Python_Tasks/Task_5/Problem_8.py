## PRoblem 8: set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    stamps = set()
    for _ in range(n):
        country = input().strip()
        stamps.add(country) 
    print(len(stamps))