from card import Card
from deck import Deck 

class Hand(Deck) :
    def __init__(self, cards = []) :
        super().__init__(cards, False)

    def shuffle(self) :
        pass

    def getValue(self) :
        total = 0
        for card in self :
            total += card.value
        return total

    def draw(self) :
        pass


    def add(self, card) :
        self.cards.append(card)
