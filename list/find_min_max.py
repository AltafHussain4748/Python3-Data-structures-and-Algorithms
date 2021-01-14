"""Write a program to reverse a list in python"""


def return_min_max(arr):
    min_number = arr[0]
    max_number = arr[0]
    for i in range(len(arr)):
        if min_number > arr[i]:
            min_number = arr[i]
        if max_number < arr[i]:
            max_number = arr[i]
    return min_number, max_number
