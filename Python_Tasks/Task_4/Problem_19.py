## problem 19: collection.Counter()

if __name__ == '__main__':
    n = int(input())
    sizes = list(map(int, input().split()))
    stock = {}
    for size in sizes:
        if size in stock:
            stock[size] += 1
        else:
            stock[size] = 1
    customers = int(input())
    earnings = 0
    for _ in range(customers):
        size, price = map(int, input().split())
       
        if size in stock and stock[size] > 0:
            earnings += price
            stock[size] -= 1  

    print(earnings)
