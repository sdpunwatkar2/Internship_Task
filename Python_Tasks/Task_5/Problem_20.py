## problem 20: p+Piling up!

# Enter your code here. Read input from STDIN. Print output to STDOUT

def piling_up(cubes):
    left, right = 0, len(cubes) - 1
    last = float('inf')
    while left <= right:
        if cubes[left] >= cubes[right]:
            chosen = cubes[left]
            left += 1
        else:
            chosen = cubes[right]
            right -= 1
        if chosen > last:
            return "No"
        last = chosen

    return "Yes"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(piling_up(cubes))

