import random

#class definition of a standard card class

class Card :
    def __init__(self, value = 1, suit = "Spades") :

        if type(value) is int :
            self.suit = suit
            self.value = value
        else :                      #to enable the parameters to be passed in any order
            self.suit = value
            self.value = suit

        self.cardToValue = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        self.suitFromNum = {
            1: "Spades",
            2: "Clubs",
            3: "Diamonds",
            4: "Hearts"
        }

    def __str__(self) :
        return self.cardToValue.get(self.value, "Class rules violated!!!") + " of " + self.suit

    def __eq__(self, other) :
        return self.suit == other.suit and self.value == other.value

    def generateRandomValue(self) :
        self.suit = self.suitFromNum.get(random.randint(1,4), "Error")
        self.value = random.randint(1,13)


