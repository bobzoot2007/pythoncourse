import sys

def choiceSys():
    
    print("Please choose your drink of choice: ")
    print("1. espreseo - $2.50")
    print("2. latte - $3.50")
    print("3. cappeccino - $4.50")
    print("4. tea - $1.50")
    print("5. cocoa - $6.50")
    print("6. exit")

    # str: string(words)
    # int: integer(numbers)
    choice = int(input("Enter your drink choice: "))  # user input
    price = 0.0
    change = 0.0
    given_money = float(input("Insert money: "))

    if choice == 1:
        print("You chose espresso")
        price = 2.50
        print("Your total is: $" + str(price))
        change = given_money - price
        print("Your change is: $" + str(change))
    elif choice == 2:
        print("You chose latte")
        price = 3.50
        print("Your total is: $" + str(price))
        change = given_money - price
        print("Your change is: $" + str(change))
    elif choice == 3:
        print("You chose cappuccino")
        price = 4.50
        print("Your total is: $" + str(price))
        change = given_money - price
        print("Your change is: $" + str(change))
    elif choice == 4:
        print("You chose tea")
        price = 1.50
        print("Your total is: $" + str(price))
        change = given_money - price
        print("Your change is: $" + str(change))
    elif choice == 5:
        print("You chose cocoa")
        price = 6.50
        print("Your total is: $" + str(price))
        change = given_money - price
        print("Your change is: $" + str(change))
    elif choice == 6:
        print("You chose exit")
        print("goodbye")
        sys.exit()
    else:
        print("Invalid choice")
        sys.exit()
