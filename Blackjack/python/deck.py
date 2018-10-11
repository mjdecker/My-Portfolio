from card import Card

class Deck :
    def __init__(self, cards = [], shuffle = True) :
        self.cards = cards
        if shuffle :
            self.shuffle()

    def __len__(self) :
        return len(self.cards)

    def __str__(self) :
        temp = ""
        for card in self.cards :
            temp += str(card) + '\n'

        return temp


    def __iter__(self) :
        for card in self.cards :
            yield card

    def __contains__(self, value) :
        return value in self.cards


    def shuffle(self) :
        
        while len(self) < 52 :
            card = Card()
            card.generateRandomValue()

            if not (card in self.cards) :
                self.cards.append(card)

    def draw(self) :
        return self.cards.pop();
