
#Loop through string characters
word = "PYTHON"
for letter in word:
    print("Letter:", letter) #will print each letter of variable string
print("\n")

#Loop with conditional (even numbers only)
for i in range(1, 11): #range starts at 1 up to 10 only
    if i % 2 == 0:   #check if divisible by 2
        print("Even:", i)
print("\n")

#Nested loop → loop inside loop.
for x in range(1, 4): #Outer loop: x = 1 up to 3
    for y in range(1, 3): #Inner loop: y = 1 up to 2
        print(f"x={x}, y={y}") #the value of variable will converted to string - using fstring
print("\n")

# Generate multiplication table (1 to 5)
for x in range(1, 6):  # Outer loop: multiplier
    for y in range(1, 6):  # Inner loop: multiplicand
        print(f"{x} x {y} = {x*y}")  # Actual multiplication result
    print("--- End of Table for", x, "---")  # Separator

print("\n")

# List of t-shirt orders (number of shirts per customer)
orders = [3, 1, 5, 2, 4]

# Variable to track total shirts
total_shirts = 0


for order in orders:   # Loop through each order
    print(f"Processing order: {order} shirts")
    total_shirts += order   # add each order to the total

# Final result
print(f"\nTotal shirts to print: {total_shirts}")





