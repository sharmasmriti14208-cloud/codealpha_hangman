"""
Hangman Game
A simple, interactive, beginner-friendly Hangman game in Python.
"""

import random

# Predefined list of 5 words
WORDS = ["python", "laptop", "bottle", "guitar", "window"]

# Visual ASCII stages for Hangman (0 to 6 incorrect guesses)
HANGMAN_PICS = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========""",
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========""",
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========""",
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========""",
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========""",
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========""",
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ========="""
]


def display_word(secret_word, guessed_letters):
    """
    Returns the secret word with correctly guessed letters revealed
    and unguessed letters represented as underscores ('_').
    """
    revealed_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            revealed_letters.append(letter)
        else:
            revealed_letters.append("_")
    return " ".join(revealed_letters)


def play_hangman():
    """
    Executes a single round of the Hangman game.
    """
    print("=" * 45)
    print("         WELCOME TO HANGMAN GAME!            ")
    print("=" * 45)
    print("Instructions:")
    print("- Guess the secret word one letter at a time.")
    print("- You have a maximum of 6 incorrect attempts.")
    print("=" * 45)

    # 1. Randomly select a word from the predefined list
    secret_word = random.choice(WORDS)

    # 2. Initialize tracking variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    # 3. Main game loop using a while loop
    while incorrect_guesses < max_incorrect:
        # Display current hangman visual
        print(HANGMAN_PICS[incorrect_guesses])

        # Display current word status
        current_word_display = display_word(secret_word, guessed_letters)
        print(f"Word: {current_word_display}")

        # Display guessed letters and remaining attempts
        if len(guessed_letters) > 0:
            print(f"Guessed letters: {', '.join(guessed_letters)}")
        else:
            print("Guessed letters: None")

        remaining_attempts = max_incorrect - incorrect_guesses
        print(f"Remaining incorrect attempts: {remaining_attempts}")

        # Check for a win: all letters guessed
        if "_" not in current_word_display:
            print("\n" + "=" * 45)
            print(f"🎉 CONGRATULATIONS! You won! The word was '{secret_word}'.")
            print("=" * 45)
            return

        # 4. Get player input
        guess = input("\nEnter your guess (single letter): ").strip().lower()

        # 5. Input validation using if-else conditions
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️  Invalid input! Please enter exactly one alphabetic character.")
            continue

        if guess in guessed_letters:
            print(f"\n⚠️  You already guessed '{guess}'. Please try another letter.")
            continue

        # Add the valid guess to guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"\n✅ Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"\n❌ Oops! '{guess}' is NOT in the word.")

    # 6. Check for loss: maximum incorrect attempts reached
    if incorrect_guesses == max_incorrect:
        print(HANGMAN_PICS[max_incorrect])
        print("=" * 45)
        print("💀 GAME OVER! You ran out of attempts.")
        print(f"The secret word was: '{secret_word}'")
        print("=" * 45)


def main():
    """Main entry point allowing replay."""
    while True:
        play_hangman()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ["yes", "y"]:
            print("\nThanks for playing Hangman! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
