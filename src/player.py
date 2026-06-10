class Player:
    def __init__(self, name, roundBank = 0, totalBank = 0):
        self.name = name
        self.roundBank = roundBank
        self.totalBank = totalBank

    def resetRoundBank(self):
        self.roundBank = 0

    def updateWinnings(self, amount):
        self.roundBank += amount

    def updateTotalWinnings(self):
        self.totalBank += self.roundBank

    def get_consonant_guess(self):
        while True:
            guess = input("Guess a consonant: ").lower().strip()
            if len(guess) == 1 and guess.isalpha() and guess not in {"a", "e", "i", "o", "u"}:
                return guess
            print("Invalid input. Please enter a single consonant.")

    def buy_vowel(self, roundWord, blankWord, vowelcost, vowels):
        if self.roundBank < vowelcost:
            print("Not enough funds to buy a vowel.")
            return False

        while True:
            guess = input("Guess a vowel: ").lower().strip()
            if len(guess) == 1 and guess.isalpha() and guess in vowels:
                break
            print("Invalid input. Please enter a single vowel.")

        self.roundBank -= vowelcost
        goodGuess = False
        count = 0
        for index, char in enumerate(roundWord):
            if char.lower() == guess and blankWord[index] == "_":
                blankWord[index] = char
                goodGuess = True
                count += 1

        if goodGuess:
            print(f"Correct! The vowel '{guess}' appears {count} time(s).")
            return True

        print(f"Sorry, the vowel '{guess}' is not in the word.")
        return False

    def get_word_guess(self, roundWord, blankWord):
        guess = input("Guess the entire word or phrase: ").strip()
        if guess.lower() == roundWord.lower():
            blankWord[:] = list(roundWord)
            print("Congratulations! You've guessed the word/phrase correctly!")
            return True
        print("That guess is incorrect.")
        return False


def get_player_status(player):
    return (
        f"Player(name={player.name!r}, roundBank=${player.roundBank}, "
        f"totalBank=${player.totalBank})"
    )
