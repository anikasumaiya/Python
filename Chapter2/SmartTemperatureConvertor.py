# take input in celcius and print its equivalent in fahreinheit and kelvin
# (use explicit type conversion and arithmetic operators)

celcius = int(input("Enter temperature in celcius: "))

fahreinheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

print("equivalent fahreinheit: " ,fahreinheit )
print("equivalent kelvin  : " ,kelvin  )
