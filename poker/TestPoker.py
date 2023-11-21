import unittest
from combinations import poker_hands


class TestPoker(unittest.TestCase):

    def test_flush(self):
        self.assertEqual(poker_hands([1, 2, 3, 7, 12]), "flush")

    def test_royal_flush(self):
        self.assertEqual(poker_hands([8, 9, 10, 11, 12]), "royal_flush")

    def test_four_of_a_kind(self):
        self.assertEqual(poker_hands([1, 14, 27, 7, 40]), "four_of_a_kind")

    def test_full_house(self):
        self.assertEqual(poker_hands([3, 16, 29, 10, 23]), "full_house")

    def test_pair(self):
        self.assertEqual(poker_hands([1, 2, 3, 4, 14]), "pair")

if __name__ == '__main__':
    unittest.main()