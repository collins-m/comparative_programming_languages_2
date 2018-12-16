from classes.Node import Node

class BinaryTree:

    def __init__(self):
        """ initialize with an empty root
        """
        self._root = None

    def root(self, root=None):
        """ getter/setter of self._root
        """
        if root == None:
            return self._root
        else:
            self._root = root

    def insert(self, x):
        """ insert x into binary tree
        """
        x = int(x)
        if self.root():
            self.root().insert(x)
        else:
            self.root(Node(x))

    def search(self, x):
        """ search for x in binary tree, returns true
        """
        x = int(x)
        if self.root():
            return self.root().search(x)
        else:
            return False

    def preorder(self):
        """ list nodes using preorder
        """
        self.root().preorder()

    def inorder(self):
        """ list nodes using inorder
        """
        self.root().inorder()

    def postorder(self):
        """ list nodes using postorder
        """
        self.root().postorder()
