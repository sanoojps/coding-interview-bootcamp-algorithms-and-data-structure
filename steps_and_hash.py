# Write a function that accepts a +ve number N.
# The function should log a step shape
# with N levels using the # character.
# Make sure the step has spaces on the right side
# 
# Example
# steps(2)
# '# '
# '##'

def string_with_spaces_repeated(count: int):
    return string_with_chars_repeated(
        count=count,
        char=" "
    )

def string_with_chars_repeated(count: int, char: str = "#"):
    chars_repeated = ""
    for index in range(0,count):
        chars_repeated = chars_repeated + char
    return chars_repeated

def spaces(count: int):

    assert(isinstance(count,int))

    space_count = count - 1
    char_to_print = "#"
    spaced_string = ""

    # Loop till end of count
    # track space_count
    # make chars repeat with count
    # keep incrementing count
    # achieved here with a loop
    # make spaces repeat with count
    # decrement spaces count
    for index in range(1,count+1):
        spaced_string = \
            spaced_string + \
                string_with_chars_repeated(count=index,char="#") + \
                    string_with_spaces_repeated(count=space_count)

        if space_count > 0:
            spaced_string = spaced_string + "\n"

        space_count = space_count - 1 

    print(spaced_string)
    return spaced_string

    
        


import unittest
class TestingReverseString(unittest.TestCase):
    
    def test_spaces_count(self):
        spaces_count = 3
        spaces_string = string_with_spaces_repeated(3)

        self.assertTrue(
            len(spaces_string) == spaces_count
        )

    def test_spaced_out_string_count(self):
        spaces_count = 3
        spaces_string = spaces(count=3)
        expected_string = '#  \n## \n###'

        self.assertTrue(
            spaces_string == expected_string
        )


unittest.main()
