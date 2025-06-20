try:
    #Student Number
    for number in range(1, 6):
        number = int(input)
    marks = int(input("Please enter Marks of Student:"))

    #Check for the Grade
    if marks > 100 or marks < 0:
        print(f"Invalid")
        countdown_number -= 1 
    elif marks >= 75:
        print(f"You've got an A Grade")
    elif marks >= 65:
        print(f"You've got a B Grade")
    elif marks >= 55:
        print(f"You've got a C Grade")
    elif marks >= 45:
        print(f"You've got a S Grade")
    else :
        print(f"You've got a Fail Grade")
