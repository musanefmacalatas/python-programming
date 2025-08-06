
# This is a simple Python script that uses variables and basic data types

# String (text)
character_name = "TWEETY"
# Integer (whole number)
character_age = 20
# Boolean (True/False)
is_female = False

character_name = "TWEETY"
character_age = "20"
print ("The story of my life is when i met " + character_name + ".")
print ("She was "+ character_age +" years old at that time.")
print("" + character_name + " is so sexy that time like wow")
print("Is this person female? " + str(is_female))
# str() is used to convert non-string data to a string so you can include it in print()

number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))
if number1 > number2:
    print("The first number is greater than the second number.")
elif number1 < number2:
    print("The first number is less than the second number.")

print("The sum of the numbers is " + str(number1 + number2))
