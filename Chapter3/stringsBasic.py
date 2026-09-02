x = 'I am a girl'
y = "If I don't take care of myself, "
z = '''Nobody is going to take care of yours.'''

print(x)
print(y)
print(z)

# string concatenation
print("mental peace" + "physical peace")

# string length
print(len("umbrella"))
p = "Queen"
print(len(p))


w = "I am a queen"
print("who are you? " + "I am a queen " + "string length is " + str(len(w)))

# indexing
# each character in a string has a position(index)

# index: 0 1 2 3 4 5 6 7 8 9 10 11
# char:  A N I K A S U M A I  Y  A
# summary- index starts from 0
vegetable ="TOMATO"

print(vegetable[0]) # prints T
print ("index number is for 5 : " + vegetable[5])

# string is a sequence of character and it provides position of character by index
# strings are immutable
print(vegetable)
print("now index 5: "+ vegetable[5])

# vegetable[5] = 's'
# print(vegetable[5]) ERROR why? 
# summarry - immutable (strings cannot change directly)



