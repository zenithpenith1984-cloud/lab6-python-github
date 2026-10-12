print("Thank you for using the calculator!\nHere are your options:")
print("1.Addition\n2.Subtraction\n3.Multipication\n4.Division\n5.Check Even/Odd\n6.Calculate Percentage\n7.Exit")
continueCalc = True

def even_or_odd(num1):
    answer = ""
    result = num1 % 2
    if result == 0:
        answer = f"The number {num1} is even"
    else:
        answer = f"The number {num1} is odd"
    return answer

def percentage(num1, num2):
    perc = (num1 / num2) * 100
    return f"{num1} is {perc} of {num2}"

while continueCalc:
    userOption = input("\nChoose the option number (1-7): ")
    if userOption == "1":
        num1 = float(input("Input a number: "))
        num2 = float(input("Input a second number: "))
        summation = num1 + num2
        print(summation)

    elif userOption == "2":
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a second number: "))
            difference = num1 - num2
            print(difference)

    elif userOption == "3":
        num1 = float(input("Input a number: "))
        num2 = float(input("Input a second number: "))
        product = num1 * num2
        print(product)

    elif userOption == "4":
        try:
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a second number: "))
            fraction = num1 / num2
            print(fraction)
        except ZeroDivisionError:
            result = float('inf') 
            print("Cannot divide by zero. Result set to infinity.")

    elif userOption == "5":
        num1 = int(input("Input a number: "))
        result = even_or_odd(num1)
        print(result)

    elif userOption == "6":
        num1 = float(input("Input a number: "))
        num2 = float(input("Input a second number: "))
        perc = percentage(num1,num2)
        print(perc)

    elif userOption == "7":
        continueCalc = False

    else:
        print("Input a valid number!")

print("Have a nice day!")
