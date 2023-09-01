# PokerProject
# In the main class, I use images and display them in rows and columns to represent the players hands. The find winner method uses another method I made, compare two hands, and compares hands against each other until a winner is found. Some list methods I use here are insert, remove, and index.
# The Card class is used to create everything necessary for a card. It has two instance attributes, suit and value, that are the suit of the card and the value of the card, so a number 2-14. There aren't any major algorithms in this class. In this class, I have a tuple as a class attribute that stores the names of the cards because they won't change at any point.
# The Deck class is used to create a deck of 52 cards, shuffle, and deal cards. I have one instance attribute, deck, that uses a nested for loop to create all of the cards with their specified values. I also have a class attribute, suits, that is a tuple of strings for the suits of the cards. The deal card method is used to deal the cards to player's hands. First, it checks to make sure that there are still cards in the deck that can be dealt, and if there are, then it will deal the "top" of the deck, which is the first position in the list of cards. It is a random card because it is shuffled beforehand. Once a card is dealt, it is removed from the list. I use the list methods copy and remove here.
# This is the Hand class that is used to create the hands of the players, add cards to the hand, get the point value of the hand, and then compare them to see who wins. It only has one attribute, hand, which represents the hand of the player. This class uses method decomposition in order to make simpler helper methods. I created a method to check for every possible hand value for a poker game, from just a high card to a royal flush. The largest algorithm in this class is the compare method. It checks to see if the rank, the amount of points a hand is worth, of one hand is greater than another. However, if they are equal then it checks the high card for some as that is the deciding factor in who wins or it could check to see which pair, three of a kind, or four of a kind is the larger number. Rank and get hand type are also fairly big, but simple. Rank uses the simpler helper methods to check what the hand is, and gives a corresponding point value for the hand. The get hand type checks what the rank of the hand is and gives the actual name that corresponds with the value of the hand. Some list methods I use here are append, sort, and reverse.
