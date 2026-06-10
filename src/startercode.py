from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize # you must set this in your config.py file
from config import finalRoundTextLoc
from config import debug
# Be sure to check the config.py file and make sure that your paths for all of the different locations match those in the config.py file.


import random

players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""},
        }

roundNum = 0
dictionary = []
turntext = ""
wheellist = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""

def load_words():
    with open(dictionaryloc) as f:
        print(f.read().splitlines())

def mask_phrase(phrase):
    masked = ""
    for char in phrase:
        if char.isalpha():
            masked += "_"
        else:
            masked += char
    return masked

def get_wheel_value():
    with open(wheeltextloc) as f:
        wheel_list = f.read().splitlines()
    return random.choice(wheel_list)

def spinWheel(playerNum):
    global wheellist
    global players

    player = players[playerNum]
    wheel_value = get_wheel_value()
    print(f"{player.name} spun: {wheel_value}")

    if wheel_value.upper() == "BANKRUPT":
        player.roundBank = 0
        print("BANKRUPT! You lose your round bank.")
        return False
    if wheel_value.upper() == "LOSE A TURN":
        print("LOSE A TURN. Your turn ends.")
        return False

    amount = int(wheel_value.replace("$", "").replace(",", ""))

    guess = player.get_consonant_guess()
    goodGuess, count = guessletter(guess)
    if goodGuess:
        winnings = amount * count
        player.roundBank += winnings
        print(f"{count} letter(s) found. Added ${winnings} to {player.name}'s round bank.")
        return True

    print("No letters found. Turn ends.")
    return False

def readDictionaryFile():
    global dictionary
    with open(dictionaryloc) as f:
        dictionary = f.read().splitlines()
    # Read dictionary.txt file in from dictionary file location.
    # Store each word from the dictionary.txt file in a list.
      
    
def readTurnTxtFile():
    global turntext   
    # Read in initial turn status "message" from turntext.txt file.

        
def readFinalRoundTxtFile():
    global finalroundtext   
    # Read in the final round text "message" from finalround.txt file.

def readRoundStatusTxtFile():
    global roundstatus
    # Read in the round status text from the roundstatus.txt file location. 

def readWheelTxtFile():
    global wheellist
    # Read the Wheel name from input using the wheeldata.txt file location.
    
def getPlayerInfo():
    global players
    # Read in player names from command prompt input


def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary
        
    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile() 
    
def getWord():
    global dictionary
    if debug == True:
        print(roundWord)
    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.
    return roundWord,roundUnderscoreWord

def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    if debug == True:
        print(roundWord)
    # Set round total for each player = 0
    # Return the starting player number (random)
    # Use getWord function to retrieve the word and the underscore word (blankWord)

    return initPlayer


def spinWheel(playerNum):
    global wheellist
    global players
    global vowels

    # Get random value for wheellist
    # Check for bankrupcy, and take action.
    # Check for loose turn
    # Get amount from wheel if not loose turn or bankruptcy
    # Ask user for letter guess
    # Use guessletter function to see if guess is in word, and return count
    # Change player round total if they guess right.     
    return stillinTurn


def guessletter(letter, playerNum): 
    global blankWord
    global roundWord

    goodGuess = False
    count = 0
    letter_lower = letter.lower().strip()

    for index, char in enumerate(roundWord):
        if char.lower() == letter_lower and blankWord[index] == "_":
            blankWord[index] = char
            goodGuess = True
            count += 1

    return goodGuess, count

def buyVowel(playerNum):
    player = players[playerNum]
    return player.buy_vowel(roundWord, blankWord, vowelcost, vowels)     
        
def guessWord(playerNum):
    player = players[playerNum]
    player.get_word_guess(roundWord, blankWord)
    return False
    
    
def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global turntext
    global players

    player = players[playerNum]
    if debug:
        print(roundWord)

    while True:
        print("\nCurrent puzzle:", "".join(blankWord))
        print(f"{turntext}")
        print(f"Player: {player.name}, Round Bank: ${player.roundBank}")
        choice = input("Choose (S)pin, (B)uy a vowel, or (G)uess the word: ").strip().upper()

        if choice == "S":
            stillinTurn = spinWheel(playerNum)
        elif choice == "B":
            stillinTurn = buyVowel(playerNum)
        elif choice == "G":
            stillinTurn = guessWord(playerNum)
        else:
            print("Not a correct option")
            continue

        if "_" not in blankWord:
            return False
        return stillinTurn


def wofRound():
    global players
    global roundWord
    global blankWord
    global roundstatus

    currentPlayer = wofRoundSetup()
    if debug:
        print(roundWord)

    while True:
        turnContinues = wofTurn(currentPlayer)
        if "_" not in blankWord:
            print(f"Round solved! The word was: {roundWord}")
            players[currentPlayer].totalBank += players[currentPlayer].roundBank
            break

        if not turnContinues:
            currentPlayer = (currentPlayer + 1) % len(players)

    if roundstatus:
        print(roundstatus)
    else:
        print("Round complete.")

def wofFinalRound():
    global roundWord
    global blankWord
    global finalroundtext

    winner = max(players.values(), key=lambda p: p.totalBank)
    print(f"{winner.name} is playing the final round with ${winner.totalBank} total.")
    if finalroundtext:
        print(finalroundtext)

    getWord()
    for letter in ["R", "S", "T", "L", "N", "E"]:
        guessletter(letter)

    print("Current puzzle after RSTLNE:", "".join(blankWord))

    consonants = []
    while len(consonants) < 3:
        guess = input(f"Choose consonant {len(consonants)+1}: ").lower().strip()
        if len(guess) == 1 and guess.isalpha() and guess not in vowels and guess not in consonants:
            consonants.append(guess)
        else:
            print("Invalid consonant. Try again.")

    vowel = ""
    while True:
        guess = input("Choose a vowel: ").lower().strip()
        if len(guess) == 1 and guess.isalpha() and guess in vowels:
            vowel = guess
            break
        print("Invalid vowel. Try again.")

    for letter in consonants + [vowel]:
        guessletter(letter)

    print("Current puzzle after bonus letters:", "".join(blankWord))
    final_guess = input("Final guess for the word or phrase: ").strip()
    if final_guess.lower() == roundWord.lower():
        winner.totalBank += finalprize
        print(f"Congratulations {winner.name}! You won the final prize of ${finalprize}.")
    else:
        print("Sorry, that final guess was incorrect.")


def main():
    gameSetup()    

    for i in range(0,maxrounds):
        if i in [0,1]:
            wofRound()
        else:
            wofFinalRound()

if __name__ == "__main__":
    main()
    
    
