# Expense Tracker Project

expenses = [] # list of all expenses in form of dictionary
print("Welcome to Expence Tracker : Spend less as you can")


while True:
    print("============= Menu ============")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. View total expense")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))
    # ADD EXPENSES
    if(choice == 1):
        
        category = input(" Enter category of your expense ( e.g. travel,food,makeup,clothes) : ")
        description = input("Give details of your category : ")
        amount = float(input("How much did you spend? "))

        expense = {
            
            "category" : category,
            "description" : description,
            "amount" :  amount
        }

        expenses.append(expense)
        print(" \n DONE!!! Expenses added successfully")

    # VIEW ALL EXPENSES 
    elif(choice == 2) :
        if(len(expenses) == 0) :
            print("First Do  some expenses.")
        else :
            print("Here all of your expenses: ")
            count = 1
            for each_expenses in expenses:
                # print(f"expenseNumber{count} -> {each_expenses['date']}, {each_expenses['category']}, {each_expenses['description']},{each_expenses['amount']} ")
                print(f"expenseNumber{count} ->  {each_expenses['category']}, {each_expenses['description']},{each_expenses['amount']} ")

                count = count + 1
    
    # VIEW TOTAL EXPENSE
    elif(choice == 3) :
        total = 0
        for each_expenses in expenses :
            total = total + each_expenses["amount"]

        print("\n  Total expenditure:  " , total)

    # EXIT 
    elif(choice == 4) :
        print("Thanks for using our system.")
        break

    else:
        print("Invalid!!!.Please try again later.")



