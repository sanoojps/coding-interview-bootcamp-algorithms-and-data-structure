# reversing signed integers

def reverse_a_signed_int(integer):
    
    reversed_integer = list(integer)
    
    is_signed = ""
    if reversed_integer[0] == "-":
        is_signed = reversed_integer[0]
        reversed_integer.pop(0)

    length_of_int = len(reversed_integer)
    assert(length_of_int >= 2)

    first_index = 0
    last_index = length_of_int - 1

    while first_index <= last_index:
        # swap
        tmp = reversed_integer[first_index]
        reversed_integer[first_index] = reversed_integer[last_index]
        reversed_integer[last_index] = tmp 

        first_index+=1
        last_index-=1

    return is_signed + "".join(reversed_integer)


print(
    reverse_a_signed_int("-67")
)

print(
    reverse_a_signed_int("67")
)


    
