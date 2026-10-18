## Problem 19: Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        result = ""
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)