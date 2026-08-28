# arithmetic operator
x = 2
y = 3

print("arithmetic operator result", x, ",", y)
print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) #  true division type float
print(x // y) #  floor division type int
print(x % y) # remainder
print(x ** 2) # square

# comparison operators compare values returns true / false
print("comparison operator result")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)

# logical operator combine conditions


print("AND operator result: ", x > y and x < y) # false
print("OR operator result: ", x > y or x < y) # true
print("NOT operator result: " , not(x > y)) # true

# assignment operator
a = 10
a = a + 6 # result 16
a += 6 # result 16
