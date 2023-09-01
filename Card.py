#  This class is used to create everything necessary for a card. It has two instance attributes,
# suit and value, that are the suit of the card and the value of the card, so a number 2-14.
# There aren't any major algorithms in this class. In this class, I have a tuple as a class
# attribute that stores the names of the cards because they won't change at any point

class Card:

    names = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack",
             "queen", "king", "ace")

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_name(self):
        return f"{Card.names[self.value - 2]} of {self.suit}"

    def image_file_name(self):
        if self.value <= 10:
            return f"{self.value}_of_{self.suit}.png"
        else:
            return f"{Card.names[self.value - 2]}_of_{self.suit}.png"


