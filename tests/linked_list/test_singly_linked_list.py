from linked_list.doubly_linked_list import DoublyList
from linked_list.singly_linked_list import LinkedList

"""Siingly Linked list test cases"""


def test_singly_linked_list():
    linked_list = LinkedList()
    linked_list.insert_at_first(10)
    assert list(linked_list.get_list()) == [10]
    linked_list.insert_at_last(13)
    assert list(linked_list.get_list()) == [10, 13]
    linked_list.add_element_at_specific_location(9, 0)
    assert list(linked_list.get_list()) == [9, 10, 13]
    linked_list.add_element_at_specific_location(19, 3)
    assert list(linked_list.get_list()) == [9, 10, 13, 19]
    assert linked_list.search_element(19)
    assert not linked_list.search_element(100)


def test_doubly_linked_list():
    linked_list = DoublyList()
    linked_list.insert_at_first(10)
    assert list(linked_list.get_list()) == [10]
    linked_list.insert_at_last(13)
    assert list(linked_list.get_list()) == [10, 13]
    linked_list.add_element_at_specific_location(9, 0)
    assert list(linked_list.get_list()) == [9, 10, 13]
    assert list(linked_list.get_reverse_list()) == [13, 10, 9]
