def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string): #The startswith() method returns True if the string starts with the specified value, otherwise False.
            count +=1
    return count        
        

if __name__ == '__main__':
