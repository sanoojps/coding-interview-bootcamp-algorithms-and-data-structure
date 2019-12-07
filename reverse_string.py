# reverse string

import unittest


def reverse_string(string_to_reverse):
    reversed_string = ""
    # reverse iterator
    length_of_string = len(string_to_reverse)
    index = length_of_string - 1
    while index >= 0:
        reversed_string += string_to_reverse[index]
        index -= 1

    print("{}-{}".format(string_to_reverse, reversed_string))


# UNITTEST


class TestingReverseString(unittest.TestCase):

    def test_apple_reversed_is_elppa(self):
        string_to_reverse = "Apple"
        expected = "elppA"
        self.assertFalse(
            expr=reverse_string(string_to_reverse),
            msg="string {} is reversed".format(expected)
        )

    def test_hello_reversed_is_hello(self):
        string_to_reverse = "hello"
        expected = "olleh"
        self.assertFalse(
            expr=reverse_string(string_to_reverse),
            msg="string {} is reversed".format(expected)
        )

    def test_Greetings_reversed(self):
        string_to_reverse = "Greetings!"
        expected = "!sgniteerG"
        self.assertFalse(
            expr=reverse_string(string_to_reverse),
            msg="string {} is reversed".format(expected)   
        )


unittest.main()

reverse_string("apple")
reverse_string("hello")
reverse_string("Greetings!")
