bankBalance = 5000
accountNumber = 4859420059932

print("Welcome to Nation's bank")
print("Press 1 to withdraw money\nPress 2 to deposit money\nPress 3 to print account details\nPress 4 to stop using the service")
action1= int(input("Enter your input: "))

if action1 == 1:
    amount1 = int(input("Enter the amount you want to withdraw: "))

    if amount1 <= bankBalance:

        class Bank1:
            def withdraw(self):
                result1 = bankBalance - amount1
                print("Withdraw Successful.\nYour updated bank balance for your account number", accountNumber, "is", result1)

            bankBalance = bankBalance - amount1

        obj = Bank1()
        obj.withdraw()

    else:
        print("Insufficient funds")

elif action1 == 2:
    amount2= int(input("Enter the amount you want to deposit: "))

    class Bank2:
        def deposit(self):
            result2= bankBalance + amount2
            print("Deposit successful.\nYour updated bank balance for your account number", accountNumber, "is", result2)

        bankBalance = bankBalance + amount2

    obj = Bank2()
    obj.deposit()

elif action1 == 3:
    print("You current balance for account number", accountNumber, "is", bankBalance)

elif action1 == 4:
    print("Thank you for banking with Nation's bank")

else:
    print("Invalid input")
