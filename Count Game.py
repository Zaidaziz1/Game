import random

# Set the range of numbers for the game
min_number = 1
max_number = 10

# Set the number of guesses allowed
max_guesses = 3

# Generate a random number
number = random.randint(min_number, max_number)

# Initialize the number of guesses
guesses = 0

# Loop until the user guesses the number or runs out of guesses
while guesses < max_guesses:
    # Get the user's guess
    guess = int(input("Guess a number between " + str(min_number) + " and " + str(max_number) + ": "))
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in " + str(guesses + 1) + " guesses.")
        break
    else:
        print("Sorry, that's not the number.")
        
    # Increment the number of guesses
    guesses += 1
    
    # Check if the user has run out of guesses
    if guesses == max_guesses:
        print("Sorry, you've run out of guesses. The number was " + str(number) + ".")

