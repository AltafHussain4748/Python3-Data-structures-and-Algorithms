"""Write a program to reverse a list in python"""


def reverse_list(arr):
    for i in range(len(arr)):
        arr[i], arr[-(i + 1)] = arr[-(i + 1)], arr[i]
        if i + 1 == int(len(arr) / 2):
            break
    return arr