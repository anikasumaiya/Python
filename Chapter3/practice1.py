# write a python program that takes users name as input and prints
# 1. The first character
# 2. The last character
# 3. The total name of the length
 
userName = input("Write down your name: ")
print("First character: " + userName[0])
print("Last character: " + userName[len(userName) - 1])
print("The total name of the length is " +  str(len(userName)))