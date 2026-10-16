##problem 13: symmetric difference
if __name__ == '__main__':
    # Read first set
    n1 = int(input())
    arr1 = set(map(int, input().split()))
    
    # Read second set
    n2 = int(input())
    arr2 = set(map(int, input().split()))
    
    # Symmetric difference: elements in arr1 or arr2 but not both
    result = sorted(arr1 ^ arr2)
    
    # Print each element on a new line
    for num in result:
        print(num)
