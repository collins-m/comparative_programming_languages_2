class Node:

    def __init__(self, data):
        """ initialize with a data value and left/right links
        """
        self._data = data
        self._left = None
        self._right = None

    def data(self):
        """ getter for data
        """
        return self._data

    def left(self):
        """ getter for left traversal
        """
        return self._left

    def right(self):
        """ getter for right traversal
        """
        return self._right

    def ___str___(self):
        """ string method returns data
        """
        return str(self._data)
