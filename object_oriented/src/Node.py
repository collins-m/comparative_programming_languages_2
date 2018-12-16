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

    def ___str___(self):
        """ string method returns data
        """
        return str(self._data)
