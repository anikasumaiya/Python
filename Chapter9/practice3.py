class Student:
    schoolName = "MB Grammar School"

    def __init__(self):
        print("I am init method whenever object created I will come automatically .")

    def __init__(self, name, course):
        self.name = name
        self.course = course
        
obj1 = Student("mischmichi", "Bsc")
print("student1 name - ", obj1.name)


#     # Python uses double underscores (__) before and after init
#     def __init__(self): 
#         print("I am init method whenever object created I will come .")
#   init constructor
# inside class related functions -called methods
