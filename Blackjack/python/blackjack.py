from blackjackhand import BlackjackHand 
from card import Card 
from usaMoney import USA
from deck import Deck 

def yOn(q) :
    while True:
        answer = input(q + " [Y | N] ")
        answer = answer.lower()

        if answer == 'y' or answer == 'yes' :
            return True
        elif answer == 'n' or answer == 'no' :
            return False
        else :
            print("Sorry, I didn't get that. Please enter 'Y' or 'N'")


class BlackjackGame :
    def __init__(self) :

        self.playerMoney = USA('5.00')
        self.handNum = 0


        if not yOn("Welcome to Sam's Blackjack table! Would you like to start a game?") :
            print("Well then why are you here? Get out!")
            exit()

        else :
            print("Awesome, let's get started!")

        print('')
        

    def printRules(self) :
        print("Okay, here are the rules:")
        print("1. The minimum bet for each round is $0.10")
        print("2. The dealer does NOT hit on a soft 17")
        print("3. The dealer gets a 'hole card' at the beginning of each hand.")
        print("     The dealer will show the card if it has a blackjack.")
        print("4. You start with $2.00. If you run out of money, you lose.")
        print("5. The house always wins. You will not win the overall game")
        print("     (You will probably win a few hands though)")
        print("6. This game is entirely between you and the dealer. There are no other players")
        print("7. We don't care if you count cards!")
        print("8. These rules need to be updated")

        print('')


    class Hand :
        def __init__ (self, BlackjackGame) :
            self.deck = Deck()
            self.playerHands = [BlackjackHand([self.deck.draw()])]
            self.dealerHand = BlackjackHand([self.deck.draw()])
            self.BlackjackGame = BlackjackGame
            self.amtBet = USA('0.10')
            self.playerHands[0].add(self.deck.draw())
            self.dealerHand.add(self.deck.draw())
            self.playerTurn = True

        def __str__(self) :
            temp = ""
            temp += "Dealer's hand:\n"

            if self.playerTurn and self.dealerHand != 21 :
                temp += str(self.dealerHand.cards[0]) + '\n'
            else :
                temp += str(self.dealerHand)

            temp += '\n'

            for i in range(len(self.playerHands)) :
                if len(self.playerHands) > 1 :
                    temp += "Player " + str(i + 1) + '\n'
                temp += "Your hand:\n" + str(self.playerHands[i]) + '\n'
                temp += "Current Value: " + str(self.playerHands[i].getValue())
                temp += " Your bet: " + str(self.amtBet) + "  You have: " + str(self.BlackjackGame.playerMoney)

            return temp

        #returns None if no further moves by player possible. Otherwise, returns the number option 
        #of their choice. 
        def getPlayerMove(self, playerNum) :
            if self.dealerHand.getValue() == 21 :
                self.BlackjackGame.playerMoney -= self.amtBet
                print("Dealer blackjack! Hand lost.  Your balance:", self.BlackjackGame.playerMoney)

            elif self.playerHands[playerNum].getValue() == 21 :
                self.BlackjackGame.playerMoney += self.amtBet
                print("You got a blackjack! Hand won.  Your balance:", self.BlackjackGame.playerMoney)

            elif self.playerHands[0].getValue() > 21 :
                self.BlackjackGame.playerMoney -= self.amtBet
                print("You busted! Hand lost.  Your balance:", self.BlackjackGame.playerMoney)

            else :
                print("What would you like to do?  Your balance: ", self.BlackjackGame.playerMoney)

                hitLocked = self.playerHands[playerNum].getValue() == 20
                splitAvailable = False

                #checking for split availability
                if self.playerHands[playerNum].getValue() % 2 == 0 :
                    if self.playerHands[playerNum].cards[0].value < 10 :
                        splitAvailable = self.playerHands[playerNum].cards[1].value == self.playerHands[playerNum].cards[0].value
                    else :
                        splitAvailable = self.playerHands[playerNum].cards[1].value >= 10
                
                #outputting player options
                option = 0
                while option == 0 :
                    if hitLocked :
                        print("[-] Hit locked due to hand value")
                    else :
                        print("[1] Hit")
                    print("[2] Stand")
                    if hitLocked :
                        print("[-] Double Down locked due to hand value")
                    else :
                        print("[3] Double Down")
                    if splitAvailable :
                        print("[4] Split")
                    else :
                        print("[-] Split not available")
                    print("[5] Surrender")

                    answer = input()
                    answer = answer.lower()

                    if (answer == '1' or answer == 'h' or answer == 'hit') and not hitLocked :
                        option = 1
                    elif answer == '2' or answer == 'stand' :
                        option = 2
                    elif (answer == '3' or answer == 'd' or answer =='double' 
                            or answer == 'double down') and not hitLocked :
                        option = 3
                    elif (answer == '4' or answer == 'split') and splitAvailable :
                        option = 4
                    elif answer == '5' or answer == 'surrender' :
                        option = 5

                    if option == 0 :
                        print("Unable to determine answer. Please choose a valid option.")

                return option

        def playerHit(self, playerNum) :
            self.playerHands[playerNum].add(self.deck.draw())

        def playerDoubleDown(self, playerNum) :
            self.amtBet *= 2
            self.playerHit(playerNum)




    def playHand(self) :
        self.handNum += 1

        hand = self.Hand(self)

        print(hand)


        option = hand.getPlayerMove(0)
        while option != None :
            if option == 1 :
                hand.playerHit(0)
            elif option == 2 :
                option = None
            elif option == 3 :
                hand.playerDoubleDown(0)
                option = None
            elif option == 4 :
                print("Split not yet supported")
            elif option == 5 :
                self.playerMoney -= (hand.amtBet / 2)
                option = None


            if option != None :     #the flag if execution must stop
                option = hand.getPlayerMove()







game = BlackjackGame()

if yOn("Would you like to know the rules?") :
    game.printRules()
else :
    print("Ah an expert then! Alrighty, let's get started!")

keepPlaying = True
while keepPlaying :
    game.playHand()


    keepPlaying = yOn("Would you like to keep playing?")