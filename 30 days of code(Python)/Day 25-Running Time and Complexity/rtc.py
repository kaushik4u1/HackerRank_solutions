# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            return False
    else:
        return True
n = int(input())
for i in range(n):
    checkNumber = int(input())
    if isPrime(checkNumber):
        print("Prime")  
    else:
        print("Not prime")          