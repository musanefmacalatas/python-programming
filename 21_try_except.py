
try:
    number = int(input("Enter a number: ")) # Ask the user for input, try to convert to integer
    result = 10/0   # Perform a division (division by zero)
    print(number)     # Print the number entered by the user
except ZeroDivisionError as err:   # If a division by zero happens, catch the error
    print(err)       # Print the error message from Python
except ValueError:    # If user enters something not convertible to int
    print("Invalid input")  # Show custom error message

print("\n")

# try/except CHEAT SHEET
try:
    # Code that might cause an error
    number = int(input("Enter a number: "))     # may cause ValueError
    result = 10 / number                        # may cause ZeroDivisionError

except ValueError:
    print("Invalid input. Please enter a number.") # Runs if the input cannot be converted to int

except ZeroDivisionError as err:
    print("Error:", err)  # "division by zero"   # Runs if division by zero happens

except Exception as err:
    print("Unexpected error occurred:", err) # Catches any other unexpected error

else:
    print("Success! The result is:", result)  # Runs only if no exception was raised

finally:
    print("Program finished.") # Runs no matter what (error or no error)
