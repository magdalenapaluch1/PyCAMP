"""Card class"""
CARD_NAMES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_COLORS = ['hearts', 'diamonds', 'spades', 'clubs']
CARD_SYMBOLS = {'hearts': "\u2665", 'diamonds': "\u2666", 'spades': "\u2660", 'clubs': "\u2663"}

class Card:
    """Card class. Creating new card. Card fields cannot change."""
    def __init__(self, name, color) -> None:
        if name in CARD_NAMES and color in CARD_COLORS:
            self._name = name
            self._color = color
        else:
            raise Exception('Attempt to create an invalid card.')
        
    def __str__(self):
        return self._name + CARD_SYMBOLS[self._color]