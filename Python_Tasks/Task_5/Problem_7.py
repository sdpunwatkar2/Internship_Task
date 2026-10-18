## Problem 7: symmetric difference

if __name__ == '__main__':
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(map(int, input().split()))
    result = sorted(set(arr1) ^ set(arr2))
    for num in result:
        print(num)
