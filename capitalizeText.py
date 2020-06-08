# Capitalize first letter of each word
from enum import Enum

class CapitalizationRules(Enum):
    FIRST_LETTER_OF_EVERY_WORD = "1"
    EVERY_WORD = "2"
    FIRST_LETTER_OF_FIRST_WORD = "3"
    EVERY_LETTER = "4"

def capitalize(
    string: str, 
    rule: CapitalizationRules = CapitalizationRules.FIRST_LETTER_OF_EVERY_WORD
    ):

    if rule is CapitalizationRules.FIRST_LETTER_OF_EVERY_WORD:

        capitalized_string = ""
        should_capitalize_next_char = True

        for index,char in enumerate(string):
            
            if should_capitalize_next_char is True:
                capitalized_string = \
                    capitalized_string + char.upper()
                # reset flag
                should_capitalize_next_char = False
            else:
                capitalized_string = \
                    capitalized_string + char
            
            # look for space
            # letter after space needs to be capitalized
            # mark that
            if char is " ":
                should_capitalize_next_char = True

        return capitalized_string

    if rule is CapitalizationRules.EVERY_LETTER:
        capitalized_string = ""
        should_capitalize_next_char = True

        for char in string:
            capitalized_string = \
                    capitalized_string + char.upper()

        return capitalized_string

# UNIT TEST
import unittest

class TestingReverseString(unittest.TestCase):
    
    def test_capitalize_word(self):
        test_string = "a small world"
        expected_string = "A Small World"

        self.assertTrue(
            capitalize(
                test_string
            ) == \
                expected_string
        )

    def test_capitalize_word_single_letter(self):
        test_string = "a"
        expected_string = "A"

        self.assertTrue(
            capitalize(
                test_string
            ) == \
                expected_string
        )

    def test_capitalize_word_single_word(self):
        test_string = "ab"
        expected_string = "Ab"

        self.assertTrue(
            capitalize(
                test_string
            ) == \
                expected_string
        )

    def test_capitalize_every_letter(self):
        test_string = "ab cd"
        expected_string = "AB CD"

        self.assertTrue(
            capitalize(
                test_string,
                rule=CapitalizationRules.EVERY_LETTER
            ) == \
                expected_string
        )



unittest.main()
            


