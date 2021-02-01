if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s)) #str.isalnum()-This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    print(any(c.isalpha() for c in s)) #str.isalpha()-This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    print(any(c.isdigit() for c in s)) #str.isdigit()-This method checks if all the characters of a string are digits (0-9).
    print(any(c.islower() for c in s)) #str.islower()-This method checks if all the characters of a string are lowercase characters (a-z).
    print(any(c.isupper() for c in s)) #str.isupper()-This method checks if all the characters of a string are uppercase characters (A-Z).
