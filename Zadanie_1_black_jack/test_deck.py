import pytest
from deck import Deck
from card import Card

def test_valid_deck():
    """Try to create valid deck without jokers."""
    new_deck = Deck()

    assert len(new_deck._card_list) == 52

def test_2_of_hearts_once_in_deck():
    """Check if given card is present only once in deck."""
    new_deck = Deck()
    hearts2 = Card("2", "hearts")

    assert new_deck._card_list.count(hearts2) == 1

def test_draw_1_card():
    """Try to draw one card."""
    new_deck = Deck()

    new_deck.draw_card()

    assert len(new_deck._card_list) == 51

def test_draw_52_cards():
    """Try to draw all cards."""
    new_deck = Deck()

    for i in range(52):
        new_deck.draw_card()

    assert len(new_deck._card_list) == 0

def test_try_to_draw_53_cards():
    """Try to draw 53 cards."""
    with pytest.raises(Exception):
        new_deck = Deck()

        for i in range(53):
            new_deck.draw_card()

    assert len(new_deck._card_list) == 0
