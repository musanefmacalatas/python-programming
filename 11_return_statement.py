# Function to calculate the cube of a given number
def cube (number):
    return number**6  # Raise the number to the power of 6
result = cube(5)  # when you want to store the result of cube(5) in a variable
print(result + 30) # it will print the result , or you can add another operations

print("\n")

# THIS ONE IS WITH USER INPUT
def cube(number):
    return number ** 6  # Raise the number to the power of 6

# Ask the user to enter a number
user_number = float(input("Enter a number: "))

# Store the result of cube(user_number) in a variable
result = cube(user_number)

# Print the result plus 30
print(f"The cube of {user_number} is {result + 30} ") # I used fstrings so it will make it simple and minimize the code.

print("\n")

# Function to get the cube of a number
def cube(number):
    return number ** 3

# Function to add 10 to the result
def add_ten(number):
    return number + 10

# Function to divide the result by 2
def divide_by_two(number):
    return number / 2

# User input as float
num = float(input("Enter a number: "))

# Step-by-step computation
cube_result = cube(num)              # Cube first
added_result = add_ten(cube_result)  # Add 10
final_result = divide_by_two(added_result)  # Divide by 2
print(f"Cube of {num} is {cube_result}")
print(f"After adding 10: {added_result}")
print(f"Final result after dividing by 2: {final_result}")
print("\n")

#1 - mock exercise "AREA AND PERIMETER TRANSFORMER"

def rectangle_area(width, length):
    return width * length
def rectangle_perimeter(width, length):
    return 2 * (width + length)
def transform_value(value):
    return value * 3
user_length = float(input("Enter length (cm): "))
user_width = float(input("Enter width (cm): "))

area = rectangle_area(user_length, user_width)
transformed_area = transform_value(area)
perimeter = rectangle_perimeter(user_width, user_length)
transformed_perimeter = transform_value(perimeter)

print(f"The area of the rectangle is {area} cm²")
print(f"The transformed area is {transformed_area} cm²")
print(f"The perimeter of the rectangle is {perimeter} cm")
print(f"The transformed perimeter is {transformed_perimeter} cm")
print("\n")

#2 - mock exercise "RECTANGLE TRANSFORMER CHALLENGE"

def rectangle_area(width, length):
    return width * length

def rectangle_perimeter(width, length):
    return 2 * (width + length)

def transform_value(value):
    # Trick: multiply by 3 if even, divide by 2 if odd / without using if else
    # True = 1, False = 0, so we can use math
    return (value * 3) * (value % 2 == 0) + (value / 2) * (value % 2 != 0)

# User inputs
user_length = float(input("Enter length (cm): "))
user_width = float(input("Enter width (cm): "))

# Calculations
area = rectangle_area(user_width, user_length)
transformed_area = transform_value(area)

perimeter = rectangle_perimeter(user_width, user_length)
transformed_perimeter = transform_value(perimeter)

# Output
print(f"The original area is: {area} cm²")
print(f"The transformed area is: {transformed_area} cm²")
print(f"The original perimeter is: {perimeter} cm")
print(f"The transformed perimeter is: {transformed_perimeter} cm")