def split_and_join(line):
    # write your code here
    a=line.split(' ')       #In Python, we can use the function split() to split a string and join() to join a string.
    line = '-'.join(a)
      
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
