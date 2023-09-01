from Card import Card
from Deck import Deck
from Hand import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# This is the main class, where I use images and display them in rows and columns to represent
# the players hands. The find winner method uses another method I made, compare two hands, and
# compares hands against each other until a winner is found. Some list methods I use here are
# insert, remove, and index.

def make_row(im1, im2, im3, im4, im5):
    img1 = Image.open(im1)
    img2 = Image.open(im2)
    img3 = Image.open(im3)
    img4 = Image.open(im4)
    img5 = Image.open(im5)
    row = Image.new('RGB', (img1.width * 6, min(img1.height, img2.height)))
    row.paste(img1, (0, 0))
    row.paste(img2, (img1.width, 0))
    row.paste(img3, (img1.width + img2.width, 0))
    row.paste(img4, (img1.width + img2.width + img3.width, 0))
    row.paste(img5, (img1.width + img2.width + img3.width + img4.width, 0))
    return row


def make_column(img1, img2, img3, img4):
    column = Image.new('RGB', (img1.width, img1.height * 4))
    column.paste(img1, (0, 0))
    column.paste(img2, (0, img1.height))
    column.paste(img3, (0, img1.height + img2.height))
    column.paste(img4, (0, img1.height + img2.height + img3.height))
    return column


new_deck = Deck()
new_deck.shuffle()

sean_hand = Hand()
alex_hand = Hand()
max_hand = Hand()
alex2_hand = Hand()
winners = []
tied = []
game = [sean_hand, alex_hand, max_hand, alex2_hand]

for x in range(5):
    game[0].add_card(new_deck.deal_card())
    game[1].add_card(new_deck.deal_card())
    game[2].add_card(new_deck.deal_card())
    game[3].add_card(new_deck.deal_card())


def compare_two_hands(hand_one, hand_two):
    compare = hand_one.compare_hand(hand_two)
    if compare == 1:
        return hand_one
    elif compare == -1:
        return hand_two
    else:
        return hand_one


def find_winner(hand_one, hand_two, hand_three, hand_four):
    compare_one = compare_two_hands(hand_one, hand_two)
    compare_two = compare_two_hands(hand_three, hand_four)
    return compare_two_hands(compare_one, compare_two)


Winner = find_winner(game[0], game[1], game[2], game[3])
winners.append(Winner)
position = game.index(Winner)
game.remove(Winner)
for x in game:
    if Winner.compare_hand(x) == 0:
        tied.append(x)
game.insert(position, Winner)

hand1 = make_row("cards/" + game[0].get_hand()[0].image_file_name(),
                 "cards/" + game[0].get_hand()[1].image_file_name(),
                 "cards/" + game[0].get_hand()[2].image_file_name(),
                 "cards/" + game[0].get_hand()[3].image_file_name(),
                 "cards/" + game[0].get_hand()[4].image_file_name())
hand2 = make_row("cards/" + game[1].get_hand()[0].image_file_name(),
                 "cards/" + game[1].get_hand()[1].image_file_name(),
                 "cards/" + game[1].get_hand()[2].image_file_name(),
                 "cards/" + game[1].get_hand()[3].image_file_name(),
                 "cards/" + game[1].get_hand()[4].image_file_name())
hand3 = make_row("cards/" + game[2].get_hand()[0].image_file_name(),
                 "cards/" + game[2].get_hand()[1].image_file_name(),
                 "cards/" + game[2].get_hand()[2].image_file_name(),
                 "cards/" + game[2].get_hand()[3].image_file_name(),
                 "cards/" + game[2].get_hand()[4].image_file_name())
hand4 = make_row("cards/" + game[3].get_hand()[0].image_file_name(),
                 "cards/" + game[3].get_hand()[1].image_file_name(),
                 "cards/" + game[3].get_hand()[2].image_file_name(),
                 "cards/" + game[3].get_hand()[3].image_file_name(),
                 "cards/" + game[3].get_hand()[4].image_file_name())

c = make_column(hand1, hand2, hand3, hand4)

draw = ImageDraw.Draw(c)
for x in range(4):
    text = game[x].get_hand_type()
    for i in winners:
        if i == game[x]:
            text = f"{game[x].get_hand_type()} \n winner!"
    draw.text((510, (150 * x) + 50), text)

c.show()
