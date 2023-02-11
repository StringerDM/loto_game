import random

from card import Card

player_card = Card()
player_card.print_card()
num = random.choice(random.choice(player_card.card))
player_card.try_number(num)
player_card.print_card()
