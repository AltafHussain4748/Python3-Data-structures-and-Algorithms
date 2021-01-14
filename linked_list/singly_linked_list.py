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
        if location == 0:
            print("Insert at 0")
            return self.insert_at_first(data)
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
                return True
            temp = temp.next
            location += 1
        return False

    def is_head_null(self, node):
        """If head is none add first element to list"""
        if self.head is None:
            self.head = node
            self.last = node
            return True

    def get_list(self):
        """Print List data"""
        temp = self.head
        while True:
            yield temp.data
            if temp.next is None:
                break
            temp = temp.next

    def get_list_size(self):
        return self.size

# Please refere test cases
