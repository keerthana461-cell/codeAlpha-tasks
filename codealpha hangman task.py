#hangman game

import random

def play_hangman():
    # List of words to choose from
    words = ['python', 'programming', 'hangman', 'developer', 'algorithm']
    # Choose a random word
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        # Display the word with underscores for unguessed letters
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Check if user won
        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            return

        # Get player input
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    print(f"\nGame Over! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
