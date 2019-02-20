# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        tmp = cur_index
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = tmp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # wikipedia pseudocode solution
    # for i in range(1, len(arr)):
    #     j = i
    #     while j > 0 and arr[j-1] > arr[j]:
    #         tmp = arr[j-1]
    #         arr[j-1] = arr[j]
    #         arr[j] = tmp
    #         j -= 1

    # Separate the first element from the rest of the array. Think about it as
    # a sorted list of one element. For all other indices, beginning with [1]:
    for i in range(1, len(arr)):
        # Copy the item at that index into a temp variable
        tmp = arr[i]
        # Iterate to the left until you find the correct index in the "sorted"
        # part of the array at which this element should be inserted - Shift
        # items over to the right as you iterate
        j = i
        while j > 0 and arr[j-1] > tmp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = tmp

    return arr


# STRETCH: implement the Bubble Sort function below
# Walk through the array, comparing each element to its right neighbor. If it's
# smaller than that neighbor, swap the elements. Repeat this until you make it
# through an entire pass without any swaps.
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
