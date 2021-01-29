def swap_case(s):
    return s.swapcase() #The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)