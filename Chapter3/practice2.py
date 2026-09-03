# write a program that takes your favourite food name as input and prints :
# The middle 3 characters 
# The last 2 characters

favFood = "fuchka"
print(favFood[1 : 4]) # uck
print(favFood[3 : ]) # ka

# Solution
favFood1 = input("your favourite food: ")
mid = len(favFood1) // 2 # length / 2 = actual which  can be float so used // int 
str1 = favFood [mid-1:mid+2]
# mid-1 prints mid character
# mid+2 prints here mid is 3 so 3+2 = 5  end 5
print(str1)
print(mid)
print(favFood1[-2: ])
