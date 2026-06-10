# Wheel of Fortune

A simple command-line Wheel of Fortune–style game implemented in Python.

## Project Purpose

This project provides a playable text-based version of Wheel of Fortune. It uses a dictionary of phrases, a wheel file for spins, and text prompts for each round. Players take turns spinning the wheel, guessing consonants, buying vowels, and solving puzzles.

## Files and Data

- `src/startercode.py` — main game logic and entry point
- `src/player.py` — player class and input handling for guesses
- `src/config.py` — file locations, game settings, and pricing
- `data/dictionary.txt` — puzzle phrases used in rounds
- `data/wheeldata.txt` — available wheel values and special spaces
- `data/turntext.txt` — gameplay prompt displayed during each turn
- `data/roundstatus.txt` — end-of-round status message
- `data/finalround.txt` — instructions shown before the final round

## Installation

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. (Optional) Create and activate a virtual environment:

## Example Session

A successful run should prompt for player names and then proceed through the rounds, for example:

```text
Enter name for Player 1: Alice
Enter name for Player 2: Bob
Enter name for Player 3: Carol

Current puzzle: ____________
Spin the wheel to earn money by guessing a consonant. Buy a vowel for $250, or solve the puzzle at any time to win the round. Good luck!
Player: Alice, Round Bank: $0
Choose (S)pin, (B)uy a vowel, or (G)uess the word: S
Alice spun: $1,000
Guess a consonant: T
1 letter(s) found. Added $1000 to Alice's round bank.

Current puzzle: _ _ _ _ _ T _ _ _ _ _
Player: Alice, Round Bank: $1000
Choose (S)pin, (B)uy a vowel, or (G)uess the word: G
Guess the entire word or phrase: A GREAT TIME
Congratulations! You've guessed the word/phrase correctly!
Round complete. The puzzle has been solved and scores have been updated. Get ready for the next round.
```

The final round displays the final round instructions and allows the winner to choose letters before making their final guess.
