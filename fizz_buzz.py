# print numbers from 1 to 100
# if multiples of 3 print Fizz
# if multiples of 5 print Buzz
# for both print Fizz Buzz
# 
# 
#  

def fizz_buzz(range_of_numbers):
    for index in range(1,range_of_numbers):
        string_to_print = index
        # divisible by 3 and 5
        if index % 3 == 0:
            string_to_print = "Fizz"
        if index % 5 == 0:
            buzz_string = "Buzz"
            if string_to_print is index:
                string_to_print = buzz_string
            else: 
                string_to_print+=buzz_string
        print("{}-{}".format(index,string_to_print))

fizz_buzz(16)


            

