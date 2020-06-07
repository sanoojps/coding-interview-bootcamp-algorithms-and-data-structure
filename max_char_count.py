# max characters in a  string
from mostCommonlyUsedChar import generate_char_to_count_map

def max_char_count(string):
    
    char_to_count_map = generate_char_to_count_map(
        string
    )

    # find max
    max_count = 0
    max_count_char = []
    for key,value in char_to_count_map.items():
         if value >= max_count:
             max_count = value
             max_count_char.append(
                 (key,value)
             )


    return max_count_char


print(
    max_char_count(
        "proper"
    )
)


