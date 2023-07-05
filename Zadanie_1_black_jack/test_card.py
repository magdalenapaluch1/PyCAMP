import pytest
from card import Card

def test__INIT__valid_card_2_hearts():
    """Try to create valid card : 2 of hearts"""
    new_card = Card("2", "hearts")

    assert new_card._name == "2"
    assert new_card._color == "hearts"

def test__INIT__valid_card_Ace_spades():
    """Try to create valid card : A of spades"""
    new_card = Card("A", "spades")

    assert new_card._name == "A"
    assert new_card._color == "spades"

def test__INIT__invalid_card_22_hearts():
    """Try to create invalid card : 22 of hearts"""
    with pytest.raises(Exception):
        new_card = Card("22", "hearts")

def test__INIT__invalid_card_2_heart():
    """Try to create invalid card : 2 of heart (missing s)"""
    with pytest.raises(Exception):
        new_card = Card("2", "heart")

def test__INIT__invalid_card_22_heart():
    """Try to create invalid card : 22 of heart (missing s)"""
    with pytest.raises(Exception):
        new_card = Card("22", "heart")

def test__STR__print_valid_card_2_hearts():
    """Try to create valid card : 2 of hearts"""
    new_card = Card("2", "hearts")

    assert str(new_card) == "2♥"

def test__REPR__print_valid_card_2_and_3_hearts():
    """Try to create valid card : 2 of hearts and 3 of hearts"""
    new_card = Card("2", "hearts")
    new_card2 = Card("3", "hearts")

    assert str([new_card, new_card2]) == "[2♥, 3♥]"

def test__EQ__valid_comparation_card_2_and_2_hearts():
    """Try to create valid card : 2 of hearts and 2 of hearts"""
    new_card = Card("2", "hearts")
    new_card2 = Card("2", "hearts")

    assert Card.__eq__(new_card, new_card2) is True

def test__EQ__invalid_comparation_card_2_and_3_hearts():
    """Try to create valid card : 2 of hearts and 3 of hearts"""
    new_card = Card("2", "hearts")
    new_card2 = Card("3", "hearts")

    assert Card.__eq__(new_card, new_card2) is False