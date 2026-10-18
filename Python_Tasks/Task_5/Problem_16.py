## Problem 16: Collections.Counter()

from collections import Counter

if __name__ == '__main__':
    n = int(input())
    sizes = list(map(int, input().split()))
    stock = Counter(sizes)
    customers = int(input())
    earnings = 0
    for _ in range(customers):
        size, price = map(int, input().split())
        if stock[size] > 0:
            earnings += price
            stock[size] -= 1
    print(earnings)