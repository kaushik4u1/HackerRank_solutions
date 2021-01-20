# Enter your code here. Read input from STDIN. Print output to STDOUT
First = list(map(int,input().split()))
Second= list(map(int,input().split()))

Day1 = First[0]
Day2 = Second[0]

Month1 = First[1]
Month2 = Second[1]

Year1 =First[2]
Year2 =Second[2]

fine = 0

if(Year1 == Year2):
    if(Month1 == Month2):
        if(Day1 > Day2):
            fine = (Day1 - Day2)*15
    elif(Month1 > Month2): 
        fine = (Month1 - Month2)*500  
elif(Year1 > Year2):   
    fine = 10000
    
print(fine)   
            
