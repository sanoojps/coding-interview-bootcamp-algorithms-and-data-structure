# most commonly used char

def generate_char_to_count_map(string: str):

    char_to_count_map = dict()

    for char in string:
        if char in char_to_count_map:
            current_char_count = char_to_count_map[char]
            char_to_count_map[char] = int(current_char_count) + 1
        else:
            char_to_count_map[char] = 1

    return char_to_count_map


print(
    generate_char_to_count_map(
        "paper"
    )
)
