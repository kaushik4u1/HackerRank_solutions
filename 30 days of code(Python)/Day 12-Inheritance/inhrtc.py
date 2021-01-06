class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber,scores):      
    #   Parameters:
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores  = scores
            
    # Write your constructor here
    def calculate(self):
        sum = 0
        for i in range(len(self.scores)):
            sum = sum + self.scores[i]
        Avgscore = sum//len(self.scores)
        if 90 <= Avgscore <= 100:
            return "O"
        elif 80 <= Avgscore < 90:
            return "E" 
        elif 70 <= Avgscore < 80:   
            return "A"
        elif 55 <= Avgscore < 70:
            return "P"
        elif 40 <= Avgscore < 55:
            return "D"
        elif Avgscore < 40:
            return "T"
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())