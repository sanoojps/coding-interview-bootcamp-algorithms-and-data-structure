# Give an array and chunk size
# divide the array into many sub arrays where 
# each subarray is of length size

def slices_array(array: list, size:int):

    list_of_slices = []
    slice = list()

    for element in array:
        if len(slice) < size:
            slice.append(element)

        if len(slice) == size:
            list_of_slices.append(slice)
            slice = []

    if len(slice) > 0:
        list_of_slices.append(
            slice
        )

    print(
        list_of_slices
    )

    return list_of_slices

assert(
    slices_array(
    [1,2,3,4,5],
    2
) == [ 
    [1,2], 
    [3,4],
    [5] 
    ]
)

assert(
    slices_array(
    [1,2,3,4],
    2
) == [
     [1,2], 
     [3,4]
      ]
)

assert(
    slices_array(
    [1,2,3,4],
    5
) == [
     [1,2,3,4]
      ]
)

assert(
    slices_array(
    [1,2,3,4,5],
    10
) == [
     [1,2,3,4,5]
      ]
)
