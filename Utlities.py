
DEBUG = 1

def reverse_string(string_to_reverse):
    reversed_string = ""
    # reverse iterator
    length_of_string = len(string_to_reverse)
    index = length_of_string - 1
    while index >= 0:
        reversed_string += string_to_reverse[index]
        index -= 1

    if DEBUG is 1:
        print("{}-{}".format(string_to_reverse, reversed_string))

    return reversed_string

def generate_char_to_count_map(string: str, lower: bool = False):
    
    char_to_count_map = dict()

    for char in string:
        char_to_use = char
        if lower == True:
            char_to_use = char.lower()
            
        if char_to_use in char_to_count_map:
            current_char_count = char_to_count_map[char_to_use]
            char_to_count_map[char_to_use] = int(current_char_count) + 1
        else:
            char_to_count_map[char_to_use] = 1

    return char_to_count_map

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

    if DEBUG is 1:
        print(
            "{} -> {}".format(
                string,
                final_string
            )
        )

    return final_string