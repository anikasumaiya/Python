# write a program takes a sentence as input
# convert it to lower case
# replaces all spaces with underscores
# Prints the new string
sentence = input("write a sentence: ")
print(sentence.lower())
print(sentence.replace(" ","_"))

newSentence = sentence.lower().replace(" ","_") # chaining together
print(newSentence)