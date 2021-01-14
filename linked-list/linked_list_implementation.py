""" Implementation of LinkedList using python3 """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.last = None

    def insert_at_first(self, data):
        """Insert node at the start of the list"""
        self.size += 1
        node = Node(data)
        if self.is_head_null(node):
            return
        node.next = self.head
        self.head = node

    def insert_at_last(self, data):
        """Insert node at the end of the list"""
        self.size += 1
        node = Node(data)
        if self.is_head_null(node):
            return
        self.last.next = node
        self.last = node

    def add_element_at_specific_location(self, data, location):
        if location > self.get_list_size():
            print("Out of size list given")
            return
        node = Node(data)
        if self.is_head_null(node):
            return
        temp = self.head
        count = 1
        while count != location:
            count += 1
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def search_element(self, element):
        """Search in linked list"""
        temp = self.head
        location = 1
        while temp is not None:
            if element == temp.data:
                print(f"Element found in list at location {location}")
                return
            temp = temp.next
            location += 1
        print("Element not found in list")

    def is_head_null(self, node):
        """If head is none add first element to list"""
        if self.head is None:
            self.head = node
            self.last = node
            return True

    def print_list(self):
        """Print List data"""
        temp = self.head
        while True:
            print(temp.data)
            if temp.next is None:
                break
            temp = temp.next

    def get_list_size(self):
        return self.size


linked_list = LinkedList()

# Insert at beginning
linked_list.insert_at_first(300)
linked_list.insert_at_first(15)
linked_list.insert_at_last(100)
# insert at last
linked_list.insert_at_last(200)
linked_list.insert_at_last(10)
# insert at specific location
linked_list.add_element_at_specific_location(200003, 5)
# print list
linked_list.print_list()
# Search in Linked List
linked_list.search_element(2002)
