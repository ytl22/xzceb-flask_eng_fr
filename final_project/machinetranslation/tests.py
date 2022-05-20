import unittest
from translator import french_to_english, english_to_french

class TestEnToFr(unittest.TestCase): 
    def test_null(self):
        self.assertNotEqual(english_to_french('None'), '')
    def test_Hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
    def test_Thanks(self):
        self.assertEqual(english_to_french('Thanks'), 'Merci')  # test when 'Thanks' is given as input the output is 'Merci'.
    def test_bread(self):
        self.assertNotEqual(english_to_french('bread'), 'pain')  # test when 'bread' is given as input the output is not 'pain'.


class TestFrToEn(unittest.TestCase): 
    def test_null(self):
        self.assertNotEqual(english_to_french('None'), '')
    def test_Bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
    def test_Merci(self):
        self.assertEqual(french_to_english('Merci'), 'Thank you')  # test when 'Merci' is given as input the output is 'Thank you'.
    def test_pain(self):
        self.assertNotEqual(french_to_english('pain'), 'bread')  # test when 'pain' is given as input the output is not 'bread'.

unittest.main()