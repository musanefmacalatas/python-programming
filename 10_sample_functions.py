# Define a function named 'animal' that takes two parameters: 'name' and 'size'
def animal (name, size):
    print("Hello " + name + " you're" + size)  # The '+' operator here is used to concatenate (join) strings

animal("ZEBRA" , " short") # Call the 'animal' function and pass "ZEBRA" as the 'name' and " short" as the 'size'
animal("GIRAFFE", " tall") # Call the 'animal' function and pass "GIRAFFE" as the 'name' and " tall" as the 'size'
print("\n")
def animal(name, size):
    print(f"Hello {name} you're {size}") # Here, i used fstrings so i can minimize the spaces and make short code

animal("ZEBRA", "short")
animal("GIRAFFE", "tall")
print("\n")
# Here is my example of function using fstrings instead of concatenation "+" .
def travel_info (name,age,country,transport,budget):
    print(f"Hello, my name is {name}. I am {age} years old. I will travel to {country} using my {transport} and my budget is around {budget} pesos")

travel_info("MUSANEF", "32", "DUBAI","PASSPORT","500,000")
