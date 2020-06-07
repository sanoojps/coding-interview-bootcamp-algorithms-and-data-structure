# reversing signed integers
def reverse_a_signed_integer(integer: int):
    
    if isinstance(integer,int) is True:
        reversed_integer = 0
        base = 10
        # check if integer is signed
        is_signed = True if integer < 0 else False
        # get abs values
        remainder = abs(integer)     
        # reverse each digit
        while remainder > 0:
            # get the last digit
            last_digit = remainder % base
            # append to reversed_integer
            reversed_integer = \
                (reversed_integer * base) + last_digit
            # get the rest of the number
            remainder = remainder // base

        if is_signed is True:
            reversed_integer = reversed_integer * -1

        return reversed_integer

def reverse_a_signed_integer_passed_in_as_string(integer):
    
    if isinstance(integer,str) is True:

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

    else:
        return reverse_a_signed_integer (
            integer=integer
        )







print(
    "{} -> {}".format(
        "-67",reverse_a_signed_integer_passed_in_as_string("-67")
    )
    
)

print(
    "{} -> {}".format(
        "67",reverse_a_signed_integer_passed_in_as_string("67")
    )
    
)

print(
    "{} -> {}".format(
        -67,reverse_a_signed_integer_passed_in_as_string(-67)
    )
    
)

print(
    "{} -> {}".format(
        60007,
        reverse_a_signed_integer_passed_in_as_string(60007)
    )
)

print(
    "{} -> {}".format(
        6000,
        reverse_a_signed_integer_passed_in_as_string(6000)
    )
)   

print(
    "{} -> {}".format(
        6600,
        reverse_a_signed_integer_passed_in_as_string(6600)
    )
)   

print(
    "{} -> {}".format(
        6600600,
        reverse_a_signed_integer_passed_in_as_string(6600600)
    )
)   

print(
    "{} -> {}".format(
        67009900100,
        reverse_a_signed_integer_passed_in_as_string(67009900100)
    )
)   

print(
    "{} -> {}".format(
        -19,
        reverse_a_signed_integer_passed_in_as_string(-19)
    )
)   

print(
    "{} -> {}".format(
        -1090,
        reverse_a_signed_integer_passed_in_as_string(-1090)
    )
)   