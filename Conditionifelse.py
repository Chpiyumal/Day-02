#Ask to enter an integer
#Use try exception to handle potential valu mismatches

try:
    number = int(input("Please enter a number:"))

    #Check if the number is positive, negative or zero
    if number > 0:
        print(f"The number {number} is positive")
    elif number < 0:
        print(f"The number {number} is negative")
    else: #For zero
        print(f"The number is {number}")
except :
    print("Invalid entry")
