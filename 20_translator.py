
# Function that takes a phrase (string) as input
def translate(phrase):
    # Create an empty string to store the translated result
    translation = ""

    # Loop through each letter in the given phrase
    for letter in phrase:
        # Check if the current letter is a vowel (uppercase or lowercase)
        if letter in "AEIOUaeiou":
            # If the vowel is uppercase, replace it with uppercase 'G'
            if letter.isupper():
                translation += "G"
            # If the vowel is lowercase, replace it with lowercase 'g'
            else:
                translation += "g"
        else:
            # If the letter is not a vowel, keep it as it is
            translation += letter

    # Return the fully translated string
    return translation

# Ask the user to input a phrase, then call the translate() function
# and print the translated version of the phrase
print(translate(input("Enter a phrase: ")))
print("\n")

# Function to censor an email address. It hides the part before '@' except the first and last character.
# Example: "nefmacmod@example.com" -> "n******d@example.com

def censor_email(email):

    # Split the email into two parts: before '@' and after '@'
    username, domain = email.split("@")

    # If username is longer than 2 characters, censor the middle part
    if len(username) > 2:
        censored_username = username[0] + "*" * (len(username) - 2) + username[-1]
    else:
        censored_username = username[0] + "*"

    # Combine censored username with the domain
    return censored_username + "@" + domain


# Example usage
email_input = input("Enter your email: ")
print("Censored email:", censor_email(email_input))

