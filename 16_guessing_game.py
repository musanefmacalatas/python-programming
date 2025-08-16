#guessing game using WHILE, IF-ELSE

correct_word = "SPIDERMAN" # The correct word to guess
guess = ""                  # Stores the user's guess input
guess_count = 0           # Counter to track the number of guesses made
guess_limit = 3           # Maximum number of allowed guesses
out_of_guess = False      # Flag to indicate if the user has no more guesses

while guess != correct_word and not (out_of_guess): # Loop until the correct word is guessed or the user runs out of guesses
    if guess_count < guess_limit:  # Check if guesses are still available
        guess = input("Enter your guess: ") # Ask the user for a guess

        if guess != correct_word: # Check if the guess is incorrect
            attempts_left = guess_limit - (guess_count + 1)  # Calculate remaining attempts
            if attempts_left > 0:   # Display feedback only if there are attempts left
             print("Sorry, you didn't guess correctly. Try again.")
             print(f"{attempts_left} attempt(s) left.")
        guess_count += 1   # Increase the guess counter after each guess
    else:
        out_of_guess = True  # Set flag to True if user has reached the maximum number of guesses

if out_of_guess:
    print("Sorry, you are out of guess.")  # After the loop ends, check if the user won or lost
else:
    print("Congratulations!, you guessed the correct word.") # User wins if guessed correctly