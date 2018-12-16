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
        self.root().insert(x)

    def search(self, x):
        """ search for x in binary tree, returns true
        """
        if self.root():
            self.root()search(x)

    def preorder(self):
        """ list nodes using preorder
        """
        pass

    def inorder(self):
        """ list nodes using inorder
        """
        pass

    def postorder(self):
        """ list nodes using postorder
        """
        pass
