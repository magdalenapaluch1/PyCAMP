from card import *
import random

class Deck:
    def __init__(self) -> None:
        self._card_list = []

        for color in CARD_COLORS:
            for name in CARD_NAMES:
                self._card_list.append(Card(name, color))

    def __str__(self) -> str:
        card_string = ''
        for card in self._card_list:
            card_string += str(card) + ' '
        return card_string

    def shuffle(self) -> None:
        """Shuffle all deck"""
        if len(self._card_list) > 1:
            random.shuffle(self._card_list)

    def draw_card(self) -> Card:
        """Draw card from deck, when there is anything to draw"""
        if len(self._card_list) > 0:
            card = self._card_list.pop(0)
        else:
            raise Exception("Deck is empty. Cannot draw next card.")

        return card
