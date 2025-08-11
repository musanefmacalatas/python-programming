# Example string
phrase = "WE JUST PRINT BY HARITH AITZY"

print("")
# Basic string functions
print(phrase)                         # Prints the string as is
print(phrase.lower())                 # Converts to lowercase
print(phrase.upper())                 # Converts to uppercase
print(phrase.isupper())               # Checks if string is in uppercase (True)
print(phrase.upper().islower())      # Converts then checks if it's lowercase (False)
print("")
# String length
print(len(phrase))                   # Number of characters
print("")
# Accessing specific characters
print(phrase[0])                     # First character (W)
print(phrase[8])                     # 7th character (T)
print("")      #LINE SPACE print("")
# Finding substrings
print(phrase.index("JUST"))        # Starting index of "JUST"
print(phrase.index("AITZY"))         # Starting index of "AITZY"
print("")
# Replacing text
print(phrase.replace("WE JUST PRINT BY HARITH AITZY", "LITTLE HARITH KIDS WEAR"))  # "LITTLE HARITH KIDS WEAR

# lower() and upper() convert case
#isupper() checks if all letters are uppercase
#len() counts characters / STARTS COUNT 1
#[] accesses specific letters using index / START FROM ZERO "0"
#index() finds where a word/letter starts / START FROM ZERO "0"
#replace() substitutes words
