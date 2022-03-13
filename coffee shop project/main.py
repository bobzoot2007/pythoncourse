import sys
import choiceSys as choice

print("welcome to the coffee shop")

name = input("Enter your name please: ")  # user input

print("welcome back " + name + " to the coffee shop")
    
amount = int(input("Enter your amount of orders (maximum orders 3): ")) # user input

if amount == 1:
    choice.choiceSys()
    print("thanks for your order")
elif amount == 2:
    choice.choiceSys()
    print("you have " + str(amount - 1) + " orders left")
    choice.choiceSys()
    print("thanks for your orders")
elif amount == 3:
    choice.choiceSys()
    print("you have " + str(amount - 1) + " orders left")
    choice.choiceSys()
    print("you have " + str(amount - 2) + " orders left")
    choice.choiceSys()  # call the function
    print("thanks for your orders")
else:
    print("Invalid amount")
    sys.exit()

