# create a class Laptop  attributes: brand,Ram,price .
# Create 2 objects with two different values
class Laptop:
    brand =""
    Ram = ""
    price = ""

obj1 = Laptop()
obj1.brand = "asus"
obj1.price = "200000"
obj1.Ram = "25GB"

obj2 = Laptop()
obj2.brand = "mac"
obj2.price = "300000"
obj2.Ram = "20GB"

print("object 1 laptop brand: ",obj1.brand)
print("object 2 laptop brand: ",obj2.brand)