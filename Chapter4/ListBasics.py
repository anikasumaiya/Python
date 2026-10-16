# List in python
# List is a built in data type it is mutable and it can store multiple values of different data tyoe

fruit= ["apple", "banana", "guava", "orange"]
print(len(fruit))
print(fruit[0])
# print(fruit[9])
print(fruit[3])

# List is very useful because it can store in a single variable multiple values of different data type
value= ["apple", 4, 4.0, False]
print(len(value))
print(value[2])
print(value[3])
print(value[0])
# List are mutable
value[0] = "pineapple"
print(value[0])

# max(list)=> returns largest value of list
# min(list)=> returns smallest value of list
value= [99, 98.7, 96, 90]
print(max(value))
print(min(value))

# list supports also slicing
print(value[1:9])
print(value[0:9])
print(value[-1:-6])

