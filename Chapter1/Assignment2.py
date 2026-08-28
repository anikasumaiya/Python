#Question: Take a diameter as input and calculate the area of a circle. (Area of circle = π * r * r, where r = radius of circle and π = 3.14)

diameter = int(input("Enter diameter of a circle: "))
radius = diameter / 2

area = 3.1416 * (radius**2)
print ("Given diameter of circle is: ", diameter)
print("Radius of the circle is: ", radius)
print("Area of the circle: ", area)
