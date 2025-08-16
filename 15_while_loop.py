
i = 1 # Initialize the counter variable
while i <= 20: # Loop while i is less than or equal to 20
    print(i)  # Print the current value of i
    i += 1 # Increase i by 1 for the next loop iteration
print("DONE WITH LOOP")  # This line runs after the loop finishes


# mock exercise using ATM/PIN verification
correct_pin = "1234"  # declaration of correct pin

# If wrong PIN entered, it will repeat the question until it's correct
pin = ""
while pin != correct_pin:
    pin = input("Please enter your PIN: ")

    if pin != correct_pin:
        print("Wrong PIN. Please try again.\n")

print("Access granted")
print("\n")
# mock exercise using water bottles
water_bottles = 10
while water_bottles > 0:  #while this condition is TRUE it will continue to execute the flow inside
    water = input("Do you want to buy a bottle? (yes/no): ")

    if water.lower() == "yes":
        water_bottles -= 1
        print(f"Bottles left: {water_bottles}")
    elif water.lower() == "no":
        print("Okay, maybe next time!")
        break
    else:
        print("Please answer yes or no.")

if water_bottles == 0:
    print("Out of stock!")
print("\n")
# mock exercise using dictionary with products and number of stocks
inventory = {
    "banana": 4,
    "apple": 3
}

while inventory:
    # It will display to the customer the products and number of stocks available
    print("\nCurrent Inventory:")
    for product, stock in inventory.items():
        print(f"{product}: {stock} left")

    # Ask user AFTER showing inventory
    item = input("\nEnter product to buy (or 'exit'): ") #enter products

    if item == "exit":
        break                #it will end program for exit selection
    if item in inventory:
        inventory[item] -= 1   #it will deduct/minus (-1) the number of stocks of the selected item
        print(f"Sold 1 {item}!") #display the item purchased , also it will display the updated inventory of products

        if inventory[item] == 0:        #if the item/product is equal to zero or no more stocks available
            del inventory[item]           # will delete automically in the dictionary or inventory
            print(f"{item} is now out of stock!")
    else:
        print("Sorry, we don't have that item.")

print("\nAll done. Thank you for shopping!")



