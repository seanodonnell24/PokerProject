from Card import Card
from Deck import Deck


# This is the hand class that is used to create the hands of the players, add cards to the hand,
# get the point value of the hand, and then compare them to see who wins. It only has one
# attribute, hand, which represents the hand of the player. This class uses method
# decomposition in order to make simpler helper methods. I created a method to check for every
# possible hand value for a poker game, from just a high card to a royal flush. The largest
# algorithm in this class is the compare method. It checks to see if the rank, the amount of
# points a hand is worth, of one hand is greater than another. However, if they are equal then
# it checks the high card for some as that is the deciding factor in who wins or it could check
# to see which pair, three of a kind, or four of a kind is the larger number. Rank and get hand
# type are also fairly big, but simple. Rank uses the simpler helper methods to check what the
# hand is, and gives a corresponding point value for the hand. The get hand type checks what
# the rank of the hand is and gives the actual name that corresponds with the value of the hand.
# Some list methods I use here are append, sort, and reverse.

def by_value(card):
    return card.value


class Hand:

    def __init__(self):
        self.hand = []

    def add_card(self, card: Card):
        if len(self.hand) < 5:
            self.hand.append(card)
            self.hand.sort(reverse=True, key=by_value)
        else:
            print("You already have 5 cards")

    def get_hand(self):
        return self.hand

    def print_hand(self):
        [print(x.get_name()) for x in self.hand]

    def is_pair(self):
        is_pair = False
        count = 0
        pair = 0
        for i in range(len(self.hand) - 1):
            if self.hand[i].value == self.hand[i + 1].value:
                pair = self.hand[i].value
                count += 1
        if count == 1:
            is_pair = True
        return [is_pair, pair]

    def is_two_pair(self):
        is_two_pair = False
        count = 0
        high_pair = 0
        if self.is_three_of_a_kind():
            return False
        for i in range(len(self.hand) - 1):
            if self.hand[i].value == self.hand[i + 1].value:
                count += 1
        if count == 2:
            is_two_pair = True
        return is_two_pair

    def check_three_pair(self):
        is_three_pair = False
        count = 0
        for i in range(len(self.hand) - 1):
            if self.hand[i].value == self.hand[i + 1].value:
                count += 1
        if count == 3:
            is_three_pair = True
        return is_three_pair

    def is_three_of_a_kind(self):
        return self.hand[0].value == self.hand[2].value or self.hand[1].value == self.hand[3].value \
            or self.hand[2].value == self.hand[4].value

    def is_straight(self):
        is_straight = True
        if self.hand[0].value == 14 and self.hand[1].value == 5:
            for x in range(len(self.hand) - 2):
                if self.hand[x + 1].value - self.hand[x + 2].value != 1:
                    is_straight = False
        else:
            for x in range(len(self.hand) - 1):
                if self.hand[x].value - self.hand[x + 1].value != 1:
                    is_straight = False
        return is_straight

    def is_flush(self):
        return not any([x.suit != self.hand[0].suit for x in self.hand])

    def is_full_house(self):
        is_full_house = False
        if self.is_four_of_a_kind():
            return False
        if self.is_three_of_a_kind() and self.check_three_pair():
            is_full_house = True
        return is_full_house

    def is_four_of_a_kind(self):
        return self.hand[0].value == self.hand[3].value or self.hand[1].value == self.hand[4].value

    def is_straight_flush(self):
        is_straight_flush = False
        if self.is_straight() and self.is_flush():
            is_straight_flush = True
        return is_straight_flush

    def is_royal_flush(self):
        is_royal_flush = False
        if self.is_straight_flush() and sum(x.value for x in self.hand) == 60:
            is_royal_flush = True
        return is_royal_flush

    def rank(self):
        rank = 0
        high_card = self.hand[0].value
        if self.is_pair()[0]:
            rank = 1
            high_card = self.hand[0].value
        if self.is_two_pair():
            rank = 2
            high_card = self.hand[0].value
        if self.is_three_of_a_kind():
            rank = 3
            high_card = self.hand[0].value
        if self.is_straight():
            rank = 4
            high_card = self.hand[0].value
        if self.is_flush():
            rank = 5
            high_card = self.hand[0].value
        if self.is_full_house():
            rank = 6
            high_card = self.hand[0].value
        if self.is_four_of_a_kind():
            rank = 7
            high_card = self.hand[0].value
        if self.is_straight_flush():
            rank = 8
            high_card = self.hand[0].value
        if self.is_royal_flush():
            rank = 9
            high_card = self.hand[0].value
        return [rank, high_card]

    def get_hand_type(self):
        #     # print(f"High Card: {self.hand[0].get_name()}")
        if self.rank()[0] == 9:
            return "Royal Flush"
        elif self.rank()[0] == 8:
            return "Straight Flush"
        elif self.rank()[0] == 7:
            return "Four of a Kind"
        elif self.rank()[0] == 6:
            return "Full House"
        elif self.rank()[0] == 5:
            return "Flush"
        elif self.rank()[0] == 4:
            return "Straight"
        elif self.rank()[0] == 3:
            return "Three of a Kind"
        elif self.rank()[0] == 2:
            return "Two Pair"
        elif self.rank()[0] == 1:
            return "Pair"
        elif self.rank()[0] == 0:
            return "High Card"
        # return self.rank()[0]

    def compare_hand(self, other_hand):
        if self.rank()[0] > other_hand.rank()[0]:
            return 1
        elif other_hand.rank()[0] > self.rank()[0]:
            return -1
        elif self.rank()[0] == other_hand.rank()[0]:
            if self.rank()[0] == 9:
                return 0
            if self.rank()[0] == 8 or self.rank()[0] == 4:
                if self.rank()[1] > other_hand.rank()[1]:
                    return 1
                elif other_hand.rank()[1] > self.rank()[1]:
                    return -1
                elif self.rank()[1] == other_hand.rank()[1]:
                    return 0
            if self.rank()[0] == 7:
                if self.hand[3].value > other_hand.hand[3].value:
                    return 1
                elif other_hand.hand[3].value > self.hand[3].value:
                    return -1
            if self.rank()[0] == 6 or self.rank()[0] == 3:
                if self.hand[2].value > other_hand.hand[2].value:
                    return 1
                elif other_hand.hand[2].value > self.hand[2].value:
                    return -1
            if self.rank()[0] == 5:
                if self.rank()[1] > other_hand.rank()[1]:
                    return 1
                elif other_hand.rank()[1] > self.rank()[1]:
                    return -1
            if self.rank()[0] == 2:
                if self.hand[1].value > other_hand.hand[1].value:
                    return 1
                elif other_hand.hand[1].value > self.hand[1].value:
                    return -1
                elif self.hand[3].value > other_hand.hand[3].value:
                    return 1
                elif other_hand.hand[3].value > self.hand[3].value:
                    return -1
                else:
                    if sum(x.value for x in self.hand) > sum(x.value for x in other_hand.hand):
                        return 1
                    elif sum(x.value for x in other_hand.hand) > sum(x.value for x in self.hand):
                        return -1
                    else:
                        return 0
            if self.rank()[0] == 1:
                if self.is_pair()[1] > other_hand.is_pair()[1]:
                    return 1
                elif other_hand.is_pair()[1] > self.is_pair()[1]:
                    return -1
                else:
                    if self.check_highest_card(other_hand) == 1:
                        return 1
                    elif self.check_highest_card(other_hand) == -1:
                        return -1
                    else:
                        return 0
            if self.rank()[0] == 0:
                if self.check_highest_card(other_hand) == 1:
                    return 1
                elif self.check_highest_card(other_hand) == -1:
                    return -1
                else:
                    return 0

    def check_highest_card(self, other_hand):
        for x in range(0, 5):
            if self.hand[x].value > other_hand.hand[x].value:
                return 1
            elif other_hand.hand[x].value > self.hand[x].value:
                return -1
        return 0

