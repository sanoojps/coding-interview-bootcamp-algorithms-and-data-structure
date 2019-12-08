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

    # print("{}-{}".format(string_to_reverse, reversed_string))
    return reversed_string

print(reverse_string("apple"))
print(reverse_string("hello"))
print(reverse_string("Greetings!"))

# UNITTEST


class TestingReverseString(unittest.TestCase):

    def test_apple_reversed_is_elppa(self):
        string_to_reverse = "Apple"
        expected = "elppA"
        self.assertTrue(
            expr=reverse_string(string_to_reverse) == expected,
            msg="string {} is reversed".format(expected)
        )
        # print(reverse_string(string_to_reverse) == expected)
        # self.assertTrue(reverse_string(string_to_reverse) == expected)

    def test_hello_reversed_is_hello(self):
        string_to_reverse = "hello"
        expected = "olleh"
        self.assertTrue(
            expr=reverse_string(string_to_reverse) == expected,
            msg="string {} is reversed".format(expected)
        )

    def test_Greetings_reversed(self):
        string_to_reverse = "Greetings!"
        expected = "!sgniteerG"
        self.assertTrue(
            expr=reverse_string(string_to_reverse) == expected,
            msg="string {} is reversed".format(expected)   
        )


unittest.main()


