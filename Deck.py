from Card import Card
import random

# This class is used to create a deck of 52 cards, shuffle, and deal cards. I have one instance
# attribute, deck, that uses a nested for loop to create all of the cards with their specified
# values. I also have a class attribute, suits, that is a tuple of strings for the suits of
# the cards. The deal card method is used to deal the cards to player's hands. First, it checks
# to make sure that there are still cards in the deck that can be dealt, and if there are,
# then it will deal the "top" of the deck, which is the first position in the list of cards.
# It is a random card because it is shuffled beforehand. Once a card is dealt, it is removed
# from the list. I use the list methods copy and remove here.


class Deck:
    suits = ("Diamonds", "Hearts", "Spades", "Clubs")

    def __init__(self):
        self.deck = []
        for x in range(2, 15):
            for y in self.suits:
                self.deck.append(Card(y, x))

    def get_deck(self):
        return self.deck.copy()

    def print_deck(self):
        [print(x.get_name()) for x in self.deck]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) == 0:
            return "none"
        else:
            top = self.deck[0]
            self.deck.remove(top)
            return top





