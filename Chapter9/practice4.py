# create a class student that takes 3 marks and has a method average
class Student:
    def __init__(self, name, listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def average(self):
        sum = 0
        for eachValue in self.listOfMarks:
            sum = sum+eachValue

        avg = sum/3
        print("Average is :", avg)

student1 = Student("Adi", [99,90,100])
student1.average()
        
        
        
       