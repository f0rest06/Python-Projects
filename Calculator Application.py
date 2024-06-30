while True:

    print("Welcome To Tushar's Calculator")
    print("Press 1 to Add\nPress 2 to Subtract\nPress 3 to Multiply\nPress 4 to Divide\nPress 5 to do Modulus\nPress 6 to Exit")

    calculate1 = int(input("Enter the number: "))

    if calculate1 == 1:
        sumCalc = int(input("Please enter number 1: "))
        sumCalc2 = int(input("Please enter number 2: "))
        def sum(nm1, nm2):
            result = nm1 + nm2
            print(result)
        sum(sumCalc, sumCalc2)

    elif calculate1 == 2:
        sumCalc = int(input("Please enter number 1: "))
        sumCalc2 = int(input("Please enter number 2: "))
        def subtract(nm1, nm2):
            result = nm1 - nm2
            print(result)
        subtract(sumCalc, sumCalc2)

    elif calculate1 == 3:
        sumCalc = int(input("Please enter number 1: "))
        sumCalc2 = int(input("Please enter number 2: "))
        def multi(nm1, nm2):
            result = nm1 * nm2
            print(result)
        multi(sumCalc, sumCalc2)

    elif calculate1 == 4:
        sumCalc = int(input("Please enter number 1: "))
        sumCalc2 = int(input("Please enter number 2: "))
        def div(nm1, nm2):
            if nm2 == 0:
                print("Cannot divide by 0")
            else:
                result = nm1 / nm2
                print(result)
        div(sumCalc, sumCalc2)

    elif calculate1 == 5:
        sumCalc = int(input("Please enter number 1: "))
        sumCalc2 = int(input("Please enter number 2: "))
        def mod(nm1, nm2):
            result = nm1 % nm2
            print(result)
        mod(sumCalc, sumCalc2)

    elif calculate1 == 6:
        print("Thank your for using Tushar's calculator")
        break

    else:
        print("Invalid input")

    calculate2=input("Do you wish to continue? (Y/N) ")
    if calculate2.lower() != "y":
        print("Thank your for using Tushar's calculator")
        break
