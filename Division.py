#handle valu errors and zero deniminator
try:
    #Numerator
    numerator_input = input("Input the numerator:")
    numerator = float(numerator_input)
    #Denominator
    denominater_input = input("Input the denominator:")
    denominator = float(denominater_input)

    result = numerator / denominator

    #Result Print
    print(f"You entered: Numerator = {numerator}, Denominator = {denominator}")
    print(f"Result is: {result}")
except ValueError:
    print("Invalid Input, Please put valid numbers")
except ZeroDivisionError:
    print(f"Can't divide by zero!!")
except Exception as e:
    print(f"An unexpected error occured: {e}")
