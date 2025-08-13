#with comparison sample
# This is the sample function to find the maximum of three numbers using if-elif-else
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # Check if num1 is greater than or equal to both num2 and num3
        return num1
    elif num2 >= num1 and num2 >= num3: # If not, check if num2 is greater than or equal to both num1 and num3
        return num2
    else:
        return num3  # If neither num1 nor num2 is the largest, then num3 must be the largest
print(max_num(358,150,220)) # Test the function with three numbers
print("\n")


