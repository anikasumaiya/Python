
#how to take input from user
#input() function always return string type value. If we want to take numeric type value from user then we have to convert it into numeric type using int() or float() function.

user_name = input("What's your name? ")
print("Hello, " + user_name + "!")

age = int(input("Enter your age also: "))
print("see your age now: ",age)