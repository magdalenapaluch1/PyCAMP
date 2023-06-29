import pytest
from deck import Deck
from card import Card
from player import *

def test_Player_Human():
    """Create human player."""
    human = Human("Wojtek")

    assert human.name == "Wojtek"

def test_Player_Croupier():
    """Create croupier player."""
    croupier = Croupier()

    assert croupier.name == "Croupier"

def test_Player_Human_Draw_1_Card():
    """Create human player."""
    human = Human("Wojtek")

    deck = Deck()

    human.draw_card(deck)

    assert len(human.hand) == 1
    assert human.hand[0] == Card("2", "hearts")
    assert len(deck._card_list) == 51

def test_Player_Human_Hand_Is_Empty_Hand_Value_Equals_0():
    human = Human("Wojtek")

    points = human.get_hand_value()

    assert points == 0

def test_Player_Human_Hand_Is_J_Hand_Value_Equals_10():
    human = Human("Wojtek")

    human.hand.append(Card("J", "hearts"))

    points = human.get_hand_value()

    assert points == 10

def test_Player_Human_Hand_Is_Ace_Hand_Less_Or_Equal_2_Cards_Hand_Value_Equals_11():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))

    points = human.get_hand_value()

    assert points == 11

def test_Player_Human_Hand_Is_Ace_Hand_Has_More_Than_2_Cards_Hand_Value_Equals_16():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))
    human.hand.append(Card("J", "hearts"))
    human.hand.append(Card("5", "hearts"))

    points = human.get_hand_value()

    assert points == 16

def test_Player_Human_Hand_Is_10_Hand_Value_Equals_10():
    human = Human("Wojtek")

    human.hand.append(Card("10", "hearts"))

    points = human.get_hand_value()

    assert points == 10

def test_Player_Human_Hand_Is_0_Hand_Value_Equals_10():
    human = Human("Wojtek")
    invalid_card = Card("2", "hearts")
    invalid_card._name = "1"

    human.hand.append(invalid_card)

    with pytest.raises(Exception):
        human.get_hand_value()

def test_Player_Human_Hand_2_Aces_Hand_Value_Equals_12():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))
    human.hand.append(Card("A", "spades"))

    points = human.get_hand_value()

    assert points == 12

def test_Player_Human_Hand_3_Aces_Hand_Value_Equals_13():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))
    human.hand.append(Card("A", "spades"))
    human.hand.append(Card("A", "diamonds"))

    points = human.get_hand_value()

    assert points == 13

def test_Player_Human_Hand_3_Aces_And_7_Hand_Value_Equals_20():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))
    human.hand.append(Card("A", "spades"))
    human.hand.append(Card("A", "diamonds"))
    human.hand.append(Card("7", "diamonds"))

    points = human.get_hand_value()

    assert points == 20

def test_Player_Human_Hand_3_Aces_And_K_Hand_Value_Equals_13():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))
    human.hand.append(Card("A", "spades"))
    human.hand.append(Card("A", "diamonds"))
    human.hand.append(Card("K", "diamonds"))

    points = human.get_hand_value()

    assert points == 13

def test_Player_Human_Hand_3_Aces_3_Kings_Hand_Value_Equals_23():
    human = Human("Wojtek")

    human.hand.append(Card("A", "hearts"))
    human.hand.append(Card("A", "spades"))
    human.hand.append(Card("A", "diamonds"))
    human.hand.append(Card("K", "spades"))
    human.hand.append(Card("K", "diamonds"))

    points = human.get_hand_value()

    assert points == 23