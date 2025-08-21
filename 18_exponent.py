

# Define a function that raises a number to a power
def raise_to_power(base_num, pow_num):
    result = 1   #Start with result = 1 (multiplicative identity)
    for index in range(pow_num):  # Loop through the range of pow_num times
        result = result * base_num # Multiply result by base_num in each iteration
    return result # Return the final computed power
print(raise_to_power(3, 8))  # Example: Calculate 3 raised to the power of 8
print("\n")

# Exercise: Sum of powers of numbers from 1 to n

def sum_of_powers(n, power): #declaring function with 2 parameter
    total = 0 #initialized variable equal to zero
    for i in range(1, n+1): #loop through numbers 1 to n.
        total += i ** power  # i raised to 'power' and add to total
    return total

print(sum_of_powers(5, 5))  # 1^5 + 2^5 + 3^5 + 4^5 + 5^5 = 4425
print(sum_of_powers(4, 3))  # 1^3 + 2^3 + 3^3 + 4^3 = 100
