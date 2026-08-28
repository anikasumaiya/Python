#  write a program that takes total bill amount and number of friends as input
# calculate how much amount each person will pay
# also print the  data type of each variable  used

totalBillAmount = (input("Enter total amount to pay: "))

Total = float(totalBillAmount)

numOfFriends = int(input("Enter number of friends: "))

eachPersonPay = Total / numOfFriends

print("totalBillAmount variable data type: ", type(totalBillAmount))

print("total variable data type: ", type(Total))

print("numOfFriends variable data type: ", type(numOfFriends))

print("Each person pay: ", eachPersonPay, type(eachPersonPay))