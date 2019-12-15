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

def is_palindrome_reverse_and_comparison(string_to_check):
    is_palindrome = False
    if reverse_string(string_to_check) == string_to_check:
        is_palindrome = True

    return is_palindrome

print("is_palindrome_reverse_and_comparison")
print(is_palindrome_reverse_and_comparison("madam"))
print(is_palindrome_reverse_and_comparison("india"))

def is_palindrome_loop(string_to_check):
    length = len(string_to_check)
    forward_index = 0
    reverse_index = length - 1
    mid_point = length // 2 #integer division
    is_palindrome = False
    while reverse_index >= mid_point:
        if string_to_check[forward_index] is string_to_check[reverse_index]:
            is_palindrome = True
        else:
            return False

        forward_index += 1
        reverse_index -= 1
    
    return is_palindrome
     
print("is_palindrome_loop")
print(is_palindrome_loop("madam") == True)
print(is_palindrome_loop("india") == False)
print(is_palindrome_loop("maam") == True)
print(is_palindrome_loop("1") == True)
print(is_palindrome_loop("11") == True)
print(is_palindrome_loop("12") == False)
print(is_palindrome_loop("malayalam") == True)
print(is_palindrome_loop("mam") == True)