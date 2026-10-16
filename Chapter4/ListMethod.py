# methods in lists

marks= [100, 99, 90, 80]

print("Real List: " ,marks)

marks.reverse()
print("After reverse: ", marks)

marks.append(89)
print(marks)

marks.sort()
print("after sorting list: ", marks)
print(marks)

# list are mutable 
marks.pop(2)
print(marks)

marks.remove(99)
print(marks)

marks.insert(1,0)
print(marks)

