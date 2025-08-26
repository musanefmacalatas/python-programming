# Check if the file is readable
employee_file = open("employees.txt", "r")  # Open the file "employees.txt" in read mode ("r")
print(employee_file.readable())       # Check if the file is readable → returns True or False
employee_file.close()                # Close the file (always close after using)
print("\n")

# Read the whole content of the file
employee_file = open("employees.txt", "r")   # Open the file again in read mode
print(employee_file.read())              # Read the entire file content as one big string
employee_file.close()                    # Close the file
print("\n")

# Read line by line using readline()
employee_file = open("employees.txt", "r")     # Open the file
print(employee_file.readline())           # Read the first line of the file
print(employee_file.readline())            # Read the second line
print(employee_file.readline())            # Read the third line
print(employee_file.readline())             # Read the fourth line (if exists)
employee_file.close()
print("\n")

# Read all lines at once as a list
employee_file = open("employees.txt", "r")    # Open the file
print(employee_file.readlines()[0])           # Read all lines into a list, then print the first line (index 0)
employee_file.close()
print("\n")

# Loop through each line of the file
employee_file = open("employees.txt", "r")   # Open the file
for employee in employee_file.readlines():   # Loop through the list of lines
    print(employee)                          # Print each line from the file
employee_file.close()
print("\n")

# -------------------------------------------------------------------------------------------------------------------------------------
# using (WITH) product inventory
with open("products.txt", "r") as file: # Open the file/WITH (context manager) - meaning it will automatically close the file after the block finishes
    print("Product Inventory:\n")  # print with newline break
    for line in file:              #Loops through each line in the file.
        product, price = line.strip().split(",")  # Split product and price
        print(f"- {product} costs ₱{price}")      # Uses f-string formatting to display each product with its price

