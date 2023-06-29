from game import *

def test_Croupier_Decision_Stands_And_Busted():
    game = Game()

    game.prepare("Wojtek")

    game.human.hand.append(Card("A", "spades"))
    game.human.hand.append(Card("4", "hearts"))
    game.human.hand.append(Card("3", "hearts"))

    game.croupier.hand.append(Card("A", "hearts"))
    game.croupier.hand.append(Card("5", "hearts"))
    game.croupier.hand.append(Card("Q", "hearts"))
    game.croupier.hand.append(Card("7", "hearts"))

    test_bust = game.croupier_decision()

    assert test_bust is True
    assert len(game.croupier.hand) == 4

def test_Croupier_Decision_Stands_Not_Busted():
    game = Game()

    game.prepare("Wojtek")

    game.human.hand.append(Card("A", "spades"))
    game.human.hand.append(Card("4", "hearts"))

    game.croupier.hand.append(Card("A", "hearts"))
    game.croupier.hand.append(Card("6", "hearts"))
    game.croupier.hand.append(Card("Q", "hearts"))

    test_bust = game.croupier_decision()

    assert test_bust is False
    assert len(game.croupier.hand) == 3

# TODO create test with mocks
# def test_Croupier_Decision_Hits_Busted():
#     game = Game()

#     game.prepare("Wojtek")

#     game.human.hand.append(Card("A", "spades"))
#     game.human.hand.append(Card("4", "hearts"))

#     game.croupier.hand.append(Card("", "hearts"))
#     game.croupier.hand.append(Card("5", "hearts"))

#     test_bust = game.croupier_decision()

#     #assert test_bust is False to do with mock
#     assert len(game.croupier.hand) == 3