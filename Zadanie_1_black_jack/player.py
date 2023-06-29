from deck import Deck

class Player:
    """General player class"""
    def __init__(self) -> None:
        self.hand = []

    def draw_card(self, deck: Deck):
        """Draw card from deck to player's hand"""
        card = deck.draw_card()
        self.hand.append(card)

    def get_hand_value(self) -> int:
        """Return sum of card points on players hand"""
        player_points = 0
        aces_in_hand = 0

        for card in self.hand:
            if (card._name == "J" or card._name == "Q" or card._name == "K"):
                player_points += 10
            elif card._name == "A":
                player_points += 11
                aces_in_hand += 1
            elif (int(card._name) >= 2 and int(card._name) <= 10):
                player_points += int(card._name)
            else:
                raise Exception('Invalid card in hand.')

        if aces_in_hand > 0 and player_points > 21:
            aces_remaining = aces_in_hand
            while aces_remaining > 0 and player_points > 21:
                player_points -= 10
                aces_remaining -= 1
            
        return player_points
    
    def show_hand(self):
        print(self.name, "cards:" , self.hand)

class Human(Player):
    """Human player"""
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

class Croupier(Player):
    """Croupier (computer) player"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Croupier"

    def show_first_hand(self):
        print(self.name, " cards: [", self.hand[0], ", #]", sep='')
