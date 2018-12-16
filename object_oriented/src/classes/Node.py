class Node:

    def __init__(self, data):
        """ initialize with a data value and left/right links
        """
        self._data = data
        self._left = None
        self._right = None

    def data(self, param=None):
        """ getter/setter for data
        """
        if param == None:
            return self._data
        else:
            self._data = param

    def left(self, param=None):
        """ getter/setter for left traversal
        """
        if param == None:
            return self._left
        else:
            self._left = param

    def right(self, param=None):
        """ getter/setter for right traversal
        """
        if param == None:
            return self._right
        else:
            self._right = param

    def insert(self, data):
        """ insert data onto node
        """
        if self.data():
            if data < self.data():
                if self.left() is None:
                    self.left(Node(data))
                else:
                    self.left().insert(data)
            elif data > self.data():
                if self.right() is None:
                    self.right(Node(data))
                else:
                    self.right().insert(data)
            else:
                print("Integer {} already present in tree".format(data))
        else:
            self.data(data)

    def search(self, data):
        """ search for data in tree
        """
        if data < self.data():
            if self.left() is None:
                return False
            return self.left().search(data)
        elif data > self.data():
            if self.right() is None:
                return False
            return self.right().search(data)
        else:
            return True

    def preorder(self):
        """ list nodes using preorder
        """
        print(self.data())

        if self.left():
            self.left().preorder()

        if self.right():
            self.right().preorder()

    def inorder(self):
        """ list nodes using inorder
        """
        if self.left():
            self.left().inorder()

        print(self.data())

        if self.right():
            self.right().inorder()

    def postorder(self):
        """ list nodes using postorder
        """
        if self.left():
            self.left().postorder()

        if self.right():
            self.right().postorder()

        print(self.data())

    def ___str___(self):
        """ string method returns data
        """
        return str(self._data)
