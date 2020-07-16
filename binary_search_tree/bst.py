class Node(object):
    def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None

class BT(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, '')
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, '')

    def preorder_print(self, start, traversal):
        #starts at root, then checks left subtree, then right subtree
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def inorder_print(self, start, traversal):
        #starts at left most node and works it way from left->root->right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        #starts at left->right->root
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal
# preorder output: 1-2-3-4-5-6-7-8-
# inorder output: 4-2-5-1-6-3-7-8-
# postorder output: 4-2-5-6-3-7-8-1
#     1
#   2   3
#  4 5 6 7
#         8
#

tree = BT(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))


class Node:
    def __init__(self, data=None):
        self.data = data 
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data): 
        if self.root is None:
            self.root = Node(data)
        else: 
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else: 
                self._insert(data, cur_node.right)
        
        else:
            print('the value is already present in tree')

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print(bst.find(4))
