# Dictionary basics
# Dictonaries are unordered, mutable and don't allows duplicate keys.
# for example "name" "city" key and "ANIKA SUMAIYA" "DHAKA" are value.
# we can access values through keys.

student = {
    "name": "ANIKA SUMAIYA",
    "city": "DHAKA",
    "age": 22,
    "rollNumber": 1
}
    
print(type(student))
print(student["age"])
print(student)

(student["city"]) = "CHATTOGRAM"
(student["favColour"]) = "HOT PINK"

print(student)

print(student.keys())
(student.pop("age"))
print(student)
print(student.items())