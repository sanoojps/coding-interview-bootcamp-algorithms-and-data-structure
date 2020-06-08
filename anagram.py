# check to see if two provided strings are anagrams to eachother
# 'rail safety' 'fairy tales'
# 'RAIL! SAFETY!', 'fairy tales'
from mostCommonlyUsedChar import generate_char_to_count_map
import unittest

valid_symbols = "!@#$%^&*()_-+={}[]"

def is_an_anagram(string: str,string_to_test: str):
    # flag
    is_an_anagram = False
    # generate char to count map
    char_to_count_map = generate_char_to_count_map(
        string,
        lower=True
    )
    # loop through chars in "string_to_test"
    for char in string_to_test:
        if char in char_to_count_map:
            # decrement char count in 
            # char_to_count_map for chars that match
            char_count = int(char_to_count_map[char]) - 1
            char_to_count_map[char] = char_count
        else:
            break
    # loop through char_to_count_map to see if all counts are 0
    for char,count in char_to_count_map.items():
        # ignore symbols
        if char in valid_symbols:
            continue
        else:
            if count == 0:
                is_an_anagram = True
            else:
                is_an_anagram = False
                break

    return is_an_anagram

def remove_special_chars(string: str, white_spaces: bool = False):

    regEx_with_space = r'[^0-9a-zA-Z ]+'
    regEx_without_space = r'[^0-9a-zA-Z]+'

    import re

    final_string = ""
    if white_spaces == True:
        final_string = re.sub(
            regEx_with_space,
            "",
            string
        )
    else:
        final_string = re.sub(
            regEx_without_space,
            "",
            string
        )

    print(
        "{} -> {}".format(
            string,
            final_string
        )
    )
    return final_string








# UNITTEST


class TestingAnagram(unittest.TestCase):

    def testCombo1(self):
        string = "rail safety"
        string_to_test = "fairy tales"

        self.assertTrue(
            is_an_anagram(
            string=string,
            string_to_test=string_to_test
        )
        )

    def testComboWithSymbols(self):
        string = "RAIL! SAFETY!"
        string_to_test = "fairy tales"

        self.assertTrue(
            is_an_anagram(
            string=string,
            string_to_test=string_to_test
        )
        )

    def testComboOfNotAnagrams(self):
        string = "Hi there"
        string_to_test = "Bye there"

        self.assertFalse(
            is_an_anagram(
            string=string,
            string_to_test=string_to_test
        )
        )


    def testRemoveChars(self):

        string = "HEllO $%$@ man!!!!!!"

        self.assertTrue(
            remove_special_chars(
                string
            ) == "HEllOman"
        )

    def testRemoveCharsWithSpace(self):
    
        string = "HEllO $%$@ man!!!!!!"

        self.assertTrue(
            remove_special_chars(
                string,
                white_spaces=True
            ) == "HEllO  man"
        )


# run test
unittest.main()