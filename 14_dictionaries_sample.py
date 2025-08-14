from calendar import monthcalendar
# Dictionary mapping month numbers to month names
monthcalendar = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
print(monthcalendar.get(11)) # The .get() method returns the value for the given key .If the key doesn't exist, it returns None by default
print("\n")

# mock exercise , store inventory with price
# Dictionary containing product names as keys and their prices as values
inventory = {
    "Shampoo" :85,
    "Colgate" :30,
    "Soap"    :15,
    "Perfume" :250,
}

product_info = input("Enter product name: ") # Ask the user to input the product name they want to check
if product_info in inventory: # Check if the entered product exists in the dictionary (using 'in' style)
    print(f"{product_info} is available: ₱{inventory[product_info]:.2f}") # If the product exists, display its price with 2 decimal places
else:
    print(f"Product not found.") # If the product does not exist, show a 'not found' message

print("\n")
# Dictionary containing order IDs and their statuses
orders = {
    "ORD001" : "Shipped",
    "ORD002" : "Pending",
    "ORD003" : None,

}

order_info = input("Enter Order ID: ")
order = orders.get(order_info)

if order_info in orders:
    if order is not None:
        # Order exists and has a status
        print(f"Order ID: {order_info} - Status: {order}")
    else:
        # Order exists but has no status
        print(f"Order ID: {order_info} exists but has no status yet.")
else:
    # Order not found
    print("Order not found.")
