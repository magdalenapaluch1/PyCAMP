import pytest
from card import Card

def test_valid_card_2_hearts():
    """Try to create valid card : 2 of hearts"""
    new_card = Card("2", "hearts")

    assert new_card._name == "2"
    assert new_card._color == "hearts"

def test_valid_card_Ace_spades():
    """Try to create valid card : A of spades"""
    new_card = Card("A", "spades")

    assert new_card._name == "A"
    assert new_card._color == "spades"

def test_invalid_card_22_hearts():
    """Try to create invalid card : 22 of hearts"""
    with pytest.raises(Exception):
        new_card = Card("22", "hearts")

def test_invalid_card_2_heart():
    """Try to create invalid card : 2 of heart (missing s)"""
    with pytest.raises(Exception):
        new_card = Card("2", "heart")

def test_invalid_card_22_heart():
    """Try to create invalid card : 22 of heart (missing s)"""
    with pytest.raises(Exception):
        new_card = Card("22", "heart")


def test_print_valid_card_2_hearts():
    """Try to create valid card : 2 of hearts"""
    new_card = Card("2", "hearts")

    assert str(new_card) == "2♥"

def test_repr_print_valid_card_2_and_3_hearts():
    """Try to create valid card : 2 of hearts"""
    new_card = Card("2", "hearts")
    new_card2 = Card("3", "hearts")

    assert str([new_card, new_card2]) == "[2♥, 3♥]"
