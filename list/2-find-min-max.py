"""Write a program to reverse a list in python"""


def return_min_max(arr):
    min_number = arr[0]
    max_number = arr[0]
    for i in range(len(arr)):
        if min_number > arr[i]:
            min_number = arr[i]
        if max_number < arr[i]:
            max_number = arr[i]
    print("Min number in the list is {0}".format(min_number))
    print("Max number in the list is {0}".format(max_number))


numbers = [10, 12, 9, 4, 5, 1, 6, 3, 120]
return_min_max(numbers)
