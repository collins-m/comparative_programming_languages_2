from classes.BinaryTree import BinaryTree as BT

class Main:

    def __init__(self):
        """ initialize with a binary tree
        """
        self._tree = BT()

    def help(self):
        """ helper function, prints commands
        """
        print("\n")
        print("Here is a list of commands:")
        print("insert <x> | to insert x onto tree")
        print("search <x> | returns True if x is in tree")
        print("preorder | prints list of nodes in preorder")
        print("inorder | prints list of nodes in inorder")
        print("postorder | prints list of nodes in postorder")
        print("exit | exits program")
        print("\n")

    def main(self):
        """ main method, where user interaction takes place
        """
        print("type \"help\" for list of commands")
        while 1:
            n = input().split()
            if len(n) == 1:
                n = n[0]
                if n == "exit":
                    break
                elif n == "help":
                    self.help()
                elif n == "preorder":
                    self._tree.preorder()
                elif n == "inorder":
                    self._tree.inorder()
                elif n == "postorder":
                    self._tree.postorder()
            elif n[0] == "insert":
                self._tree.insert(n[1])
            elif n[0] == "search":
                print(self._tree.search(n[1]))
                print()

if __name__ == "__main__":
    main = Main()
    main.main()
