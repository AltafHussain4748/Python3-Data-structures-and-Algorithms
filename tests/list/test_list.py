from list.find_min_max import return_min_max
from list.revere_list import reverse_list


def test_reverse_list():
    print("test reversing of array")
    numbers = [1, 2, 3, 4]
    assert reverse_list(numbers) == [4, 3, 2, 1]


def test_find_min_max():
    print("test of find min and max in array")
    numbers = [1, 2, 3, 4]
    min_number, max_number = return_min_max(numbers)
    assert min_number == 1
    assert max_number == 4
