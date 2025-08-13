#sample boolean variables
is_male = False # user is male
is_tall = True
# Decision-making using if-elif-else
if is_male and is_tall:   # Condition: both is_male and is_tall are True
    print("Male and tall ")
elif is_male and not (is_tall): # Condition: is_male is True but is_tall is False
    print("Male or tall")
elif not (is_male) and is_tall: # Condition: is_male is False but is_tall is True
    print("Not male but tall")
else:                           # Condition: none of the above (female and short in this logic)
    print("You're a female that is why you are short")

print("\n")
#mock exercise
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

if age >= 18 and height >= 150:  # Check if the person is old enough (18+) AND tall enough (150cm+
    print("✅ You are allowed to ride. Enjoy!")
elif age >= 18 and height < 150: # If the person is old enough (18+) BUT shorter than 150cm
    print("⚠️ You are old enough, but you are too short for the ride.")
elif age < 18 and height >= 150: # If the person is younger than 18 BUT tall enough (150cm+)
    print("⚠️ You are tall enough, but you must be 18 or older to ride.")
else:              # If none of the above conditions are true → too young AND too short
    print("❌ Sorry, you are too young and too short to ride.")
print("\n")

#mock exercise
# This exercise is example of coffee shop. The price is 120 and will ask the customer if he/she's a member or he/she bring tumbler to qualify on discounts.
base_price = 120          #original price
member_discount = 20     #discount if member
tumbler_discount = 10     #discount if bring tumbler

member_info = input("Are you a member?(YES/NO): ").lower()
tumbler_info = input("You have a tumbler?(YES/NO) : ").lower()

if member_info == "yes" and tumbler_info == "yes":
    final_price = base_price - member_discount - tumbler_discount     #customer will have both discounts
elif member_info == "yes" and tumbler_info == "no":
    final_price = base_price - member_discount           #customer will have member discount
elif member_info == "no" and tumbler_info == "yes":
    final_price = base_price - tumbler_discount    #customer will have tumbler discount
else:
    final_price = base_price   #customer will have NO DISCOUNT
print("Your final coffee price is:", final_price)




