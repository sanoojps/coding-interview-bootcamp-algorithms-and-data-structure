# Write a program that console logs teh numbers
# form 1 to n.
# But for multiples of 3 print "fizz" 
# for multiples of 5 print buzz
# instead of the number and for the multiples of both three and 5 print 
# fizzbuzz

def fizzbuzz(limit: int):
    
    assert(
        isinstance(
            limit,int
        ) is True
    )

    string_to_print = ""
    for index in range(1,limit+1):

        # multiples of 3
        if index % 3 ==  0:
            string_to_print = \
                string_to_print + "fizz"

        # multiples of 5
        if index % 5 == 0:
            string_to_print = \
                string_to_print + "buzz"

        if len(string_to_print) == 0:
            string_to_print = index


        print(
            string_to_print
        )

        # reset
        string_to_print = ""


fizzbuzz(
    30
)