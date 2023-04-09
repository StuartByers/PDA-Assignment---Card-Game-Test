
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("hearts", 1)

    def test_card_has_suit(self):
        self.assertEqual("hearts", self.card.suit)

    def test_card_has_value(self):
        self.assertEqual(1, self.card.value)

    def test_check_for_ace(self):
        card_game = CardGame()
        card1 = Card("hearts", 1)
        card2 = Card("spades", 2)
        self.assertTrue(card_game.check_for_ace(card1))
        self.assertFalse(card_game.check_for_ace(card2))

    def test_highest_card(self):
        card_game = CardGame()
        card1 = Card("hearts", 1)
        card2 = Card("spades", 2)
        self.assertEqual(card2, card_game.highest_card(card1, card2))

    def test_cards_total(self):
        card_game = CardGame()
        card1 = Card("hearts", 1)
        card2 = Card("spades", 2)
        cards = [card1, card2]
        self.assertEqual("You have a total of 3", card_game.cards_total(cards))