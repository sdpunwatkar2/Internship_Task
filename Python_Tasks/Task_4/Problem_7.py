## problem 7:String Split and Join

def split_and_join(line):
    # write your code 
    a = line.split()
    a = "-".join(a)
    return a
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
