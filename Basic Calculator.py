

num1 = float(input("Enter first number: "))  # Ask the user to enter the first number and convert it to float
operator = input("Enter operator (+, -, *, /): ") # Ask the user to enter an operator (+, -, *, or /)
num2 = float(input("Enter second number: ")) # Ask the user to enter the second number and convert it to float

# Check which operator the user entered and perform the corresponding operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Check if the second number is not zero before dividing
    if num2 != 0 :
        result = num1 / num2
    else:
        result = "Cannot divide by zero!" # Error message for division by zero
else:
    result = "Invalid operator" # Error message for invalid operator

# Display the result
print("The result is:", result)
