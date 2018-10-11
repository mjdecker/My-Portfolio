from hand import Hand
from card import Card 

class BlackjackHand(Hand) :
    def __init__(self, cards = []) :
        super().__init__(cards)

    def getValue(self) :
        total = 0
        numAces = 0
        for card in self :
            if card.value == 1 :
                numAces += 1
                total += 1
            elif card.value > 10 :
                total += 10
            else :
                total += card.value

        for i in range(numAces) :
            if total <= 11 :
                total += 10
            else :
                break

        return total

