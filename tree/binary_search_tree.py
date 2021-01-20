class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.traversal_types = {
            'in-order': BST.in_order_traversal,
            'post-order': BST.post_traversal,
            'pre-order': BST.pre_traversal,
            'level-order': BST.level_order_traversal
        }
        self.ddl_oprations = {
            'search': BST.search,
            'delete': BST.delete,
        }
        self.data_found = False

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            print(f'{data} inserted to root')
            self.root = node
            return
        self.insert_leaf_node(self.root, node, data)

    def insert_leaf_node(self, root, node, data):
        if root.data < data and root.right is not None:
            print("Calling to right of node")
            self.insert_leaf_node(root.right, node, data)
        elif root.data > data and root.left is not None:
            print("Calling to left of node")
            self.insert_leaf_node(root.left, node, data)
        elif root.data > data:
            print(f'{data} inserted to left of node')
            root.left = node
        elif root.data < data:
            print(f'{data} inserted to right of node')
            root.right = node

    def perform_traversal(self, traversal_type):
        if traversal_type is None:
            print("Please pass traversal type")
            return
        print('*' * 100)
        print(f'Performing traversal for {traversal_type}')
        self.traversal_types[traversal_type](self, self.root)
        print('*' * 100)

    def in_order_traversal(self, root):
        if root is None:
            return
        self.in_order_traversal(root.left)
        print(root.data)
        self.in_order_traversal(root.right)

    def pre_traversal(self, root):
        if root is None:
            return
        print(root.data)
        self.pre_traversal(root.left)
        self.pre_traversal(root.right)

    def post_traversal(self, root):
        if root is None:
            return
        self.post_traversal(root.left)
        self.post_traversal(root.right)
        print(root.data)

    def level_order_traversal(self, root):
        # initial queue with root node
        queue = [root]
        while len(queue) != 0:
            temp = queue[0]
            queue.pop(0)
            print(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    def perform_ddl_oprations(self, data, opt_type):
        if opt_type is None:
            print("Please pass ddl type")
            return
        print('*' * 100)
        print(f'Performing ddl opration for {opt_type}')
        self.ddl_oprations[opt_type](self, self.root, data)
        if self.data_found:
            print("Data was found in the tree")
        else:
            print("No data found in tree for the given search")
        print('*' * 100)

    def search(self, root, data):
        if root is None:
            return
        if data != root.data and data > root.data and root.right is not None:
            self.search(root.right, data)
        if data != root.data and data < root.data and root.left is not None:
            self.search(root.left, data)
        if data == root.data:
            self.data_found = True
            return

    def delete(self, root, data, parent_node=None):
        if root is None:
            return
        if data != root.data and data > root.data and root.right is not None:
            self.delete(root.right, data, parent_node=root)
        if data != root.data and data < root.data and root.left is not None:
            self.delete(root.left, data, parent_node=root)
        if data == root.data:
            """Node is found now we can delete it"""
            self.data_found = True
            if root.left is None and root.right is None:
                if data > parent_node.data:
                    parent_node.right = None
                    return
                if data < parent_node.data:
                    parent_node.left = None
                    return
            elif root.right is None and root.left is not None:
                parent_node.left = root.left
            elif root.right is not None and root.left is None:
                parent_node.right = root.right
            elif root.left is not None and root.right is not None:
                leaf_node = root
                prev = None
                while leaf_node.right is not None:
                    prev = leaf_node
                    leaf_node = leaf_node.right
                root.data = leaf_node.data
                prev.right = None
            return


nodes = [10, 12, 9, 20, 28, 90, 1]
bst = BST()
for node in nodes:
    bst.insert(node)

bst.perform_traversal('level-order')
bst.perform_ddl_oprations(10, 'delete')
bst.perform_traversal('level-order')
