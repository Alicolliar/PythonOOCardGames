import unittest
from PlayingCard import PlayingCard

class PlayingCardTest(unittest.TestCase):
    PlayingCard = PlayingCard()

    def test_generate_deck(self):
        self.assertEqual(52, len(self.PlayingCard.generate_deck()))

    def test_shuffle_cards(self):
        self.assertNotEqual(self.PlayingCard.shuffle_cards(self.PlayingCard.generate_deck()), self.PlayingCard.shuffle_cards(self.PlayingCard.generate_deck()))

    def test_deal_a_card(self):
        self.assertEqual(self.PlayingCard.generate_deck()[-1], self.PlayingCard.deal_a_card(self.PlayingCard.generate_deck()))

    def test_is_playing_a_card(self):
        self.assertFalse(self.PlayingCard.play_a_card(["D6", "D9"], "D5"))

    def test_convert_face_to_number(self):
        self.assertNotEqual("D14", self.PlayingCard.convert_face_to_number("DA"))

if __name__ == "__main__":
    unittest.main()
