import random

# Step 1: List of words
words = ["apple", "mango", "grape", "tiger", "chair"]

# Step 2: Choose random word
secret_word = random.choice(words)

# Step 3: Store guessed letters
guessed_letters = []

# Step 4: Limit wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Check guess
    if guess in secret_word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        wrong_guesses += 1
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print("\nYou lost!")
    print("The word was:", secret_word)