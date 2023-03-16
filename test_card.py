import unittest
import io
import sys

from card import Card


class TestCard(unittest.TestCase):

    def test_init(self):
        card = Card('Карта игрока')
        self.assertEqual(card.name, 'Карта игрока')
        self.assertListEqual(card.cals, [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(card.barrels_in_row, 5)
        self.assertEqual(card.rows, 3)
        self.assertTrue(len(card.get_card()) > 0)

    def test_get_card(self):
        card = Card('Карта игрока').get_card()
        self.assertEqual(len(card), 3)
        for row in card:
            self.assertEqual(len(row), 9)
            self.assertEqual(len([i for i in row if i > 0]), 5)

    def test_print_card(self):
        card = Card('Карта игрока')
        card.card = [[0, 63, 0, 7, 4, 18, 21, 0, 0], [0, 0, 0, 28, 15, 0, 44, 65, 51],
                     [0, 69, 0, 67, 89, 0, 81, 27, 0]]

        captured_output = io.StringIO()
        sys.stdout = captured_output
        card.print_card()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '-------Карта игрока-------\n'
                                                     '   63     7  4 18 21       \n'
                                                     '         28 15    44 65 51 \n'
                                                     '   69    67 89    81 27    \n'
                                                     '--------------------------\n')

    def test_try_number(self):
        card = Card('Карта игрока')
        card.card = [[0, 63, 0, 7, 4, 18, 21, 0, 0], [0, 0, 0, 28, 15, 0, 44, 65, 51],
                     [0, 69, 0, 67, 89, 0, 81, 27, 0]]
        self.assertTrue(card.try_number(63))
        self.assertTrue(card.try_number(28))
        self.assertTrue(card.try_number(89))

    def test_str(self):
        card = Card('Карта игрока')
        self.assertEqual(card.name, str(card))

    def test_eq(self):
        card = Card('Карта игрока')
        card1 = Card('Карта игрока')
        card2 = Card('Карта игрока1')
        self.assertTrue(card == card1)
        self.assertFalse(card == card2)

    def test_in(self):
        card = Card('Карта игрока')
        card.card = [[0, 63, 0, 7, 4, 18, 21, 0, 0], [0, 0, 0, 28, 15, 0, 44, 65, 51],
                     [0, 69, 0, 67, 89, 0, 81, 27, 0]]
        self.assertTrue(63 in card)
        self.assertTrue(28 in card)
        self.assertTrue(89 in card)

