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