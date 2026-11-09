# Hangman Game in Python

A simple, interactive, beginner-friendly command-line **Hangman Game** built with Python.

---

## 🎯 Features

- **Predefined Word List**: The computer randomly selects a secret word from a list of 5 words (`python`, `laptop`, `bottle`, `guitar`, `window`).
- **Interactive Gameplay**: The player guesses the secret word one letter at a time.
- **Visual Hangman Gallows**: ASCII art illustrations that update with every incorrect guess (0 to 6 attempts).
- **Progress Tracking**:
  - Displays correctly guessed letters revealed in their proper positions (`_` for hidden letters).
  - Shows previously guessed letters so you never forget what you've tried.
  - Displays remaining incorrect attempts (maximum of 6).
- **Input Validation**: Handles invalid characters, empty input, multi-letter inputs, and duplicate guesses without unfairly penalizing the player.
- **Win / Loss Detection**: Displays celebratory messages upon guessing the word, or reveals the secret word if you run out of attempts.
- **Replay Option**: Allows players to start a new round without restarting the program.

---

## 🐍 Python Concepts Used

| Concept | Usage in Game |
| :--- | :--- |
| **`random` module** | Used `random.choice()` to randomly pick a word from the predefined list. |
| **`while` loops** | Drives the main game loop (`while incorrect_guesses < max_incorrect`) and the replay prompt. |
| **`if-else` conditions** | Validates user inputs, checks letter matches, and handles win/loss logic. |
| **`strings`** | Used for word comparison, formatting output messages, and displaying masked words. |
| **`lists`** | Stores the predefined words, the visual hangman ASCII frames, and the guessed letters history. |

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this directory:
   ```bash
   cd c:\Users\sharm\Downloads\codealpha_hangman
   ```
3. Run the script:
   ```bash
   python hangman.py
   ```
