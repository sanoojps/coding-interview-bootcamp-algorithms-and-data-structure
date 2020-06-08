# most commonly used char

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


print(
    generate_char_to_count_map(
        "paper"
    )
)
